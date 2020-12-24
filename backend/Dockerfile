
# Create our image based on Python 3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Expose ports
EXPOSE 5000

# Tell Python to not generate .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering
ENV PYTHONUNBUFFERED 1

# Install requirements using pip
ADD app/requirements.txt .
RUN python -m pip install -r requirements.txt

# Set working directory and addour Flask API files
WORKDIR /app
ADD . /app