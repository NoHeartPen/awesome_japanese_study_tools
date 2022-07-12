from xml.dom import minidom

xmlpath = r'D:\Document\MoonReader\attachments\Eudicmemo.xml'

processfile = minidom.parse(xmlpath)

words = processfile.getElementsByTagName("CustomizeListItem")

for i in range(len(words)):
    print(words[i].getAttribute("word"))
    print(words[i].getAttribute("addTimeP")) # 
