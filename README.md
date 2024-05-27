
# Menu API

## Overview

This project is a sample Menu API application built with Python and Docker. It demonstrates the creation of a RESTful API to manage menu items, including features for CRUD operations.

## Features

- CRUD operations for menu items
- Database integration with SQLite
- Docker support for containerized deployment

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.x
- [Docker](https://www.docker.com/get-started)

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/ElaineLi0320/Menu_api.git
   cd Menu_api
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the application:
   ```sh
   python manage.py runserver
   ```

## Docker Setup

1. Build the Docker image:
   ```sh
   docker build -t menu_api .
   ```

2. Run the Docker container:
   ```sh
   docker-compose up
   ```

## Project Structure

- **menu/**: Contains the main application code.
- **tests/**: Contains test cases for the application.
- **Dockerfile**: Docker configuration for building the image.
- **docker-compose.yml**: Docker Compose configuration for running the application.

## Usage

You can use tools like Postman or cURL to interact with the API endpoints. For example, to get all menu items:

```sh
curl -X GET http://localhost:8000/api/menu/items
```
