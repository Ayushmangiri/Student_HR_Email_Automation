from gui_app import start_app
from resume_utils import extract_resume_data

def main():
    resume_path = "resume/Resume.pdf"  # apna resume path sahi rakho
    resume_data = extract_resume_data(resume_path)
    print("Extracted Resume Data:", resume_data)

if __name__ == "__main__":
    start_app()
    main()
