**※2021年11月31日以降に作成されたSlackアプリでは動作できなくなりました。**

https://api.slack.com/changelog/2021-10-rtm-start-to-stop
> Beginning November 30, 2021, newly created Slack apps will no longer be able to make API calls to rtm.start.

# my slack bot
## 機能
- 天気予報
- ...更新予定

## インストール & セットアップ
#### [slackbot](https://github.com/lins05/slackbot)パッケージのインストール。

terminal:
```
pip install slackbot
```

#### [bots](https://my.slack.com/apps/A0F7YS25R-bots)のAPIトークンを取得し、`slackbot_setting.py`に追加。

slackbot_setting.py:
```python
API_TOKEN = "<your-api-token>"
```

#### `run.py`を実行。

terminal:
```
python run.py
```

## 使用方法
1. 適当なチャンネルに[bots](https://my.slack.com/apps/A0F7YS25R-bots)を追加。
1. メッセージを送信。以下を参照。
```
メッセージにて、以下のいずれかの文字列を送信してくれたら、東京の天気予報をお知らせします。
<今日>：今日の天気をお知らせします。
<明日>：明日の天気をお知らせします。
<明後日>：明後日の天気をお知らせします。
<詳細>：詳細をお知らせします。
<天気>：以上の全てをお知らせします。
```

## 停止
`CTRL+C`でbotsを停止できる。
