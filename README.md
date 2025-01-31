# Working with HTTP actions and API parameters

This is a FastAPI application that manages tasks with CRUD operations.

## Features

- Create, Read, Update, and Delete tasks
- Supports optional task descriptions and status updates
- Returns responses in JSON format

## Installation

Ensure you have Python installed. Then, install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

## Running the API

To start the FastAPI server, run the following command:

```bash
uvicorn act2:app --reload
```

This will start the server, and the API will be available at `http://127.0.0.1:8000`.

## Usage

### Get a Task

Send a GET request to retrieve a task by ID:

```
GET /tasks/{task_id}
```

#### Example Request:
```
GET http://127.0.0.1:8000/tasks/1
```

#### Example Response:
```json
{
  "task_id": 1,
  "task_title": "Laboratory Activity",
  "task_desc": "Create Laboratory Activity 2",
  "is_finished": false
}
```

### Create a Task

Send a POST request to create a new task:

```
POST /tasks
```

#### Example Request:
```json
{
  "task_title": "New Task",
  "task_desc": "Task description",
  "is_finished": false
}
```

#### Example Response:
```json
{
  "message": "New Task Successfully Created.",
  "task": {
    "task_id": 2,
    "task_title": "New Task",
    "task_desc": "Task description",
    "is_finished": false
  }
}
```

### Update a Task

Send a PATCH request to update a task:

```
PATCH /tasks/{task_id}
```

### Delete a Task

Send a DELETE request to remove a task:

```
DELETE /tasks/{task_id}
```

### Replace a Task

Send a PUT request to replace a task:

```
PUT /tasks/{task_id}
```

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

