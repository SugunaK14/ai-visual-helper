const dropArea = document.getElementById("drop-area");
const fileElem = document.getElementById("fileElem");
const analyzeBtn = document.getElementById("analyzeBtn");
const errorMessage = document.getElementById("error-message");
const filenameDisplay = document.getElementById("filename-display");
const audioPlayer = document.getElementById("audioPlayer");
const fallbackNote = document.getElementById("fallbackNote");

let selectedFile = null;

dropArea.addEventListener("click", () => fileElem.click());

fileElem.addEventListener("change", handleFiles);

dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("highlight");
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("highlight");
});

dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.remove("highlight");
  const files = e.dataTransfer.files;
  if (files.length > 0) {
    selectedFile = files[0];
    filenameDisplay.textContent = selectedFile.name;
  }
});

function handleFiles() {
  const files = this.files;
  if (files.length > 0) {
    selectedFile = files[0];
    filenameDisplay.textContent = selectedFile.name;
  }
}

analyzeBtn.addEventListener("click", async () => {
  if (!selectedFile) {
    errorMessage.textContent = "Please select a file.";
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile);

  try {
    errorMessage.textContent = "Processing...";
    fallbackNote.style.display = "none";

    const response = await fetch("/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Something went wrong");
    }

    audioPlayer.src = data.audio;
    audioPlayer.style.display = "block";
    errorMessage.textContent = "";

    // Show fallback notice if used
    if (data.fallback_used) {
      fallbackNote.innerText = "⚠️ Fallback used: Summary generated using local AI model due to Gemini API limit.";
      fallbackNote.style.display = "block";
    } else {
      fallbackNote.style.display = "none";
    }

  } catch (err) {
    errorMessage.textContent = "Error: " + err.message;
    fallbackNote.style.display = "none";
  }
});
