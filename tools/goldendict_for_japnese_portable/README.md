本文在如下平台有备份：

[Gitee](https://gitee.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/goldendict_for_japnese_portable)
[Github](https://github.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/goldendict_for_japnese_portable)
[语雀](https://www.yuque.com/noheartpen/hbrngk/ndwk94c1m4g6lv7w)
[知乎](https://zhuanlan.zhihu.com/p/583128753)

# 介绍

## 为什么更推荐GoldenDict而不是EBWin

优点：

- GoldenDict是完全免费、基于 GNU GPLv3 分发的开源软件，即使开发者不更新，也会有其他志愿者接手维护、更新；有大量第三方辅助工具提高使用体验
- 完善的词典格式支持：除了 mdx 格式外，也支持读取Epwing等多种格式的词典。而 EBWin 不仅支持的格式较少，也不支持 mdx 的部分特性，比如跨词典跳转、播放视频以及 JavaScript 语法……这些都有可能会导致词典加载异常
- GoldenDict 背后有活跃的社区氛围：在[ FreeMdict ](https://forum.freemdict.com/)和[ PDAWIKI ](https://www.pdawiki.com/forum/)，你可以找到很多人帮助你解决使用过程遇到的问题（比如[ GoldenDict 专贴](https://www.pdawiki.com/forum/forum.php?mod=viewthread&tid=11705)），也可以白嫖许多优秀的词典（比如[大辞泉【202110数据】_20220423](https://forum.freemdict.com/t/topic/11703)），还可以和他们交流语言学习（比如[
关于 日语 的某些无关紧要的疑惑](https://forum.freemdict.com/t/topic/14129)）

缺点： 
- [不用 GoldenDict 的 10 个理由 ](https://mp.weixin.qq.com/s/HzZZhyyHMb0DpQ4AYOLzlA?)

EBWin的优点：对于 Epwing 的完美支持——部分日语词典只有这种格式；修改字体方便。

至于欧路词典，不推荐在Windows使用：
1. 收费
2. 不能加载Epwing格式的词典

但是，欧路词典的在线词典功能算是目前做的最好的，如果对这个功能有兴趣，可以看看这个回答 [有什么好用的日语词典软件？](https://www.zhihu.com/question/37052233/answer/2015870761)


# 特性

为什么要使用这个项目提供的安装包？

- 本项目基于 xiaoyifang 老师维护的[goldendict](https://github.com/xiaoyifang/goldendict)修改而成，该分支具有如下特点：
  - 由国人负责维护，沟通反馈比较方便
  - 有大量经验可供参考：[GoldenDict(Linux/macOS/Windows)基于Qt5.15.2/Qt6.X版本](https://forum.freemdict.com/t/topic/11495)
  - 通过设置即可修改字体，无需编辑代码
  - 支持 Anki 制卡，具体方法请查看[how to connect with anki.md](https://github.com/xiaoyifang/goldendict/blob/staged/howto/how%20to%20connect%20with%20anki.md)
- 无需编译,开箱即用——下载解压，只需把词典文件放到`content`文件夹，就完成了准备工作
- 本项目针对日语的剪贴板查词，做了以下优化：
  - 内置了[ MrCorn0-0 ](https://github.com/MrCorn0-0)的[ hunspell_ja_JP](https://github.com/MrCorn0-0/hunspell_ja_JP)项目的构词法文件，使Goldendict原生支持处理日语活用变形，实现了真正的一键查词
  - 内置[ NoHeartPen ](https://github.com/NoHeartPen) 的[日本語非辞書辞典](https://github.com/NoHeartPen/JapaneseConjugation)和 [日本語用言活用辞書byGary](https://www.pdawiki.com/forum/thread-40881-1-1.html)
  ：最丝滑流畅的划词解决方案
  - 内置[ NoHeartPen ](https://github.com/NoHeartPen) 的[简日汉字字典](https://github.com/NoHeartPen/Kanji2Hanzi)：通过收集 700 多个中日不一样的汉字，降低了“知道中文查日语”的难度

# 下载

## 下载软件

123 网盘：https://www.123pan.com/s/iGz0Vv-fvdVh

对于想在 Mac 或者 Linux 使用的同学，可以按照这篇[安装使用 GoldenDict 查词神器 (Windows/Mac/Linux)](https://www.cnblogs.com/keatonlao/p/12702571.html) ，安装好软件后，将以下词典文件手动添加到软件安装路径下的`content`文件夹内：

- [日本語非辞書辞典](https://github.com/NoHeartPen/JapaneseConjugation)：`NonJishoKei.mdx`
- [简日汉字字典](https://github.com/NoHeartPen/Kanji2Hanzi)：`Kanji2Hanzi.mdx`

日语的构词法文件请到这里下载，然后添加到软件安装路径下的`content`的`morphology`的文件夹内：

- [ hunspell_ja_JP ](https://github.com/MrCorn0-0/hunspell_ja_JP)：`ja_JP.dic`和`ja_JP.aff`文件

## 下载词典

受限与版权和字典大小，这里只列举链接，请根据自己的需要下载，另外，网上也有很多人分享，比如[有什么好用的日语词典软件？ - 游方的回答 - 知乎](https://www.zhihu.com/question/37052233/answer/72856818)。但其实，它们大多来自以下3个网站，其他人分享的有可能会比较旧，有时间、有需要的话，自己在下面3个网站慢慢搜罗吧 ：

### [Mdict](https://mdict.org/post/mdx/)

一个纯粹的资源站，提供的字典有很多精品，但是访问有点慢。

### [FreeMDict论坛](https://forum.freemdict.com/)

提供的资源不如 PDAWIKI 多，但质量更好，另外还提供了一套很不错的制作教程，这篇帖子 [日语mdx 下载点小集合](https://forum.freemdict.com/t/topic/15856)可以快速找到那些通用的日语词典。

### [PDAWIKI](https://www.pdawiki.com/forum/)

也可以下载到一些词典，但要花时间慢慢找，但有的帖子需要注册登录才能访问，而且现在也没有新的的作品了，所以放到最后。

这里也放一个我自己收集整理的，但不会更新维护：

天翼云盘(只有我自己最常用的词典，对于大多数人，完全够用了)：[https://cloud.189.cn/t/MzEVnyMNFbQb](https://cloud.189.cn/t/MzEVnyMNFbQb)
访问码：hf8z（先转存到自己的账号，然后下载客户端就可以不限速批量下载了）
	客户端地址：[https://cloud.189.cn/web/static/download-client/index.html](https://cloud.189.cn/web/static/download-client/index.html)

123网盘（我自己整理过的，不限于Goldendict和EBWin，还有 PDF 和 Kindle 等电子书的 mobi 格式）[https://www.123pan.com/s/iGz0Vv-Z5vVh](https://www.123pan.com/s/iGz0Vv-Z5vVh)

百度网盘（Store是我找到的所有分享）：[https://pan.baidu.com/s/1NOBbbmcrohiA4QzP7mx_gQ?pwd=05ge](https://pan.baidu.com/s/1NOBbbmcrohiA4QzP7mx_gQ?pwd=05ge)
提取码：05ge

# 第一次启动软件

下载好之后，找个地方解压，找到`content`文件夹，把之前下载的字典文件拖进去（EBWin和EBPockect的词典放到这里面也是可以加载的），然后双击`GoldenDict.exe`运行就可以了（第一次启动需要比较长的时间，以后会短得多）
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220903132416.png)
启动之后到`编辑`-`词典`
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221114002404.png)
到`群组`里面，在左边选中自己要看的词典，按住右键拖到右边就可以了
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221114002212.png)

然后，检查下软件的剪贴板查词功能是否打开：`编辑`-`首选项`-`热键`-`使用下列热键翻译剪贴板中的单词`，可以按照按自己习惯设置快捷键。

![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221113151730.png)

恭喜！你已经完成了所有基本设置，可以愉快地划词阅读了！

![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//班群_非辞書演示_动词.gif)

~~快去和青空文库对线吧~~

# 高级自定义

## 如何指定字体

之所以如此重视这个问题，是因为`明朝体`与实际书写时存在较大的差异，日语初学者最好以`教科書体`为书写的模板，而国内即使是专业的日语词典，比如 MOJi 、沪江小 D 等等都不支持`教科書体`，卡西欧的电子字典更不可能用作书写模板，至于国内出版的所谓字帖很多都是用的在简体汉字的字体印刷出来的，只是印的内容是日语而已。

注意：这部分的内容难度比较大，请确认自己是真的有需要、有能力再动手，遇到问题请先在 [ FreeMdict ](https://forum.freemdict.com/)和[ PDAWIKI ](https://www.pdawiki.com/forum/)搜索，很多问题都会迎刃而解。

### 为所有字典指定字体

打开`portable`文件夹下名为`article-style.css`（没有的话自己建一个），然后确认你已经在电脑上安装了字体（没有双击打开文件的，然后安装即可），修改下面的部分：
```css
body
{
  /*line-height: 80%;*/
  margin-top: 1px;
  margin-right: 3px;
  margin-left:  2px;
  margin-bottom: 3px;
  background: white;
  font-family: "Klee One SemiBold","LXGW WenKai";
}
```
在`font-family: `后面用""包裹你要替换的字体的名字，注意不是`字体的文件名`，是字体安装界面显示的`字体名称`
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com/20220823111051.png)

另外，有部分字体的字体名称需要参考[中文字体的英文名称对照表](https://xuui.net/ui-design/english-name-of-chinese-characters-table.html)要求。

### 单独为某一本字典指定字体

非常麻烦，你掌握一定的 HTML 和 CSS 知识，这里仅指简单指点一下方向：

- 将 MDX 格式的字典解压为源文件(使用`GetDict_2.3.exe`)，然后观察其中的字体实现方法：
	- 如果是通过`css`实现样式，修改`css`文件即可，
	- 如果不是`css`实现，你需要在词典部分添加`<link rel="stylesheet" type="text/css" href="Jisho.css">`，然后新建一个`Jisho.css`的文件
- 修改css文件：
检查文件地方是不是`@charset "UTF-8";`，不是的话最好添上去
在词典顶部添加下面这样的代码：
```css
@font-face {
  font-family: "Japanese";
  src: url("KleeOne-SemiBold.ttf") ;
}
```
其中`Japanse`可以换成你喜欢的说法，但是`KleeOne-SemiBold.ttf`这部分内容一定要和你的字体文件名保持一致

- 然后找到下面这段代码（以`body{}`这样的样式出现，包含`font-family`即可，其他内容不一样是正常情况）：
```css
body {
    font-family: "KleeOne", arial, sans-serif;
    font-size: 90%;
    margin: 0;
    padding: 0;
    text-align: left;
}
```
修改`font-family: "KleeOne", arial, sans-serif;`这一行的内容，换成这样：`font-family: "Japanese", arial, sans-serif;`，注意，这里的`Japanese`请与上面的`font-family: `保持一致

保存文件，然后在词典的源文件新建一个名为`mdd`的文件夹，把字体文件放进去。

然后使用`MdxBuilder.exe `制作词典，注意在`Date`添加上面提到的`mdd`文件夹的路径，这样制作的词典才会使用指定的字体。

## 如何同步查词记录

可以使用本人写的小脚本`goldendic2eudic`，一次设置，永远自动同步到欧路词典，不会查了就忘:)

https://github.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/golden2eudic

不能访问Google的同学请用这个：
https://gitee.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/golden2eudic

EBWin 也有一个同步查词记录的工具：

https://gitee.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/ebwin2eudic

https://github.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/ebwin2eudic

# 其他平台

本项目的核心在于针对日语的剪贴板查词，做了以下优化：
  - 内置了[ MrCorn0-0 ](https://github.com/MrCorn0-0)的[ hunspell_ja_JP ](https://github.com/MrCorn0-0/hunspell_ja_JP)项目的构词法文件，使Goldendict原生支持处理日语活用变形，实现了真正的一键查词
  - 内置[ NoHeartPen ](https://github.com/NoHeartPen) 的[日本語非辞書辞典](https://github.com/NoHeartPen/JapaneseConjugation)和 [日本語用言活用辞書byGary](https://www.pdawiki.com/forum/thread-40881-1-1.html)
  ：最丝滑流畅的划词解决方案
  - 内置[ NoHeartPen ](https://github.com/NoHeartPen) 的[简日汉字字典](https://github.com/NoHeartPen/Kanji2Hanzi)：通过收集 700 多个中日不一样的汉字，降低了“知道中文查日语”的难度

除了[ hunspell_ja_JP ](https://github.com/MrCorn0-0/hunspell_ja_JP)只能用于Goldendict软件外，其余方法也适用于欧路词典、EBWin、EBPocket、DictTango、深蓝词典、Mdict等支持加载 mdx 格式的软件，下面也进行简要的介绍。

## iPad/iOS

对于想在 iPad 用的同学，推荐去 APP Store 下载`欧路词典`（Ta 家的会员服务主要是同步笔记，不会影响看字典的体验）
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220903130847.png)

这里有一份不错的安装教程[https://www.bilibili.com/video/BV1mb411G72E](https://www.bilibili.com/video/BV1mb411G72E)

[iOS设备词典外接键盘快捷键支持](https://eusoft.kf5.com/hc/kb/article/1025930/)

## 安卓

欧路和用 EBPockect 基本一样，安装好软件之后，到`账号`-`软件设置`-`扩充词库路径`指定词典文件的文件夹即可，注意欧路词典不支持加载 EBPockect 格式的词典！

DictTango、深蓝词典、Mdict请自行百度`添加词典的方法`

对于安卓的同学，强烈推荐下载静读天下（静读天下是个用来看电子书的软件，支持非常多的格式，标注过的地方可以直接点击查词，相当于自己标出不认识的单词后下次就可以节省打字的时间了，搭配《日本語非辞書形辞典》，一晚读完青空文库不是梦！

![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220903133947.png)

静读天下的开发者人似乎润到了香港，所以软件没有在国内的软件商店上架，但针对国内用户提供了免 Google 框架的 APK 文件放在官网的最下面的地方：
[Moon+ Reader for Android (moondownload.com)](https://moondownload.com/chinese.html)
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220903134144.png)


# 参考

[ GoldenDict 中文用户手册](https://github.com/Dictionaryphile/GoldenDict_zh_manual)
[有没有什么好用的日语app词典？ - NoHeartPen的回答 - 知乎](https://www.zhihu.com/question/41084276/answer/2641329951) 

