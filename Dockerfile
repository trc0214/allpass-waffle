FROM python:3.10.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m discordbot && chown -R discordbot:discordbot /app
USER discordbot

CMD ["python", "allpass-waffle/bot.py"]