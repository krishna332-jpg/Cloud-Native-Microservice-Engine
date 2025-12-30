#  Cloud-Native Microservice (FastAPI + Docker)
**A high-performance REST API designed for containerized deployment.**

##  Key Features
* **Modern Framework:** Built with **FastAPI** for asynchronous, high-speed request handling.
* **Containerized:** Includes a **Dockerfile** for seamless deployment to IBM Cloud, AWS, or Azure.
* **Auto-Documentation:** Integrated **Swagger/OpenAPI** UI for real-time endpoint testing.
* **Microservice Architecture:** Designed as a stateless service, ideal for horizontal scaling.

##  How to Run with Docker
1. Build the image: docker build -t cloud-api .
2. Run the container: docker run -p 8000:8000 cloud-api

##  API Endpoints
* GET /: Service status and metadata.
* GET /health: System health check for orchestration (Kubernetes).
