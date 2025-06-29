# 🧠 AI Visual Helper for the Visually Impaired

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
