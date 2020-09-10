import cv2
from pyzbar.pyzbar import decode

# カメラを有効にする
qrcam = cv2.VideoCapture(0)
cv2.namedWindow('frame')

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

        # カメラ映像を表示（［Q］キーで終了）
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            qrcam.release()
            cv2.destroyAllWindows()
            break

        # QRコード、バーコードのデコード
        codes = decode(frame)
        if len(codes) > 0:
            output = codes[0][0].decode('utf-8', 'ignore')
            # 端末にデコードで作成された文字列を出力
            print(output)
            qrcam.release()
            cv2.destroyAllWindows()
            break

except KeyboardInterrupt:
    qrcam.release()
    cv2.destroyAllWindows()
