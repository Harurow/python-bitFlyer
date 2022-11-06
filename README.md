# Pythonつかって bitFlyer を操作する

## 用途

pythonを利用してbitFlayer口座照会をします。

## 準備

* pythonが利用できる環境
* `pybitflyer`が利用できる環境
* `python-dotenv`が利用できる環境
* bitFlyerAPI認証情報

### `pybitflyer`,`python-dotenv`について

`pybitflyer`,`python-dotenv`を利用しているので事前に`pip`または`pip3`でインストールが必要です

```sh
# 例
pip install pybitflyer python-dotenv
```

### bitFlyerAPI認証情報について

bitFlyerを外部から利用する場合、認証情報が別途必要です。
必要に応じて別途発行してください。必要な情報は、

* API_KEY
* API_KEY_SECRET

となります。

セキュリティの関係上、今回のコードには記載しておらず
`.env`ファイルに以下のような形で記載しています。

```sh:.env
API_KEY="xxxxxxxxxxxxxxxxx...xx"
API_KEY_SECRET="xxxxxxxxxxxx...xxxxx"
```

また`.gitignore`で`.env`を追加しているので`git`の追跡対象外にしています。

### 注意事項

カスタマイズすれば取引も可能ですが、プログラムによる取引は便利な反面、
簡単に誤った取引ができてしまいます。十分気をつけて実行してください。
