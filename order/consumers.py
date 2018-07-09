from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class OrderConsumer(WebsocketConsumer):
    def connect(self):
        self.order_id = self.scope['url_route']['kwargs']['order_id']
        self.group_name = 'order_%s' % self.order_id

        print(self.group_name, self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     order = models.Order.objects.first()
    #     serializer = serializers.OrderSerializer(order)
    #     self.send(text_data=json.dumps(serializer.data))

    def order_update(self, message):
        self.send(text_data=message['data'])
