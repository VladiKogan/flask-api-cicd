# 1. Start from an official Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy *only* the requirements file first
COPY requirements.txt .

# 4. Install all your Python dependencies
RUN pip install -r requirements.txt

# 5. Copy the rest of your project code (app.py)
COPY . .

# 6. Expose port 5000
# This tells Docker that our app *inside* the container
# will be listening on port 5000.
EXPOSE 5000

# 7. Tell Docker what command to run when the container starts
CMD ["python", "app.py"]