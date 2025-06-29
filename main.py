import os
import io
import uuid
import fitz  # PyMuPDF
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from docx import Document
from PIL import Image
import pytesseract
from gtts import gTTS
from pydub import AudioSegment  # For combining audio chunks
from google.generativeai import configure, GenerativeModel
from transformers import pipeline

# --- CONFIG ---
configure(api_key="your_gemini_api_key")
model = GenerativeModel("gemini-1.5-pro")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# --- Offline Summarizer ---
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_offline(text: str) -> str:
    try:
        input_length = len(text.split())
        max_len = min(512, input_length // 2) if input_length > 60 else 50
        min_len = max(20, int(max_len * 0.5))

        result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return f"Offline summarization failed: {str(e)}"

# --- Safe TTS Function for Long Narration ---
def save_long_tts(text: str, output_path: str):
    CHUNK_SIZE = 3000  # characters
    parts = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    combined = AudioSegment.empty()

    for part in parts:
        tts = gTTS(text=part)
        temp_file = f"temp_{uuid.uuid4()}.mp3"
        tts.save(temp_file)
        segment = AudioSegment.from_mp3(temp_file)
        combined += segment
        os.remove(temp_file)

    combined.export(output_path, format="mp3")

# --- FastAPI Setup ---
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(request: Request, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        extension = file.filename.split('.')[-1].lower()
        print(f"Uploaded: {file.filename} ({extension})")

        text = ""
        if extension == 'pdf':
            with fitz.open(stream=contents, filetype="pdf") as doc:
                text = " ".join([page.get_text() for page in doc])

        elif extension == 'docx':
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(contents)
            doc = Document(temp_path)
            text = " ".join([para.text for para in doc.paragraphs])
            os.remove(temp_path)

        elif extension in ['jpg', 'jpeg', 'png']:
            image = Image.open(io.BytesIO(contents))
            text = pytesseract.image_to_string(image)

        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported file type."})

        if not text.strip():
            return JSONResponse(status_code=400, content={"error": "No text found."})

        used_fallback = False
        try:
            summary = model.generate_content(
                f"Summarize this in detail for a 15-minute audio narration:\n{text}"
            )
            summary_text = summary.text
            print("✅ Gemini summarization successful.")
        except Exception as e:
            print("⚠️ Gemini failed, using offline summarization. Error:", e)
            summary_text = summarize_offline(text)
            used_fallback = True

        audio_path = "static/output.mp3"
        save_long_tts(summary_text, audio_path)

        return {
            "message": "Success",
            "audio": "/static/output.mp3",
            "fallback_used": used_fallback
        }

    except Exception as e:
        print("❌ Error in analyze:", str(e))
        return JSONResponse(status_code=500, content={"error": "Something went wrong during analysis."})
