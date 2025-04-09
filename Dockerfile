FROM python:3.10-slim-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y gcc && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean

EXPOSE 8501

CMD ["streamlit", "run", "login.py", "--server.port=8501", "--server.address=0.0.0.0"]
