FROM python:3.7-alpine

# Set environment variable agar Flask bisa berjalan
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /code

# Copy requirements dan install dependensi
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy seluruh source code
COPY . .

EXPOSE 5000

CMD ["flask", "run"]
