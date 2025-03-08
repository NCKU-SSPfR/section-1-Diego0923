# TODO: Install the frontend dependency package into the app folder inside the container.
# Use the official Python image as a base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire frontend app to the container's /app directory
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8088

# Default command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
