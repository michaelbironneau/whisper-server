
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import uvicorn
import multiprocessing
from faster_whisper import WhisperModel

app = FastAPI()
model = WhisperModel("./model", device="cpu", compute_type="int8")

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
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)