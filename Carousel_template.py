from linebot.models import *

def Carousel_template():
    content = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://drive.google.com/uc?export=view&id=1Rf5TILMDF-EdkRem2wFw9pQ82nuAnGm2",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "功能",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "text",
                            "text": "是草系寶可夢訓練家!",
                            "style": "italic"
                        }
                    ],
                    "maxHeight": "80px"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "聊天",
                                "text": "聊天"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "文字轉語音",
                                "text": "文字轉語音"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "天氣預報",
                                "text": "天氣預報"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "圖片人物分析",
                                "text": "圖片人物分析"
                            }
                        },
                    ]
                }
            }]}

    message = FlexSendMessage(alt_text='MM', contents=content)
    return message