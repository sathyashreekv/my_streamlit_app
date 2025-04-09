# Dockerfile

FROM python:3.10-slim

# Update the base image to ensure it has the latest security patches
RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "login.py", "--server.port=8501", "--server.address=0.0.0.0"]
