# 获取Jawbone UP中的个人数据（二）非官方API #

从Jawbone网站上，能够下载UP的个人数据，但是这个数据是以天为单位的汇总数据，如果我们需要更精细的数据，就必须通过程序获取。

Jawbone官方网站宣称已经提供开发API，用于与合作方应用之间进行数据交换。但是这个API在网上见不到。我辈苦逼的码农想玩玩自己的数据，只好另想办法。

Eric Blue曾经于2011年11月发表过一篇博文[jawbone-up-api-discovery](http://eric-blue.com/2011/11/28/jawbone-up-api-discovery/)，介绍了他通过网络侦听Jawbone UP应用与服务器之间的通讯，破解出的一些非官方API，这些API可以用于获得用户自己的运动数据。时过境迁，Jawbone UP硬件已经更新换代至UP 2，手环版本为6\-1.0.20，手机应用软件也已经升级到了2.6.8版本，Server端版本已经更新至1.34。Eric Blue公布的API部分内容已经过时。

下面的API是对Jawbone UP的Android版本进行了反编译所得到的，并借鉴了Eric Blue的方法，通过对Jawbone UP应用发出的请求进行侦听以确认，错误在所难免。这些API包括：

- 两种login方法
- UP进入后首屏信息显示所使用的：user score 和 social feeds
- 获取不同类型的用户时间：
- 详细记录：包括move, sleep, workout、mood、meal
- 统计结果数据
- 用户Profile
- 朋友列表
 
各位玩的开心！

## 客户端请求基本说明 ##

典型的 Jawbone UP 客户端请求形式如下，其中形如 **v.1.34** 的版本部分用于指明所需的Server端服务版本号，此信息可以省略：

	https://jawbone.com/nudge/api/...
	https://jawbone.com/nudge/api/v.1.34/...

在进行其他访问之前，必须先登录。正确登录之后，只需在每次请求的HTTP中，将认证时的所获得Token值设置到 HTTP Header：**x-nudge-token** 里，即可保持会话。

    x-nudge-token ： 1BkkscbY2RvUUQXF9TewzzDEEuGrKl7nJIuimAfcp8E

## 用户登录 ##

Eric Blue 提到的登录方式 "**user/signin/login**" 方法仍然可用。不过在新的UP客户端版本中，还能够通过 “**users/login**” API进行登陆。

### 利用 user/signin/login 登陆 ###

**Request：**

	POST	
	https://jawbone.com/nudge/api/user/signin/login

**Params：**
	
	'email': email, 
	'pwd':  password, 
	'service': 'nudge'

**Return :**

Token 值为 JSON 内容中最下端的 `"token" : "un_ZHV8Uiq1pyJCPnqCljjDEEuGrKl7nURWQYUScC6E"` 

用户 XID 值取 `"user"."xid” : "RGaCBFg9CsDYVvm2kchbcw"` ：

完整JSON示例如下：
	
	{
	    "newly": false, 
	    "user": {
	        "last_name": "VisHealth", 
	        "uid": 37291881, 
	        "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	        "time_removed": 0, 
	        "basic_info": {
	            "weight": 56.2, 
	            "dob": "1976-06-09", 
	            "gender": "female", 
	            "metric": 1, 
	            "height": 1.58, 
	            "locale": "zh-cn"
	        }, 
	        "share_move": true, 
	        "birth_day": "09", 
	        "text_1": "", 
	        "first_name": "Tester", 
	        "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "smart_alarm": {
	            "stopTimeMinsPastMidnight": 390, 
	            "dayMask": 62, 
	            "enable": true, 
	            "startTimeMinsPastMidnight": 370
	        }, 
	        "apps": [
	            {
	                "xid": "bVvQvURXOKc", 
	                "share": true
	            }, 
	            {
	                "xid": "__3Ao7ntG68", 
	                "share": true
	            }
	        ], 
	        "share_eat": false, 
	        "birth_month": "06", 
	        "type": 0, 
	        "email": "iasc@163.com", 
	        "birth_year": "1976", 
	        "band_name": "iasc's jawbone up", 
	        "up_goals": {
	            "move": {
	                "steps": 10000, 
	                "workout_time": null
	            }, 
	            "sleep": {
	                "total": 27000, 
	                "bedtime": null, 
	                "deep": null
	            }, 
	            "meals": {
	                "carbs": null, 
	                "fiber": null, 
	                "sodium": null, 
	                "sugar": null, 
	                "calcium": null, 
	                "unsat_fat": null, 
	                "cholesterol": null, 
	                "protein": null, 
	                "sat_fat": null
	            }
	        }, 
	        "first": "Tester", 
	        "share_mood": true, 
	        "primary_address": {
	            "city": "", 
	            "xid": "P9Q5vjiI-M0", 
	            "country": "CN", 
	            "zipcode": "", 
	            "state": "", 
	            "street_1": "", 
	            "street_2": ""
	        }, 
	        "share_sleep": false, 
	        "power_nap": {
	            "use_optimal_duration": 0, 
	            "custom_duration": 2400, 
	            "maximum_duration": 3600
	        }, 
	        "active_alert": {
	            "stopTimeMinsPastMidnight": 1020, 
	            "threshold": 0, 
	            "durationMins": 60, 
	            "type": 1, 
	            "startTimeMinsPastMidnight": 480
	        }, 
	        "last": "VisHealth", 
	        "name": "Tester VisHealth", 
	        "gender": "female", 
	        "profile_privacy": "friends", 
	        "data_2": 0, 
	        "data_1": 0, 
	        "flags": 1, 
	        "time_created": 1370439133, 
	        "mail_opts": {
	            "mail_opt_in_new_products": null, 
	            "mail_opt_in": null, 
	            "mail_opt_in_products_owned_updates": null, 
	            "mail_opt_in_customer_surveys": null, 
	            "mail_opt_in_deals_n_promotions": null
	        }, 
	        "goals": {
	            "move": 3500, 
	            "sleep": 21600, 
	            "eat": 2
	        }
	    }, 
	    "token": "un_ZHV8Uiq1pyJCPnqCljjDEEuGrKl7nURWQYUScC6E", 
	    "rc": 0
	}	

