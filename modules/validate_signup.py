def validate_signup(name, dateOfBirth, gender, bloodType, phone, address, email, password):
    missing_fields = []
    if not name:
        missing_fields.append("Name")
    if not dateOfBirth:
        missing_fields.append("Date of Birth")
    if not gender:
        missing_fields.append("Gender")
    if not bloodType:
        missing_fields.append("Blood Type")
    if not phone:
        missing_fields.append("Phone Number")
    if not address:
        missing_fields.append("Address")
    if not email:
        missing_fields.append("Email")
    if not password:
        missing_fields.append("Password")
    
    return missing_fields