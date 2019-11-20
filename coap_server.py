import datetime
import logging
import asyncio

import aiocoap.resource as resource
import aiocoap
import json

class SensorResource(resource.Resource):
    def __init__(self):
        self.content = { 'humidity': 0 }

    def set_content(self, key, content):
        self.content[key] = content

    async def render_get(self, request):
        payload = json.loads(request.payload.decode())

        sensor = payload.get('sensor', None)
        response = self.content.get(sensor, {})
        to_send = json.dumps({sensor: response}).encode('utf-8')
        return aiocoap.Message(payload=to_send)

    async def render_put(self, request):
        request = json.loads(request.payload.decode())
        key, content = list(request.items())[0]
        self.set_content(key, content)
        to_send = json.dumps(self.content).encode('utf-8')
        return aiocoap.Message(code=aiocoap.CHANGED, payload=to_send)

# logging setup
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    #Resource tree creation
    root = resource.Site()

    root.add_resource(['sensor'], SensorResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
