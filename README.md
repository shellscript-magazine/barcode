# 書籍バーコードの生成、バーコード/QRコードの読み取り

## barcode_make.py
書籍に使われるISBN13のバーコードを生成するPythonスクリプトです。
Windows 10の環境で動かしています。

以下の通りに実行できる環境を構築してください。

- Webブラウザを開いて「[Pythonの公式サイト](https://www.python.org/downloads/)」からWindows版Pythonのインストーラを入手して導入します（インストール画面の最後に表示される「Add Python 3.x to PATH」にはチェックを付けてください） 。
- コマンドプロンプトを開いて次のコマンドを実行します。
```
> pip install python_barcode
> pip install pillow
> pip install pypng
```

「barcode_make.py」は次のように実行します。「barcode.png」のPNG形式の画像ファイル、「barcode.svg」のSVG形式のベクター画像ファイルが生成されます。
```
>  python barcode_make.py ISBN13の番号
```

## bar_qr_read.py
USBカメラやパソコン内蔵カメラを使ってバーコードやQRコードを読み取るPythonスクリプトです。画像処理をしていないのでバーコードやQRコードは黒色にしてください。カメラによっては、後処理ができなくてエラーが発生します（テストに用いたバッファロー製の「BSWHD06MBK」はOK）。ISBN13に限らずいろいろなバーコード、QRコードが読めます。
Windows 10の環境で動かしています。

以下の通りに実行できる環境を構築してください。

- Webブラウザを開いて「[Pythonの公式サイト](https://www.python.org/downloads/)」からWindows版Pythonのインストーラを入手して導入します（インストール画面の最後に表示される「Add Python 3.x to PATH」にはチェックを付けてください）。
- コマンドプロンプトを開いて次のコマンドを実行します。
```
> pip install opencv-python
> pip install pyzbar
```
「bar_qr_read.py」は次のように実行します。カメラの映像が表示され、端末に「準備完了」の文字が表示したら、バーコードやQRコードをカメラに向けます。読み取りとデコードが完了すると、端末上にコードに書かれた文字列が表示されます。
```
>  python bar_qr_read.py
```
## bar_qr_read_beep.py
USBカメラやパソコン内蔵カメラを使ってバーコードやQRコードを読み取るPythonスクリプトです。映像を表示せずに、バーコードやQRコードが読み取れたら、ビープ音を鳴らします。環境構築、使い方は、bar_qr_read.pyとコマンド名が異なるだけで同様です。なお、ビープ音の出力に「winsound」モジュールを使っているのでWindows専用です。

※シェルスクリプトマガジンの記事には関係ありませんが、必要性に迫られて作りました。
