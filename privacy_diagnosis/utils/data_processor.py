def preprocess_data(data):
    """
    Preprocess patient data before encryption and diagnosis
    """
    processed_data = {}
    
    # Handle temperature
    if 'temperature' in data:
        try:
            temp = float(data['temperature'])
            # Convert to Celsius if in Fahrenheit
            if temp > 50:  # Likely Fahrenheit
                temp = (temp - 32) * 5/9
            processed_data['temperature'] = round(temp, 1)
        except ValueError:
            processed_data['temperature'] = None
    
    # Handle heart rate
    if 'heart_rate' in data:
        try:
            processed_data['heart_rate'] = int(data['heart_rate'])
        except ValueError:
            processed_data['heart_rate'] = None
    
    # Handle blood pressure
    if 'blood_pressure' in data:
        processed_data['blood_pressure'] = data['blood_pressure']
    
    # Handle oxygen level
    if 'oxygen_level' in data:
        try:
            oxygen = float(data['oxygen_level'])
            processed_data['oxygen_level'] = min(100, max(0, oxygen))  # Ensure between 0-100%
        except ValueError:
            processed_data['oxygen_level'] = None
    
    # Handle symptoms (as a list)
    if 'symptoms' in data:
        if isinstance(data['symptoms'], list):
            processed_data['symptoms'] = data['symptoms']
        else:
            # Convert comma-separated string to list
            processed_data['symptoms'] = [s.strip() for s in data['symptoms'].split(',')]
    
    return processed_data