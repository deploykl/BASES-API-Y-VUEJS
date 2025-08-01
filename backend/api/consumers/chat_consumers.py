from channels.generic.websocket import AsyncWebsocketConsumer
import json
import uuid

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "chat_room"
        self.room_group_name = f"chat_{self.room_name}"
        self.user_id = str(uuid.uuid4())[:8]  
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        await self.send(json.dumps({
            'type': 'system',
            'message': f'Tu ID de usuario es: {self.user_id}'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': self.user_id,
                'is_me': False  # Para que otros sepan que no es su mensaje
            }
        )

    async def chat_message(self, event):
        # Enviar mensaje al WebSocket con información del remitente
        await self.send(json.dumps({
            'type': 'chat',
            'message': event['message'],
            'sender_id': event['sender_id'],
            'is_me': event.get('is_me', False)
        }))
        
