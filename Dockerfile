FROM python:3.11-slim-buster

WORKDIR /app

COPY . .

RUN python -m venv venv
RUN /bin/bash -c " source venv/bin/activate && pip install -r requirements.txt"

CMD [ "python", "./main.py" ]
