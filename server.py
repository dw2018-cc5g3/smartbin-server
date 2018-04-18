"""

"""

from flask import Flask, Response, jsonify, request
app = Flask(__name__)
from pprint import pformat

from db_interface import db_interface_pg as dbi


@app.route('/user/<can_dirty>')
def get_user_by_can(can_dirty):
    try:
        response_raw = dbi.get_user_by_can(can_dirty, as_json=True)
        if response_raw == '':
            return jsonify(error='no user')
        else:
            return Response(response_raw,
                            mimetype='application/json')
    except ValueError as e:
        return jsonify(error=e.args[0])


@app.route('/item/by_user/<int:user_id>')
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


@app.route('/user', methods=['POST'])
def create_user():
    try:
        params_raw = request.get_json()
        params = {k: v for k, v in params_raw.items()
                  if k in ('can', 'name', 'display_name', 'phone_number')}

        if len(params) != 4:
            raise ValueError('Parameter error')

        user_id = dbi.create_user(
            **params,
            active=True
        )

        return jsonify(user_id=user_id)
    except ValueError as e:
        return jsonify(error=e.args[0])


@app.route('/item', methods=['POST'])
def create_item():
    try:
        params_raw = request.get_json()
        params = {k: v for k, v in params_raw.items()
                  if k in ('score', 'mass', 'category', 'deposited_by')}

        if len(params) != 4:
            raise ValueError('Parameter error')

        item_id = dbi.create_item(**params)

        return jsonify(item_id=item_id)
    except ValueError as e:
        return jsonify(error=e.args[0])
