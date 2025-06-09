FROM python:3.11.13-alpine3.22

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY frontend/. ./frontend
COPY config.py ./config.py

# Set environment variable for Flask app factory
ENV FLASK_APP=frontend:create_frontend()

# Default command for frontend
CMD ["flask", "run", "--debug", "--host", "0.0.0.0", "--port", "5001"]
