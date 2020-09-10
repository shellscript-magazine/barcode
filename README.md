# 書籍バーコードの生成・読み取り

## barcode_make.py
書籍に使われるISBN13のバーコードを生成するPythonスクリプトです。
Windows 10の環境で動かしています。

以下の通りに実行できる環境を構築してください。

- Webブラウザを開いて「[Pythonの公式サイト](https://www.python.org/downloads/)」からWindows版Pythonのインストーラを入手して導入します。
- コマンドプロンプトを開いて次のコマンドを実行します。
```
> pip install python_barcode
> pip install pillow
> pip install pypng
```

「barcode_make.py」は次のように実行します。「barcode.png」のPNG形式の画像ファイル、「barcode.svg」のSVG形式のベクター画像ファイルが生成されます。
```
>  barcode_make.py ISBN13の番号
```

