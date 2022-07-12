这里介绍一种不太一样的词典软件的使用方法，即「在线词典」这个功能——不用专门切到浏览器再去输一遍自己要查的词，而是借助软件本身实现输入的过程。

不过与使用离线词典相比，欧路这个功能一些不完善的地方：既不能高亮划重点记笔记（倒是可以通过制卡和导出来曲线救国），也不能分享链接，查到有意思的信息只能靠截图记录……

MOJi的在线词典功能虽然更鸡肋，但交互设计确实要好得多，只是可惜官方已经明确表态不会再跟进、维护这一功能……

另外，GoldenDic和EBpoct其实都是有类似的功能，但它们的规则都稍有不同，有需要的同学可以自己动手。

# 操作

## 手动添加

为方便大家手动导入，以下我修改过的链接，直接打开有可能提示“网页不存在”，但添加到欧路后再查词可能才能正常用。

另外，除非特意注明，以下网站在国内都可以正常访问。

### 电脑端

可以参考[不用花钱就能将新词典添加到欧陆词典的方法](https://www.bilibili.com/video/BV1Pg4y1i7gB?)，虽然UP主使用的是Mac端，但是Windows端的操作也差不多，至于使用Linux端的大佬，请随意……

###  手机端

可以参考[欧路词典的在线词典功能你会用吗？ - 支离的文章 - 知乎](https://zhuanlan.zhihu.com/p/91584001)

## 一键导入

文末附有词典配置，可以直接下载导入使用。

但一定要注意，直接导入后会丢失**原有**的词典配置（词典多的同学辛辛苦苦分的组会**直接**被抹掉），强烈建议自己编辑一下，需要有一点点的编程知识，了解一下xml语法即可。

# 词典网站推荐

按照个人使用频率推荐，如果想知道更多的词典网站，可以关注这个[项目](https://github.com/Dictionaryphile/All_Dictionaries#%E5%AE%87%E5%AE%99%E6%9C%80%E5%85%A8%E5%9C%A8%E7%BA%BF%E8%AF%8D%E5%85%B8%E7%BD%91%E7%AB%99%E5%AF%BC%E8%88%AA)，也可以关注作者的，除了词典网站外，也会不定期更新日语学习相关网站.

## 日日词典

- [Weblio辞書](https://www.weblio.jp/)
	- [https://www.weblio.jp/content/{w}](https://www.weblio.jp/content/{w})
	- 永远滴神~与它齐名的还有goo辞書，但可惜后者在国内访问不了……

- [goo辞書](https://dictionary.goo.ne.jp/)
	- [https://dictionary.goo.ne.jp/srch/all/{w}](https://dictionary.goo.ne.jp/srch/all/{w})
		- 与Weblio基本上使用的是同一个词典『デジタル大辞泉』的数据，
		- 不过额外提供了几个有用的小功能，比如除了『デジタル大辞泉』本身自带的例句外，还收录了『青空文庫』中包含该单词的例句，以及惯用句
		- ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-22-09-55-11.png)

- [JapaDic](https://www.japandict.com)
	- [https://www.japandict.com/{w}](https://www.japandict.com/{w})
		- 可以看到声调
		- ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220606001458.png)
		- 还能看到汉字的写法
		- ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220606001518.png)
		- 甚至还有动词变形后的声调音频！
		- ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220606001540.png)
		- 但可惜，国内完全用不了，而且解释是用的英语，所以才放在第三个位置介绍

- [OJAD日语声调词典](https://www.gavo.t.u-tokyo.ac.jp/ojad/)
	- [https://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/sortprefix:accent/narabi1:kata_asc/narabi2:accent_asc/narabi3:mola_asc/yure:visible/curve:invisible/details:invisible/limit:20/word:%7bw%7d](https://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/sortprefix:accent/narabi1:kata_asc/narabi2:accent_asc/narabi3:mola_asc/yure:visible/curve:invisible/details:invisible/limit:20/word:%7bw%7d)
	   - 共有大约3，500个用言，同时还配有真人朗读示范录音(包括了**動词变形**后的录音，『NHK日本語発音アクセント辞典』都没有这么贴心)，
	   - 最后几页还有一些音调特殊的词，但可惜这部分单词只是标注了声调，并没有配备录音
   - [OJAD - 韻律読み上げチュータ スズキクン (u-tokyo.ac.jp)](http://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index)这个子网页可以给一段话标出声调，也会提供机器生成的录音

- [语源由来辞典](https://gogen-yurai.jp/?s={w})
  - 比起Google搜索，这里的解释要严谨一些，而且

- [四字熟語](http://www.kotoba-library.com/?s={w}&x=17&y=16)和[平明四字熟語辞典](http://search.yojijyukugo.com/search.cgi?charset=utf8&q={w}&s=%E6%A4%9C%E7%B4%A2)
   - 第二个比四字熟語访问速度更快，结果也更全面
 
- [日本語俗語辞書](http://search.zokugo-dict.com/search.cgi?charset=utf8&q={w})
  - 能查到一些近年来新出现的新词，还会附带详细的解释

- [故事ことわざ辞典](http://search.kotowaza-allguide.com/search.cgi?charset=utf8&q={w}&s=%E6%A4%9C%E7%B4%A2)和[ことわざの参考書](http://tantaka.com/mt/mt-search.cgi?IncludeBlogs=4&search={w})
   - 就搜索结果而言，难分伯仲

- [違いがわかる事典](https://chigai-allguide.com/?s={w})
  - 区分了一些易混淆的单词，但不多

- [連想類語辞典](https://renso-ruigo.com/)：[(https://renso-ruigo.com/word/{w}](https://renso-ruigo.com/word/{w}) 
	- 相当于近义词词典

- [広辞苑無料検索](https://sakura-paris.org/dict/)
	- [https://sakura-paris.org/dict/広辞苑/prefix/{w}](https://sakura-paris.org/dict/広辞苑/prefix/{w})
		- 虽然网站叫“广辞苑”，但是实际上不止一本词典
		- 这个词典网站的网址有点奇怪，如果需要每次指定查询那几本词典，请自己研究
		- ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-22-09-31-56.png)

- [読み方は？](https://yomikatawa.com/kanji/%7Bw%7D?search=1)
   - 偶尔用来查些人名之类的东西
  
- [日本語辞典・漢字字典・ことわざ辞典・四字熟語辞典](http://www.nihonjiten.com/search/search.php?word={w})
   - 偶尔会突然访问不了……但提供的词典不少
   ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-23-15-32-44.png)

- [言葉バンク](https://kotobank.jp/gs/?q={w})
   - 搜索结果过多，排版有点乱，用得不多，另外有时访问速度很慢
  
- [通信用語の基礎知識](https://www.wdic.org/search?word=%7Bw%7D&mode=auto)
	- 大多数人可能用不到…但作者对这个领域词汇挺感兴，但注意，搜索完后还要点击红框部分才能看到解释
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-23-17-19-45.png)

## 中日词典

- [白水社 中国語辞典](https://cjjc.weblio.jp/content/{w})
  - 非常好用的词典，尤其是碰到一些难写又正好不知道读音的单词时，这个网站就是最后一根救命稻草(欧路词典不像MOJi/小D，会自动将输入简体中文汉字识别为对应漢字)
  ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220208215223.png)

- [BitEx中国語学習](https://bitex-cn.com/?m=Dic&a=search&dickeyword={w})
   - 比下面的北辞郎稍微专业严谨一些，可以查到很多中国菜和经典电影的日文说法
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-21-11-20-45.png)
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-21-11-22-21.png)

- [中日辞書 北辞郎](http://www.ctrans.org/index.php)
	- [http://www.ctrans.org/search.php?word={w}](http://www.ctrans.org/search.php?word={w})
	- 几个中日词典里最不正经的一个(o(￣┰￣*)ゞ)…… 
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-23-15-50-32.png)
   - 不过确实收录了很多流行语
![|350](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-21-11-32-39.png)
   - 只不过个人觉得有些单词说法没有那么权威，可能是某些热心的志愿者自己的翻译，但也有一定的参考价值，如果对这类流行语感兴趣的话，公众号“联普日语社区”可能更好（他们一般会以日本的报道作为参考）
![|350](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-23-15-55-37.png)
 ![|350](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220208215145.png)

## 百科

- [百度百科](https://baike.baidu.com/)
	- [https://baike.baidu.com/item/{w}](https://baike.baidu.com/item/{w})
	- 还是可以用用的，可以用来搜搜日本文化、地理相关的知识

- [维基百科](https://zh.m.wikipedia.org/wiki/{w})和[维基百科(日语版)](https://ja.m.wikipedia.org/wiki/{w})
	- [https://zh.m.wikipedia.org/wiki/{w}](https://zh.m.wikipedia.org/wiki/{w})
		- 汉语版
	- [https://ja.m.wikipedia.org/wiki/{w}](https://ja.m.wikipedia.org/wiki/{w})
		- 日语版
	- 可以发现很多好玩的东西，不过国内访问不了
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220208215108.png)

-   [萌娘百科](https://mzh.moegirl.org.cn)
	- [https://mzh.moegirl.org.cn/index.php?search={w}](https://mzh.moegirl.org.cn/index.php?search={w})
	- 好像混进了奇怪的东西(囧……)

-   [Yahoo知恵袋](https://chiebukuro.yahoo.co.jp/search?p=%7Bw%7D&fr=common-navi)
	- [https://chiebukuro.yahoo.co.jp/search?p={w}&fr=common-navi](https://chiebukuro.yahoo.co.jp/search?p={w}&fr=common-navi)
	- 相当于国内的百度知道和知乎
	- 如果查阅了以上的网站仍然搞不清楚某个词的用法，可以去这里试试看
	- 这个网页在国内可以正常访问:)

-   [豆瓣](https://m.douban.com)
	- [https://m.douban.com/search/?query={w}](https://m.douban.com/search/?query={w})
	- 书籍、影视作品的翻译最好参考一下国内已经出版的译名
	- 豆瓣好像对每天的访问次数有一定的限制，超过之后，就得登录

## 汉字

说实话，对于非日语专业的学生来说，这一部分的词典用处不是很大，毕竟各类考试都很少会考字形，但架不住专业课老师要听写啊o(TヘTo)

-   [文字拡大]([httpsl](https://moji.tekkai.com/)
	- [https://moji.tekkai.com/zoom/{w}/page.html](https://moji.tekkai.com/zoom/{w}/page.html)
		-  提供了日文汉字的不同字体的图片（包括教科书体），如果对教材上的汉字字形存在疑虑，可以参考这个网站。
		- 注意一次只能输入一个汉字

- [漢字の正しい書き順](https://kakijun.jp/) 
	- [https://kakijun.jp/m-s/ms_kensakupage.html](https://kakijun.jp/m-s/ms_kensakupage.html)
		- 这个需要再手动输入一次
	- [https://cn.bing.com/search?q={w}+site%3Akakijun.jp](https://cn.bing.com/search?q={w}+site%3Akakijun.jp)
		- 借助Bing的搜索语法实现，可能会有遗漏的，如果查不到，可以在用上面的链接

-   [漢字ペディア](https://www.kanjipedia.jp/search?k=%7Bw%7D&kt=1&sk=leftHand)
	- 遇到实在记不住汉字，可以在这个网站上查查字源说不定会有收获

-   [汉典](https://www.zdic.net/)
	- [https://www.zdic.net/hans/{w}](https://www.zdic.net/hans/{w})
		- 现在基本不用百度汉语了，主要是汉典就可以快速比较比较中日文汉字字形差异
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220606002123.png)

- [百度汉语](https://hanyu.baidu.com/s?wd={w})
	- [https://hanyu.baidu.com/s?wd={w}](https://hanyu.baidu.com/s?wd={w})
	- 原来是用来比较一些汉字写法的细微差别，比如:
	 ![|250](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-23-15-00-05.png)![|250](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220208215301.png)
	- 偶尔也来比较一些日语四字熟语和汉语成语之间的细微差别，比如
![|400](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-07-23-14-39-00.png)![|400](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220208215004.png)

## 搜索引擎

之所以列出来，纯粹是作者懒得专门切到浏览器，再输入一遍……

- [必应搜索](https://cn.bing.com)
	- [https://cn.bing.com/search?q={w}](https://cn.bing.com/search?q={w})
	- - 勉强可以当成个Google镜像来用

- [必应图片](https://cn.bing.com/images)
	- [https://cn.bing.com/images/search?q={w}](https://cn.bing.com/images/search?q={w})
		- 有些时候看不懂字典描述，找张图片一看一下就明白了

- [Google搜索](https://www.google.com)
	- [https://www.google.com/search?q={w}](https://www.google.com/search?q={w})
		-  知名404网站，用过的都说好，就不展开介绍了，另外，这个其实可以与`+site%3A+Weblio.jp`这样的搜索语法配合，就不展开介绍了，有兴趣的话，可以自己研究

- [百度搜索](https://www.baidu.com/)
	- [https://www.baidu.com/s?ie=utf-8&wd={w}](https://www.baidu.com/s?ie=utf-8&wd={w})
		- 将就一下也不是不行

## 机器翻译

好吧……这部分可能会引起争议，所以我才放到了最后，注意掌握好度。

下面只列出我个人最常用的三个网站，欧路的Android现在已经内置了3个翻译引擎了，不过输入中文时是翻译成英语；电脑似乎还是给的一个引擎。

 -  百度机翻
	 - [https://fanyi.baidu.com/?aldtype=16047#jp/zh/{w}](https://fanyi.baidu.com/?aldtype=16047#jp/zh/{w})
		 - 注意上面是日到中的语言对，虽然可以手动改
	 - [https://fanyi.baidu.com/?aldtype=16047#zh/jp/{w}](https://fanyi.baidu.com/?aldtype=16047#zh/jp/{w})
		 - 中到日的话得用这个

- 搜狗机翻
	- [https://fanyi.sogou.com/text?keyword={w}%0A&transfrom=auto&transto=ja&model=general&exchange=true](https://fanyi.sogou.com/text?keyword={w}%0A&transfrom=auto&transto=ja&model=general&exchange=true)
	- 放在后面完全是因为搜狗大多时候与百度差不了多少，只是在有些细节上做得很好

 - Google机翻
	 - [https://translate.google.com/?hl=zh-CN&tab=TT&sl=auto&tl=zh-CN&text={w}&op=translate](https://translate.google.com/?hl=zh-CN&tab=TT&sl=auto&tl=zh-CN&text={w}&op=translate)
	 - 虽然很多时候都不如百度，但还是列出来吧

如果你对机器翻译方面有兴趣，可以读读这篇文章。

## 其他

- [日语语法酷](https://grammar.izaodao.com/)
	- [https://grammar.izaodao.com/grammar.php?action=search](https://grammar.izaodao.com/grammar.php?action=search)
	- 这个只能自己手动输入一遍啦
	- 当然也可以下载APP

- [Yahoo知恵袋](https://chiebukuro.yahoo.co.jp/)
- [https://chiebukuro.yahoo.co.jp/search?p={w}&fr=common-navi](https://chiebukuro.yahoo.co.jp/search?p={w}&fr=common-navi)
  - 相当于国内的百度知道，如果查阅了以上的网站仍然搞不清楚某个词的用法，可以去这里试试看，这个可以正常访问

# 词典配置

 [欧路词典在线词典配置备份 蓝奏云](https://wwa.lanzoui.com/b010n89re) 密码:9jzz

