FROM python:3.9-slim

# Instalar FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY requirements.txt .
COPY transcribe.py .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do Flask
EXPOSE 5001

# Comando para rodar a aplicação
CMD ["python", "transcribe.py"]
