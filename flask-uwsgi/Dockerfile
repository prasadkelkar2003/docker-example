# Replacing debian:wheezy with a modern, slim Python base image
FROM python:3.9-slim

# Install system dependencies required to compile uWSGI
RUN apt-get update && apt-get install -y -q --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the original base requirements (Flask, uWSGI, etc.) and install them
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create a place to deploy the application (matching the original structure)
ENV APP_DIR=/var/www/app
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

# --- Original ONBUILD triggers preserved for downstream apps ---
# When app1 or app2 are built FROM this image, these lines trigger automatically
ONBUILD COPY . $APP_DIR/
ONBUILD RUN if [ -f $APP_DIR/requirements.txt ]; then pip install --no-cache-dir -r $APP_DIR/requirements.txt; fi
