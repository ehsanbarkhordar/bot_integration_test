#!/usr/bin/env python

import asyncio
# WS server example
import json

import websockets

from balebot.models.base_models import Peer
from balebot.models.constants.peer_type import PeerType
from server_models.photo_message import ServerPhotoMessage
from server_models.read_message import ServerReadUpdate
from server_models.text_message import ServerTextMessage


def get_request_id(client_request):
    client_request_json = json.loads(client_request)
    request_id = client_request_json.get("id")
    return request_id


async def start_bot(websocket, path):
    peer = Peer(PeerType.user, 201707397, "-2675024364153751067")
    server_text_message = ServerTextMessage("/start", peer)
    await websocket.send(server_text_message.get_json_str())
    name = await websocket.recv()
    request_id = get_request_id(name)
    read_update = ServerReadUpdate(request_id)
    await websocket.send(read_update.get_json_str())

    server_text_message = ServerPhotoMessage(peer)
    await websocket.send(server_text_message.get_json_str())
    client_request = await websocket.recv()
    request_id = get_request_id(client_request)
    read_update = ServerReadUpdate(request_id)
    await websocket.send(read_update.get_json_str())
    print("*********************SuccessFull*********************")
    await websocket.recv()


start_server = websockets.serve(start_bot, 'localhost', '8765')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
