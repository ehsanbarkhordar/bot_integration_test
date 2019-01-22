import json

from balebot.models.constants.document_type import DocumentType
from balebot.models.messages import TextMessage
from server_models.document_message import ServerDocumentMessage


class ServerPhotoMessage(ServerDocumentMessage):
    def __init__(self, peer, file_id="7406116810654813185", access_hash="201707397", name="Page.jpg",
                 file_size="385192", mime_type="image/jpeg", thumb="", width=80, height=80,
                 ext_width=None, ext_height=None, file_storage_version=1, caption_text=TextMessage("hey"),
                 checksum=None, algorithm=None, sender=None):
        super().__init__(peer, file_id, access_hash, name, file_size, mime_type, caption_text, checksum, algorithm,
                         file_storage_version, sender)

        self.thumb = str(thumb)
        self.width = int(width)
        self.height = int(height)
        self.ext_width = int(ext_width) if ext_width else width
        self.ext_height = int(ext_height) if ext_height else height

    def get_json_object(self):
        data = super().get_json_object()
        data["thumb"] = {
            "width": self.width,
            "height": self.height,
            "thumb": self.thumb
        }
        data["ext"] = {
            "$type": DocumentType.photo_document,
            "width": self.ext_width,
            "height": self.ext_height,
        }

        return data

    def get_json_str(self):
        return json.dumps(self.get_json_object())
