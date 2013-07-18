# 获取咕咚运动移动应用中的数据——非官方API #

---

Author : iascchen(at)gmail(dot)com

Date : 2013-07-17

新浪微博 : [@问天鼓](http://www.weibo.com/iascchen)

---

这些 API 通过对 Codoon 运动的 Android 版本 [下载地址](http://static.codoon.com/app/android/codoonsports.apk) 进行了反编译所得到的，错误在所难免，随时可能失效，仅供大家学习和自娱自乐。

下面所列举的 API 均为读取运动数据相关的API。不包括其他发消息、发微博、更新状态等功能。

这个工作已经做了些日子，一直想等着用咕咚手环数据测试一下，所以没有写下来。不过照着目前网友们对咕咚手环的测试样品的评论来看，估计还需要一段时间才能有结果。申波在七月初参加2013移动互联网创新大会时透露 Codoon 官方的 API 要到明年才会开放。在目前这个过渡时期，大家可以用这个来玩玩吧。


详细内容如下：

1. 概述和登录

2. 用户运动成就

3. 用户运动历史

4. 智能配件相关 API(疑似)

5. 其他

# 1. 概述和登录 #

## 客户端请求基本说明 ##

Codoon App 一般通过 HTTP 协议与 api.codoon.com 通讯。在进行其他访问之前，必须先登录。可以用 Codoon 网注册用户通过 HTTP Basic 协议进行登陆。正确登录之后，在每次请求的HTTP中，需要将认证时的所获得 access_token 值设置到 HTTP Header：**Authorization** 里，即可保持会话。除此之外，还需要将**Charset**设置为 UTF-8。如：

	Authorization : Bearer  4836c512060faa34793730959daa901f
    Charset : UTF-8

Codoon App 还支持利用新浪微博、腾讯微博、人人网的用户，通过OAuth协议登录（这几种登录方式本文并未论述）。

### 带参数的请求 ###

需要向 Server 端提交参数的请求，均需要采用 POST 方式传参。比较特殊的是，在 Codoon 的接口中，需要将参数需要转化为 JSON 之后，放在 POST 体中再提交。

下面的 Python 代码作为参考示例：

	startDate = "2013-06-01"
    endDate =  "2013-06-30"
	command = "http://api.codoon.com/api/gps_statistic"

	request_data = {"from_date" : fromDate , "to_date" : toDate}
	response = requests.post(command , data = json.dumps(request_data),  headers = self.codoonHeaders )
    content = json.loads(response.content)

---

## 利用 Codoon 网注册用户登录 ##

![登陆](imgs/IMG_1689.PNG)

**Request：**

	POST	
	http://api.codoon.com/token

**Params：**
	
	# 下面两个参数为常量，说明登录方式
	"grant_type" : "password" ,
	"scope" : "user" ,

	# Client_ID 的值为来自于应用的静态变量值。此处一般不需修改。
    "client_id" : "dc039f07e003da02938a5bc4605b5acc" ,

    # 您个人在 Codoon 网注册的Email地址和用户密码。
    "email": email, 
	"password" : password 

**Return :**

Access Token 值为 JSON 内容中的 `"access_token" : "4836c512060faa34793730959daa901f"` 

完整JSON示例如下：
	
	{
	    "user_id": "bcf5ea34-891f-xxxx-a26f-496604a5xxxx", 
	    "access_token": "4836c512060faa34793730959daa901f", 
	    "token_type": "bearer", 
	    "scope": "user", 
	    "expire_in": 93312000, 
	    "refresh_token": "fb17cfd5ab4b61ee23de1a4c28969fec"
	}

---

## 获得用户基本信息凭证 ##

从数据上看，用户基本信息凭证所包含的数据主要在软件的“更多”页面中显示。

![更多](imgs/IMG_1696.PNG) ![个人信息](imgs/IMG_1697.PNG)

**Request：**

	GET	
	http://api.codoon.com/verify_credentials

**Params：**
	
	无

**Return :**

完整JSON示例如下：
	
	{
	    "get_icon_tiny": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4!24m24", 
	    "mobilenumber": "I1370574493782", 
	    "domain": "~iyp2ix", 
	    "certificatename": "", 
	    "weight": 58.2, 
	    "week_goal_value": 70000, 
	    "get_icon_large": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4!220m220", 
	    "height": 160, 
	    "_auto_id": 1053580, 
	    "portrait": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4", 
	    "id": "bcf5ea34-891f-xxxx-a26f-496604a5xxxx", 
	    "is_newuser": true, 
	    "mobile_portraits": [], 
	    "nick": "iascchen", 
	    "descroption": "\u6ce1\u6ce1", 
	    "followers": 0, 
	    "location": "\u5317\u4eac ", 
	    "last_login": 0, 
	    "get_icon_middle": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4!50m50", 
	    "email": "iasc@163.com", 
	    "certificateinfo": "", 
	    "installed_apps": "CDN_SPORTS CDN_LEPHONERUN", 
	    "realname": " ", 
	    "emailverified": true, 
	    "stridelength": 66, 
	    "verify_code": "6281585409bf448eb8cae5b54da57253", 
	    "birthday": {
	        "y": 2013, 
	        "m": 6, 
	        "d": 9
	    }, 
	    "routes_count": 3, 
	    "hobby": "\u8dd1\u6b65", 
	    "get_icon_xlarge": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4!640m640", 
	    "fighting_level": 1, 
	    "mobile_portraits_l": [], 
	    "get_icon_small": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4!40m40", 
	    "gender": "0", 
	    "followings": 1, 
	    "week_goal_type": "steps", 
	    "certificateid": "", 
	    "mobile_portraits_x": [], 
	    "runstridelength": 80, 
	    "mobileverified": false, 
	    "group_ids": "", 
	    "tmp_portrait": "http://img3.codoon.com/portraitce67a9da19db4d6ebf85f8eeb24d44f4", 
	    "age": 0, 
	    "address": ""
	}

---

# 2. 用户运动成就 #

## 用户成就积分 ##

用户成就激励系统上的积分和卡币展示。

![成就](imgs/IMG_1690.PNG)

**Request：**

	GET
	http://api.codoon.com/api/get_user_growing_point_related

**Params：**
	
    无

**Return :** 

	{
	    "status": "OK", 
	    "data": {
	        "fighting_level": 1, 
	        "user_growing_point": 3, 
	        "user_calbank_balance": 300
	    }, 
	    "description": ""
	}

---

## 用户运动纪录 ##

用户个人纪录显示。

![纪录](imgs/IMG_1692.PNG)

**Request：**

	GET
	http://api.codoon.com/api/gps_highest_record

**Params：**
	
    无

**Return :** 
	
	{
	    "status": "OK", 
	    "data": {
	        "ride_record": {
	            "route_count": 0
	        }, 
	        "run_record": {
	            "route_count": 0
	        }, 
	        "ski_record": {
	            "route_count": 0
	        }, 
	        "skate_record": {
	            "route_count": 0
	        }, 
	        "walk_record": {
	            "highest_speed_time": "2013-06-14T16:02:31", 
	            "highest_time": 740.0, 
	            "highest_speed": 10.15969, 
	            "highest_length_time": "2013-06-24T18:39:10", 
	            "highest_time_time": "2013-06-24T18:39:10", 
	            "route_count": 3, 
	            "highest_kmspeed": 643, 
	            "highest_kmspeed_time": "2013-06-24T18:39:10", 
	            "highest_length": 1160
	        }
	    }, 
	    "description": ""
	}

---

## 用户奖章 ##

用户奖章展示。

![勋章](imgs/IMG_1691.PNG)

**Request：**

	GET
	http://api.codoon.com/api/get_user_medal

**Params：**
	
    无

**Return :** 

返回结果会将所有用户可能获得的勋章均列出来。如果用户已经拥有这个勋章，"data"."medals"."owned" 取值为 true.

	{
	    "status": "OK", 
	    "data": [
	        {
	            "total_count": 7, 
	            "owend_count": 0, 
	            "display_group": 0, 
	            "medals": [
	                {
	                    "code": "01", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a87\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+2", 
	                    "name": "\u5e78\u8fd07", 
	                    "owned": false, 
	                    "gpoint": 2
	                }, 
	                {
	                    "code": "02", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a815\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+3", 
	                    "name": "\u575a\u6301\u8fd0\u52a8", 
	                    "owned": false, 
	                    "gpoint": 3
	                }, 
	                {
	                    "code": "03", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a821\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+5", 
	                    "name": "\u4e60\u60ef\u8fd0\u52a8", 
	                    "owned": false, 
	                    "gpoint": 5
	                }, 
	                {
	                    "code": "04", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a830\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "\u7231\u4e0a\u8fd0\u52a8", 
	                    "owned": false, 
	                    "gpoint": 10
	                }, 
	                {
	                    "code": "05", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a860\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "60\u6b21\u8fd0\u52a8", 
	                    "owned": false, 
	                    "gpoint": 10
	                }, 
	                {
	                    "code": "06", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a890\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "90\u6b21\u8fd0\u52a8", 
	                    "owned": false, 
	                    "gpoint": 10
	                }, 
	                {
	                    "code": "07", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8fd0\u52a8120\u6b21\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "120\u6b21\u8fd0\u52a8", 
	                    "owned": false, 
	                    "gpoint": 10
	                }
	            ], 
	            "display_group_name": "\u6b21\u6570\u5956\u7ae0"
	        }, 
	        {
	            "total_count": 10, 
	            "owend_count": 1, 
	            "display_group": 1, 
	            "medals": [
	                {
	                    "code": "10", 
	                    "name": "\u8fc8\u51fa\u7b2c\u4e00\u6b65", 
	                    "des": "\u4f60\u8fc8\u51fa\u8fd0\u52a8\u7684\u7b2c\u4e00\u6b65\uff0c\u5b8c\u6210\u4efb\u610f\u8fd0\u52a81\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+1", 
	                    "gpoint": 1, 
	                    "owned": true, 
	                    "time": "2013-06-24 18:51:43"
	                }, 
	                {
	                    "code": "11", 
	                    "des": "\u4f60\u4e00\u6b21\u8dd1\u6b65/\u8d70\u8def\u8fd0\u52a8\u8fbe\u52305\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+2", 
	                    "name": "\u6162\u8dd15\u516c\u91cc", 
	                    "owned": false, 
	                    "gpoint": 2
	                }, 
	                {
	                    "code": "12", 
	                    "des": "\u4f60\u4e00\u6b21\u8dd1\u6b65/\u8d70\u8def\u8fd0\u52a8\u8fbe\u523010\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+5", 
	                    "name": "\u6162\u8dd110\u516c\u91cc", 
	                    "owned": false, 
	                    "gpoint": 5
	                }, 
	                {
	                    "code": "17", 
	                    "des": "\u4f60\u4e00\u6b21\u9a91\u884c\u8fd0\u52a8\u8fbe\u523010\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+2", 
	                    "name": "10\u516c\u91cc\u9a91\u884c", 
	                    "owned": false, 
	                    "gpoint": 2
	                }, 
	                {
	                    "code": "18", 
	                    "des": "\u4f60\u4e00\u6b21\u9a91\u884c\u8fd0\u52a8\u8fbe\u523030\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+5", 
	                    "name": "30\u516c\u91cc\u9a91\u884c", 
	                    "owned": false, 
	                    "gpoint": 5
	                }, 
	                {
	                    "code": "15", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8dd1\u6b65/\u8d70\u8def\u8fd0\u52a8\u8fbe\u5230100\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "\u6311\u6218100\u516c\u91cc", 
	                    "owned": false, 
	                    "gpoint": 10
	                }, 
	                {
	                    "code": "1a", 
	                    "des": "\u4f60\u7d2f\u8ba1\u9a91\u884c\u8fd0\u52a8\u8fbe\u5230100\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "100\u516c\u91cc\u9a91\u884c", 
	                    "owned": false, 
	                    "gpoint": 10
	                }, 
	                {
	                    "code": "16", 
	                    "des": "\u4f60\u7d2f\u8ba1\u8dd1\u6b65/\u8d70\u8def\u8fd0\u52a8\u8fbe\u5230500\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+10", 
	                    "name": "\u6311\u6218500\u516c\u91cc", 
	                    "owned": false, 
	                    "gpoint": 10
	                }, 
	                {
	                    "code": "1b", 
	                    "des": "\u4f60\u7d2f\u8ba1\u9a91\u884c\u8fd0\u52a8\u8fbe\u5230500\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+30", 
	                    "name": "\u5343\u91cc\u8d70\u5355\u9a91", 
	                    "owned": false, 
	                    "gpoint": 30
	                }, 
	                {
	                    "code": "1c", 
	                    "des": "\u4f60\u7d2f\u8ba1\u9a91\u884c\u8fd0\u52a8\u8fbe\u52303200\u516c\u91cc\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+50", 
	                    "name": "\u73af\u6cd5\u5956\u676f", 
	                    "owned": false, 
	                    "gpoint": 50
	                }
	            ], 
	            "display_group_name": "\u8ddd\u79bb\u5956\u7ae0"
	        }, 
	        {
	            "total_count": 5, 
	            "owend_count": 1, 
	            "display_group": 2, 
	            "medals": [
	                {
	                    "code": "21", 
	                    "name": "\u5f00\u59cb\u8d70\u8def", 
	                    "des": "\u4f60\u5b8c\u6210\u7b2c\u4e00\u6b21\u8d70\u8def\u8fd0\u52a8\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+1", 
	                    "gpoint": 1, 
	                    "owned": true, 
	                    "time": "2013-06-14 16:02:45"
	                }, 
	                {
	                    "code": "20", 
	                    "des": "\u4f60\u5b8c\u6210\u7b2c\u4e00\u6b21\u8dd1\u6b65\u8fd0\u52a8\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+1", 
	                    "name": "\u5f00\u59cb\u8dd1\u6b65", 
	                    "owned": false, 
	                    "gpoint": 1
	                }, 
	                {
	                    "code": "22", 
	                    "des": "\u4f60\u5b8c\u6210\u7b2c\u4e00\u6b21\u9a91\u884c\u8fd0\u52a8\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+1", 
	                    "name": "\u5f00\u59cb\u9a91\u884c", 
	                    "owned": false, 
	                    "gpoint": 1
	                }, 
	                {
	                    "code": "23", 
	                    "des": "\u4f60\u5b8c\u6210\u7b2c\u4e00\u6b21\u6ed1\u96ea\u8fd0\u52a8\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+1", 
	                    "name": "\u5f00\u59cb\u6ed1\u96ea", 
	                    "owned": false, 
	                    "gpoint": 1
	                }, 
	                {
	                    "code": "24", 
	                    "des": "\u4f60\u5b8c\u6210\u7b2c\u4e00\u6b21\u6ed1\u51b0\u8fd0\u52a8\uff0c\u83b7\u5f97\u8be5\u679a\u5956\u7ae0 \u6210\u5c31\u70b9+1", 
	                    "name": "\u5f00\u59cb\u6ed1\u51b0", 
	                    "owned": false, 
	                    "gpoint": 1
	                }
	            ], 
	            "display_group_name": "\u7c7b\u578b\u5956\u7ae0"
	        }
	    ], 
	    "description": ""
	}

---

## 用户统计 ##

用户历史数据统计。

![统计](imgs/IMG_1699.PNG)

**Request：**

	POST
	http://api.codoon.com/api/gps_statistic

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    # 日期格式如：2013-06-01
	"from_date" : fromDate , 
	"to_date" : toDate

**Return :** 

以下数据返回 2013-06-01 和 2013-06-30 之间的GPS统计数据。

	{
	    "status": "OK", 
	    "data": {
	        "detail": [
	            {
	                "date": "2013-06-01", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-02", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-03", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-04", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-05", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-06", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-07", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-08", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-09", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-10", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-11", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-12", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-13", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-14", 
	                "length": 28
	            }, 
	            {
	                "date": "2013-06-15", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-16", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-17", 
	                "length": 370
	            }, 
	            {
	                "date": "2013-06-18", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-19", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-20", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-21", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-22", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-23", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-24", 
	                "length": 1160
	            }, 
	            {
	                "date": "2013-06-25", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-26", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-27", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-28", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-29", 
	                "length": 0
	            }, 
	            {
	                "date": "2013-06-30", 
	                "length": 0
	            }
	        ], 
	        "summary": {
	            "total_time": 1082.0, 
	            "total_length": 1558.22135, 
	            "speed": 5.18447, 
	            "total_calories": 82.45851
	        }
	    }, 
	    "description": ""
	}

---

# 3.用户运动历史 #

## 运动历史记录 ##

![健身历史](imgs/IMG_1693.PNG)

**Request：**

	POST
	http://api.codoon.com/api/get_route_log

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。

    # product_id 为本机 IMEI 号，写个假的也可以	
	"product_id" : productId , 

	# 应该是最大返回结果
    "count" : count , 

	# 缺省值为""， 格式不明
    "excluded" : excluded ,

	# 页码
	"page" : page ,

	# 是否为概述信息， 1 概述信息, 0 详情
    "is_part" : isPart

**Return :** 

以下为设置 is_part = 1 的返回结果

	{
	    "status": "OK", 
	    "data": [
	        {
	            "sports_type": 0, 
	            "offset_text": "-0.001356,-0.006105", 
	            "MaxToPreviousSpeed": 10.15968, 
	            "history_version": 5, 
	            "is_open": 1, 
	            "goal_value": 0, 
	            "stage_des": "", 
	            "MaxAltitude": 152.88058, 
	            "sportsMode": 0, 
	            "total_calories": 2.38503, 
	            "version": "3.3.5", 
	            "location": "", 
	            "total_length": 28.22135, 
	            "activity_result": 0, 
	            "total_time": 10, 
	            "highest_speed_perkm": 0, 
	            "start_time": "2013-06-14T16:02:31", 
	            "custom_words": "", 
	            "program_name": "", 
	            "is_baidu": 0, 
	            "last_of_program": 0, 
	            "usettime_per_km": [], 
	            "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	            "locationcount": 4, 
	            "goal_type": 2, 
	            "route_id": "cbccd39e-d4c8-11e2-9f4b-00163e0012d9", 
	            "end_time": "2013-06-14T16:02:43", 
	            "AverageSpeed": 10.15968, 
	            "activity_type": 0
	        }, 
	        {
	            "sports_type": 0, 
	            "offset_text": "-0.001612,-0.006148", 
	            "MaxToPreviousSpeed": 5.10312, 
	            "history_version": 5, 
	            "is_open": 1, 
	            "goal_value": 0, 
	            "stage_des": "", 
	            "MaxAltitude": 83.49992, 
	            "sportsMode": 0, 
	            "total_calories": 17.67462, 
	            "version": "3.3.5", 
	            "location": "", 
	            "total_length": 370, 
	            "activity_result": 0, 
	            "total_time": 332, 
	            "highest_speed_perkm": 0, 
	            "start_time": "2013-06-17T12:42:02", 
	            "custom_words": "", 
	            "program_name": "", 
	            "is_baidu": 0, 
	            "last_of_program": 0, 
	            "usettime_per_km": [], 
	            "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	            "locationcount": 34, 
	            "goal_type": 2, 
	            "route_id": "0c371e48-d709-11e2-a8a2-00163e020001", 
	            "end_time": "2013-06-17T12:47:38", 
	            "AverageSpeed": 4.0481, 
	            "activity_type": 0
	        }, 
	        {
	            "sports_type": 0, 
	            "offset_text": "-0.001415,-0.005905", 
	            "MaxToPreviousSpeed": 6.15464, 
	            "history_version": 5, 
	            "is_open": 1, 
	            "goal_value": 0, 
	            "stage_des": "", 
	            "MaxAltitude": 76.74859, 
	            "sportsMode": 0, 
	            "total_calories": 62.39886, 
	            "version": "3.3.5", 
	            "location": "", 
	            "total_length": 1160, 
	            "activity_result": 0, 
	            "total_time": 740, 
	            "highest_speed_perkm": 643, 
	            "start_time": "2013-06-24T18:39:10", 
	            "custom_words": "", 
	            "program_name": "", 
	            "is_baidu": 0, 
	            "last_of_program": 0, 
	            "usettime_per_km": [
	                {
	                    "totalUseTime": 643000, 
	                    "distance": 1, 
	                    "speed": 5.63429, 
	                    "useTime": 643000
	                }
	            ], 
	            "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	            "locationcount": 100, 
	            "goal_type": 2, 
	            "route_id": "0e891f6c-dcbc-11e2-846f-00163e020001", 
	            "end_time": "2013-06-24T18:51:34", 
	            "AverageSpeed": 5.64779, 
	            "activity_type": 0
	        }
	    ], 
	    "description": ""
	}

以下为设置 is_part = 0 的返回结果，对比上面的数据，你会发现多了"data"."points"

	{
	    "status": "OK", 
	    "data": [
	        {
	            "sports_type": 0, 
	            "offset_text": "-0.001356,-0.006105", 
	            "MaxToPreviousSpeed": 10.15968, 
	            "history_version": 5, 
	            "is_open": 1, 
	            "goal_value": 0, 
	            "stage_des": "", 
	            "MaxAltitude": 152.88058, 
	            "sportsMode": 0, 
	            "total_calories": 2.38503, 
	            "version": "3.3.5", 
	            "location": "", 
	            "total_length": 28.22135, 
	            "activity_result": 0, 
	            "total_time": 10, 
	            "highest_speed_perkm": 0, 
	            "start_time": "2013-06-14T16:02:31", 
	            "custom_words": "", 
	            "calories_per_m": [], 
	            "program_name": "", 
	            "is_baidu": 0, 
	            "last_of_program": 0, 
	            "usettime_per_km": [], 
	            "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	            "locationcount": 4, 
	            "goal_type": 2, 
	            "route_id": "cbccd39e-d4c8-11e2-9f4b-00163e0012d9", 
	            "points": [
	                {
	                    "topreviousenergy": 0, 
	                    "distance": 0, 
	                    "tostartdistance": 0, 
	                    "elevation": 0, 
	                    "topreviouscostTime": 0, 
	                    "tostartcostTime": 0, 
	                    "topreviousspeed": 0, 
	                    "longitude": 116.36103, 
	                    "latitude": 39.7732, 
	                    "time_stamp": "2013-06-14T16:02:31", 
	                    "type": 0
	                }, 
	                {
	                    "topreviousenergy": 1.88562, 
	                    "distance": 18.21924, 
	                    "tostartdistance": 18.21924, 
	                    "elevation": 152.88058, 
	                    "topreviouscostTime": 2000, 
	                    "tostartcostTime": 0, 
	                    "topreviousspeed": -1, 
	                    "longitude": 116.36117, 
	                    "latitude": 39.77307, 
	                    "time_stamp": "2013-06-14T16:02:32", 
	                    "type": 0
	                }, 
	                {
	                    "topreviousenergy": 0, 
	                    "distance": 0, 
	                    "tostartdistance": 8.42734, 
	                    "elevation": 150.37465, 
	                    "topreviouscostTime": 0, 
	                    "tostartcostTime": 1000, 
	                    "topreviousspeed": 0, 
	                    "longitude": 116.36108, 
	                    "latitude": 39.77313, 
	                    "time_stamp": "2013-06-14T16:02:33", 
	                    "type": 0
	                }
	            ], 
	            "end_time": "2013-06-14T16:02:43", 
	            "AverageSpeed": 10.15968, 
	            "activity_type": 0
	        }, 
	        {
	            "sports_type": 0, 
	            "offset_text": "-0.001612,-0.006148", 
	            "MaxToPreviousSpeed": 5.10312, 
	            "history_version": 5, 
	            "is_open": 1, 
	            "goal_value": 0, 
	            "stage_des": "", 
	            "MaxAltitude": 83.49992, 
	            "sportsMode": 0, 
	            "total_calories": 17.67462, 
	            "version": "3.3.5", 
	            "location": "", 
	            "total_length": 370, 
	            "activity_result": 0, 
	            "total_time": 332, 
	            "highest_speed_perkm": 0, 
	            "start_time": "2013-06-17T12:42:02", 
	            "custom_words": "", 
	            "calories_per_m": [
	                3.26844, 
	                2.71223, 
	                3.97497, 
	                3.7459, 
	                3.53769
	            ], 
	            "program_name": "", 
	            "is_baidu": 0, 
	            "last_of_program": 0, 
	            "usettime_per_km": [], 
	            "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	            "locationcount": 34, 
	            "goal_type": 2, 
	            "route_id": "0c371e48-d709-11e2-a8a2-00163e020001", 
	            "points": [
	                {
	                    "topreviousenergy": 0.49607, 
	                    "distance": 11.44946, 
	                    "tostartdistance": 52.73877, 
	                    "elevation": 71.36803, 
	                    "topreviouscostTime": 11000, 
	                    "tostartcostTime": 56000, 
	                    "topreviousspeed": 1.00906, 
	                    "longitude": 116.36321, 
	                    "latitude": 39.77255, 
	                    "time_stamp": "2013-06-17T12:42:59", 
	                    "type": 0
	                }, 
	                {
	                    "topreviousenergy": 0.61301, 
	                    "distance": 11.64821, 
	                    "tostartdistance": 63.90634, 
	                    "elevation": 65.04083, 
	                    "topreviouscostTime": 7000, 
	                    "tostartcostTime": 64000, 
	                    "topreviousspeed": 1.02715, 
	                    "longitude": 116.36307, 
	                    "latitude": 39.77256, 
	                    "time_stamp": "2013-06-17T12:43:07", 
	                    "type": 0
	                }, 
	                {
	                    "topreviousenergy": 0.29957, 
	                    "distance": 10.89229, 
	                    "tostartdistance": 74.34602, 
	                    "elevation": 62.91219, 
	                    "topreviouscostTime": 9000, 
	                    "tostartcostTime": 73000, 
	                    "topreviousspeed": 1.04158, 
	                    "longitude": 116.36295, 
	                    "latitude": 39.77258, 
	                    "time_stamp": "2013-06-17T12:43:16", 
	                    "type": 0
	                } 
	            ], 
	            "end_time": "2013-06-17T12:47:38", 
	            "AverageSpeed": 4.0481, 
	            "activity_type": 0
	        }, 
	        {
	            "sports_type": 0, 
	            "offset_text": "-0.001415,-0.005905", 
	            "MaxToPreviousSpeed": 6.15464, 
	            "history_version": 5, 
	            "is_open": 1, 
	            "goal_value": 0, 
	            "stage_des": "", 
	            "MaxAltitude": 76.74859, 
	            "sportsMode": 0, 
	            "total_calories": 62.39886, 
	            "version": "3.3.5", 
	            "location": "", 
	            "total_length": 1160, 
	            "activity_result": 0, 
	            "total_time": 740, 
	            "highest_speed_perkm": 643, 
	            "start_time": "2013-06-24T18:39:10", 
	            "custom_words": "", 
	            "calories_per_m": [
	                4.70714, 
	                5.23058, 
	                4.80711, 
	                6.65419, 
	                4.56336, 
	                4.82053, 
	                4.1488, 
	                5.04789, 
	                4.78563, 
	                5.40337, 
	                4.53003, 
	                6.21815
	            ], 
	            "program_name": "", 
	            "is_baidu": 0, 
	            "last_of_program": 0, 
	            "usettime_per_km": [
	                {
	                    "totalUseTime": 643000, 
	                    "distance": 1, 
	                    "speed": 5.63429, 
	                    "useTime": 643000
	                }
	            ], 
	            "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	            "locationcount": 100, 
	            "goal_type": 2, 
	            "route_id": "0e891f6c-dcbc-11e2-846f-00163e020001", 
	            "points": [
	                {
	                    "topreviousenergy": 0, 
	                    "distance": 0, 
	                    "tostartdistance": 0, 
	                    "elevation": 0, 
	                    "topreviouscostTime": 0, 
	                    "tostartcostTime": 0, 
	                    "topreviousspeed": 0, 
	                    "longitude": 116.31056, 
	                    "latitude": 39.90225, 
	                    "time_stamp": "2013-06-24T18:39:10", 
	                    "type": 0
	                }, 
	                {
	                    "topreviousenergy": 0.57431, 
	                    "distance": 10.24455, 
	                    "tostartdistance": 10.24455, 
	                    "elevation": 51.45178, 
	                    "topreviouscostTime": 7000, 
	                    "tostartcostTime": 6000, 
	                    "topreviousspeed": 0, 
	                    "longitude": 116.31064, 
	                    "latitude": 39.90217, 
	                    "time_stamp": "2013-06-24T18:39:17", 
	                    "type": 0
	                }, 
	                {
	                    "topreviousenergy": 0, 
	                    "distance": 0, 
	                    "tostartdistance": 792.45592, 
	                    "elevation": 49.47266, 
	                    "topreviouscostTime": 0, 
	                    "tostartcostTime": 730000, 
	                    "topreviousspeed": 0, 
	                    "longitude": 116.30484, 
	                    "latitude": 39.89663, 
	                    "time_stamp": "2013-06-24T18:51:23", 
	                    "type": 0
	                }
	            ], 
	            "end_time": "2013-06-24T18:51:34", 
	            "AverageSpeed": 5.64779, 
	            "activity_type": 0
	        }
	    ], 
	    "description": ""
	}
---

## 单次运动轨迹 ##

![健身历史](imgs/IMG_1694.PNG)

**Request：**

	POST
	http://api.codoon.com/api/get_single_log

**Params：**

此处参数来自于 **运动历史记录 API** 返回结果中的 `"data"."route_id"`。

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。

	"route_id" : routeId

**Return :** 

考虑到数据量的问题，此数据中 "data"."points" 节点数据有所删减。

	{
	    "status": "OK", 
	    "data": {
	        "sports_type": 0, 
	        "offset_text": "-0.001612,-0.006148", 
	        "MaxToPreviousSpeed": 5.10312, 
	        "history_version": 5, 
	        "is_open": 1, 
	        "goal_value": 0, 
	        "stage_des": "", 
	        "MaxAltitude": 83.49992, 
	        "sportsMode": 0, 
	        "total_calories": 17.67462, 
	        "version": "3.3.5", 
	        "location": "", 
	        "total_length": 370, 
	        "activity_result": 0, 
	        "total_time": 332, 
	        "highest_speed_perkm": 0, 
	        "start_time": "2013-06-17T12:42:02", 
	        "custom_words": "", 
	        "calories_per_m": [
	            3.26844, 
	            2.71223, 
	            3.97497, 
	            3.7459, 
	            3.53769
	        ], 
	        "program_name": "", 
	        "is_baidu": 0, 
	        "last_of_program": 0, 
	        "usettime_per_km": [], 
	        "product_id": "23-f7ab41d522cf48cc57575d86e18a3e34", 
	        "goal_type": 2, 
	        "route_id": "0c371e48-d709-11e2-a8a2-00163e020001", 
	        "points": [
	            {
	                "topreviousenergy": 0, 
	                "distance": 0, 
	                "tostartdistance": 0, 
	                "elevation": 0, 
	                "topreviouscostTime": 0, 
	                "tostartcostTime": 0, 
	                "topreviousspeed": 0, 
	                "longitude": 116.36381, 
	                "latitude": 39.77266, 
	                "time_stamp": "2013-06-17T12:42:02", 
	                "type": 0
	            }, 
	            {
	                "topreviousenergy": 0.69659, 
	                "distance": 14.08985, 
	                "tostartdistance": 14.08985, 
	                "elevation": 83.49992, 
	                "topreviouscostTime": 12000, 
	                "tostartcostTime": 11000, 
	                "topreviousspeed": 0, 
	                "longitude": 116.36366, 
	                "latitude": 39.7727, 
	                "time_stamp": "2013-06-17T12:42:14", 
	                "type": 0
	            }
	        ], 
	        "end_time": "2013-06-24T18:51:34", 
	        "AverageSpeed": 5.64779, 
	        "activity_type": 0
	    }, 
	    "description": ""
	}

---

# 4. 智能配件相关 API（疑似） #

以下API疑似和智能配件有关，因为手里暂时没有，所以没法确信。

如果哪位有了解，或者有带智能设备账号愿意分享一下，请直接和我联系，以将下面的API补充完整。谢谢。

## mobile_portraits ##

**Request：**

	GET
	http://api.codoon.com/api/get_mobile_portraits

**Params：**
	
    无

**Return :** 

	{
	    "status": "OK", 
	    "data": {
	        "portraits_l": [], 
	        "portraits_x": []
	    }, 
	    "description": ""
	}

---

## tracker_goal ##

**Request：**

	GET
	http://api.codoon.com/api/get_tracker_goal

**Params：**
	
    无

**Return :** 

Step的值 70000 是一周步行目标。

	{
	    "status": "OK", 
	    "data": {
	        "status": "OK", 
	        "data": {
	            "type": "steps", 
	            "value": 70000
	        }, 
	        "description": ""
	    }, 
	    "description": ""
	}

---

## tracker_summary ##

**Request：**

	POST
	http://api.codoon.com/api/get_tracker_summary

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    # 截止日期，日期格式如：2013-06-30
    "date_end" : endDate, 

	# 整数，向前回溯多少天。
	"days_back" : daysBack

**Return :** 

以下返回结果为 date_end = 2013-06-30 ， days_back = 3

	{
	    "status": "OK", 
	    "data": [
	        {
	            "status": "null", 
	            "calories": 0, 
	            "meters": 0, 
	            "activity": 0.0, 
	            "date": "2013-06-28", 
	            "steps": 0, 
	            "minutes": 0
	        }, 
	        {
	            "status": "null", 
	            "calories": 0, 
	            "meters": 0, 
	            "activity": 0.0, 
	            "date": "2013-06-29", 
	            "steps": 0, 
	            "minutes": 0
	        }, 
	        {
	            "status": "null", 
	            "calories": 0, 
	            "meters": 0, 
	            "activity": 0.0, 
	            "date": "2013-06-30", 
	            "steps": 0, 
	            "minutes": 0
	        }
	    ], 
	    "description": ""
	}

---

## tracker_data ##

**Request：**

	POST
	http://api.codoon.com/api/get_tracker_data

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    # 日期格式如：2013-06-01
    "the_day" : datestr

**Return :** 

	{
	    "status": "OK", 
	    "data": {
	        "data": {
	            "meters": [
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0
	            ], 
	            "sports_duration": 0, 
	            "steps": [
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0
	            ], 
	            "calories": [
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0, 
	                0
	            ], 
	            "sports_complete": 0
	        }
	    }, 
	    "description": ""
	}

---

## sleep_data ##

想都不用想，必然是给咕咚手环准备的，睡眠 API

**Request：**

	POST
	http://api.codoon.com/api/get_sleep_data

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    # 日期格式如：2013-06-01
    "the_day" : datestr

**Return :** 

	{
	    "status": "OK", 
	    "data": {
	        "data": {
	            "total_minutes": 0, 
	            "light_minutes": 0, 
	            "deep_minutes": 0, 
	            "detail": [
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1, 
	                -1
	            ], 
	            "sleep_complete": 0.0
	        }
	    }, 
	    "description": ""
	}

---

# 5. 其他 API #

## 约跑 ##

查看周边的跑友，需要输入用户当前的经纬度信息。

![](imgs/IMG_1702.PNG)

**Request：**

	POST
	http://api.codoon.com/api/people_surrounding

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
	# 地理位置，形式为两个浮点数组成的字符串。如："36.5,112.32"
    "point" : point , 

	# 性别 : 1 Male, 0 Female. Gender is not 0 or 1, will return all
	"gender" : gender , 

    # 缺省设置为 ""
	# Bug : if hobby is Chinese , will return 500 error, :(
	"hobby" : hobby ,

	# 整数，页码 
	"page" : page 

**Return :** 

下面的数据做了部分删减。

	{
	    "status": "OK", 
	    "data": [
	        {
	            "feed": "\u6211\u7528#\u5495\u549a\u8fd0\u52a8+#\u5b8c\u6210\u8d70\u8def3.00\u516c\u91cc\uff0c\u7528\u65f631\u5206\u949f\uff0c\u901f\u5ea65.71\u516c\u91cc/\u5c0f\u65f6\uff0c200.10\u5927\u5361\u3002", 
	            "distance": 2273.60153, 
	            "portrait_l": "http://static.codoon.com/image/default_header/female_l.png", 
	            "user_id": "58aa2aad-b470-4437-8984-fe02691c7b3d", 
	            "feed_time": "2013-07-06T22:22:05", 
	            "point": [
	                36.50452, 
	                112.34037
	            ], 
	            "gender": "1", 
	            "user_icon": "http://static.codoon.com/image/default_header/female_m.png", 
	            "mobile_portraits_x": [], 
	            "nick": "493068814", 
	            "descroption": "", 
	            "location": "\u5317\u4eac", 
	            "portrait_x": "http://static.codoon.com/image/default_header/female_x.png", 
	            "time": "2013-07-06T22:23:40.524956", 
	            "mobile_portraits_l": [], 
	            "hobby": "\u5176\u4ed6", 
	            "feed_pic": "http://img3.codoon.com/gps85677695463441cb9a4c709a838b11a1!240m0"
	        }, 	        
	        {
	            "feed": "\u6211\u5728\u300c\u664b\u57ce\u300d\u7528#\u5495\u549a\u8fd0\u52a8+#\u5b8c\u6210\u8d70\u8def2.55\u516c\u91cc\uff0c\u7528\u65f641\u5206\u949f\uff0c\u901f\u5ea63.72\u516c\u91cc/\u5c0f\u65f6\uff0c191.60\u5927\u5361\u3002", 
	            "distance": 36825.33643, 
	            "portrait_l": "http://img3.codoon.com/portraitde99214b5a6145bbb253c7e233a65d03!220m220", 
	            "user_id": "8f381494-52aa-4015-bb31-f644d9486553", 
	            "feed_time": "2013-07-15T10:59:56", 
	            "point": [
	                35.69323, 
	                112.19228
	            ], 
	            "gender": "0", 
	            "user_icon": "http://img3.codoon.com/portraitde99214b5a6145bbb253c7e233a65d03!50m50", 
	            "mobile_portraits_x": [], 
	            "nick": "\u55e8696", 
	            "descroption": "", 
	            "location": "\u5317\u4eac", 
	            "portrait_x": "http://img3.codoon.com/portraitde99214b5a6145bbb253c7e233a65d03!640m640", 
	            "time": "2013-07-15T10:59:56.101487", 
	            "mobile_portraits_l": [], 
	            "hobby": "\u8dd1\u6b65", 
	            "feed_pic": "http://img3.codoon.com/gpsf2996fd5d5d840d087f97e8857ddc5e7!240m0"
	        }
	    ], 
	    "description": ""
	}

---

## 运动计划描述 ##

运动计划列表

![](imgs/IMG_1701.PNG)

**Request：**

	POST
	http://api.codoon.com/api/sports_program_manifest_for_codoon

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    # 被**排除在外**的 Program ID 列表，多个ID之间可以用逗号分隔，如“3,4”。
	# 这个参数命名比较诡异:P
    "ids" : programIds

**Return :** 

	{
	    "status": "OK", 
	    "data": [
	        {
	            "publish_time": "2012-05-25T15:21:28", 
	            "des": "\u8fc8\u51fa\u5065\u5eb7\u751f\u6d3b\u7684\u7b2c\u4e00\u6b65\uff0c\u4ece\u8d70\u8def\u8fd0\u52a8\u5f00\u59cb\uff01\n\u8be5\u8ba1\u5212\u6301\u7eed\u56db\u5468\uff0c\u6bcf\u5468\u8fd0\u52a83\u6b21", 
	            "id": 3, 
	            "name": "\u8d70\u8def\u8fd0\u52a8\u521d\u7ea7\u8ba1\u5212"
	        }, 
	        {
	            "publish_time": "2012-05-25T15:21:56", 
	            "des": "\u6b64\u8ba1\u5212\u5171\u56db\u5468\uff0c\u6bcf\u54684\u6b21\u8fd0\u52a8", 
	            "id": 4, 
	            "name": "\u5f00\u59cb\u6162\u8dd1\u8fd0\u52a8\u5427\uff01"
	        }, 
	        {
	            "publish_time": "2012-05-25T15:21:56", 
	            "des": "\u6b64\u8ba1\u5212\u5171\u516d\u5468\uff0c\u6bcf\u54684\u6b21\u8fd0\u52a8", 
	            "id": 5, 
	            "name": "\u6162\u8dd1\u8fd0\u52a8\u8fdb\u9636\u8ba1\u5212"
	        }
	    ], 
	    "description": ""
	}

---

## 运动计划细节 ##

Codoon 运动计划详情

![](imgs/IMG_1703.PNG)

**Request：**

	POST
	http://api.codoon.com/api/sports_program_detail

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    "id" : programId 

**Return :** 

"data"."program_detail"."procedure"."detail" 中的 "t" 代表运动类型，"d" 代表持续几分钟：

t 的取值包括： j 快走，s 慢走，c 放松，m 慢跑，n 走路等。

	{
	    "status": "OK", 
	    "data": {
	        "version": 1, 
	        "id": 3, 
	        "program_detail": {
	            "small_unit": "day", 
	            "big_unit": "week", 
	            "procedure": [
	                [
	                    {
	                        "des": "\u5feb\u8d705\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d705\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 5
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 5
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d705\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d705\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 5
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 5
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d705\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d705\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 5
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 5
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }
	                ], 
	                [
	                    {
	                        "des": "\u5feb\u8d706\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d707\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 6
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 7
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d706\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d707\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 6
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 7
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d706\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d707\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 6
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 7
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }
	                ], 
	                [
	                    {
	                        "des": "\u5feb\u8d708\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d708\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 8
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 8
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d708\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d708\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 8
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 8
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d708\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d708\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 8
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 8
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }
	                ], 
	                [
	                    {
	                        "des": "\u5feb\u8d7010\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d7010\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 10
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 10
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d7010\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d7010\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 10
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 10
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u5feb\u8d7010\u5206\u949f\uff1b\u6162\u8d703\u5206\u949f\uff1b\u5feb\u8d7010\u5206\u949f\uff1b\u653e\u677e\u8fd0\u52a81\u5206\u949f", 
	                        "detail": [
	                            {
	                                "t": "j", 
	                                "d": 10
	                            }, 
	                            {
	                                "t": "s", 
	                                "d": 3
	                            }, 
	                            {
	                                "t": "j", 
	                                "d": 10
	                            }, 
	                            {
	                                "t": "c", 
	                                "d": 1
	                            }
	                        ]
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }, 
	                    {
	                        "des": "\u4f11\u606f", 
	                        "detail": []
	                    }
	                ]
	            ]
	        }, 
	        "hint": {
	            "detect_time": 2, 
	            "min_speed": 7, 
	            "detect_bar": 4
	        }
	    }, 
	    "description": ""
	}

## 空气质量 ##

根据输入的城市名，获得空气质量信息。

**Request：**

	POST
	http://api.codoon.com/api/city_name

**Params：**

此处参数需要转化为 JSON 之后，放在 POST 消息体中再提交。
	
    # 城市名称，如: "北京"
    "city_name" : cityName

**Return :** 
	
	{
	    "status": "OK", 
	    "data": {
	        "pm10": {
	            "city_name": "\u5317\u4eac", 
	            "update_time": "2013-07-18T11:00:00", 
	            "des": "\u4e2d\u5ea6\u6c61\u67d3", 
	            "suggestion": "\u4e0d\u592a\u9002\u5b9c\u8fd0\u52a8", 
	            "value": 162.0
	        }, 
	        "pm25": {
	            "city_name": "\u5317\u4eac", 
	            "update_time": "2013-07-18T11:00:00", 
	            "des": "\u91cd\u5ea6\u6c61\u67d3", 
	            "suggestion": "\u4e0d\u9002\u5b9c\u8fd0\u52a8", 
	            "value": 177.0
	        }
	    }, 
	    "description": ""
	}

---

## 获得最新可用 Android 软件版本信息 ##

**Request：**

	GET	
	http://static.codoon.com/app/android/version_run.xml

**Params：**
	
	无

**Return :**

完整XML示例如下：
	
	<client>
		<version>53</version>
		<date>2013-07-10 18:33:59</date>
		<description>&#21653;&#21658;&#36816;&#21160;+&#23458;&#25143;&#31471;3.3.8</description>
		<app_name>codoonsportsv3.3.8.apk</app_name>
		<app_url>http://static.codoon.com/app/android/codoonsports.apk</app_url>
	</client>

---

结束 :D