### 利用 users/login 登陆 ###

**users/login** 是目前Jawbone UP客户端采用的登录方式，由于其将用户密码进行 SHA-1 之后再传递，所以更加安全。

![登陆页面](imgs/IMG_1613.PNG)

**Request：**

	POST
	https://jawbone.com/nudge/api/users/login

**Params：**
	
    'email' : email,
	'hash_pwd' : hash #将 password 进行 SHA-1 之后，再转换成 HEX 格式

**Return :** 

Token 值为 JSON 内容中的 `"data"."session_uid" : "1BkkscbY2RvUUQXF9TewzzDEEuGrKl7nJIuimAfcp8E"` 

用户 XID 值为 `"data"."user"."xid" : "RGaCBFg9CsDYVvm2kchbcw"`：

完整JSON示例如下：

	{
	    "meta": {
	        "message": "OK", 
	        "code": 200, 
	        "time": 1371960908
	    }, 
	    "data": {
	        "session_uid": "1BkkscbY2RvUUQXF9TewzzDEEuGrKl7nJIuimAfcp8E", 
	        "config": {
	            "i18n": null, 
	            "configuration": {
	                "twitter_character_count": 24, 
	                "system_message": ""
	            }, 
	            "features": {
	                "up_food_gallery": [
	                    "off", 
	                    null
	                ], 
	                "up_twitter_share": [
	                    "on", 
	                    null
	                ], 
	                "up_fooditem_search_typeahead": [
	                    "on", 
	                    null
	                ], 
	                "up_app_gallery": [
	                    "off", 
	                    null
	                ], 
	                "up_addressbook_import": [
	                    "on", 
	                    null
	                ], 
	                "up_daily_dashboards": [
	                    "off", 
	                    null
	                ], 
	                "up_search": [
	                    "on", 
	                    null
	                ], 
	                "up_fb_share": [
	                    "on", 
	                    null
	                ], 
	                "system": [
	                    "on", 
	                    null
	                ], 
	                "up_cheers": [
	                    "off", 
	                    null
	                ], 
	                "barcode_search": [
	                    "on", 
	                    null
	                ], 
	                "up_twitter_import": [
	                    "on", 
	                    null
	                ], 
	                "up_twitter_friend_suggestions": [
	                    "on", 
	                    null
	                ], 
	                "up_fb_import": [
	                    "on", 
	                    null
	                ], 
	                "up_slideshow": [
	                    "on", 
	                    {}
	                ], 
	                "up_fb_friend_suggestions": [
	                    "on", 
	                    null
	                ]
	            }
	        }, 
	        "user": {
	            "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	            "name": "Tester VisHealth", 
	            "short_name": "Tester", 
	            "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	            "has_settings": true, 
	            "last": "VisHealth", 
	            "type": "user", 
	            "first": "Tester"
	        }
	    }
	}

