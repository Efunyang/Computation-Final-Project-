from transitions.extensions import GraphMachine

from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from bs4 import BeautifulSoup
import requests
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
import pandas as pd

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose(self, event):
        text = event.message.text
        return text.lower() == 'start'

    def on_enter_choose(self, event):
        title = '請選擇想要的長度'
        text = '『短髮』還是『長髮』'
        btn = [
            MessageTemplateAction(
                label = '短髮',
                text ='短髮'
            ),
            MessageTemplateAction(
                label = '長髮',
                text = '長髮'
            ),
        ]
        url = ''
        send_button_message(event.reply_token, title, text, btn, url)

   def is_going_to_girlshorthair(self, event):
        text = event.message.text
        if (text == '短髮') or ((self.state == 'girlshortshow')and (text.lower() == 'back')):
            return True
        return False

    def on_enter_girlshorthair(self, event):
        title = '想知道的內容'
        text = '輸入『髮型』可以查看髮型推薦。\n輸入『介紹』或『髮廊』會有文字說明。\n輸入『back』返回選單。'
        btn = [
            MessageTemplateAction(
                label = '短髮髮型',
                text ='短髮髮型'
            ),
            MessageTemplateAction(
                label = '短髮介紹',
                text = '短髮介紹'
            ),
            MessageTemplateAction(
                label = '短髮髮廊',
                text = '短髮髮廊'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://www.look-in.com.tw/rails/active_storage/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBN1NzQXc9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--3d66de08de9f0d150129eaf457a76a345a99a524/COVER.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_girlshortshow(self, event):
        text = event.message.text
        if text == '短髮髮型' or ((self.state == 'girlshortimg3' or self.state == 'girlshortimg2' or self.state == 'girlshortimg1')and (text.lower() == 'back')):
            return True
        return False

    def on_enter_girlshortshow(self, event):
        title = '共有三張圖示'
        text = '輸入『圖1』或『圖2』或『圖3』。\n輸入『back』返回選單。'
        btn = [
            MessageTemplateAction(
                label = '圖1',
                text ='圖1'
            ),
            MessageTemplateAction(
                label = '圖2',
                text = '圖2'
            ),
            MessageTemplateAction(
                label = '圖3',
                text ='圖3'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://imgur.dcard.tw/m0RK021h.png'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_girlshortimg1(self, event):
        text = event.message.text
        if text == '圖1':
            return True
        return False

    def on_enter_show_girlshortimg1(self, event):
        url = 'http://i1.kknews.cc/KtYeFRDYgRpy7L0ZhvxBHGE6Zwm4z4HvGswgviiLZ9NN7iwnI9uBSH4rzIPp/0.jpg'
        send_image_message(event.reply_token, url)

    def is_going_to_girlshortimg2(self, event):
        text = event.message.text
        if text == '圖2':
            return True
        return False
    def on_enter_show_girlshortimg2(self, event):
        url = 'https://i1.xiumeipai.com/ca54f7/9101a29e/9a50a8dd98b3a7389f65.jpg'
        send_image_message(event.reply_token, url)

    def is_going_to_girlshortimg3(self, event):
        text = event.message.text
        if text == '圖3':
            return True
        return False
    def on_enter_show_girlshortimg3(self, event):
        url = 'https://i1.xiumeipai.com/ca54f7/9101a398/ce57e0cc9bafa779843e.jpg'
        send_image_message(event.reply_token, url)

    def is_going_to_girllonghair(self, event):
        text = event.message.text
        if (text == '長髮') or ((self.state == 'girllongshow')and (text.lower() == 'back')):
            return True
        return False

    def on_enter_girlshorthair(self, event):
        title = '想知道的內容'
        text = '輸入『髮型』可以查看髮型推薦。\n輸入『介紹』或『髮廊』會有文字說明。\n輸入『back』返回選單。'
        btn = [
            MessageTemplateAction(
                label = '長髮髮型',
                text ='長髮髮型'
            ),
            MessageTemplateAction(
                label = '長髮介紹',
                text = '長髮介紹'
            ),
            MessageTemplateAction(
                label = '長髮髮廊',
                text = '長髮髮廊'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://beauty-upgrade.tw/wp-content/uploads/2019/02/%E9%95%B7%E9%AB%AE%E9%80%A0%E5%9E%8B.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_girllongshow(self, event):
        text = event.message.text
        if text == '長髮髮型' or ((self.state == 'girllongimg3' or self.state == 'girllongimg2' or self.state == 'girllongimg1')and (text.lower() == 'back')):
            return True
        return False

    def on_enter_girllongshow(self, event):
        title = '共有三張圖示'
        text = '輸入『圖1』或『圖2』或『圖3』。\n輸入『back』返回選單。'
        btn = [
            MessageTemplateAction(
                label = '圖1',
                text ='圖1'
            ),
            MessageTemplateAction(
                label = '圖2',
                text = '圖2'
            ),
            MessageTemplateAction(
                label = '圖3',
                text ='圖3'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        url = 'https://cdn2.ettoday.net/images/4142/4142529.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_girllongimg1(self, event):
        text = event.message.text
        if text == '圖1':
            return True
        return False

    def on_enter_show_girllongimg1(self, event):
        url = 'https://image.topbeautyhk.com/wp-content/uploads/2020/12/241e362d.jpg'
        send_image_message(event.reply_token, url)

    def is_going_to_girllongimg2(self, event):
        text = event.message.text
        if text == '圖2':
            return True
        return False
    def on_enter_show_girllongimg2(self, event):
        url = 'https://image.topbeautyhk.com/wp-content/uploads/2020/12/0f71f78f.jpg'
        send_image_message(event.reply_token, url)

    def is_going_to_girllongimg3(self, event):
        text = event.message.text
        if text == '圖3':
            return True
        return False
    def on_enter_show_girllongimg3(self, event):
        url = 'https://image.topbeautyhk.com/wp-content/uploads/2020/12/a53e47c6.jpg'
        send_image_message(event.reply_token, url)
