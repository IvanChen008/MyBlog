import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web


# logging.basicConfig(level=logging.INFO)


async def index(request):
    resp = web.Response(text="<h1>Awesome</h1>")#(body=b'<div><h1>Awesome</h1></div>')
    resp.content_type = 'text/html'
    return resp


async def init(loop):
    server = web.Server(index)
    srv = await loop.create_server(server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


