# projet-cours-python

Author : *Thomas Lochet*

A Flask-based REST API for calculating health metrics like BMI (Body Mass Index) and BMR (Basal Metabolic Rate).

## Features

- BMI (Body Mass Index) calculation
- BMR (Basal Metabolic Rate) calculation using Harris-Benedict equation
- Interactive API documentation
- Health check endpoint

## Installation

```bash
# Clone the repository
git clone https://github.com/thomaslochet/projet-cours-python.git

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
make init
```

## Usage 

### Running the server

```bash
make run
```

The server will start on http://localhost:5001

### API Endpoints

#### Health Check

```bash
curl -X GET http://localhost:5000/health
```
#### Calculate BMI

```bash
curl -X POST http://localhost:5000/bmi \
    -H 'Content-Type: application/json' \
    -d '{
        "height": 1.75,
        "weight": 70
    }'
```

#### Calculate BMR

```bash
curl -X POST http://localhost:5000/bmr \
    -H 'Content-Type: application/json' \
    -d '{
        "height": 175,
        "weight": 70,
        "age": 30,
        "gender": "male"
    }'
```

## Testing

Run the test suite:

```bash
make test
```