from flask import Blueprint, send_from_directory
from config.app_contex import data_handler
from werkzeug.utils import secure_filename
from monitoring.metrics import files_served, serves_per_file
import os
from config.logger_config import log

serve_file_bp = Blueprint('serve_file', __name__, url_prefix='/files')
file_directory = data_handler.file_client.base_dir

@serve_file_bp.route('/<path:filename>')
def serve_file(filename):
    """
    Serve uploaded files.

    This route is responsible for serving uploaded files by their filenames.

    Args:
        filename (str): The name of the file to serve.

    Returns:
        Flask Response: The requested file or a "File not found" message.
    """
    filename = secure_filename(filename)
    # Check if the file exists
    if os.path.exists(os.path.join(file_directory, filename)):
        # Use Flask's send_from_directory to serve the file
        files_served.inc()
        serves_per_file.labels(filename).inc()
        log.info(f"The following file served {filename}")
        return send_from_directory(file_directory, filename)
    else:
        return "File not found", 404