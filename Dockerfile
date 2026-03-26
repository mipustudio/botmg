FROM python:3.11-slim

WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота
COPY main.py .
COPY config.py .
COPY logo.png .

# Запускаем бота
CMD ["python", "main.py"]
