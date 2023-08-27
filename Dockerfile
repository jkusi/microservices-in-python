FROM python:alpine3.18
# Set the working directory in the container
WORKDIR /app

# Copy the app source code and templates into the container
COPY src/ /app/
COPY src/templates/ /app/templates/

# Install Flask
RUN pip install Flask

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Flask app
CMD ["python3", "app.py"]
