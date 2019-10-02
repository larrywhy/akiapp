from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('W9FSrz5L/qhElUSfCUjzEUabwJeLx93nKIWxVPZLwUe6nRVSvpYvvieCcSFcEe+wu+77uGTGIgQ8pqFEiJC0nzrA1OMZ+SEwoZ9lChxQIkOrFULGrBCeYByGDHTArSHULJDeVp4aqVb+SZVuErKXeQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('91fd388abaa4d73d75555356e6fafa1e')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    message = TextSendMessage(text="hello world")
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
