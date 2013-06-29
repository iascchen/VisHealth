# 获取Jawbone UP中的个人数据（二）非官方API #

---

Author : iascchen(at)gmail(dot)com

Date : 2013-06-20

新浪微博 : [@问天鼓]([@问天鼓](http://www.weibo.com/iascchen)

---

从Jawbone网站上，能够下载UP的个人数据，但是这个数据是以天为单位的汇总数据，如果我们需要更精细的数据，就必须通过程序获取。

Jawbone官方网站宣称已经提供开发API，用于与合作方应用之间进行数据交换。但是这个API在网上见不到。我辈苦逼的码农想玩玩自己的数据，只好另想办法。

Eric Blue曾经于2011年11月发表过一篇博文[jawbone-up-api-discovery](http://eric-blue.com/2011/11/28/jawbone-up-api-discovery/)，介绍了他通过网络侦听Jawbone UP应用与服务器之间的通讯，破解出的一些非官方API，这些API可以用于获得用户自己的运动数据。时过境迁，Jawbone UP硬件已经更新换代至UP 2，手环版本为6\-1.0.20，手机应用软件也已经升级到了2.6.8版本，Server端版本已经更新至1.34。Eric Blue公布的API部分内容已经过时。

下面的API是对Jawbone UP的Android版本进行了反编译所得到的，并借鉴了Eric Blue的方法，通过对Jawbone UP应用发出的请求进行侦听以确认，错误在所难免。

详细内容如下：

[1. 概述和登陆 ](how-to-fetch-jawbone-data-unofficial-api_1.md)

[2. 用户行为概况 ](how-to-fetch-jawbone-data-unofficial-api_2.md)

[3. 睡眠情况细节——Sleeps ](how-to-fetch-jawbone-data-unofficial-api_3.md)

[4. 运动情况细节——Moves ](how-to-fetch-jawbone-data-unofficial-api_4.md)

[5. 锻炼情况细节——Workouts ](how-to-fetch-jawbone-data-unofficial-api_5.md)

[6. Meals 和 Mood ](how-to-fetch-jawbone-data-unofficial-api_6.md)

[7. 其他个人信息 ](how-to-fetch-jawbone-data-unofficial-api_7.md)

[8. 运动趋势统计和生命线 ](how-to-fetch-jawbone-data-unofficial-api_8.md)
 
其他还有一些社交类、饮食类 API 与用户行为数据相关性不大，不再进行分析。

Jawbone UP 非官方 API 到此为止，祝各位玩的开心！

