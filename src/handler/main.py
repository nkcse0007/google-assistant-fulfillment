from src.components.main import GoogleResponse
import requests
import json
import os


def handle_action(action):
    bot_data = get_botpenguin_res(action)
    response = get_response(bot_data)

    return response


def get_botpenguin_res(action):
    if action == 'input.unknown':
        params = {
            "event": "get_started",
            "s_id": "12345678",
            "ps_id": "863257040682292",
            "platform": "facebook"
        }
        res = requests.request("POST", os.environ.get('FLOW_URL'), data=json.dumps(params))
        print(res.json())
        return res.json()


def get_response(bot_data):
    cmp_obj = GoogleResponse()
    base_cmp = cmp_obj.base_cmp()
    count = 0
    for res in bot_data['response']:
        if res['type'] == 'statement':
            if count == 0:
                base_cmp['payload']['google']['expectUserResponse'] = True
                base_cmp['payload']['google']['richResponse']['items'].append(cmp_obj.simple(res['value']))
            else:
                resp = base_cmp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech']
                base_cmp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = resp+' '+res['value']
            count += 1
        elif res['type'] == 'question':
            base_cmp['payload']['google']['expectUserResponse'] = True
            base_cmp['payload']['google']['richResponse']['items'].append(cmp_obj.simple_tts(res['value']))

    return base_cmp
