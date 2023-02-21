# login_jannah/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class LoginWithGoogleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.workflow_name = self.scope["url_route"]["kwargs"]["workflow_name"]
        self.workflow_group_name = "login_%s" % self.workflow_name
        print(f"scope: {self.scope}")
        # Join workflow group
        await self.channel_layer.group_add(self.workflow_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave workflow group
        await self.channel_layer.group_discard(self.workflow_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        print(f"messsage: {message}")
        # Send message to room group
        await self.channel_layer.group_send(
            self.workflow_group_name, {"type": "workflow_message", "message": message}
        )

    # Receive message from room group
    async def workflow_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))