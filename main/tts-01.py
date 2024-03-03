import requests
import json

headers = {
    'Authorization': f'Bearer {'sk-xxxxx'}', # 注：key为OpenAI API申请的key
    'Content-Type':'application/json'
}
url = "https://api.openai.com/v1/audio/speech"

input_text = input("请输入需要转换成语音的文本: ")
query = {
            "model":"tts-1",
            "input":input_text,
            "voice":"alloy",
            "response_format":"mp3",
            "speed":1,
        }
response = requests.post(url=url, data=json.dumps(query), headers=headers)
# 保存文件
filename = input("请输入预期的文件名: ")
f = open(filename+'.mp3', "wb")
f.write(response.content)
f.close()