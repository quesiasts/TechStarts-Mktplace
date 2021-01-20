from flask import render_template, Blueprint

from backend.controller.log_controller import LogController

CONTROLLER = LogController()

log_bp = Blueprint('log', __name__)


@log_bp.route('/listagem_logs')
def list_log():
    logs = CONTROLLER.read_all()
    return render_template('listagem_logs.html', lista_logs=logs)
