def create_email_message(hr_name, hr_email, job_role, sender_email, resume_path):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = hr_email  # Use the actual email
    msg['Subject'] = f"Application for {job_role} - Ayushman Giri"

    # Body of the email
    body = f"""
Dear {hr_name},

I hope this email finds you well.

I am Ayushman Giri, currently pursuing MCA at HBTU. 
With experience in Java, Spring Boot, and Android Development, 
I am very interested in the {job_role} position at your company.

Please find attached my resume for your kind consideration.  
I would be grateful for the opportunity to discuss how my skills 
align with your requirements.

Thank you for your time and consideration.

Best Regards,  
Ayushman Giri  
📧 ayushmangiri98@gmail.com  
📱 9839185001  
"""
    msg.attach(MIMEText(body, 'plain'))

    # Attach resume
    with open(resume_path, "rb") as resume_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(resume_file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename=resume.pdf')
        msg.attach(part)

    return msg
