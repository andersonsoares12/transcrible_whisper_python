from flask import Flask, request
import whisper
import os

app = Flask(__name__)

# Carrega o modelo Whisper (escolha: tiny, base, small, medium, large, turbo)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if 'data' not in request.files:
        return {"error": "No audio file provided"}, 400
    
    file = request.files["data"]
    file_path = "temp_audio.wav"
    file.save(file_path)  # Salva o arquivo de áudio temporariamente

    # Transcreve o áudio
    result = model.transcribe(file_path, language="pt")  # Especifica português
    os.remove(file_path)  # Remove o arquivo temporário

    return {"text": result["text"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
