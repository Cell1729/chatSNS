# ChatSNS

ミニSNS製作
[親リポジトリ](https://github.com/Cell1729/PythonTasks)

## 製作経緯

Pythonの練習題材として製作

## 環境

python 3.12

## 起動

環境変数を読み込む

```sh
set DJANGO_SETTINGS_MODULE=chatSNS.settings
```

環境変数を読み込んだ後にuvicornで起動する

```sh
uvicorn chatSNS.asgi:application --host 127.0.0.1 --port 8000
```

## 再起動

```sh
uvicorn chatSNS.asgi:application --reload
```
