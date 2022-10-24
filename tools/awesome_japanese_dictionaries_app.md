先说我的推荐：Android 端 欧路词典+ EBPocket，电脑端 GoldenDic。

下面按照软件上手难度递增，介绍下接触过的同类软件。

# Android 端

## 网易

基础释义免费，会员才可使用《新世纪日汉双解大辞典》（2009年出版，近17万词条）的词库

年卡168（买一年送一年），半年卡128，月卡25，连续包月首月6元，次月18

## 沪江小D

完全免费，词库数据是《现代日汉双解词典》（2012年出版，4万2千余条词库），

## MOJi

基础释义免费，词库数据未知，由于支持用户自己创词，搜索结果和前面的相比会好一点（个人主观评价）。

基础会员78，高级会员每月8元，半年25元，1年35元

与上面的相比，接下来介绍的词典都是由出版社和软件公司共同出品的软件，都没有丰富的拓展功能，但胜在解释权威可靠更新及时。

## 版权词典

## [海笛词典公司](https://haidii.com/hdmcenter.html)

整体质量都比较一般，功能单一

### 日语大词典

[官网下载链接](https://pkgdl.haidii.com/pkg/25200/lnrm_xrhhrcd_25200_fxxz.apk)
买断制：98
数据是新日汉辞典和
[新汉日辞典](https://book.douban.com/subject/26991436/)，其中新日汉辞典在2017年出了修订版，有兴趣的话可以去验证一下看看是不是最新版。

## 外研社日语词典

[官网下载链接](https://pkgdl.haidii.com/pkg/8015/wys_rhhr_8015_fxxz.apk)
软件买断制：45元
数据是《现代日汉汉日词典》
收词：日汉一万八千，汉日一万八千

## Google Play Store 上架的日语词典App

虽然[该网站](http://blog.sina.cn/dpool/blog/u/3704881170#type=-1)给出了原文词典App的文件，但要安装到手机上，还有很多繁琐的步骤，所以请根据自己的能力和时间决定是否要花时间来折腾。

不想折腾，要购买的话，可以参考这篇文章[跨境通VISA/万事达借记卡介绍与网上支付体验](https://poplite.xyz/post/2018/03/05/boc-debit-card-guide-for-online-payment.html#8-%E6%9D%82%E9%A1%B9)办张卡,然后注意自己的代理位置——最好是一直都挂在日本。

接下来介绍的词典软件都需要自己导入词典资源才可使用，上手较为麻烦。

## [欧路词典](https://www.eudic.net/v4/en/app/eudic)

由于并非为日语设计的词典软件，对输入十分敏感，无法转换简体汉字和日语漢字，比如输入“踌躇”是无法查到「躊躇」，所以新手用起来会比较有压力。

买断制 78元，不过不解锁会员，单「查词」功能而言，几乎没有影响影响（会员功能主要是云同步）

再提下欧路的在线词典，详细的操作步骤在[eudic_handbook_for_japanese](../websites/eudic_handbook_for_japanese.md)

## [EBPocket](http://ebstudio.info/manual/EBPocket_android/)

作者提供了免 Google 框架的免费版本的APK文件：[EBPocket.apk](http://ebstudio.info/download/ebpocket/1_15_0/EBPocket.apk)，但是这个非常旧了，虽然能用，但是不能加载太多的词典。

词典资源可以参考[【资源分享】史上最强词典EBPocket安装教程+24G词典资源免费放送](https://mp.weixin.qq.com/s/RYUHtLszaD6I7enp518L-g)和知乎这个回答

## [AnkiHelper](https://github.com/mmjang/ankihelper)

这个实际上要与Anki搭配使用，上手难度极大，可以参考这个回答[有哪些背日语单词的app推荐?](https://www.zhihu.com/question/36247408/answer/2672293167) 
 
# Windows 端

之前介绍的词典软件大都由有自己的网页版，在电脑上都能用。

下列介绍词典软件都需要自己下载词典文件的外壳软件，如果只需要一个可查词的网站，请参考[websites](websites)部分的内容。

另外，接下来介绍的软件，都在不同程度上支持剪贴板查词，也就是像这样：

![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//_00_00_00-00_00_30.gif)

但就整体效果而言：
1. GoldenDict：需要借助[日本語非辞書辞書](https://github.com/NoHeartPen/JapaneseConjugation)项目的 v2 版本的`日本語非辞書辞書.mdx`文件 和[ hunspell_ja_JP](https://github.com/MrCorn0-0/hunspell_ja_JP)，才可以可以实现完美的划词体验
2. 欧陆词典：无法处理形容词，以及特殊标记，但是支持多重嵌套（使被态、部分简单的句型），
3. 沙拉查词：无法处理用言变形，但是可以借助 [日本語非辞書辞書](https://github.com/NoHeartPen/JapaneseConjugation) v3版本来实现类似 GoldenDict 的查词体验
4. EBWin：无法处理用言变形，但是可以通过 [日本語非辞書辞書](https://github.com/NoHeartPen/JapaneseConjugation) v3版本来实现类似 GoldenDict 的查词体验
5. MOJi辞書 Plugin ： 准确率不稳定，向开发者反应过相关问题，以后也许会提高准确率
6. Yomichan 和 rikaikun ：支持简单的动词活用，没有第三方的工具来提高准确率

## 欧路词典

电脑付费168，不付费就只能加载3本词典，但不影响同步。

不想折腾、愿意付费的用户的首选，但注意欧路词典不能加载EBWin格式的词典。

## [EBWin](http://ebstudio.info/manual/EBWin4/EBWin4.html)

免费，不支持云同步笔记和查词记录；

有很多独家词典，但都比较旧；不过也支持加载mdx格式词典（这种格式有很多比较新的词典）；切换字体很方便；

可以用第三方工具[ebwin2eudic](ebwin2eudic)来同步查词记录

## GoldenDict

可以直接使用[goldendict_for_japnese_portable](goldendict_for_japnese_portable)开箱即用版，相关评价和教程在[README.md](goldendict_for_japnese_portable\README.md)。

# 浏览器拓展

推荐使用 Microsoft Edge 浏览器，兼容 Chrome 的拓展，不用FQ

## [沙拉查词](https://saladict.crimx.com/)

### 优点

1. 国内开发者开发，上手难度较低
2. 可以和Anki、欧路词典、扇贝单词等同步单词本，但需要自己动手
3. 内置沪江小D 和 Weblio 辞書，基本满足日常需要

## [MOJi辞書 Plugin](https://www.mojidict.com/article/1BvHLjMm8u)

还行，闲逛时也能学点日语，不过只能在浏览器内使用

## [rikaikun](https://github.com/melink14/rikaikun) 和 [Yomichan](https://foosoft.net/projects/yomichan/)

由于都是国外开发者开发，所以干脆放在一起说。

上手难度都比较大，作者也没怎么仔细研究，只是简单体验了下。由于是专门为了日语学习而设计，所以有些细节做得比沙拉查词好: 比如 Yomichan 除了可以与 Anki 搭配，还可以导入 EBwin 格式的词典，对于动词活用变形也有一定的支持。