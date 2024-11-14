from flask import Flask, request, jsonify, render_template_string 
from health_utils import calculate_bmi, calculate_bmr
from docs_utils import get_api_docs_template


app = Flask(__name__)

@app.route('/')
def index():
    """Serve API documentation"""
    return render_template_string(get_api_docs_template())

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/bmi', methods=['POST'])
def bmi():
    """Calculate BMI endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'height' not in data or 'weight' not in data:
            return jsonify({
                "error": "Missing required parameters. Please provide height (meters) and weight (kg)"
            }), 400
            
        height = float(data['height'])
        weight = float(data['weight'])
        
        result = calculate_bmi(height, weight)
        
        return jsonify({
            "bmi": round(result, 2),
            "category": get_bmi_category(result)
        })
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    """Calculate BMR endpoint"""
    try:
        data = request.get_json()
        
        required_fields = ['height', 'weight', 'age', 'gender']
        if not data or not all(field in data for field in required_fields):
            return jsonify({
                "error": "Missing required parameters. Please provide height (cm), weight (kg), age (years), and gender"
            }), 400
            
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = str(data['gender'])
        
        result = calculate_bmr(height, weight, age, gender)
        
        return jsonify({"bmr": round(result, 2)})
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

def get_bmi_category(bmi):
    """Helper function to determine BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)