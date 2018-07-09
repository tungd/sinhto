import order.routing
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        order.routing.websocket_urlpatterns
    ),
})
