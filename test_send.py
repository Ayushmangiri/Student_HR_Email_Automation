from email_sender import send_email

result = send_email(
    to_email="hr_email@example.com",
    subject="Application for Internship",
    body="Hello HR,\n\nPlease find attached my resume.\n\nRegards,\nAyushman"
)
print(result)
