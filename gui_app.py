import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

class HREmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student HR Email Automation")
        self.root.geometry("700x600")

        # ----- Recipients Upload -----
        tk.Label(root, text="Upload Recipients File (CSV/Excel):").pack(anchor="w", padx=10, pady=5)
        self.recipients_path = tk.Entry(root, width=50)
        self.recipients_path.pack(padx=10, pady=2)
        tk.Button(root, text="Browse", command=self.upload_recipients).pack(padx=10, pady=5)

        # ----- Resume Upload -----
        tk.Label(root, text="Upload Resume (PDF):").pack(anchor="w", padx=10, pady=5)
        self.resume_path = tk.Entry(root, width=50)
        self.resume_path.pack(padx=10, pady=2)
        tk.Button(root, text="Browse", command=self.upload_resume).pack(padx=10, pady=5)

        # ----- Template Selection -----
        tk.Label(root, text="Choose Email Template:").pack(anchor="w", padx=10, pady=5)
        self.template_var = tk.StringVar()
        self.template_dropdown = ttk.Combobox(
            root, textvariable=self.template_var,
            values=["template1.txt", "template2.txt"]
        )
        self.template_dropdown.pack(padx=10, pady=5)

        # ----- Subject -----
        tk.Label(root, text="Email Subject:").pack(anchor="w", padx=10, pady=5)
        self.subject_entry = tk.Entry(root, width=70)
        self.subject_entry.pack(padx=10, pady=5)

        # ----- Body -----
        tk.Label(root, text="Email Body:").pack(anchor="w", padx=10, pady=5)
        self.body_text = scrolledtext.ScrolledText(root, width=80, height=10)
        self.body_text.pack(padx=10, pady=5)

        # ----- SMTP Settings -----
        tk.Label(root, text="SMTP Server:").pack(anchor="w", padx=10, pady=2)
        self.smtp_server = tk.Entry(root, width=40)
        self.smtp_server.pack(padx=10, pady=2)
        self.smtp_server.insert(0, "smtp.gmail.com")

        tk.Label(root, text="SMTP Port:").pack(anchor="w", padx=10, pady=2)
        self.smtp_port = tk.Entry(root, width=10)
        self.smtp_port.pack(padx=10, pady=2)
        self.smtp_port.insert(0, "587")

        tk.Label(root, text="Your Email:").pack(anchor="w", padx=10, pady=2)
        self.sender_email = tk.Entry(root, width=40)
        self.sender_email.pack(padx=10, pady=2)

        tk.Label(root, text="Your Password:").pack(anchor="w", padx=10, pady=2)
        self.sender_password = tk.Entry(root, width=40, show="*")
        self.sender_password.pack(padx=10, pady=2)

        # ----- Buttons -----
        tk.Button(root, text="Preview Email", command=self.preview_email, bg="lightblue").pack(pady=10)
        tk.Button(root, text="Start Automation", command=self.start_automation, bg="lightgreen").pack(pady=5)

    # --------- Functions -----------
    def upload_recipients(self):
        file = filedialog.askopenfilename(filetypes=[("CSV/Excel files", "*.csv *.xlsx")])
        if file:
            self.recipients_path.delete(0, tk.END)
            self.recipients_path.insert(0, file)

    def upload_resume(self):
        file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file:
            self.resume_path.delete(0, tk.END)
            self.resume_path.insert(0, file)

    def preview_email(self):
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END).strip()
        template = self.template_var.get()
        resume = self.resume_path.get()

        preview_msg = f"Subject: {subject}\n\nBody:\n{body}\n\nTemplate: {template}\nResume: {resume}"
        messagebox.showinfo("Email Preview", preview_msg)

    def start_automation(self):
        messagebox.showinfo("Automation Started", "Emails will be sent as per schedule!")

# ✅ main.py will call this
def start_app():
    root = tk.Tk()
    app = HREmailApp(root)
    root.mainloop()
