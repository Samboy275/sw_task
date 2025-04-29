# Use Python runtime as parent image
From python:3.11-slim


# Working directory in container
WORKDIR /app

# Copy requirements to working directory
COPY requirements.txt .


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



# Copy the files into the container
COPY . .


# Command to start up the application using gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "your_project_name.wsgi:application"]
