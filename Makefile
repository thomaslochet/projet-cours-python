.PHONY: init test run build clean

# Variables
IMAGE_NAME = health-calculator-service
PORT = 5000

# Initialize the project
init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run tests
test:
	@echo "Running tests..."
	python -m pytest test_health_calculator.py -v

# Run the application locally
run:
	@echo "Running the Flask app..."
	python app.py

# Build Docker image
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

# Run Docker container
docker-run:
	@echo "Running Docker container..."
	docker run -p $(PORT):$(PORT) $(IMAGE_NAME)

# Clean up
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete