from channels.routing import route
channels_routing = [
    route('websocket.receive', 'chat.consumers.ws_echo')
]
