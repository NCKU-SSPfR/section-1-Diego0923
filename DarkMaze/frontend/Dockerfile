# TODO: Install the frontend dependency package into the app folder inside the container.
# Use the official Python image as a base
# Use a smaller base image
FROM python:3.11-slim

# Set a non-root user for security
RUN useradd --create-home appuser
WORKDIR /app
USER appuser

# Copy only necessary files (avoid copying sensitive data)
COPY requirements.txt /app/

# Pin dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src /app/src
COPY config /app/config

# Expose the frontend port
EXPOSE 8088

# Run application with limited privileges
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]

