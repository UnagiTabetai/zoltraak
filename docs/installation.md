# インストール方法(MACユーザー向け）
## STEP1：環境変数の設定
Zoltraakは、.env ファイルに環境変数を設定する必要があります。

```
export ANTHROPIC_API_KEY={自分のANTHROPICのAPIキーを記入}
```
※仕様上はsite-packagesの配下に設定するのですが、現状動かないケースが多いようです。
※仮想環境を切って、直接exportで書き込むのが今のところ確実です。

※{}は必要ありません。


## STEP2：インストール
ターミナルに以下のコマンドを入力することでZoltraakをインストールします。
```
pip install zoltraak
```

### バージョンアップしたい時
   ```sh
   pip install --upgrade zoltraak
   ```
