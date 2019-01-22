import json

from balebot.models.base_models import Peer
from balebot.models.constants.errors import Error
from balebot.models.constants.message_type import MessageType
from balebot.models.messages import TextMessage


class ServerDocumentMessage:
    def __init__(self, peer, file_id, access_hash, name, file_size, mime_type, caption_text=None, checksum=None,
                 algorithm=None, file_storage_version=1, sender=None):
        if isinstance(peer, Peer):
            self.peer = peer
        else:
            raise ValueError(Error.unacceptable_object_type)
        if isinstance(sender, Peer):
            self.sender = sender
        else:
            self.sender = peer
        self.file_id = str(file_id)
        self.access_hash = str(access_hash)
        self.file_size = str(file_size)
        self.name = str(name)
        self.mime_type = str(mime_type)

        if caption_text:
            if isinstance(caption_text, TextMessage):
                self.caption_text = caption_text
        else:
            self.caption_text = None

        self.checksum = str(checksum) if checksum else "checkSum"
        self.algorithm = str(algorithm) if algorithm else "algorithm"
        self.file_storage_version = int(file_storage_version)

    def get_json_object(self):
        data = {
            "$type": "FatSeqUpdate",
            "seq": 19979,
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
                "date": "1548071082638",
                "randomId": "-5360894418397220326",
                "message": {
                    "$type": MessageType.document_message,
                    "fileId": self.file_id,
                    "accessHash": self.access_hash,
                    "fileSize": self.file_size,
                    "name": self.name,
                    "mimeType": self.mime_type,
                    "thumb": None,
                    "ext": None,
                    "caption": self.caption_text.get_json_object() if self.caption_text else None,
                    "checkSum": self.checksum,
                    "algorithm": self.algorithm,
                    "fileStorageVersion": self.file_storage_version
                }
            },
            "users": [],
            "groups": []
        }
        return data

    def get_json_str(self):
        return json.dumps(self.get_json_object())
