# Local (Faster) Whisper Server
A minimal server that uses faster-whisper to transcribe audio segments, fast. Segments that have a high probability of not being speech are dropped.

It's cross-platform and has been tested on Windows and (soon) MacOS.

This is just a thin wrapper around some Python scripts so if this doesn't quite fit your use case please fork the repo.

# Model Files

You'll want to download one of the faster-whisper models and put them in the `model` folder. You can get these from `https://huggingface.co/Systran`.

# Dev

Install the dependencies with `pip install -r requirements.txt` then run `python main.py`. 

# Building

Install the dependencies with `pip install -r requirements.txt`, then run `pyinstaller main.py`.

# How to

Make an HTTP `POST` request to `http://localhost:8000/segment` with multipart/form-data with a field named `file` containing the audio file you wish to transcribe. I've tested this with WAV files made of int16 PCM buffers, but it should work with any audio format supported by Faster Whisper.

The response is a JSON object with a `text` field containing the transcription.

# License

This code is licensed under the MIT license (see License.md).