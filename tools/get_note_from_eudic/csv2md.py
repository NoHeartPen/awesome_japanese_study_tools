# 这个脚本可以将欧陆词典导出的学习记录，整理为可以直接导入Obsidian内的md
import csv
import os
from xml.dom import minidom
import datetime

# 用于将导出的xml文件的UTC时间转换为北京时间


def TranferTimestamp(time_str):
    time_format = "%Y%m%dT%H%M%S"
    now = datetime.datetime.strptime(time_str, time_format)
    now_utc = now.replace(tzinfo=datetime.timezone.utc)
    now_local = now_utc.astimezone()
    return now_local


csvpath = r'D:\Document\Dairy\Eudicmemo.csv'
outpath = r'D:\Document\Dairy\Eudicmemo.md'
xmlpath = r'D:\Document\Dairy\Eudicmemo.xml'

processfile = minidom.parse(xmlpath)
words = processfile.getElementsByTagName("CustomizeListItem")

wordsdic = {}

# 通过键值对储存添加单词的时间
for i in range(len(words)):
    word = words[i].getAttribute("word")
    addtime = words[i].getAttribute("addTimeP")
    addtime = TranferTimestamp(addtime)
    wordsdic[word] = str(addtime)[0:10]  # 只获取前8位数字

oldtimestamp = ''
newtimestamp = ''

# 判断xml和csv文件是否包含相同数量的单词
with open(csvpath, 'r', encoding='UTF-8') as processfile:
    csv_reader = csv.DictReader(processfile, delimiter=",")
    csvworddic = []
    for row in csv_reader:
        csvworddic.append(row['单词'])

    if len(csvworddic) == len(wordsdic):
        with open(csvpath, 'r', encoding='UTF-8') as processfile:
            lines = []
            csv_reader = csv.DictReader(processfile, delimiter=",")

            for row in csv_reader:

                oldtimestamp = newtimestamp
                newtimestamp = wordsdic.get(row['单词'])

                line = "# " + newtimestamp + '\n'  # 请注意保证xml文件和csv文件所含的单词一致

                if oldtimestamp != newtimestamp:
                    obdl = True  # 请结合自己的双链笔记习惯进行设置 bi-directional link
                    if obdl == True:
                        # 获取导出的年月日信息
                        Obsidantimestamp = r'[[' + newtimestamp + r']]'
                        line = "# " + Obsidantimestamp + '\n'

                    lines.append(line + '\n')

                wordline = '`' + row['单词'] + '`'  # 用md的代码语法区别单词和笔记
                noteline = row['笔记'].replace(r'<p dir="ltr">', '')  # 删除复制粘贴的换行
                noteline = noteline.replace(' ', '==')  # 手机端使用输入法可以用空格代替
                noteline = noteline.replace('====', '==')  # 删除多余的==
                line = wordline + noteline + '\n'  # md的换行需要2个\n
                lines.append(line + '\n')
    else:
        print("请确保xml文件和csv文件的一致！")
with open(outpath, 'w', encoding='UTF-8') as outputfile:
    outputfile.writelines(lines)

# 以默认的打开方式启动最后的md文件？

# noteapppath =  r'C:\Users\无心散卓\AppData\Local\Obsidian\Obsidian.exe'

os.system(
    r'notepad ' + outpath
)  # MyKeyMap指令 cmd.exe /c "python D:\Document\03Code\02Python\all2eudic\csv2md.py"
