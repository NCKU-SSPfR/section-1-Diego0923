# TODO: Install the backend dependency package into the app folder inside the container.
# Use the official Python image as a base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file first (for better caching) and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project into the container
COPY . /app/

# Expose the correct backend port
EXPOSE 8000

# Command to start the FastAPI backend application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
