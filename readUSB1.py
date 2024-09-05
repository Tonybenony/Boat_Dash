import asyncio
import websockets
import serial

ser = serial.Serial('/dev/ttyUSB1', 9600)
# create handler for each connection
async def handler(websocket, path):
    Speed = ser.readline()
    Value = (Speed.decode())

    data = await websocket.recv()
    reply = f"{Value}"
    await websocket.send(reply)
    ser.flushInput();ser.flushOutput()

start_server = websockets.serve(handler, "192.168.178.129", 9990)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
ser.close()




