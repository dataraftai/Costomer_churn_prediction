FROM python:3.12.11

WORKDIR /app

COPY reequirements.txt .
RUN pip install --no-chache-dir -r reequirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]