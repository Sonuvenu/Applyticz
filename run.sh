#!/bin/bash

# Change to the backend directory
cd backend  # Ensure the directory name matches (case-sensitive)

# Check if Python 3 or Python is available and use the correct one
if command -v python3 &>/dev/null; then
    PYTHON_EXEC=python3
    PIP_EXEC=pip3
    echo "Python 3 is available."
elif command -v python &>/dev/null; then
    PYTHON_EXEC=python
    PIP_EXEC=pip
    echo "Python is available."
else
    echo "Python is not installed. Please install Python 3."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [[ ! -d .venv ]]; then
    echo "Creating a virtual environment..."
    $PYTHON_EXEC -m venv .venv
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate

# Install required packages from requirements.txt
echo "Installing required packages..."
$PIP_EXEC install -r requirements.txt

# Ask the user if they want to use Docker
echo -n "Do you want to use Docker to run the backend? (y/n): "
read -r USE_DOCKER

if [[ "$USE_DOCKER" =~ ^[Yy]$ ]]; then
    cd ..

    # Run the FastAPI application using Docker
    if [ -f "./docker_backend.sh" ]; then
        chmod u+rwx "./docker_backend.sh"
        dos2unix "./docker_backend.sh"
        echo "Starting the backend server using Docker..."
        ./docker_backend.sh
    else
        echo "Could not find docker_backend.sh file. Please ensure the script exists."
        exit 1
    fi
else
    echo "Skipping Docker setup. Starting the backend server directly..."

    # Ensure you are in the backend directory
    cd backend

    # Check if port 8000 is in use
    PORT=8000
    PID=$(lsof -ti tcp:$PORT)  # Find the PID of the process using the port

    if [ ! -z "$PID" ]; then
        echo "Port $PORT is in use by process $PID. Terminating the process..."
        kill -9 $PID  # Kill the process using the port
        echo "Process $PID terminated. Proceeding to start the backend."
    else
        echo "Port $PORT is free. Starting the backend."
    fi

    # Start the backend server directly on port 8000
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 &
    cd ..
fi

# Change to the frontend directory
cd Frontend/app

# Install dependencies if they haven't been installed yet or if new ones have been added
echo "Ensuring dependencies are up-to-date..."
npm install

# Start the React development server
echo "Starting the React development server..."
npm start
