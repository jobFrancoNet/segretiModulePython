# Usa una immagine leggera di Python
FROM python:3.11-slim

# Imposta la working directory
WORKDIR /app

# Copia requirements prima (meglio per caching Docker)
COPY requirements.txt .

# Installa dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice
COPY . .

# Espone la porta del server FastAPI
EXPOSE 8000

# Comando di avvio del server FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
