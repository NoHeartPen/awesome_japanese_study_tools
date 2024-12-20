# 影音漫画小说词汇挖矿指路

分享者：[Oshibuki](https://github.com/Oshibuki)

整理者：[NoHeartPen](https://github.com/NoHeartPen)

原文链接：<https://github.com/NoHeartPen/awesome-japanese-study-tools/issues/6#issue-1909744937>

词汇挖矿是 “mine from sentence” 的直译，指选择难度略微超过舒适区，又存在少量生词、难度适中的材料进行阅读，记录生词，整理成笔记后再复习的过程。

大体而言，记录生词的最终目标都是制作带有语境的 Anki 卡牌。但具体的挖掘方法又随着材料种类和技术进步的发展有所不同。

## 必备基础

### yomichan

* yomichan 教程视频：<https://space.bilibili.com/1659314118/channel/collectiondetail?sid=1675392>
* yomichan 辞书：上述 B 站教程视频下方简介有中日双语版本
* anki-connect

### anki

* 挖矿模板比较推荐 tatsumoto 的 japanese sentence 模板 <https://ankiweb.net/shared/info/1557722832>
* 对应的 Anki 设置 <https://tatsumoto.neocities.org/blog/setting-up-anki#import-an-example-mining-deck>

## 视频

这类材料以能找到单独字幕文件（需要严格对轴视频材料）的动画、影视作品为主。

字幕与视频重新同步：<https://animecards.site/subtitles/>。

### 字幕网站列表

* 日文字幕：
  * kitsunekko：
    * <https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese>
  * kitsunekko 的备份：
    * <https://learnjapanese.moe/kitsubackup.html#/ja/>
    * <https://djtguide.github.io/library/sub.html>
* 中文字幕：
  * <https://github.com/bipy/Anime-Subtitles>
* 中日双语字幕：
  * <https://github.com/Nekomoekissaten-SUB/Nekomoekissaten-Storage>

### 动漫网站

<https://animelon.com/> 专为日语学习者设计，自带字幕。

<https://aniwatch.to/> 能找到比较久远的视频。

### 日剧

[2022 年下载日剧生肉和外挂字幕的方法](https://springwood.me/raw-drama-and-soft-subtitle/)

### 手动挖掘工具

浏览器插件： [asbplayer](https://github.com/killergerbah/asbplayer) [animebook](https://animebook.github.io/)

asbplayer 可看作是 animebook 的升级版本，二者均需要手动配置输入 Anki 的目标字段。

### 自动挖掘工具

[subs2srs](https://subs2srs.sourceforge.net/) 用于批量从字幕和视频中生成 Anki，缺点是后处理费时费力。

## 漫画

当下这一领域流行的是来自 HuggingFace 的 AI 模型 [Manga-OCR](https://huggingface.co/kha-white/manga-ocr-base)，而不是比较老的 Capture2Text。

Manga-OCR 衍生了一系列工具，较为有名的有：

* Poricom： 漫画阅读器，需要手动框选进行文字识别
* kha-white/mokuro 及它的移动端适配分支
* ZXY101/mokuro： 对漫画进行 OCR 并生成元数据和 html 文件，在浏览器打开 html 文件即可选中文本调用 Yomichan 查询并加入 Anki。

经过 mokuro 预处理的漫画资源可在 <https://mokuro.moe/manga/> 找到，比较推荐通过 <https://mokuro.moe/manga/_torrents/> 内的 BT 种子文件下载，降低网站服务器压力。

mokuro 阅读器：<https://reader.mokuro.app/>

PC 端设置阅读漫画：<https://xelieu.github.io/jp-lazy-guide/setupMangaOnPC>

[jidoujisho](https://github.com/lrorpilla/jidoujisho): 一款功能齐全的沉浸式移动语言学习套件，内置 Yomichan （需导入辞典），mokuro 漫画阅读器、ttu 阅读器（用于 epub 阅读），webview 浏览器（特定程序注入网页便于翻译和查询），音视频播放器等。

## epub 阅读

浏览器阅读推荐 <https://reader.ttsu.app/> ，可安装为 PWA 应用，适合日文文本 epub 阅读。默认垂直排版，设置内可调整为水平排版。

## 挖矿技巧总结

[Shiki’s Lazy Sentence Mining Workflow](https://docs.google.com/document/d/e/2PACX-1vQuEAoZFoJbULZzCJ3_tW7ayT_DcQl9eDlrXMnuPGTwDk62r5fQrXak3ayxBsEgkL85_Z-YY5W4yUom/pub)

[Mining from Anime](https://animecards.site/minefromanime/)
