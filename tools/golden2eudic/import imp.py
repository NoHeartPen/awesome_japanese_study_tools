import requests

URL = "https://www.jcinfo.net/zh-hans/tools/kanji/_token=02eQD3VFo4VE5Me3tV17MPVt1qLM4hN5PfZgXv0D&text=%E6%B1%89%E5%AD%97&lang=zh-Hans"

print(requests.get(URL).content)
#Test = requests.get(URL,  headers={"text": "艺术"})
# print(Test.content)
