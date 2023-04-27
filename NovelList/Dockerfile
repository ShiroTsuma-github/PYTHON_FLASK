FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y bash
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
