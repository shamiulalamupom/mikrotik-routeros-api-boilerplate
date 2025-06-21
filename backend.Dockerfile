FROM python:3.11.13-alpine3.22

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY backend/. ./backend
COPY config.py ./config.py

# Set environment variable for Flask app factory
ENV FLASK_APP=backend:create_backend()

# Default command for backend
CMD ["uvicorn", "backend:create_backend", "--factory", "--host", "0.0.0.0", "--port", "5000", "--reload"]

