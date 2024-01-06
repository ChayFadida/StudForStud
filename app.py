from config.app_contex import data_handler
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
from routes import edit, upload, serve_file, metrics

app = Flask(__name__)

# Add the following lines to configure the static folder
app.config['STATIC_FOLDER'] = 'static'

# Use ProxyFix middleware to handle headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

app.register_blueprint(edit.edit_bp)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(serve_file.serve_file_bp)
app.register_blueprint(metrics.metrics_bp)

@app.route('/')
def index():
    """
    Render the main web page.

    This route is responsible for rendering the main web page, displaying data from the data handler.

    Returns:
        Flask Response: The rendered HTML template.
    """
    data = data_handler.get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
