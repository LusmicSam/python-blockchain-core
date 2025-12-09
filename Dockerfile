# Use an official Python runtime as a parent image
# Slim version is best practice to keep image size small
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose ports for Flask API and Streamlit dashboard
EXPOSE 5000 8501

# Default command - can be overridden in docker-compose
CMD ["python", "src/api.py", "5000"]
