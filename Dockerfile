FROM python:3.10-slim

WORKDIR /app

COPY learnmate.py requirements.txt ./

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove python3-pip && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8777

CMD ["python3", "-m", "streamlit", "run", "learnmate.py"]