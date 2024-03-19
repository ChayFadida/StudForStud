import os
from PyPDF2 import PdfReader, PdfWriter
import shutil
from config.logger_config import log

class LocalClient:
    def __init__(self, base_dir='/nfs/studforstud'):
        self.base_dir = base_dir

    def get_base_dir(self):
        return self.base_dir

    def create_directory_if_not_exists(self, new_dir: str) -> None:
        """
        Create a new directory if it does not exist already.

        Args:
            new_dir (str): The path to the directory to be created.
        """
        full_path = os.path.join(self.base_dir, new_dir)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    def write_file_with_metadata(self, input_file_path: str, output_file_name: str, pdf_metadata: dict) -> None:
        """
        Create a new PDF file with metadata by adding metadata to an existing PDF file or creating a new one.

        Args:
            input_file_path (str): The path to the input PDF file (existing or new).
            output_file_name (str): The name of the output PDF file with added metadata.
            pdf_metadata (dict): Metadata to be added to the PDF file.
        """
        # Ensure input and output files have .pdf extension
        if not input_file_path.endswith('.pdf'):
            raise ValueError("Input file must have a .pdf extension")
        if not output_file_name.endswith('.pdf'):
            output_file_name += '.pdf'

        # Create a PDF writer for the output
        pdf_writer = PdfWriter()

        output_file_path = os.path.join(self.base_dir, output_file_name)

        if os.path.exists(output_file_path):
            # If the output file already exists, generate a unique name
            base_name, ext = os.path.splitext(output_file_path)
            count = 1
            while os.path.exists(output_file_path):
                output_file_path = f"{base_name}_{count}{ext}"
                count += 1

        # Read the existing PDF (if it exists)
        if os.path.exists(input_file_path):
            pdf_reader = PdfReader(open(input_file_path, 'rb'))

            # Copy the existing pages to the output PDF
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        # Add metadata to the output PDF
        pdf_writer.add_metadata(pdf_metadata)

        # Save the PDF with metadata
        with open(output_file_path, 'wb') as pdf_output:
            pdf_writer.write(pdf_output)

        log.debug(f"PDF file with metadata saved to '{output_file_path}'.")

    def add_metadata_to_file(self, file_path: str, pdf_metadata: dict) -> None:
        """
        Add metadata to an existing PDF file.

        Args:
            file_path (str): The path to the PDF file to which metadata will be added.
            pdf_metadata (dict): Metadata to be added to the PDF file.
        """
        # Create a PDF writer for the file
        pdf_writer = PdfWriter(file_path)

        # Add metadata to the file
        pdf_writer.add_metadata(pdf_metadata)

        # Save the file with metadata
        pdf_writer.write()

        log.debug(f"Metadata added to file '{file_path}'.")

    def get_metadata_from_file(self, file_path: str) -> dict:
        """
        Extract metadata from an existing PDF file.

        Args:
            file_path (str): The path to the PDF file from which metadata will be extracted.

        Returns:
            dict: A dictionary containing the extracted metadata.
        """
        pdf_reader = PdfReader(open(file_path, 'rb'))
        metadata_dict = {}

        # Extract metadata properties and values and store them in a dictionary
        for key, value in pdf_reader.metadata.items():
            if isinstance(value, bytes):
                # If the value is bytes, decode it into a string
                value = value.decode('utf-8', errors='ignore')
            metadata_dict[key] = value

        return metadata_dict

    def get_all_metadata(self) -> list:
        """
        Retrieve metadata from all PDF files within the base directory.

        Returns:
            list: A list of dictionaries, each containing metadata from a PDF file.
        """
        metadata_array = []

        for root, dirs, files in os.walk(self.base_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                metadata = self.get_metadata_from_file(file_path)
                if metadata:
                    metadata_array.append(metadata)

        return metadata_array
    
    def change_metadata_by_name(self, file_name: str, pdf_metadata: dict) -> None:
        """
        Change the metadata of an existing PDF file by its name.

        Args:
            file_name (str): The name of the PDF file (with extension) for which metadata will be changed.
            pdf_metadata (dict): New metadata to replace the existing metadata.
        """
        for root, dirs, files in os.walk(self.base_dir):
            if file_name in files:
                file_path = os.path.join(root, file_name)

                # Read the existing PDF
                pdf_reader = PdfReader(open(file_path, 'rb'))

                # Create a PDF writer for the file
                pdf_writer = PdfWriter()

                # Copy pages from the original PDF
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                # Add metadata to the file
                pdf_writer.add_metadata(pdf_metadata)

                # Save the file with the updated metadata
                with open(file_path, 'wb') as pdf_output:
                    pdf_writer.write(pdf_output)

                log.debug(f"Metadata changed for file '{file_path}'.")
                return

        log.debug(f"File with name '{file_name}' not found in the base directory.")

    def delete_file(self, file_path: str) -> None:
        """
        Delete a file from the specified file path.

        :param file_path: The path to the file to be deleted.
        """
        try:
            os.remove(file_path)
        except Exception as e:
            # Handle any exceptions that may occur during the force delete.
            log.error(f"Error: {str(e)}")

    def delete_fuse_hidden_files(self, directory_path: str) -> None:
        """
        Delete files with names starting with '.fuse_hidden' within a directory.

        :param directory_path: The path to the directory containing the files to be deleted.
        """
        try:
            for filename in os.listdir(directory_path):
                if filename.startswith('.fuse_hidden'):
                    file_path = os.path.join(directory_path, filename)
                    os.remove(file_path)
                    log.debug(f"Deleted: {file_path}")
            log.debug("Finished deleting .fuse_hidden files.")
        except Exception as e:
            log.error(f"An error occurred: {str(e)}")

    def copy_file(self, source_path: str, destination_path: str) -> None:
        """
        Copy a file from the source path to the destination path.
        
        :param source_path: The path to the source file.
        :param destination_path: The path to the destination where the file will be copied.
        """
        try:
            # Check if the destination directory exists, and create it if not.
            dest_dir = os.path.dirname(destination_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            shutil.copy2(source_path, destination_path)
            log.debug(f"File copied from '{source_path}' to '{destination_path}' successfully.")
        except Exception as e:
            # Handle any exceptions that may occur during the copy process.
            log.error(f"Error: {str(e)}")

    def change_file_name(self, current_path: str, new_name: str) -> None:
        """
        Change the name of a file at the current path to a new name.

        :param current_path: The path to the current file.
        :param new_name: The new name for the file.
        """
        try:
            # Check if the file exists at the current path.
            if not os.path.exists(current_path):
                log.debug(f"File '{current_path}' does not exist.")
                return

            # Get the directory of the current file and create a new path with the new name.
            current_directory = os.path.dirname(current_path)
            new_path = os.path.join(current_directory, new_name)

            # Rename the file to the new name.
            os.rename(current_path, new_path)

            (f"File '{current_path}' renamed to '{new_name}' successfully.")
        except Exception as e:
            # Handle any exceptions that may occur during the renaming process.
            log.error(f"Error: {str(e)}")

def main():
    # Initialize the PDF metadata manager
    pdf_metadata_manager = LocalClient()

    # Write a PDF file with metadata
    pdf_metadata = {
        '/course_code': 'CS101',
        '/course_name': 'Introduction to Computer Science',
        '/grade': '123',
        '/semester': 'Spring 2023',
        '/exam_type': 'A',
        '/lecturer': 'Dr. Smith',
        '/notes': 'Sample notes for the PDF'
    }
    pdf_metadata_manager.change_metadata_by_name('61743_2023_summer_99', pdf_metadata)

if __name__ == "__main__":
    main()