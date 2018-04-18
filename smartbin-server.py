"""

"""

from flask import Flask, Response, jsonify
app = Flask(__name__)
from pprint import pformat

from db_interface import db_interface_pg as dbi


@app.route('/user/<can_dirty>')
def get_user_by_can(can_dirty):
    try:
        return Response(dbi.get_user_by_can(can_dirty, as_json=True),
                        mimetype='application/json')
    except ValueError as e:
        return jsonify(error=e.args[0])


@app.route('/items/by_user/<user_id>')
def get_user_items(user_id):
    try:
        return Response(dbi.get_user_items(user_id, as_json=True),
                        mimetype='application/json')
    except ValueError as e:
        return jsonify(error=e.args[0])


@app.route('/leaderboard')
def leaderboard():
    return Response(dbi.get_leaderboard(as_json=True),
                    mimetype='application/json')


