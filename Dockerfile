FROM python:latest

RUN echo "Installing requirements..." && pip install -r requirements.txt

RUN python ./CanvasScraper.py
