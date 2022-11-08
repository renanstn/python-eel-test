import base64
import json
from os.path import exists
import urllib3

import requests
import eel


urllib3.disable_warnings()


@eel.expose
def save_data(data: dict) -> None:
    with open("data.json", "w") as file:
        json.dump(data, file)


@eel.expose
def load_data() -> dict:
    if not exists("data.json"):
        return
    with open("data.json", "r") as file:
        data = json.load(file)
        return data


@eel.expose
def send_data(url: str, table: str, query: str, fields: str) -> list:
    request_url = f"{url}/snow/genericQuery"
    fields_list = fields.split('\n')
    request_fields = ",".join(fields_list)
    request_headers = {
        'Content-Type': 'application/json',
    }
    request_payload = {
        'table': table,
        'sysparam_fields': request_fields,
        'sysparam_display_value': True,
        'sysparam_exclude_reference_link': True,
        'sysparam_limit': 5000,
        'sysparam_offset': 0,
        'sysparam_query': query
    }
    request_data = json.dumps(request_payload)
    response = requests.post(
        request_url,
        headers=request_headers,
        data=request_data,
        verify=False
    )
    results = response.json().get('result', [])
    if results:
        results = base64.b64decode(results)
        result_str = results.decode("utf-8")
        return json.loads(f'[{result_str}]')
    return []