## 用户概况 ##

打开 UP 的 Home 页，首先会展示用户当天的任务完成情况，以及用户的历史行为。下面我们就来讨论，这个页面使用到两个API **users/%s/score** 和 **users/%s/social** 。

请注意，Eric 提到的 **users/%s/healthCredits** API 似乎已经**不再可用**。

![Home页](imgs/jawbone_up_1.png)

在使用 users/%s/Action 类型的 API 时，需要注意的其中 %s 的取值可以有两种形式：

- @me ，用于访问自己的信息
- User XID 值 ，可以使用 login 返回的 “user.xid”访问自己的信息。或者可以利用从朋友查找中获取的 User XID值，查询他人的信息（推测，未实验）。

### users/%s/score ###

**users/%s/score** 用于查看用户的运动完成情况，显示当天用户运动、睡眠、饮食等综合信息。



**Request：**

	GET
	https://jawbone.com/nudge/api/users/@me/score	#返回结果与下条完全一致
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/score
	https://jawbone.com/nudge/api/users/@me/score?date=20130609		#返回结果与下条完全一致
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/score?date=20130609

**Params：**
	
    'date' : datestr #格式为yyyymmdd，如果没有 date 参数，返回今日数据

**Return :** 

返回信息包括 Mood、Move、Sleep、Meals 等按日统计信息，这个数据还包括了当用户点击各种行为的状态条时，打开具体行为统计页面的信息：

![Score](imgs/jawbone_up_2.png)

完整JSON示例如下：

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1371960912
	    }, 
	    "data": {
	        "mood": {
	            "time_updated": 1370731786, 
	            "xid": "EJpCkyAtwoMpB8b_a5GOLQ", 
	            "title": "\u5f88\u5174\u594b\uff0c\u7761\u5f97\u4e0d\u9519", 
	            "time_created": 1370731760, 
	            "app_generated": false, 
	            "details": {
	                "tz": "Asia/Shanghai"
	            }, 
	            "date": 20130609, 
	            "shared": true, 
	            "type": "mood", 
	            "sub_type": 2
	        }, 
	        "move": {
	            "distance": 7.965, 
	            "longest_idle": 7260, 
	            "calories": 496.492103646, 
	            "bmr_calories_day": 1198.44050706, 
	            "goals": {
	                "steps": [
	                    11611.0, 
	                    10000
	                ], 
	                "workout_time": [
	                    1800.0, 
	                    null
	                ]
	            }, 
	            "longest_active": 1800, 
	            "hidden": false, 
	            "bg_steps": 11611.0, 
	            "bmr_calories": 1112.31734078, 
	            "active_time": 7917.0
	        }, 
	        "sleep": {
	            "awakenings": 2, 
	            "light": 12406.0, 
	            "time_to_sleep": 262, 
	            "goals": {
	                "total": [
	                    28542.0, 
	                    28800
	                ], 
	                "bedtime": [
	                    1317, 
	                    null
	                ], 
	                "deep": [
	                    16136.0, 
	                    null
	                ]
	            }, 
	            "qualities": [
	                99
	            ], 
	            "awake": 2189.0, 
	            "hidden": false
	        }, 
	        "user_metrics": {
	            "dob": 19760609, 
	            "gender": 1, 
	            "pal": null, 
	            "weight": 57.0, 
	            "height": 1.58
	        }, 
	        "meals": {
	            "num_meals": 1, 
	            "calories": 232.0, 
	            "num_drinks": 0, 
	            "goals": {
	                "carbs": [
	                    4.76000010967, 
	                    null
	                ], 
	                "fiber": [
	                    0.300000011921, 
	                    null
	                ], 
	                "sodium": [
	                    663.0, 
	                    null
	                ], 
	                "sugar": [
	                    0.939999982715, 
	                    null
	                ], 
	                "calcium": [
	                    70.0, 
	                    null
	                ], 
	                "unsat_fat": [
	                    9.69599956274, 
	                    null
	                ], 
	                "cholesterol": [
	                    460.0, 
	                    null
	                ], 
	                "protein": [
	                    15.3100000619, 
	                    null
	                ], 
	                "sat_fat": [
	                    4.5640001595, 
	                    null
	                ]
	            }, 
	            "hidden": false, 
	            "num_foods": 2
	        }, 
	        "insights": {
	            "items": []
	        }
	    }
	}

