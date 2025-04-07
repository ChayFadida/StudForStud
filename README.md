# StudForStud - Test Notes Sharing and Learning Platform

Welcome to StudForStud, a web application designed to facilitate students in sharing their test notes and learning resources. StudForStud allows students to upload their test notes, categorize them by semester and year, and associate them with the name of the lecturer. Users can also access and learn from test notes shared by their peers and lecturers in PDF format. The application is scalable due to its use of NFS for storing notes and is containerized with Docker for easy deployment.

## Getting Started

Follow these instructions to get the StudForStud application up and running on your system.

### Prerequisites
 
Before you begin, make sure you have the following software installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the StudForStud repository from GitHub to your local machine:

2. Change directory to the project folder:

3. Open the `config/app_context.py` file and modify the `base_dir` variable if you want to change the NFS storage directory. By default, the notes will be stored in `/nfs/studforstud`.

4. Create a volume on your filesystem for the NFS storage directory. Replace `/path/to/studforstud` with your desired directory path:

5. Update the NFS export configuration on your server to allow access to the `/path/to/studforstud` directory. Refer to the documentation for your NFS server for instructions on how to do this.

6. Use Docker Compose to build and run the StudForStud web application: docker-compose up -d web


The StudForStud application should now be accessible at `http://localhost` in your web browser.

## Usage

1. Access the StudForStud web application at `http://localhost` (or your server's IP if deployed remotely).

2. Sign in or register to create an account.

3. Upload your test notes, specifying the semester, year, and the lecturer's name.

4. Explore and access test notes shared by other students and lecturers.

5. Use the PDF viewer to study and learn from the shared notes.

## Contributing

We welcome contributions from the open-source community. To contribute to the StudForStud project, please follow these steps:

1. Fork the project on GitHub.

2. Create a new branch for your feature or bug fix:
   
3. Make your changes and commit them.

4. Push your changes to your forked repository:

5. Create a pull request on the original StudForStud repository, explaining the changes you made and why they are valuable.

6. Your pull request will be reviewed, and once approved, it will be merged into the main project.
   
If you have any questions or need assistance, feel free to contact us:

- Email: ChayFadida1997@gmail.com

We hope StudForStud enhances your learning experience and makes sharing test notes easier for all students!

