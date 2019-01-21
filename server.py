#!/usr/bin/env python

# WS server example
import json

import asyncio
import websockets

from balebot.models.base_models import Peer
from balebot.models.constants.peer_type import PeerType
from server_update_models.text_message import ServerTextMessage


async def start_bot(websocket, path):
    peer = Peer(PeerType.user, 201707397, "-2675024364153751067")
    server_text_message = ServerTextMessage("/start", peer)
    await websocket.send(server_text_message.get_json_str())
    name = await websocket.recv()
    read_message_update_json = {"$type": "Response", "id": "0", "body": {"date": "1547895898824"}}
    read_message_update_str = json.dumps(read_message_update_json)
    await websocket.send(read_message_update_str)
    print("*********************SuccessFull*********************")
    await websocket.recv()


start_server = websockets.serve(start_bot, 'localhost', '8765')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
