FROM python:latest

RUN mkdir app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install -e .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]