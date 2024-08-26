from faster_whisper import WhisperModel 

if __name__ == '__main__':
    model_size = "base.en"

    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe("sample.wav", beam_size=5)



    for segment in segments:
        print("[%.2fs -> %.2fs] %s %.2f" % (segment.start, segment.end, segment.text, segment.no_speech_prob))