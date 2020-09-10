import cv2
from pyzbar.pyzbar import decode
import winsound

# カメラを有効にする
qrcam = cv2.VideoCapture(0)

# カメラに接続できない
if not qrcam.isOpened():
    print("カメラが使えません")
    exit()

cam_start = 0

try:
    while True:
        # QRコード、バーコードの取り込み準備
        ret, frame = qrcam.read()
        if ret and cam_start == 0:
                print("準備完了")
                cam_start += 1

        # QRコード、バーコードのデコード
        codes = decode(frame)
        if len(codes) > 0:
            output = codes[0][0].decode('utf-8', 'ignore')
            winsound.Beep(1200, 200)
            # 端末にデコードで作成された文字列を出力
            print(output)
            qrcam.release()
            break

except KeyboardInterrupt:
    qrcam.release()
