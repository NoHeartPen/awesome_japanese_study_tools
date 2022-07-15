# 这个脚本可以将欧陆词典导出的学习记录，整理为可以直接导入Obsidian内的md
import csv
import os
from xml.dom import minidom
import datetime
import json
import pyperclip

Outputlines = []  # 保存导出的笔记
wordsdic = {}  # 保存添加单词的时间

# 用于将导出的xml文件的UTC时间转换为北京时间


def TranferTimestamp(time_str):
    time_format = "%Y%m%dT%H%M%S"
    now = datetime.datetime.strptime(time_str, time_format)
    now_utc = now.replace(tzinfo=datetime.timezone.utc)
    now_local = now_utc.astimezone()
    return now_local


def Readcsv():
    with open(SettingDict['csvpath'], 'r', encoding='UTF-8') as processfile:
        csv_reader = csv.DictReader(processfile, delimiter=",")

        for row in csv_reader:
            wordline = row['单词']   # Anki字段对应规则

            noteline = row['笔记'].replace(r'<p dir="ltr">', '')  # 删除复制粘贴的换行
            if noteline == '':
                noteline = ' '
            
            # Anki导入时一条笔记只能占一行，中间分隔符号
            if SettingDict['xmlpath'] != '':
                timestampline = wordsdic.get(row['单词'])
                AnkiWord = wordline + '\t' + noteline + '\t' + \
                timestampline + '\n'  
            else:
                AnkiWord = wordline + '\t' + noteline+ '\n'
            Outputlines.append(AnkiWord)


def Readxml():
    processfile = minidom.parse(SettingDict['xmlpath'])
    words = processfile.getElementsByTagName("CustomizeListItem")
    # 通过键值对储存添加单词的时间
    for i in range(len(words)):
        word = words[i].getAttribute("word")
        addtime = words[i].getAttribute("addTimeP")
        addtime = TranferTimestamp(addtime)
        wordsdic[word] = str(addtime)[0:10]  # 只获取前8位数字

    # 获取csv中的单词数量，与xml中的是否一致
    with open(SettingDict['csvpath'], 'r', encoding='UTF-8') as processfile:
        csv_reader = csv.DictReader(processfile, delimiter=",")
        csvworddic = []
        for row in csv_reader:
            csvworddic.append(row['单词'])

        if len(csvworddic) == len(wordsdic):
            Readcsv()
        else:
            print("请重新导出xml和csv文件！")


ProcessFilePath = os.getcwd()
SettingFile = ProcessFilePath+'\\' + 'csv2txt_for_anki_setting.json'

with open(SettingFile, 'r', encoding='UTF-8') as file:
    SettingDict = json.load(file)

# 如果xml文件路径不为空，那么
if SettingDict['xmlpath'] != '':
    print("xml文件路径为："+SettingDict['xmlpath'])
    Readxml()
    Readcsv()
else:
    Readcsv()

# 保存数据
if SettingDict['outpath'] != '':
    print("导出的txt路径为："+SettingDict['outpath'])
    with open(SettingDict['outpath'], 'w', encoding='UTF-8') as outputfile:
        outputfile.writelines(Outputlines)
else:
    print('请在csv2txt_for_anki_setting.json的"outpath": ""的""内输入导出文件的路径')

pyperclip.copy(SettingDict['outpath'])

if SettingDict['AnkiexePath'] != '':
    print("Anki程序路径为："+SettingDict['AnkiexePath'])
    os.system(SettingDict['AnkiexePath'])
else:
    print("手动启动Anki")
