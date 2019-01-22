import json

import datetime


class ServerReadUpdate:
    def __init__(self, request_id):
        self.date = datetime.datetime.now().timestamp()
        self.request_id = request_id

    def get_json_object(self):
        data = {"$type": "Response", "id": self.request_id, "body": {"date": self.date}}
        return data

    def get_json_str(self):
        return json.dumps(self.get_json_object())
