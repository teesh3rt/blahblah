import asyncio
import websockets
import json

clients = []

async def bbsend(websocket, msg):
    print(f"> {msg}")
    await websocket.send(json.dumps(msg))

async def bbrecv(websocket):
    msg = await websocket.recv()
    res = json.loads(msg)
    print(f"< {res}")
    return res

async def blahblah(ws: websockets.WebSocketServer):
    # await websocket.send("blahblah")
    await bbsend(ws, {
        "what": "system",
        "content": "bb"
    })

    bbok = await bbrecv(ws)

    if bbok["content"] != "bbok":
        await bbsend(ws, {
            "what": "system",
            "content": "bbhangup"
        })

        await ws.close()

    await bbsend(ws, {
        "what": "system",
        "content": "bbidentification"
    })

    msg = await bbrecv(ws)

    service = msg["service"]

    clients.append(ws)

    await bbsend(ws, {
        "what": "system",
        "content": "bbready"
    })

    while True:
        msg = await bbrecv(ws)

        for client in clients:
            await bbsend(client, {
                "what": "system",
                "content": "gotmessage",
                "using": service,
                "from": msg["user"],
                "message": msg["content"],
                "channel": msg["channel"]
            })

async def main():
    async with websockets.serve(blahblah, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())