### users/%s/social ###

**users/%s/social** 用于查看用户各种活动的综合情况，按照当日或设定的截止访问时间，由近至远排列。



**Request：**

	GET
	https://jawbone.com/nudge/api/users/@me/social	#返回结果与下条完全一致
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/social
	https://jawbone.com/nudge/api/users/@me/social?date=20130609		#返回结果与下条完全一致
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/social?date=20130609
	https://jawbone.com/nudge/api/users/@me/social?date=20130609&limit=20	#返回结果与下条完全一致
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/social?date=20130609&limit=20

**Params：**
	
    'date' : datestr #格式为yyyymmdd，如果没有 date 参数，返回今日数据
	'limit' : limit	 #整数，缺省为20。用于限制返回多少条结果

**Return :** 

返回信息包括 Mood、Move、Sleep、Meals、WorkOut 等活动的分项信息，这个数据相当详细，还包括了当用户点击各种行为的状态条时，打开分项详细页面的信息：

![Score](imgs/jawbone_up_3.png)

完整JSON示例如下：

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1371960914
	    }, 
	    "data": {
	        "feed": [
	            {
	                "user": {
	                    "last": "VisHealth", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_updated": 1370812786, 
	                "subtitle": null, 
	                "title": "6 \u5c0f\u65f6 40 \u5206\u949f", 
	                "quality": 78, 
	                "image": "/nudge/api/v.1.34/sleeps/EJpCkyAtwoNhHfcKmXhLDQ/image/11370812792", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-Ypd7aQb52I3A", 
	                "app_generated": false, 
	                "awake": 806, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370812786, 
	                "duration": 24852, 
	                "xid": "EJpCkyAtwoNhHfcKmXhLDQ", 
	                "type": "sleep", 
	                "networks": [], 
	                "is_private": true, 
	                "tz": "Asia/Shanghai"
	            }, 
	            {
	                "time_updated": 1370787960, 
	                "xid": "EJpCkyAtwoPJKCOzFyu89A", 
	                "title": "11,611 \u6b65", 
	                "image": "/nudge/api/v.1.34/moves/EJpCkyAtwoPJKCOzFyu89A/image/11370812791", 
	                "reached_goal": true, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-bWv8AvxdlIPg", 
	                "app_generated": false, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370730601, 
	                "date": 20130609, 
	                "tz": "Asia/Shanghai", 
	                "type": "move", 
	                "networks": [], 
	                "is_private": false, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "reaction": null, 
	                "time_updated": 1370732127, 
	                "tz": "Asia/Shanghai", 
	                "subtitle": null, 
	                "title": "Fried Egg \u548c Noodle Soup", 
	                "image": null, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "note": "Fried Egg \u548c Noodle Soup", 
	                "activity_xid": "lX5iJd5Y8-ZDW7VvQnqXGA", 
	                "app_generated": false, 
	                "details": {
	                    "carbohydrate": 4.76000010967, 
	                    "saturated_fat": 4.5640001595, 
	                    "protein": 15.3100000619, 
	                    "tz": "Asia/Shanghai", 
	                    "sodium": 663, 
	                    "vitamin_c": 0, 
	                    "vitamin_a": 0, 
	                    "unsaturated_fat": 9.69599956274, 
	                    "sugar": 0.939999982715, 
	                    "num_drinks": 0, 
	                    "accuracy": 0.0, 
	                    "fiber": 0.300000011921, 
	                    "potassium": 0, 
	                    "fat": 0, 
	                    "num_foods": 2, 
	                    "monounsaturated_fat": 0, 
	                    "calories": 232, 
	                    "place_type": "", 
	                    "polyunsaturated_fat": 0, 
	                    "calcium": 70, 
	                    "iron": 0, 
	                    "cholesterol": 460
	                }, 
	                "time_created": 1370732127, 
	                "xid": "EJpCkyAtwoMKaoaitjJHmg", 
	                "place_name": "", 
	                "type": "meal", 
	                "networks": [], 
	                "is_private": true, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "time_updated": 1370731760, 
	                "tz": "Asia/Shanghai", 
	                "title": "\u5f88\u5174\u594b\uff0c\u7761\u5f97\u4e0d\u9519", 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-ZoG48PRRZa5g", 
	                "app_generated": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370731760, 
	                "xid": "EJpCkyAtwoMpB8b_a5GOLQ", 
	                "type": "mood", 
	                "sub_type": 2, 
	                "is_private": false, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "reaction": null, 
	                "time_updated": 1370730615, 
	                "subtitle": null, 
	                "title": "\u745c\u4f3d", 
	                "type": "workout", 
	                "is_completed": 1, 
	                "networks": [], 
	                "km": 0.0, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-Yth6ROIP2QPA", 
	                "app_generated": false, 
	                "steps": 0, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_created": 1370730615, 
	                "xid": "EJpCkyAtwoPa1a-leTNHQg", 
	                "duration": 1800, 
	                "tz": "Asia/Shanghai", 
	                "image": "/ver/static/images/up/Workout_Feedv2_yoga.png", 
	                "sub_type": 6, 
	                "is_private": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }
	            }, 
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_updated": 1370730588, 
	                "subtitle": null, 
	                "title": "7 \u5c0f\u65f6 55 \u5206\u949f", 
	                "quality": 99, 
	                "image": "/nudge/api/v.1.34/sleeps/EJpCkyAtwoPx-NDQaWEnSw/image/11370730602", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-aWWUdEvsk67g", 
	                "app_generated": false, 
	                "awake": 2189, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370730588, 
	                "duration": 30731, 
	                "xid": "EJpCkyAtwoPx-NDQaWEnSw", 
	                "type": "sleep", 
	                "networks": [], 
	                "is_private": true, 
	                "tz": "Asia/Shanghai"
	            }, 
	            {
	                "time_updated": 1370699820, 
	                "xid": "EJpCkyAtwoPW1YD0X277hA", 
	                "title": "6,693 \u6b65", 
	                "image": "/nudge/api/v.1.34/moves/EJpCkyAtwoPW1YD0X277hA/image/11370730599", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-aUJI6pRVGHRQ", 
	                "app_generated": false, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370645647, 
	                "date": 20130608, 
	                "tz": "Asia/Shanghai", 
	                "type": "move", 
	                "networks": [], 
	                "is_private": false, 
	                "user": {
	                    "last": "VisHealth", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_updated": 1370644226, 
	                "subtitle": null, 
	                "title": "7 \u5c0f\u65f6 0 \u5206\u949f", 
	                "quality": 0, 
	                "image": "/ver/static/images/up/Sleep_Feed_Manual.png", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-bV0p1Rp8I6xw", 
	                "app_generated": false, 
	                "awake": 0, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370644226, 
	                "duration": 25200, 
	                "xid": "EJpCkyAtwoP5F4HBk72dng", 
	                "type": "sleep", 
	                "networks": [], 
	                "is_private": true, 
	                "tz": "Asia/Shanghai"
	            }, 
	            {
	                "time_updated": 1370620620, 
	                "xid": "BXM3Lg0tIY39TAWZF9J3LA", 
	                "title": "13,030 \u6b65", 
	                "image": "/nudge/api/v.1.34/moves/BXM3Lg0tIY39TAWZF9J3LA/image/11370645645", 
	                "reached_goal": true, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-bAiFLwbwZ9IQ", 
	                "app_generated": false, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370575326, 
	                "date": 20130607, 
	                "tz": "Asia/Shanghai", 
	                "type": "move", 
	                "networks": [], 
	                "is_private": false, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_updated": 1370619840, 
	                "subtitle": null, 
	                "title": "1 \u5c0f\u65f6 29 \u5206\u949f", 
	                "quality": 18, 
	                "image": "/nudge/api/v.1.34/sleeps/EJpCkyAtwoOF3sVPoMzjNw/image/11370645648", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-ap8twiX42Qtw", 
	                "app_generated": false, 
	                "awake": 1052, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370619840, 
	                "duration": 6394, 
	                "xid": "EJpCkyAtwoOF3sVPoMzjNw", 
	                "type": "sleep", 
	                "networks": [], 
	                "is_private": true, 
	                "tz": "Asia/Shanghai"
	            }, 
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_updated": 1370557817, 
	                "subtitle": null, 
	                "title": "5 \u5c0f\u65f6 56 \u5206\u949f", 
	                "quality": 64, 
	                "image": "/nudge/api/v.1.34/sleeps/BXM3Lg0tIY0DwwLlUXmstA/image/11370557855", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-Yb3mDOv7V1qA", 
	                "app_generated": false, 
	                "awake": 3297, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370557817, 
	                "duration": 24682, 
	                "xid": "BXM3Lg0tIY0DwwLlUXmstA", 
	                "type": "sleep", 
	                "networks": [], 
	                "is_private": true, 
	                "tz": "Asia/Shanghai"
	            }, 
	            {
	                "time_updated": 1370533080, 
	                "xid": "BXM3Lg0tIY2dRqV_zVk94A", 
	                "title": "12,339 \u6b65", 
	                "image": "/nudge/api/v.1.34/moves/BXM3Lg0tIY2dRqV_zVk94A/image/11370557868", 
	                "reached_goal": true, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-bV19tQDrHFBg", 
	                "app_generated": false, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370472153, 
	                "date": 20130606, 
	                "tz": "Asia/Shanghai", 
	                "type": "move", 
	                "networks": [], 
	                "is_private": false, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "time_updated": 1370471100, 
	                "subtitle": null, 
	                "title": "5 \u5c0f\u65f6 35 \u5206\u949f", 
	                "quality": 71, 
	                "image": "/nudge/api/v.1.34/sleeps/BXM3Lg0tIY2H-2uHcDwYSg/image/11370472155", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-b9nP8F8UDNHA", 
	                "app_generated": false, 
	                "awake": 2082, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370471100, 
	                "duration": 22233, 
	                "xid": "BXM3Lg0tIY2H-2uHcDwYSg", 
	                "type": "sleep", 
	                "networks": [], 
	                "is_private": true, 
	                "tz": "Asia/Shanghai"
	            }, 
	            {
	                "time_updated": 1370447940, 
	                "xid": "BXM3Lg0tIY14vuEzUfC9QA", 
	                "title": "367 \u6b65", 
	                "image": "/nudge/api/v.1.34/moves/BXM3Lg0tIY14vuEzUfC9QA/image/11370447939", 
	                "reached_goal": false, 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-aHK_ym9GCZIA", 
	                "app_generated": false, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370439710, 
	                "date": 20130605, 
	                "tz": "Asia/Shanghai", 
	                "type": "move", 
	                "networks": [], 
	                "is_private": false, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }, 
	            {
	                "time_updated": 1370439133, 
	                "tz": "Asia/Shanghai", 
	                "comments": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "activity_xid": "lX5iJd5Y8-aRU1FwEZIFfQ", 
	                "app_generated": false, 
	                "emotions": {
	                    "items": [], 
	                    "size": 0
	                }, 
	                "time_created": 1370439133, 
	                "type": "user_joined", 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }
	            }
	        ], 
	        "links": {
	            "next": "/nudge/api/v.1.34/users/RGaCBFg9CsDYVvm2kchbcw/social?page_token=1370439133&limit=20"
	        }
	    }
	}
