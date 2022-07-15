# 使用方法

如果你是第一次使用，请先登录[欧路词典官网](https://my.eudic.net/OpenAPI/Authorization)获取下图红框部分的内容
![](Assets/Pasted_image_20220714111636.png)

启动GoldenDic软件，点击`编辑`
![](Assets/Pasted_image_20220714113402.png)
点击`首选项`
![](Assets/Pasted_image_20220714113725.png)

点击`高级`，设置红框所勾的地方
![](Assets/Pasted_image_20220714113422.png)

设置好了之后，关闭页面，回到软件的启动页面

找到`配置文件夹`这个按钮，点击打开文件夹
![](Assets/Pasted_image_20220714112339.png)

把`.exe`和`setting.json`文件复制到这里

# Todo

- [x] 导出的xml文件的时间戳不是北京时间，而是伦敦时间，会有一定的误差
- [x] 优化大多数Markdown笔记软件的所见即所得的效果导致复制时容易选中多余的标点符号（比如`清浄`这样被包裹起来的）
- [x] 不重复导入已经导入的单词
- [x] 自定义弹窗时间
	- [x] （显示上传结果）
- [ ] 通过`setting.json`保存、自定义设置
- [ ] 不上传「日本語非辞書形辞典」中动词变形
	- [ ] （比较相邻的2个单词在[-1]位置上的差别）
	- [ ] 通过还原出原型载判断是否是重复单词
- [ ] 支持后台定时运行
	- [ ] （现阶段可借助Win计划任务程序实现自动上传传，或者使用[MyKeymap](https://xianyukang.com/MyKeymap.html#mykeymap-%E7%AE%80%E4%BB%8B)、[Quiker](https://getquicker.net/)等工具实现快捷上传）
- [ ] 修复Win11下现无法关闭弹窗的问题（Win10下没有这个问题）