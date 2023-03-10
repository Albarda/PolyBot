


FROM python:3.9.16-slim
ARG TELEGRAM_TOKEN
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
#COPY . .
RUN echo $TELEGRAM_TOKEN > .telegramToken
CMD ["python3", "bot.py"]
