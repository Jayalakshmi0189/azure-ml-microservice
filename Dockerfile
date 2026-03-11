# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install flask pandas scikit-learn==1.2.2 joblib==1.2.1 pylint pytest

# Expose Flask port
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
