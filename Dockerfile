FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN echo "Installing requirements..." && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./CanvasScraper.py" ]
