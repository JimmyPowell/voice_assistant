import requests
import json

headers = {
    'Authorization': f'Bearer {'sk-'}', # 注：在这里输入你的api key
    'Content-Type':'application/json'
}
# 请求地址,需要根据实际情况修改,如果你的中转站点支持tts，则直接将‘https://openai.com’替换为’https://your_dormin.com即可‘
url = "https://openai.com/v1/audio/speech"#这里的后缀不要修改！

input_text = input("请输入需要转换成语音的文本: ")
query = {
            "model":"tts-1",
            "input":input_text,
            "voice":"echo",# 人物角色
            "response_format":"mp3",# 返回格式
            "speed":1,
        }
"""现阶段支持的人物角色：
alloy
echo
fable
onyx
nova
shimmer
具体效果可以自行尝试
"""
#
"""
现阶段支持的返回格式：
默认格式为mp3
opus：用于互联网流媒体和通信，延迟低。
aac：用于数字音频压缩，被YouTube、Android和iOS青睐。
flac：用于无损音频压缩，音频发烧友用于存档。
wav：无压缩的WAV音频，适用于需要低延迟的应用以避免解码开销。
pcm：类似于WAV，但包含24kHz（16位有符号，低端字节序）的原始样本，没有头部。
"""
# 发送请求

response = requests.post(url=url, data=json.dumps(query), headers=headers)
# 保存文件
#以下两行代码是状态检查代码，请求正常会返回200，如果返回的是400或者其他错误代码，说明请求失败
print("Status Code:", response.status_code)
print("Response Content:", response.content[:100])  # 打印前100个字节以检查

filename = input("请输入预期的文件名: ")
f = open(filename+'.mp3', "wb")#这里需要根据上面的格式自行修改后缀名
f.write(response.content)
f.close()