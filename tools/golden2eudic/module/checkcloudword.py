import requests
import os
import re
import sys

path = os.chdir(
    r"D:\03Program\#Often\GoldenDic\portable")  # 如果要支持GUI的话，这个路径考虑支持填入

path = os.getcwd()

authorization = ""  # 尝试这里也用GUI的数据
with open(r'goldendic2eudic.txt', 'rt', encoding='UTF-8') as file:
    authorization = file.readline().replace("\n", "")
file.close()

url = 'https://api.frdic.com/api/open/v1/studylist/words'

addedword_url = url + "/0?language=en&category_id=0"

addedword = requests.get(addedword_url,
                         headers={'Authorization': authorization})

AuthorizationUrl = "https://api.frdic.com/api/open/v1/studylist/category?language=en"
Authorization = requests.get(AuthorizationUrl,
                             headers={'Authorization': authorization})
response = str(Authorization.status_code)

if response == "401":
    print(
        "请确认填入正确的授权信息，\n或者去https://my.eudic.net/OpenAPI/Authorization \n再重新生成一个吧"
    )
elif response == "200":
    print("恭喜！添加授权信息成功，快去尝试查几个单词吧")
elif response == '403':
    print('访问过于频繁，被禁止访问啦，一会儿再来试吧')
else:
    print("ﾟдﾟ你似乎遇到了一个很棘手的问题，快去报告一下吧")

uploadwords = []

with open(r'history', 'rt', encoding='UTF-8') as file:
    wordlist = file.readlines()
    for oldword in wordlist:
        newword = re.sub(r'^1 ', '', oldword)  #删除GoldenDic导出的数字部分
        newword = newword.replace('\n', '')
        newword = newword.strip('`')
        # newword = re.sub(r'[\u2000-\u206f]', '', neword) #中文常见的标点符号不在此范围内，需要手动自己的指定，可以自己收集
        # print(neword)
        if newword in addedword.text:
            continue
        elif newword not in addedword.text:
            uploadwords.append(newword)
        else:
            print(newword + "出现异常")
file.close()

if len(uploadwords) == 0:
    print("无新单词需要添加")
    sys.exit()

myword = {"id": "0", "language": "en", "words": uploadwords}

addword = requests.post(url,
                        json=myword,
                        headers={"Authorization": authorization})
addwordresponse = addword.text.replace('}', "")
addwordresponse = addwordresponse.replace('{"message":', '')
print(addwordresponse)  # 尝试将执行的信息返回控制台，或者悬浮窗直接显示
