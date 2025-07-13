from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("¡Cliente WebSocket conectado!")

    async def receive(self, text_data):
        await self.send(text_data=f"Eco: {text_data}")