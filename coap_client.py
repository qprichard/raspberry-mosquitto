import logging

from asyncio import *
from aiocoap import *
from config import COAP_HOST

logging.basicConfig(level=logging.INFO)

async def get():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri= f"coap://{COAP_HOST}/time")

    try:
        response = await protocol.request(request).response

    except Exception as e:
        print('Failed to fetch resource')
        print(e)
    else:
        print(f"Result: {response.code} \n {response.payload}")


async def put():
    context = await Context.create_client_context()

    await sleep(2)

    payload = b"I hope this will not break the internet..."
    request = Message(code=PUT, payload=payload, uri=f"coap://{COAP_HOST}/other/block")

    response = await context.request(request).response

    print(f"Result: {response.code} \n {response.payload}")

if __name__ == "__main__":
    get_event_loop().run_until_complete(get())
    get_event_loop().run_until_complete(put())
