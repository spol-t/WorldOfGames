FROM python:3.11-alpine3.18
WORKDIR /app
ADD . /app
RUN pip install
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3", "MainScores.py"]
