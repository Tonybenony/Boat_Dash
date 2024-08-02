import asyncio
import websockets
import serial

ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=0)
print(ser)
# create handler for each connection
async def handler(websocket, path):
    line = ser.readline()
    print(line)
    data = await websocket.recv()
    reply = f"{line}"
    await websocket.send(reply)


start_server = websockets.serve(handler, "localhost", 9990)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
ser.close()
