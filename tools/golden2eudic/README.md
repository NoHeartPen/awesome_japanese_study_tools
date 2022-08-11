# 下载地址

你可以通过下面的2种方式，下载名为`goldendic2eudic.zip`的文件。其他文件可以不下载。

[Gitee](https://gitee.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/golden2eudic/dist)，由于政策原因，这种方式下载需要扫码注册登录

[GitHub](https://github.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/golden2eudic/dist)，如果你不能访问Google主页，推荐使用上面的下载方式

# 使用方法

## 基本设置

如果你是第一次使用，请先登录[欧路词典官网](https://my.eudic.net/OpenAPI/Authorization)获取下图红框部分的内容
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220714111636.png)

启动GoldenDic软件，点击`编辑`
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220714113402.png)

点击`首选项`
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220714113725.png)

点击`高级`，设置红框所勾的地方
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220714113422.png)

设置好了之后，关闭页面，回到软件的启动页面，找到`配置文件夹`这个按钮，点击打开文件夹。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220714112339.png)

把`goldendic2eudic.exe`和`setting.json`文件复制到这里。

然后右键点击`setting.json`，通过`打开方式`，选择用记事本打开它

将之前在[欧路词典官网](https://my.eudic.net/OpenAPI/Authorization)获取的内容替换下面的红框的部分的`1234567890`，注意不要删掉附近的英文双引号。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811202233.png)

完成后，我们可以把GoldenDict软件打开，看看有没有查词记录，如果没有的话，随便查一个单词，然后我们等待1分钟，打开`history`，确认里面有单词之后，就可以关了。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811203716.png)

当然，你也可以通过文件大小来判断，只要不是`0KB`，你都可以直接直接进入下一步。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811203730.png)

我们在资源管理的这个位置，输入`cmd`
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811203102.png)

会有个黑漆漆的命令行的弹窗，我们把`goldendic2eudic.exe`拖进去，然后按下回车键
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811203204.png)

看到`单词导入成功，导入数量：`这样的提示，恭喜你！已经完成了基本设置，以后可以直接双击运行这个脚本了:)
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811204056.png)

如果在上一步你看到了其他提示，很抱歉，你似乎遇到了一些问题。

你可以先休息一下，然后再看一遍这个教程，看看有没有遗漏的地方，然后你可以参考[遇到了问题？](# 遇到了问题？)部分

你可以右键把快捷方式放到桌面，这样你以后每次只需轻轻一点，就可以同步了:)
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220811204922.png)

## 高级设置

如果你不想每次都自己双击脚本，你可以借助Windows的计划任务程序，每隔5分钟自动同步一次。

需要注意的是在Win11系统上这样做的话，每隔5分钟就会有一个弹窗一闪而过，所以你最好通过其他方式来快速执行这个脚本，比如[MyKeymap](https://xianyukang.com/MyKeymap.html#mykeymap-%E7%AE%80%E4%BB%8B)、[Quiker](https://getquicker.net/)等工具。

我也会尽量想办法解决这个问题，请耐心等待。

# 遇到了问题？

如果你确定自己的每一步都是按照教程执行，但还是遇到问题，你可以通过我的邮箱NoHeartPen@outlook.com向我寻求帮助。

如果你能按照[《提问的智慧》](https://zhuanlan.zhihu.com/p/19761517)中的方法向我提问，我会非常高兴地回答你的问题。

通常，我会在3天之内回复邮件。

如果你没有收到任何回复，你应该认认真真把我说的这本[《提问的智慧》](https://zhuanlan.zhihu.com/p/19761517)看一遍，然后模仿其中的例子向我提问，这样能节省大家的时间。

# Todo

如果你有什么建议，欢迎提出来，我非常愿意让这个项目帮助到更多人:)。

- [x] 导出的xml文件的时间戳不是北京时间，而是伦敦时间，会有一定的误差
- [x] 优化大多数Markdown笔记软件的所见即所得的效果导致复制时容易选中多余的标点符号（比如`清浄`这样被包裹起来的）
- [x] 不重复导入已经导入的单词
- [x] 自定义弹窗时间
	- [x] （显示上传结果）
- [x] 支持删除已同步的单词
	- 需要在关闭GoldenDict的前提下运行脚本才有效
- [ ] 通过`setting.json`保存、自定义设置
	- 在任务计划程序的`添加参数`，填入GoldenDict的portable文件夹的绝对路径
- [ ] 不上传动词变形
	- [ ] （比较相邻的2个单词在[-1]位置上的差别）
	- [ ] 通过“日本語非辞書形辞典”项目判断是否是重复单词
- [ ] 支持后台定时运行
	- [ ] （现阶段可借助Win计划任务程序实现自动上传，或者使用[MyKeymap](https://xianyukang.com/MyKeymap.html#mykeymap-%E7%AE%80%E4%BB%8B)、[Quiker](https://getquicker.net/)等工具实现快捷上传）
- [ ] 修复Win11通过计划任务程序无法关闭弹窗的问题（Win10下没有这个问题）

注：本文是[goldendic2eudic](https://gitee.com/NoHeartPen/awesome_japanese_study_tools/tree/master/tools/golden2eudic/)项目的说明文档。