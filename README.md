# Smart Crop Management System

A simple Flask web application that displays predefined crop management information for Rice, Wheat, and Cotton.

## Technologies
- Python
- Flask
- HTML/CSS
- Docker
- Docker Compose
- AWS EC2
- Render

## Run with Docker Compose

```bash
docker compose up -d --build
```

Open:
http://localhost:5000

## Deploy on Render

Create a new **Web Service** from this GitHub repository and select **Docker** as the runtime.

The included `Dockerfile` starts the Flask application on port 5000. Render automatically routes public traffic to the container's exposed web port.

If using the Render Blueprint, the included `render.yaml` can be used.

## Supported Crops
- Rice
- Wheat
- Cotton
