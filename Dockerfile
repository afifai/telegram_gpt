FROM python:3.11-slim

WORKDIR /home/chatbot

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python","main.py"]