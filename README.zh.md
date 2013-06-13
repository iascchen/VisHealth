# VisHealth

VisHealth 是一个面向运动和健康监控数据挖掘和可视化的开源项目，目前版本采用python 2.7.3开发。
目标在于集成各种可穿戴设备，将用户的运动和健康监控信息整合在一起，打破不同可穿戴设备厂家的数据壁垒，形成用于运动和健康数据的可视化和挖掘代码包。
创建数据挖掘的样本数据集。

## 许可证信息
这个项目目前是个人兴趣和业余爱好，主要是对基于健康的数据挖掘比较感兴趣，项目遵循GPLv3许可。

## 开发计划

初步计划的内容包括：
1. 在服务端实现对于Jawbone、Bitfit、Withings、Codoon等穿戴式运动和健康设备数据的集成。
2. 实现响应式的健康数据可视化Web应用，初步计划是基于Python、Flask、Bootstraps进行，前端数据可视化展现以D3为基础实现。
3. 在2的基础上，对收集到的数据进行数据挖掘实验。

## 版本发布

20130613
首先实现了Jawbone up 手环的非官方API。这些请求目前能够在Jawbone的 v.1.34 中使用，随时可能失效。
参考链接 : [eric-blue](http://eric-blue.com/2011/11/28/jawbone-up-api-discovery/), the "healthCredits" method can't be accessed. [alexburrell](https://github.com/alexburrell/up-for-status-board])

## 使用

### Jawbone UP API
如果想使用这段代码，可以在打开 /devices/jawboneup.py， 在main方法中，修改自己的用户名和密码，然后执行main即可。此代码会将交互的json文件存放在 data/jawboneup 目录下
```python
account = { "email" : "iasc@163.com" , "passwd" : "yourpassword" }
```

## 帮助

###加入开发 : 
如果您熟悉HTML5、JavaScript、D3、Python，而且对于穿戴式数据集成、可视化、以及挖掘感兴趣，可以自由加入开发，贡献您的代码。

###关注穿戴式设备数据挖掘 ： 
即使您不具有开发能力，你也可以通过加我为好友，允许我访问您的健身和健康设备为实验数据。
如果您有其他的穿戴式设备，希望能够集成到这个系统中，可以联系我，提供相应的测试账号和数据，用于VisHealth相关开发和测试使用，未经您的允许，不会被用于任何商业用途。
如果您生产的设备已经提供开放API，也可以告知我，增加到VisHealth的支持中。

## 联系我

邮件：
iascchen AT gmail.com or iasc AT 163.com

加我为好友 ：
1. 新浪微博 ： [@问天鼓](http://www.weibo.com/u/2090594487）
2. Jawbone Up 账号 ： iasc@163.com 

