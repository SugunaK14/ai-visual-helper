# AI Visual Helper for the Visually Impaired

An AI-powered assistive tool designed to help visually impaired users understand the contents of images, PDFs, documents, and printed material by converting them into **audio summaries** using powerful AI models like **Gemini 1.5 Pro** and **offline Transformers** (as a fallback).


## 📌 What is This?

This project allows users to upload various types of documents—such as resumes, posters, images, PDFs, and DOCX files—and get a **spoken summary** of the content. It combines OCR (Optical Character Recognition), Summarization AI, and Text-to-Speech to provide an audio playback experience, enabling a low-vision user to understand the document without seeing it.

## 💡 Innovation and Impact

- 🎯 **Target Audience:** Visually impaired individuals or anyone who benefits from audio-based content consumption.
- 🧩 **Multimodal Input Support:** Works with images, scanned text, PDFs, Word documents.
- 🔁 **Offline AI fallback:** Works even if Gemini API quota is exceeded, using HuggingFace Transformers.
- 🔊 **Audio Narration:** Uses `gTTS` (Google Text-to-Speech) to generate spoken output in `.mp3` format.
- 📶 **Runs Offline + Online:** Can function both with API and locally for summarization.

## 🧪 Features

- Upload support: `.pdf`, `.docx`, `.jpg`, `.jpeg`, `.png`
- Text extraction using OCR (`pytesseract`)
- Summarization using:
  - `Google Gemini 1.5 Pro` (primary)
  - `facebook/bart-large-cnn` (fallback)
- Audio generation via `gTTS`
- FastAPI-based web UI with drag & drop

## 🛠️ Tech Stack

| Layer                | Tool/Library Used                             |
|----------------------|---------------------------------------------- |
| 👓 OCR               | `pytesseract` (Tesseract OCR engine)          |
| 🧠 Summarization     | `Google Gemini 1.5 Pro`, `transformers`       |
| 🔊 TTS               | `gTTS (Google Text-to-Speech)`                |
| 🎛️ Web Framework     | `FastAPI`, `Uvicorn`, `Jinja2`, `HTML/CSS/JS` |
| 📄 File Handling     | `PyMuPDF`, `python-docx`, `PIL`                |
| 🧪 API Testing       | `Google AI Studio` (prompt & key testing)     |

## 🔑 How to Get Gemini API Key?

1. Go to [Google AI Studio](https://makersuite.google.com/app).
2. Sign in with your Google account.
3. Create a project.
4. Navigate to [Google Cloud Console → APIs & Services → Credentials](https://console.cloud.google.com/apis/credentials).
5. Generate an API key for Gemini Pro.
6. Replace the placeholder in `main.py`:
   ```python
   configure(api_key="YOUR_API_KEY")
⚠️ Free-tier has rate limits. The app includes offline summarization fallback when quota is exceeded.

## 🧭 Local Setup Instructions
1. Clone the Repo a, git clone https://github.com/sugunak14/ai-visual-helper.git b, cd ai-visual-helper

2. Create Virtual Environment a, conda create -n genai-helper python=3.10 b, conda activate genai-helper

3. Install Requirements
   pip install -r requirements.txt

4. Download and Install Tesseract
   Download for Windows - https://github.com/UB-Mannheim/tesseract/wiki

   Set the path in main.py:
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

5. Start Server
   uvicorn main:app --reload --log-level debug

7. Open Browser
   Visit: http://127.0.0.1:8000

## UI Screens for Your Reference
  ![image](https://github.com/user-attachments/assets/a22c2924-2423-4c43-a6d8-6b1f2116b4f3)

## 📷 Example Use Cases
   Use Case	Input	Output
Resume Summary	.pdf or .docx	Audio summary
Poster / Ad	.jpeg / .png	Spoken content
Old scanned documents	.pdf	Audio
Image with text	.jpg	OCR + Audio
![image](https://github.com/user-attachments/assets/f39c7e66-a9fb-4739-a505-3e424787da41)


## 🚧 Limitations & Future Scope

📉 Gemini free quota is limited; offline fallback works but may not match Gemini's quality.

🔒 No user login/session management.

🚀 Future: Add translation, voice tone selection, longer narration chunks (>15 mins), and chatbot integration.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

# 🙋‍♀️ Author
Suguna Kanagaraj

⭐ If you found this project useful or inspiring, consider giving it a star!
