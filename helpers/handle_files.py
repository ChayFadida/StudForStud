import os
from config.bradue_conf import season_dict, moded_dict, get_course_name, generate_years_array
from werkzeug.utils import secure_filename

class HandleData:
    def __init__(self, file_client):
        """
        Initialize a HandleData instance.

        Args:
            file_client: An instance of a file client that interacts with file storage.
        """
        self.file_client = file_client
        self.temp_dir = 'temp'

    def upload_test(self, file_content: bytes, course_code: str, semester: str, grade: str, notes: str, lecturer: str, exam_type: str) -> None:
        """
        Upload a test file with associated metadata.

        Args:
            file_content (bytes): The content of the test file as bytes.
            course_code (str): The code of the course for which the test is being uploaded.
            semester (str): The semester in which the test was conducted.
            grade (str): The grade or level of the test (e.g., 'midterm', 'final').
            notes (str): Additional notes or information about the test.
            lecturer (str): The name of the lecturer who conducted the test.
            exam_type (str): The type of exam (e.g., 'moed').

        Returns:
            None
        """
        file_name = self.generate_file_name(course_code, semester, grade)
        file_name = secure_filename(file_name)

        metadata = self.generate_json_metadata(course_code, semester, grade, notes, lecturer, exam_type, file_name)

        # Dynamically create the temporary directory if it doesn't exist
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        
        # Temporarily save the file content to a local file
        temp_file_path = os.path.join(self.temp_dir, file_name)

        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(file_content)
        self.file_client.write_file_with_metadata(temp_file_path, file_name, metadata)
        # Clean up the temporary file
        os.remove(temp_file_path)

    

    def generate_file_name(self, course_code: str, semester: str, grade: str) -> str:
        """
        Generate a unique file name based on course, semester, and grade.

        Args:
            course_code (str): The code of the course.
            semester (str): The semester in which the test was conducted.
            grade (str): The grade or level of the test.

        Returns:
            str: The generated file name.
        """
        semester_info = semester.split(' ')
        year = semester_info[0]
        semester_part = season_dict[semester_info[1]]
        return f"{course_code}_{year}_{semester_part}_{grade}.pdf"
    
    def generate_json_metadata(self, course_code: str, semester: str, grade: str, notes: str, lecturer: str, exam_type: str, file_name: str) -> dict:
        """
        Generate metadata in JSON format for a test file.

        Args:
            course_code (str): The code of the course.
            semester (str): The semester in which the test was conducted.
            grade (str): The grade or level of the test.
            notes (str): Additional notes or information about the test.
            lecturer (str): The name of the lecturer who conducted the test.
            exam_type (str): The type of exam (e.g., 'moed').
            file_name (str): The name of the test file.

        Returns:
            dict: Metadata in JSON format.
        """
        data = {
            "/course_code": course_code,
            "/grade": grade,
            "/semester": semester,
            "/exam_type": exam_type, # moed
            "/lecturer": lecturer,
            "/notes": notes,
            "/file_name": file_name,
            "/download_link": f"/files/{file_name}"
        }
        return data

    def get_data(self) -> dict:
        """
        Retrieve data including table data, exam dates, and exam type dictionary.

        Returns:
            dict: A dictionary containing table data, exam dates, and exam type dictionary.
        """
        table_data = self.file_client.get_all_metadata()
        for metadata in table_data:
            metadata['/course_name'] = get_course_name(metadata['/course_code']) 
            metadata['/exam_type'] = moded_dict[metadata['/exam_type']]
        data = {'table_data': table_data, 'exam_dates': generate_years_array(), 'moed_dict': {value: key for key, value in moded_dict.items()}}
        return data

    def edit_data(self, semester: str, grade: str, course_code: str, notes: str, exam_type: str, lecturer: str, file_name: str) -> None:
        """
        Edit the metadata of an existing test file.

        Args:
            semester (str): The semester in which the test was conducted.
            grade (str): The grade or level of the test.
            course_code (str): The code of the course.
            notes (str): Additional notes or information about the test.
            exam_type (str): The type of exam (e.g., 'moed').
            lecturer (str): The name of the lecturer who conducted the test.
            file_name (str): The name of the test file to be edited.

        Returns:
            None
        """
        for root, dirs, files in os.walk(self.file_client.get_base_dir()):
            if file_name in files:
                original_file_path = os.path.join(root, file_name)
        current_metadata = self.file_client.get_metadata_from_file(original_file_path)
        if current_metadata['/course_code'] != course_code or current_metadata['/semester'] != semester or  current_metadata['/grade'] != grade:
            file_name = self.generate_file_name(course_code, semester, grade)
        self.file_client.change_file_name(original_file_path, file_name)
        metadata = self.generate_json_metadata(course_code, semester, grade, notes, lecturer, exam_type, file_name)
        self.file_client.change_metadata_by_name(file_name, metadata)
        return None
        

