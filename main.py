<<<<<<< HEAD
import os
import pandas as pd
from dotenv import load_dotenv
import smtplib
from email_log import create_email_message  # import your function

# ---------------- Load environment variables ----------------
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RESUME_PATH = os.getenv("RESUME_PATH")

if not RESUME_PATH or not os.path.isfile(RESUME_PATH):
    raise FileNotFoundError(f"❌ Resume path not found or invalid: {RESUME_PATH}")

# ---------------- Read recipients CSV ----------------
csv_file = "recipients.csv"  # ensure this file exists
df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip().str.lower()  # normalize column names

# ---------------- Send emails ----------------
log_list = []

for index, row in df.iterrows():
    to_email = row['email']        # recipient email
    hr_name = row.get('hr_name', '')   # HR name
    job_role = row.get('job_role', 'Fresher Position')  # Job role

    # Create email message using your function
    msg = create_email_message(hr_name, to_email, job_role, EMAIL_USER, RESUME_PATH)

    # Send email via Gmail
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
        print(f"✅ Email sent to {to_email}")
        log_list.append({"email": to_email, "status": "Success"})
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")
        log_list.append({"email": to_email, "status": f"Failed: {e}"})

# ---------------- Save log ----------------
log_df = pd.DataFrame(log_list)
log_df.to_csv("email_log.csv", index=False)
print("✅ Log saved to email_log.csv")
=======
from gui_app import start_app
from resume_utils import extract_resume_data

def main():
    resume_path = "resume/Resume.pdf"  # apna resume path sahi rakho
    resume_data = extract_resume_data(resume_path)
    print("Extracted Resume Data:", resume_data)

if __name__ == "__main__":
    start_app()
    main()
>>>>>>> c363f89e169fa61bd5bb005c7dca8d02f7a83730
