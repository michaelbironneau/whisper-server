# Local (Faster) Whisper Server
A minimal server that uses faster-whisper to transcribe audio segments, fast. Segments that have a high probability of not being speech are dropped.

It's cross-platform and has been tested on Windows and (soon) MacOS.

This is just a thin wrapper around some Python scripts so if this doesn't quite fit your use case please fork the repo.

# Building

Install the dependencies with `pip install -r requirements.txt`, then run `pyinstaller main.py`.