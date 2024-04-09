# Counter Service Documentation

Welcome to the Counter Service documentation. This guide will walk you through the steps required to set up and run the Counter Service project on your local machine.

## Getting Started

To get started with the Counter Service project, follow these steps:

### 1. Clone the Repository

First, clone the Counter Service repository from GitHub to your local machine using the following command:

```bash
git clone https://github.com/mojdeh-moazamian/Counter_Service.git
```

### 2. Install Requirements

Navigate to the project directory and install the required dependencies using `pip` and the provided `requirements.txt` file:

```bash
cd Counter_Service
pip install -r requirements.txt
```

### 3. Run the Server

Once the dependencies are installed, you can start the server using [uvicorn](https://www.uvicorn.org/) with the following command:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables automatic reloading of the server when changes are made to the code, making development easier.

### 4. Explore the API Documentation

Open your web browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs). This URL will display the Swagger documentation for the Counter Service API.

In the Swagger UI, you can explore all the available endpoints, submit requests, and view responses. This interface provides an interactive way to test the APIs.

## Testing the APIs

You can also test the APIs using tools like [Postman](https://www.postman.com/) or [Thunder Client](https://www.thunderclient.io/) in Visual Studio Code. Simply make requests to the appropriate endpoints and observe the responses.
