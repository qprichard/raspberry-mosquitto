import logging

from asyncio import *
from aiocoap import *
from config import SERVER_HOST
import json

logging.basicConfig(level=logging.INFO)

async def get(sensor):
    protocol = await Context.create_client_context()

    payload = json.dumps({ 'sensor': sensor }).encode('utf-8')
    request = Message(code=GET, payload=payload, uri= f"coap://{SERVER_HOST}/sensor")

    try:
        response = await protocol.request(request).response

    except Exception as e:
        print('Failed to fetch resource')
        print(e)
    else:
        print(f"Result: {response.code} \n {response.payload}")


async def put(sensor, value):
    context = await Context.create_client_context()

    payload = json.dumps({ sensor: value }).encode('utf-8')
    request = Message(code=PUT, payload=payload, uri=f"coap://{SERVER_HOST}/sensor")

    response = await context.request(request).response

    print(f"Result: {response.code} \n {response.payload}")

# if __name__ == "__main__":
#     get_event_loop().run_until_complete(get('pression'))
#     #get_event_loop().run_until_complete(put('pression', 12))
