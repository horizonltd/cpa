from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import hub.routing

#This serve the websocking routing
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            #Ref to app routing
            hub.routing.websocket_urlpatterns
            
        )

    )
})



