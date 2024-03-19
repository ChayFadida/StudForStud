from flask import Blueprint
from prometheus_client import generate_latest, REGISTRY
from monitoring.metrics import initialize_metrics

metrics_bp = Blueprint('metrics', __name__, url_prefix='/metrics')

@metrics_bp.route('/')
def metrics():
    initialize_metrics()
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; charset=utf-8'}