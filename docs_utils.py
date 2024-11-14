def get_api_docs_template():
    """Returns HTML template for API documentation"""
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Health Calculator API Documentation</title>
    <style>
        body {
            font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            text-align: center;
        }
        pre {
            background: #f4f4f4;
            border-left: 3px solid #338;
            padding: 15px;
            border-radius: 3px;
            overflow-x: auto;
            text-align: left;
        }
        .endpoint {
            margin: 30px 0;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            text-align: left;
        }
        h2 { color: #333; }
        .method { 
            display: inline-block;
            padding: 3px 8px;
            border-radius: 3px;
            background: #338;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Health Calculator API Documentation</h1>
    
    <div class="endpoint">
        <span class="method">GET</span>
        <h2>/health</h2>
        <p>Health check endpoint to verify API status.</p>
        <strong>Example:</strong>
        <pre>curl -X GET https://projet-cours-python-thomas-lochet.azurewebsites.net/health</pre>
    </div>

    <div class="endpoint">
        <span class="method">POST</span>
        <h2>/bmi</h2>
        <p>Calculate Body Mass Index (BMI) given height and weight.</p>
        <strong>Parameters:</strong>
        <ul>
            <li>height (float): Height in meters</li>
            <li>weight (float): Weight in kilograms</li>
        </ul>
        <strong>Example:</strong>
        <pre>curl -X POST https://projet-cours-python-thomas-lochet.azurewebsites.net/bmi \\
    -H 'Content-Type: application/json' \\
    -d '{
        "height": 1.75,
        "weight": 70
    }'</pre>
    </div>

    <div class="endpoint">
        <span class="method">POST</span>
        <h2>/bmr</h2>
        <p>Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.</p>
        <strong>Parameters:</strong>
        <ul>
            <li>height (float): Height in centimeters</li>
            <li>weight (float): Weight in kilograms</li>
            <li>age (int): Age in years</li>
            <li>gender (string): Either 'male' or 'female'</li>
        </ul>
        <strong>Example:</strong>
        <pre>curl -X POST https://projet-cours-python-thomas-lochet.azurewebsites.net/bmr \\
    -H 'Content-Type: application/json' \\
    -d '{
        "height": 175,
        "weight": 70,
        "age": 30,
        "gender": "male"
    }'</pre>
    </div>

    <footer>
        <p>Thomas Lochet - 2024</p>
    </footer>
</body>
</html>
"""