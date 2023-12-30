from flask import Blueprint, request, redirect
from config.app_contex import data_handler

edit_bp = Blueprint('edit', __name__, url_prefix='/edit')

@edit_bp.route('/', methods=['POST'])
def edit_file():
    """
    Handle the file editing POST request.

    This route is responsible for processing edited file metadata and form data.

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
        file_name = request.form['hidden-file-name'].strip()
        data_handler.edit_data(semester, grade ,course_code ,notes ,exam_type ,lecturer ,file_name)
        return redirect('/')
    except KeyError:
        return "Invalid form data", 400