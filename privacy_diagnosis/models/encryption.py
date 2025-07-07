import hashlib
import base64
import json

def encrypt_data(data):
    """
    Encrypt patient data to preserve privacy
    
    In a real application, you would use a proper homomorphic encryption library
    like Microsoft SEAL, Palisade, or HElib.
    
    This is a simplified demonstration using basic encoding.
    """
    # Simple encryption for demonstration purposes
    # DO NOT use this in production - it's not secure!
    
    encrypted_data = {}
    for key, value in data.items():
        try:
            # Convert value to string if it's not already
            value_str = str(value)
            
            # Create a simple "encryption" (base64 encoding with salt)
            salted = f"privacy_salt_{value_str}_edge"
            hashed = hashlib.sha256(salted.encode()).digest()
            encoded = base64.b64encode(hashed).decode('utf-8')
            
            encrypted_data[key] = encoded
        except Exception as e:
            encrypted_data[key] = f"Error encrypting: {str(e)}"
    
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypt the diagnosis results
    
    In a real application, this would use proper homomorphic decryption.
    Here, we simulate the decryption process.
    """
    # For demonstration, we'll return simulated decrypted data
    # In a real system, you would use the private key to decrypt
    
    # Simulate some diagnoses based on encrypted values
    diagnoses = [
        "Common Cold", 
        "Influenza", 
        "Allergic Reaction", 
        "Hypertension"
    ]
    
    import random
    diagnosis = random.choice(diagnoses)
    probability = random.uniform(0.65, 0.95)
    
    decrypted_result = {
        "diagnosis": diagnosis,
        "probability": f"{probability:.2f}",
        "recommendation": f"Based on your symptoms, you may have {diagnosis}. " 
                          f"Confidence level: {probability:.2f}. "
                          f"Please consult with a healthcare professional for confirmation."
    }
    
    return decrypted_result