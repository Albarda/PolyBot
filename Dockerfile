#test
#

FROM python:3.13.0a6-slim
ARG TELEGRAM_TOKEN
WORKDIR /devops/polybot/PolyBot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN echo $TELEGRAM_TOKEN > .telegramToken
CMD ["python3", "bot.py"]
