# 介绍

获取欧路词典单词本单词，并制作一个可以直接导入Anki使用的txt。

# 下载

Github：[dist](dist)文件夹内的压缩包（在Github的get_from_api的README页面内可以通过这种方式下载）

蓝奏云：[https://wwp.lanzouf.com/b011tqz9c  ](https://wwp.lanzouf.com/b011tqz9c  )密码:gbn2，文件名`get_from_api.zip`

# 注意事项

1. 软件被电脑管家认为是病毒，2种解决方法：
	1. 自行百度添加`白名单`/`信任区`的方法
	2. 安装Python，直接跑源代码，具体安装过程及注意事项请自行搜索
2. 如果你需要使用mdx词典的解释，请参考[【Anki插件篇】（04）批量制卡：Fast Word Query ]( https://zhuanlan.zhihu.com/p/81645669)

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220715170152.png" width="500">
3. 请保证`get_from_api.exe`和`get_from_api_setting.json`存放在同一文件夹下

遇到问题，请灵活运用[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)中的方法与技巧。

# 使用方法

下载好软件之后，先用右键点击`csv2txt_for_anki_setting.json`文件，选择`记事本`打开，根据自己的需要填入参数。(图不对，但没有太大影响，下图的工具也是我开发的，感兴趣的戳[AwesomeJapaneseDictionary/tools/get_note_from_eudic/csv2txt_for_anki](https://github.com/NoHeartPen/AwesomeJapaneseDictionary/tree/master/tools/get_note_from_eudic/csv2txt_for_anki))

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220715162933.png" width="500">

下面逐项说明参数信息

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220715174349.png" width="500">

`AnkiexePath`：非必要参数，可不填
- 示例：`D:\\03Program\\Anki\\anki.exe`（可通过[everything](https://www.voidtools.com/zh-cn/)搜索`anki.exe`快速获取）
- 作用：提取完单词后会自动启动Anki

`authorization`：必要参数
- 示例：如果你是第一次使用，请先登录[欧路词典官网](https://my.eudic.net/OpenAPI/Authorization)获取下图红框部分的内容

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220714111636.png" width="500">

`outpath`：必要参数
- 示例：`D:\\Document\\Dairy\\Eudicmemo.txt`
- 作用：就是想导入Anki的txt的地址。

如果程序正确运行的话，剪贴板会有`D:\\Document\\Dairy\\Eudicmemo.txt`，启动Anki后导入文件时可以`Ctrl+V`直接用，不用到处找文件。

唯一需要注意的一点就是，路径只能是`\\`，不能是`/`或者`\`，比如，最后一个路径不能写成`D:\Document\Dairy\Eudicmemo.txt`（虽然这种形式更容易拿到）

填完参数之后，以后每次都可以直接双击运行`get_from_api.exe`

# 许可证

使用[MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/) 许可证进行许可