from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import whisper
import tempfile
import shutil
import uvicorn

app = FastAPI()

# Load Whisper model (you can use 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (index.html) at "/playground"
app.mount("/playground", StaticFiles(directory="static", html=True), name="playground")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        shutil.copyfileobj(file.file, temp_audio)
        temp_audio_path = temp_audio.name

    # Transcribe the audio
    result = model.transcribe(temp_audio_path)

    print(result["text"], "result")

    return {"filename": file.filename, "transcription": result["text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
