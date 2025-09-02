import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables
load_dotenv()

def send_email(to_email: str, subject: str, body: str) -> str:
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")
    resume_path = os.getenv("RESUME_PATH")

    if not sender_email or not sender_password:
        return "❌ Error: EMAIL_USER or EMAIL_PASS not found in .env file"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if resume_path and os.path.exists(resume_path):
        try:
            with open(resume_path, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(resume_path)}")
            msg.attach(part)
        except Exception as e:
            return f"❌ Error attaching resume: {e}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Error sending email: {e}"
