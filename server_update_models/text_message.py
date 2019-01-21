import json

from balebot.models.base_models import Peer
from balebot.models.constants.errors import Error


class ServerTextMessage:
    def __init__(self, text, peer, sender=None):
        self.text = str(text) if text else ""
        if isinstance(peer, Peer):
            self.peer = peer
        else:
            raise ValueError(Error.unacceptable_object_type)
        if isinstance(sender, Peer):
            self.sender = sender
        else:
            self.sender = peer

    def get_json_object(self):
        data = {
            "$type": "FatSeqUpdate",
            "seq": 19900,
            "body": {
                "$type": "Message",
                "peer": {
                    "$type": str(self.peer.type),
                    "id": self.peer.peer_id,
                    "accessHash": str(self.peer.access_hash)
                },
                "sender": {
                    "$type": str(self.sender.type),
                    "id": self.sender.peer_id,
                    "accessHash": str(self.sender.access_hash)
                },
                "date": "1547895898678",
                "randomId": "-1872862833315134147",
                "message": {
                    "$type": "Text",
                    "text": self.text
                }
            },
            "users": [],
            "groups": []
        }
        return data

    def get_json_str(self):
        return json.dumps(self.get_json_object())
