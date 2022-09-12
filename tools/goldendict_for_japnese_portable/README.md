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

# 特性

- 内置了[ MrCorn0-0 ](https://github.com/MrCorn0-0)的[ hunspell_ja_JP](https://github.com/MrCorn0-0/hunspell_ja_JP)项目，使Goldendict原生支持处理日语活用变形，实现了真正的一键查词
- 内置[ NoHeartPen ](https://github.com/NoHeartPen) 的[日本語非辞書辞書](https://github.com/NoHeartPen/JapaneseConjugation)项目的 v2 版本的最新成果`日本語非辞書辞書.mdx`：通过穷举用言活用，实现了近乎完美的划词体验
- 内置日语教科书字体Klee和霞鹜文楷，在实现完美的中日文混排效果的同时，也让每次查词都可以学习漢字的正确写法
	- 注意，要先安装放在`Fonts`文件夹下的2个字体：双击打开字体文件后安装字体，然后重启即可生效即可 
	- 你也可以"轻松"更换你喜欢的字体

# 注意事项

直接下载[goldendict_for_japnese_portable.zip](goldendict_for_japnese_portable.zip)文件即可。

# 如何指定字体

之所以如此重视这个问题，是因为`明朝体`与实际书写时存在较大的差异，日语初学者最好以`教科書体`为书写的模板，而国内即使是专业的日语词典，比如 MOJi 、沪江小 D 等等都不支持`教科書体`，卡西欧的电子字典更不可能用作书写模板，至于国内出版的所谓字帖很多都是用的在简体汉字的字体印刷出来的，只是印的内容是日语而已。

注意：这部分的内容难度比较大，请确认自己是真的有需要、有能力再动手，遇到问题请先在 [ FreeMdict ](https://forum.freemdict.com/)和[ PDAWIKI ](https://www.pdawiki.com/forum/)搜索，很多问题都会迎刃而解。

## 为所有字典指定字体

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
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com/20220823111051.png)

另外，有部分字体的字体名称需要参考[中文字体的英文名称对照表](https://xuui.net/ui-design/english-name-of-chinese-characters-table.html)要求。

## 单独为某一本字典指定字体

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

## 如何下载词典&词典推荐

受限与版权和字典大小，这里只列举链接，请根据自己的需要下载：

### [Mdict](https://mdict.org/post/mdx/)

一个纯粹的资源站，提供的字典有很多精品，但是访问有点慢。

### [FreeDic论坛](https://forum.freemdict.com/)

提供的资源不如 PDAWIKI 多，但质量更好，另外还提供了一套很不错的制作教程。

### [PDAWIKI](https://www.pdawiki.com/forum/)

也可以下载到一些词典，但要花时间慢慢找

# 参考

[ GoldenDict 中文用户手册](https://github.com/Dictionaryphile/GoldenDict_zh_manual)