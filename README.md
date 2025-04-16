Resume Screening App
Overview
The Resume Screening App is a web-based application built with Streamlit to extract key information from PDF resumes. It uses natural language processing (NLP) and regular expressions to identify details such as name, email, phone number, and skills. The extracted data is displayed in a user-friendly interface and can be downloaded as a JSON file. The app is designed to streamline resume screening processes for recruiters or HR professionals.
Features

PDF Resume Parsing: Extracts text from uploaded PDF resumes using pdfplumber.
Information Extraction:
Name: Identifies names using SpaCy's NLP model (en_core_web_sm).
Email: Extracts email addresses using regex.
Phone Number: Extracts phone numbers with flexible formats using regex.
Skills: Matches predefined skills (e.g., Python, Java, Machine Learning) from the resume text.


User Interface: Built with Streamlit, featuring a gradient background, styled buttons, and a file uploader.
Downloadable Output: Exports extracted data as a JSON file.
Debugging: Option to view raw extracted text for troubleshooting.
Responsive Design: Custom CSS for an enhanced user experience.

Prerequisites
To run the application, ensure you have the following installed:

Python 3.8+
System Dependencies (for pdfplumber and other libraries):
On Linux: sudo apt-get install libpdf2
On macOS: brew install pdf2
On Windows: No additional system dependencies typically required.



Installation

Clone the Repository:
git clone <repository-url>
cd resume-screening-app


Set Up a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies: Create a requirements.txt with the following:
streamlit
pdfplumber
spacy
nltk
regex

Then run:
pip install -r requirements.txt


Download SpaCy Model:
python -m spacy download en_core_web_sm


Download NLTK Resources:
The app automatically downloads punkt and stopwords on first run, but you can pre-download them:
python -m nltk.downloader punkt stopwords



Running the Application

Start the Streamlit App:
streamlit run app.py

Replace app.py with the name of your Python script.

Access the App: Open your browser and navigate to http://localhost:8501.


Usage

Upload a Resume: Use the file uploader to select a PDF resume.
Process the Resume: Click the "Process Resume" button to extract information.
View Extracted Data: See the extracted name, email, phone number, and skills displayed on the screen.
Download JSON: Click the "Download Extracted Data" button to save the extracted information as a JSON file.
Debug (Optional): Expand the "Show Extracted Text" section to view the raw text extracted from the PDF.

File Structure
resume-screening-app/
├── app.py                # Main Streamlit application script
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── venv/                 # Virtual environment (if created)

Notes

PDF Text Extraction:
The app relies on pdfplumber to extract text. If the PDF is image-based (scanned), text extraction will fail unless OCR is integrated.
Ensure the PDF contains selectable text for accurate extraction.


NLP Model:
Uses SpaCy’s en_core_web_sm for name extraction. Larger models (en_core_web_md or en_core_web_lg) may improve accuracy but require more resources.


Skills List:
The predefined skills list is hardcoded (Python, Java, etc.). Customize the skills_list in the code to match your needs.


Regex Patterns:
Email and phone number patterns are designed for common formats. Modify the regex in extract_email and extract_phone_number for specific use cases.


Styling:
Custom CSS is applied for a gradient background, styled buttons, and centered text. Adjust the set_background function to change the appearance.



Troubleshooting

PDF Text Extraction Fails:
Ensure the PDF is not image-based. If it is, consider integrating an OCR library like pytesseract.
Check for errors in the Streamlit console and verify pdfplumber is installed.


SpaCy Model Not Found:
Run python -m spacy download en_core_web_sm to install the model.


NLTK Resources Missing:
Run python -m nltk.downloader punkt stopwords to download required resources.


Streamlit Errors:
Ensure all dependencies are installed (pip install -r requirements.txt).
Run streamlit run app.py from the correct directory.


No Information Extracted:
Verify the resume contains the expected data (e.g., name, email).
Check the raw extracted text in the "Show Extracted Text" expander for debugging.



Future Enhancements

Integrate OCR (e.g., pytesseract) to handle image-based PDFs.
Expand the skills list dynamically using a machine learning model or external database.
Add support for extracting education, work experience, and certifications.
Implement a scoring system to rank resumes based on job requirements.
Enhance the UI with more interactive elements (e.g., resume preview, batch processing).

Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.


