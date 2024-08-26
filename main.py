import argparse
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import uvicorn
import multiprocessing
from faster_whisper import WhisperModel

# Argument parser to handle command-line arguments
parser = argparse.ArgumentParser(description="Whisper server")

parser.add_argument('--port', type=int, default=8000, help="Port to run the server on")
parser.add_argument('--model_dir', type=str, default="./model", help="Path to the model directory")
parser.add_argument('--device', type=str, default="cpu", help="Device to run the model on (e.g., 'cpu', 'cuda')")

args = parser.parse_args()

# Initialize the FastAPI app and model with command-line arguments
app = FastAPI()
model = WhisperModel(args.model_dir, device=args.device, compute_type="int8")

@app.post("/segment")
async def process_sample(file: Annotated[UploadFile, File()]):
    contents = file.file
    segments, _ = model.transcribe(contents)
    ret = ""

    for segment in segments:
        if segment.no_speech_prob > 0.5:
            print(f"Ignoring segment {segment.text}\n")
            continue 
        ret += segment.text + " "
    return {"text": ret.strip()}


if __name__ == '__main__':
    multiprocessing.freeze_support()  # For Windows support
    uvicorn.run(app, host="127.0.0.1", port=args.port, reload=False, workers=1)
