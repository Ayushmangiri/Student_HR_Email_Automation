# resume_utils.py

import re

def extract_resume_data(file_path):
    """
    Simple function to extract name, email, and phone from a text resume.
    """
    data = {
        "name": None,
        "email": None,
        "phone": None
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract email
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
    if email_match:
        data["email"] = email_match.group()

    # Extract phone number (simple pattern for 10 digits)
    phone_match = re.search(r'\b\d{10}\b', content)
    if phone_match:
        data["phone"] = phone_match.group()

    # Extract name (very simple: assume first line is name)
    lines = content.splitlines()
    if lines:
        data["name"] = lines[0].strip()

    return data
