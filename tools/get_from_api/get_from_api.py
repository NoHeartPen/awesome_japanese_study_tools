import requests
import os
import json
import pyperclip
import re

ProcessFilePath = os.getcwd()
SettingFile = ProcessFilePath+'\\' + 'get_from_api_setting.json'

with open(SettingFile, 'r', encoding='UTF-8') as file:
    SettingDict = json.load(file)
    
if SettingDict['authorization'] == '':
    print('请先在get_from_api_setting.json的"authorization": ""的""内输入\nhttps://my.eudic.net/OpenAPI/Authorization\n获取的APIKey')
    exit()

url = 'https://api.frdic.com/api/open/v1/studylist/words'

addedword_url = url + "/0?language=en&category_id=0"

addedword = requests.get(addedword_url,
                         headers={'Authorization': SettingDict['authorization']})

AuthorizationUrl = "https://api.frdic.com/api/open/v1/studylist/category?language=en"
Authorization = requests.get(AuthorizationUrl,
                             headers={'Authorization': SettingDict['authorization']})
response = str(Authorization.status_code)

if response == "401":
    print(
        "请确认填入正确的授权信息，\n或者去https://my.eudic.net/OpenAPI/Authorization \n再重新生成一个吧"
    )
elif response == "200":
    print("恭喜！添加授权信息成功")
elif response == '403':
    print('访问过于频繁，被禁止访问啦，一会儿再来试吧')
else:
    print("ﾟдﾟ你似乎遇到了一个很棘手的问题，快去报告一下吧")

# 保存数据
if SettingDict['outpath'] != '':
    print("导出的txt路径为："+SettingDict['outpath'])
    Outputlines = []
    with open(SettingDict['outpath'], 'w', encoding='UTF-8') as outputfile:
        regex = r"\"word\":\"(?P<word>(.*?))\""
        for iter in re.finditer(regex,addedword.text):
            line  = iter.group("word").strip('\\n') +'\n'
            Outputlines.append(line)
        outputfile.writelines(Outputlines)
else:
    print('请先在get_from_api_setting.json的"outpath": ""的""内输入导出文件的路径')

pyperclip.copy(SettingDict['outpath'])

if SettingDict['AnkiexePath'] != '':
    print("Anki程序路径为："+SettingDict['AnkiexePath'])
    os.system(SettingDict['AnkiexePath'])
else:
    print("手动启动Anki")


