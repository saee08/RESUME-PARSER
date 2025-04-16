import pdfplumber
import re
import json
import streamlit as st
import spacy
import nltk
import base64

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Load Spacy NLP Model
nlp = spacy.load("en_core_web_sm")

def set_background():
    background_color = """
    <style>
        .stApp {
            background: linear-gradient(to right, #f5f5dc, #dcdcdc);
            padding: 20px;
        }
        h1 {
            color: #ff5733;
            text-align: center;
            font-family: 'Arial Black', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
        }
        .stFileUploader {
            text-align: center;
        }
        .stMarkdown {
            font-size: 16px;
        }
    </style>
    """
    st.markdown(background_color, unsafe_allow_html=True)

set_background()

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text.strip() if text else "No text found"

# Function to extract name using Spacy NLP
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not found"

# Function to extract email using regex
def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(email_pattern, text)
    return match.group(0) if match else "Not found"

# Function to extract phone numbers using regex
def extract_phone_number(text):
    phone_pattern = r"(\+?[0-9]{1,4}[\s-]?)?(\(?[0-9]{3}\)?[\s-]?[0-9]{3}[\s-]?[0-9]{4})"
    match = re.search(phone_pattern, text)
    return match.group(0) if match else "Not found"

# Function to extract predefined skills
def extract_skills(text):
    skills_list = ["Python", "Java", "C++", "Machine Learning", "Data Science", "SQL", "TensorFlow", "Excel"]
    extracted_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return extracted_skills if extracted_skills else "Not found"

# Streamlit UI
st.title("📄 Resume screening APP")

# Upload PDF Resume
uploaded_file = st.file_uploader("Upload a Resume (PDF only)", type="pdf")

if uploaded_file:
    # Save the uploaded file
    temp_file_path = "uploaded_resume.pdf"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success("✅ File Uploaded Successfully!")
    # Extract text from PDF
    text = extract_text_from_pdf(temp_file_path)
    if st.button("🔍 Process Resume"):
        with st.spinner("Extracting information... ⏳"):
            text = extract_text_from_pdf(uploaded_file)
            name = extract_name(text)
            email = extract_email(text)
            phone = extract_phone_number(text)
            skills = extract_skills(text)

    if text == "No text found":
        st.error("❌ Unable to extract text from the uploaded PDF. Try another file.")
    else:
        # Extract structured data
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone_number(text)
        skills = extract_skills(text)

        # Display extracted data
        st.subheader("✅ Extracted Information")
        st.write(f"**🧑 Name**: {name}")
        st.write(f"**📧 Email**: {email}")
        st.write(f"**📞 Phone Number**: {phone}")
        st.write(f"**🛠️ Skills**: {', '.join(skills) if skills != 'Not found' else 'Not found'}")

        # Prepare JSON for download
        extracted_data = {
            "Name": name,
            "Email": email,
            "Phone Number": phone,
            "Skills": skills
        }

        # Add Download Button
        st.download_button(
            label="⬇️ Download Extracted Data",
            data=json.dumps(extracted_data, indent=4),
            file_name="parsed_resume.json",
            mime="application/json"
        )

        # Debugging: Display extracted text
        with st.expander("Show Extracted Text"):
            st.text(text)
