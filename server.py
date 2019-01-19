#!/usr/bin/env python

# WS server example
import json

import asyncio
import websockets

from balebot.models.base_models import FatSeqUpdate
from balebot.models.messages import *
from balebot.models.server_updates.message_update_body import MessageUpdate


async def start_bot(websocket, path):
    update_message_dict = {
        "$type": "FatSeqUpdate",
        "seq": 19900,
        "body": {
            "$type": "Message",
            "peer": {
                "$type": "User",
                "id": 201707397,
                "accessHash": "-2675024364153751067"
            },
            "sender": {
                "$type": "User",
                "id": 201707397,
                "accessHash": "-2675024364153751067"
            },
            "date": "1547895898678",
            "randomId": "-1872862833315134147",
            "message": {
                "$type": "Text",
                "text": "/start"
            }
        },
        "users": [],
        "groups": []
    }
    update_message_str = json.dumps(update_message_dict)
    await websocket.send(update_message_str)
    # print(update_message_str)
    #
    name = await websocket.recv()
    print(f"< {name}")
    read_message_update_json = {"$type": "Response", "id": "0", "body": {"date": "1547895898824"}}
    read_message_update_str = json.dumps(read_message_update_json)
    await websocket.send(read_message_update_str)
    print("*********************SuccessFull")
    await websocket.recv()


start_server = websockets.serve(start_bot, 'localhost', '8765')
print(start_server)
print(type(start_server))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
