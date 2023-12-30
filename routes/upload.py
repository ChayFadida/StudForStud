from flask import Blueprint, request, redirect
from config.app_contex import data_handler
import magic

upload_bp = Blueprint('upload', __name__, url_prefix='/upload')

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_pdf_content(file_content):
    """
    Check if the given file content represents a valid PDF.

    Args:
        file_content (bytes): The content of the file as bytes.

    Returns:
        bool: True if the file content is a valid PDF, False otherwise.
    """
    try:
        # Use python-magic to check the file's MIME type
        mime = magic.Magic()
        mime_type = mime.from_buffer(file_content)
        return 'pdf' in mime_type.lower()
    except Exception as e:
        # Handle exceptions (e.g., if python-magic is not installed or encounters an error)
        print(f"Error checking PDF content: {e}")
        return False

@upload_bp.route('/', methods=['POST'])
def upload_file():
    """
    Handle the file upload POST request.

    This route is responsible for processing uploaded files and associated form data.

    Returns:
        Flask Response: A redirect to the root URL.
    """
    try:
        semester = request.form['semester'].strip()
        grade = request.form['grade'].strip()
        course_code = request.form['course_code'].strip()
        notes = request.form['notes'].strip()
        exam_type = request.form['exam_type'].strip()
        lecturer = request.form['lecturer'].strip()
        uploaded_file = request.files['file-upload']
        if not allowed_file(uploaded_file.filename):
            return "Invalid file type. Please select a PDF file.", 400
        file_content = uploaded_file.read()
        # Check if the file is a valid PDF
        if not is_pdf_content(file_content):
            return "Invalid file format. Please select a valid PDF file.", 400
        data_handler.upload_test(file_content, course_code, semester, grade, notes, lecturer, exam_type)
        return redirect('/')
    except KeyError:
        return "Invalid form data", 400
