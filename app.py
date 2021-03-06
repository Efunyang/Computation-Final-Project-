import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message

load_dotenv()


machine = TocMachine(
    states=["choose","girlshorthair","girllonghair","girlshortshow","girlshortimg1","girlshortimg2","girlshortimg3","girllongshow","girllongimg1","girllongimg2","girllongimg3"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "choose",
            "conditions": "is_going_to_choose",
        },
        {
            "trigger": "advance",
            "source": "choose",
            "dest": "girlshorthair",
            "conditions": "is_going_to_girlshorthair",
        },
        {
            "trigger": "advance",
            "source": "choose",
            "dest": "girllonghair",
            "conditions": "is_going_to_girllonghair",
        },
        {
            "trigger": "advance",
            "source": "girlshorthair",
            "dest": "girlshortshow",
            "conditions": "is_going_to_girlshortshow",
        },
        {
            "trigger": "advance",
            "source": "girlshortshow",
            "dest": "girlshortimg1",
            "conditions": "is_going_to_girlshortimg1",
        },
        {
            "trigger": "advance",
            "source": "girlshortshow",
            "dest": "girlshortimg2",
            "conditions": "is_going_to_girlshortimg2",
        },
        {
            "trigger": "advance",
            "source": "girlshortshow",
            "dest": "girlshortimg3",
            "conditions": "is_going_to_girlshortimg3",
        },
        {
            "trigger": "advance",
            "source": "girlshortimg1",
            "dest": "girlshortshow",
            "conditions": "is_going_to_girlshortshow",
        },
        {
            "trigger": "advance",
            "source": "girlshortimg2",
            "dest": "girlshortshow",
            "conditions": "is_going_to_girlshortshow",
        },
        {
            "trigger": "advance",
            "source": "girlshortimg3",
            "dest": "girlshortshow",
            "conditions": "is_going_to_girlshortshow",
        },
        {
            "trigger": "advance",
            "source": "girlshortshow",
            "dest": "girlshorthair",
            "conditions": "is_going_to_girlshorthair",
        },
        {
            "trigger": "advance",
            "source": "girlshorthair",
            "dest": "choose",
            "conditions": "is_going_to_choose",
        },

        {
            "trigger": "advance",
            "source": "girllonghair",
            "dest": "girllongshow",
            "conditions": "is_going_to_girllongshow",
        },
        {
            "trigger": "advance",
            "source": "girllongshow",
            "dest": "girllongimg1",
            "conditions": "is_going_to_girllongimg1",
        },
        {
            "trigger": "advance",
            "source": "girllongshow",
            "dest": "girllongimg2",
            "conditions": "is_going_to_girllongimg2",
        },
        {
            "trigger": "advance",
            "source": "girllongshow",
            "dest": "girllongimg3",
            "conditions": "is_going_to_girllongimg3",
        },
        {
            "trigger": "advance",
            "source": "girllongimg1",
            "dest": "girllongshow",
            "conditions": "is_going_to_girllongshow",
        },
        {
            "trigger": "advance",
            "source": "girllongimg2",
            "dest": "girllongshow",
            "conditions": "is_going_to_girllongshow",
        },
        {
            "trigger": "advance",
            "source": "girllongimg3",
            "dest": "girllongshow",
            "conditions": "is_going_to_girllongshow",
        },
        {
            "trigger": "advance",
            "source": "girllongshow",
            "dest": "girllonghair",
            "conditions": "is_going_to_girllonghair",
        },
        {
            "trigger": "advance",
            "source": "girllonghair",
            "dest": "choose",
            "conditions": "is_going_to_choose",
        },
        {"trigger": "go_back", "source": ["choose","girlshorthair","girllonghair""girlshortshow","girlshortimg1","girlshortimg2","girlshortimg3","girllongshow","girllongimg1","girllongimg2","girllongimg3"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if machine.state != "user" and event.message.text.lower() == "restart":
                send_text_message(event.reply_token, "?????????start????????????????????????????????????\n???????????????restart????????????????????????")
                machine.go_back()
            elif machine.state == "user":
                send_text_message(event.reply_token, "?????????start????????????????????????????????????\n???????????????restart?????????????????????")
            elif machine.state == "choose":
                send_text_message(event.reply_token, "????????????????????????????????????")
            elif machine.state == "girlshorthair":
                if event.message.text.lower() == "????????????":
                    text = "?????????????????????????????????!????????????????????????????????????????????????????????????????????????????????????????????????!"
                    send_text_message(event.reply_token, text)
                elif event.message.text.lower() == "????????????":
                    text = "??????:MVSA \n??????: 701????????????????????????57???"
                    send_text_message(event.reply_token, text)
                elif event.message.text.lower() != "back":
                    send_text_message(event.reply_token, "???????????????????????????????????????????????????\n???>???????????????????????????????????????????????????????????????\n?????????back??????????????????")
            elif (machine.state == "girlshortimg1" or machine.state == "girlshortimg2"or machine.state == "girlshortimg3") and (event.message.text.lower() != "back"):
                send_text_message(event.reply_token, "?????????back??????????????????")
            elif (machine.state == "girlshortshow") and (event.message.text.lower() != "back"):
                send_text_message(event.reply_token, "????????????1????????????2????????????3??????\n?????????back??????????????????")
            elif machine.state == "girllonghair":
                if event.message.text.lower() == "????????????":
                    text = "????????????????????????????????????????????????????????????????????????????????????????????????180???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"
                    send_text_message(event.reply_token, text)
                elif event.message.text.lower() == "????????????":
                    text = "??????:Jole?????????????????????\n??????:??????????????????????????????575???4???"
                    send_text_message(event.reply_token, text)
                elif event.message.text.lower() != "back":
                    send_text_message(event.reply_token, "???????????????????????????????????????????????????\n??????????????????????????????????????????????????????????????????\n?????????back??????????????????")
            elif (machine.state == "girllongimg1" or machine.state == "girllongimg2"or machine.state == "girllongimg3") and (event.message.text.lower() != "back"):
                send_text_message(event.reply_token, "?????????back??????????????????")
            elif (machine.state == "girllongshow") and (event.message.text.lower() != "back"):
                send_text_message(event.reply_token, "????????????1????????????2????????????3??????\n?????????back??????????????????")
    return "OK"



@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)

