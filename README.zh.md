# VisHealth

VisHealth 是一个面向运动和健康监控数据挖掘和可视化的开源项目，目前版本采用python 2.7.3开发。
目标在于集成各种可穿戴设备，将用户的运动和健康监控信息整合在一起，打破不同可穿戴设备厂家的数据壁垒，形成用于运动和健康数据的可视化和挖掘代码包。
创建数据挖掘的样本数据集。

## 许可证信息
GPLv3

## 版本发布

20130613
首先实现了Jawbone up 手环的非官方API。这些请求目前能够在Jawbone的 v.1.34 中使用，随时可能失效。
参考链接 : [eric-blue](http://eric-blue.com/2011/11/28/jawbone-up-api-discovery/), the "healthCredits" method can't be accessed. [alexburrell](https://github.com/alexburrell/up-for-status-board])

## 使用

### Jawbone UP
如果想使用这段代码，可以在打开 /devices/jawboneup.py， 在main方法中，修改自己的用户名和密码，然后执行main即可。此代码会将交互的json文件存放在 data/jawboneup 目录下
```python
account = { "email" : "iasc@163.com" , "passwd" : "yourpassword" }
```

## 联系我
Email ： iascchen AT gmail.com or iasc AT 163.com
新浪微博 ： [@问天鼓](http://www.weibo.com/u/2090594487）


