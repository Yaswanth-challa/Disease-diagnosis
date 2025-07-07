from flask import Flask, render_template, request, jsonify
import os
from models.diagnosis_model import DiagnosisModel
from models.encryption import encrypt_data, decrypt_data
from utils.data_processor import preprocess_data

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

diagnosis_model = DiagnosisModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    if request.method == 'GET':
        return render_template('diagnosis.html')
    
    # For POST requests, process the medical data
    try:
        # Get data from form
        patient_data = request.form.to_dict()
        
        # Preprocess and encrypt data locally
        processed_data = preprocess_data(patient_data)
        encrypted_data = encrypt_data(processed_data)
        
        # Send encrypted data to the model for diagnosis
        # In a real implementation, this might be a separate edge device
        encrypted_result = diagnosis_model.predict(encrypted_data)
        
        # Decrypt the results locally
        result = decrypt_data(encrypted_result)
        
        return render_template('results.html', result=result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/diagnose', methods=['POST'])
def api_diagnose():
    # API endpoint for programmatic access
    try:
        data = request.get_json()
        processed_data = preprocess_data(data)
        encrypted_data = encrypt_data(processed_data)
        encrypted_result = diagnosis_model.predict(encrypted_data)
        result = decrypt_data(encrypted_result)
        return jsonify({"diagnosis": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')