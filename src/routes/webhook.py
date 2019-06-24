from flask import Blueprint, request, jsonify, make_response, Response
from flask_assistant import Assistant, ask, tell
from src.handler.main import handle_action

hook_route = Blueprint('hook_route', __name__)


@hook_route.route("/webhook", methods=['GET', 'POST'])
def hook():
    # return response
    response = results()
    print(response)
    return make_response(jsonify(response))


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    print('this is request--------------------------------------------------------------------------', req,
          '===============================')
    try:
        action = req.get('result').get('action')
    except:
        action = req.get('queryResult').get('action')
    result = handle_action(action)
    return result
