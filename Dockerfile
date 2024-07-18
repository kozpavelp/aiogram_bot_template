FROM python:3.11

# Устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем код бота в контейнер
COPY bot /app/bot
COPY bot.py /app/
COPY .env /app/.env
# Переходим в рабочую директорию
WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Команда для запуска приложения
CMD ["python", "bot.py"]