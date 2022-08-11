'''
本脚本用于将GoldenDict的查词历史中的单词同步至欧路词典
'''
import requests
import os
import re
import sys
import time
import json

# 直接使用Python脚本的同学请修改下面这行文件的路径
#Path = os.chdir('D:\\03Program\\#Often\\GoldenDic\\portable')


def SleepCMD():
    time.sleep(SettingDict['SleepTime'])


def AutoDelete():  # 上传完成后用空字符串覆盖文件，注意只有当GoldenDict未被启动时才能真正覆盖，在GoldenDict启动期间，GoldenDict只会向该文件写入查词历史，而不会读取其中的词条。关闭软件时，GoldenDict会将本次运行前的查询历史保存到history文件中，下次启动时，会读取其中的词条，生成软件界面的查询历史。
    if SettingDict['AutoDelete'] == "on":
        with open('history', 'w', encoding='utf-8') as File:
            File.write("")
            print("启动自动删除，并成功自动删除")
    elif SettingDict['AutoDelete'] == 'off':
        print("不启动自动删除")
    elif SettingDict['AutoDelete'] == '':
        print("默认不启动自动删除")
    else:
        print("启动自动删除，但AutoDelete函数异常，用户在配置文件中填入的是："+SettingDict['AutoDelete'])


ProcessFilePath = os.getcwd()

SettingFile = ProcessFilePath+'\\' + 'setting.json'

SettingDict = dict()

with open(SettingFile, 'r', encoding='UTF-8') as file:
    SettingDict = json.load(file)

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
NewVerb = ''
LastVerb = ''

with open(r'history', 'rt', encoding='UTF-8') as file:
    WordList = file.readlines()
    for Word in WordList:
        NewWord = re.sub(r'^1 ', '', Word)  # 删除GoldenDic导出的数字部分
        NewWord = NewWord.replace('\n', '')
        NewWord = NewWord.strip('`')
        # newword = re.sub(r'[\u2000-\u206f]', '', neword) #中文常见的标点符号不在此范围内，需要手动自己的指定，可以自己收集

        # 比较云端数据，已添加单词不再次添加
        if NewWord in AddedWord.text:
            continue
        elif NewWord not in AddedWord.text:

            # 通过比较第一个字符，判断是否是同一单词，注意这种方法存在一定的缺陷！
            NewVerb = NewWord[0:1]
            if NewVerb == LastVerb:
                continue
            else:
                UploadWords.append(NewWord)
            LastVerb = NewVerb
        else:
            print(NewWord + "出现异常")


if len(UploadWords) == 0:
    print("无新单词需要添加")
    AutoDelete()
    SleepCMD()
    sys.exit()

Word = {"id": "0", "language": "en", "words": UploadWords}  # API要求的格式

AddWord = requests.post(SettingDict['APIURL'],
                        json=Word,
                        headers={"Authorization": SettingDict['Authorization']})

# 将执行的信息返回控制台，或者悬浮窗直接显示
addwordresponse = AddWord.text.replace('}', "")
addwordresponse = addwordresponse.replace('{"message":', '')

print(addwordresponse)
AutoDelete()
SleepCMD()
