from operator import imod
import requests
import os
import re
import sys
import time
import json

ProcessFilePath = os.getcwd()

SettingFile = ProcessFilePath+'\\' + 'setting.json'

SettingDict = dict()

with open(SettingFile, 'r', encoding='UTF-8') as file:
    SettingDict = json.load(file)

# 悬浮窗显示运行结果
def SleepCMD():
    time.sleep(SettingDict['SleepTime'])


# 验证API的Key是否有效
Authorization = requests.get(SettingDict['AuthorizationUrl'],
                             headers={'Authorization': SettingDict['Authorization']})
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

# 获取已经在单词本中的单词
AddedWord = requests.get(SettingDict['AddedWordURL'],
                         headers={'Authorization': SettingDict['Authorization']})


# 读取待添加的单词
UploadWords = []
with open(r'history', 'rt', encoding='UTF-8') as file:
    WordList = file.readlines()
    OldWord = ''

    for Word in WordList:
        
        NewWord = re.sub(r'^1 ', '', Word)  # 删除GoldenDic导出的数字部分
        NewWord = NewWord.replace('\n', '')
        NewWord = NewWord.strip('`')
        if OldWord == 
        OldWord = ()
        # newword = re.sub(r'[\u2000-\u206f]', '', neword) #中文常见的标点符号不在此范围内，需要手动自己的指定，可以自己收集

        # 比较云端数据，已添加单词不再次添加
        if NewWord in AddedWord.text:
            continue
        elif NewWord not in AddedWord.text:
            UploadWords.append(NewWord)
        else:
            print(NewWord + "出现异常")

if len(UploadWords) == 0:
    print("无新单词需要添加")
    SleepCMD()
    sys.exit()

Word = {"id": "0", "language": "en", "words": UploadWords} # API要求的格式

AddWord = requests.post(SettingDict['APIURL'],
                        json=Word,
                        headers={"Authorization": SettingDict['Authorization']})

# 将执行的信息返回控制台，或者悬浮窗直接显示
addwordresponse = AddWord.text.replace('}', "")
addwordresponse = addwordresponse.replace('{"message":', '')

print(addwordresponse)
SleepCMD()
