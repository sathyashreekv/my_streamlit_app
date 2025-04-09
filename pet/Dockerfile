FROM python:3.10-slim-bullseye

# Update system
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Install Python deps
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "login.py", "--server.port=8501", "--server.address=0.0.0.0"]
