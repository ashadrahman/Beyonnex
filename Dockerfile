FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Install Firefox and other dependencies
RUN apt-get update && apt-get install -y firefox-esr xvfb

# Install Python packages
RUN pip install selenium

# Install xvfb and xauth packages
RUN apt-get install -y xvfb xauth

# Copy Python script
COPY . /app

# Run script.py when the container launches
CMD ["python", "app.py"]
