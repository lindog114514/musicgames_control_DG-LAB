#本文件负责open CV＿phi以及APP的连接
#ws协议
#作者为了偷懒，所以给APP的uuid以及给open CV_phi的uuid为相同ID
#注意APP和运行本程序的电脑必须在同一局域网内!!!
#2024-10-12

import asyncio
import json
import websockets
from uuid import uuid4
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
bese = '120.0.0.1:1145'


async def server():
    clientId = QR_sign()
    await websocket.send(json.dumps({"type": "bind", "clientId": client_id, "message": "targetId", "targetId": ""})) #将UUID发送给客户端
    # 主服务,启动!!!!!!!!!!!!!!!!
    async for message in websocket:
        print(f"收到了来自客户端的消息 : {message}")
        try:
            data = json.loads(message)
        except json.JSONDecodeError:
            # 非 JSON 数据处理
            await websocket.send(json.dumps({"type": "msg", "clientId": "", "targetId": "", "message": "403"}))
            print(f"收到了非 JSON 数据")
            continue



async def QR_sign():
    client_id = str(uuid4())
    print('uuid生成成功 ')
    url='https://www.dungeon-lab.com/app-download.php#DGLAB-SOCKET#'+ bese + client_id
    qr = qrcode.make(url)
    qr.save("url_qr.png")# 保存二维码
    qr.show()
    print('QR码生成成功 ')
    return client_id

async def main():
    start_server = websockets.serve(server, "localhost", 8765)