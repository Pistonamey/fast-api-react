import socketio



# create socketio server
sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

# create an application with socketio server
sio_app = socketio.ASGIApp(
    socketio_server=sio,
    socketio_path='sockets'
)


@sio.event
async def connect(sid, environ):
    print(sid, 'backend connected')



@sio.event
async def disconnect(sid):
    print(sid, 'backend disconnected')

@sio.event
async def join_room(sid, data):
    print("inside join_room")
    print(sid)
    print(data["room"])
    if sid is None:
        # Handle the case when sid is None
        # You can log an error or send an error response to the client
        return

    if "room" not in data:
        # Handle the case when the 'room' key is not present in data
        # You can log an error or send an error response to the client
        return

    sio.enter_room(sid, data["room"])

@sio.event
async def send_message(sid, data):
    await sio.emit("receive_message", data, to=data["room"], skip_sid=sid)
