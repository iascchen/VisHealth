# 获取Jawbone UP中的个人数据（二）非官方API #

# 5. 锻炼情况细节——Workouts #

锻炼使用户标注的某段时间的运动。通过“记录锻炼情况”菜单完成。

![Meals](imgs/IMG_1630.PNG)

除了前面介绍的 user/%userXid%/social 等用户行为概述 API 之外，与锻炼相关的 API 还有以下几个：
	
	user/%userXid%/workouts
	workouts/%evtXid%
	workouts/%evtXid%/snapshot

从 user/%userXid%/social 结果中的 "data"."feed"."xid"; 从 user/%userXid%/workouts 结果中的 "data"."items"."xid" 获得 %evtXid% ， 用于调用 workouts/%evtXid% 和 workouts/%evtXid%/snapshot 。

并非所有的 workouts/%evtXid%/snapshot 都会返回详细的数据，一些锻炼方式，如：步行、跑步等，使用 snapshot 能够返回细节运动数据；而另一些锻炼方式，如：瑜伽，则没有细节运动数据。

![Meals](imgs/IMG_1620.PNG)

### user/%userXid%/workouts ###

这个 API 能够返回个人的锻炼概括数据列表。在Jawbone UP 的手机应用界面中并没有对应的界面输出。

Request：
	
	GET
	https://jawbone.com/nudge/api/users/@me/workouts?start_time=1370707200&limit=100
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/workouts?start_time=1370707200&limit=100

Params：

	'start_time' : startTime, #start_time为 long 型时间，即从1970年以来的秒数，可以不填
	'end_time' : endTime,     #end_time为 long 型时间，即从1970年以来的秒数，可以不填
	'limit' : limit           #最多返回结果条数限制

Return :

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372472625
	    }, 
	    "data": {
	        "items": [
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "type": "user"
	                }, 
	                "reaction": null, 
	                "time_completed": 1370730615, 
	                "xid": "EJpCkyAtwoPa1a-leTNHQg", 
	                "band_ids": [], 
	                "title": "\u745c\u4f3d", 
	                "snapshot_image": "", 
	                "route": "", 
	                "networks": [], 
	                "time_created": 1370728815, 
	                "sub_type": 6, 
	                "date": 20130609, 
	                "app_generated": false, 
	                "time_updated": 1370732478, 
	                "time_removed": 0, 
	                "image": "", 
	                "is_manual": true, 
	                "shared": true, 
	                "type": "workout", 
	                "is_complete": true, 
	                "details": {
	                    "tz": "Asia/Shanghai", 
	                    "goal": 0, 
	                    "calories": 89.4861169007, 
	                    "km": 0.0, 
	                    "bmr": 37.8849980137, 
	                    "intensity": 1, 
	                    "bg_calories": 0, 
	                    "meters": 0, 
	                    "time": 1800, 
	                    "bg_active_time": 0, 
	                    "steps": 0, 
	                    "bmr_calories": 27.4861169007
	                }
	            }, 
	            {
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "type": "user"
	                }, 
	                "reaction": null, 
	                "time_completed": 1371016848, 
	                "xid": "EJpCkyAtwoPXN30hjKufWg", 
	                "band_ids": [], 
	                "title": "\u6b65\u884c", 
	                "snapshot_image": "/nudge/image/e/1371044854/EJpCkyAtwoPXN30hjKufWg.png", 
	                "route": "", 
	                "networks": [], 
	                "time_created": 1371006048, 
	                "sub_type": 1, 
	                "date": 20130612, 
	                "app_generated": false, 
	                "time_updated": 1371044854, 
	                "time_removed": 0, 
	                "image": "", 
	                "is_manual": true, 
	                "shared": true, 
	                "type": "workout", 
	                "is_complete": true, 
	                "details": {
	                    "tz": "Asia/Shanghai", 
	                    "goal": 0, 
	                    "calories": 802.075100205, 
	                    "km": 2.249, 
	                    "bmr": 164.075100205, 
	                    "intensity": 1, 
	                    "bg_calories": 127.953000784, 
	                    "meters": 2249, 
	                    "time": 10800, 
	                    "bg_active_time": 1871, 
	                    "steps": 3372, 
	                    "bmr_calories": 164.075100205
	                }
	            }
	        ], 
	        "size": 2
	    }
	}

### workouts/%evtXid% ###

从 user/%userXid%/social 结果中的 **"data"."feed"."xid"**; 从 user/%userXid%/workouts 结果中的 **"data"."items"."xid"** 获得 %evtXid% ， 用于调用 workouts/%evtXid% 。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/workouts/EJpCkyAtwoPa1a-leTNHQg

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372431987
	    }, 
	    "data": {
	        "image": "", 
	        "time_removed": 0, 
	        "emotions": {
	            "items": [], 
	            "size": 0
	        }, 
	        "snapshot_image": "/nudge/image/e/1371044854/EJpCkyAtwoPXN30hjKufWg.png", 
	        "networks": [], 
	        "time_completed": 1371016848, 
	        "xid": "EJpCkyAtwoPXN30hjKufWg", 
	        "title": "\u6b65\u884c", 
	        "comments": {
	            "items": [], 
	            "size": 0
	        }, 
	        "details": {
	            "tz": "Asia/Shanghai", 
	            "goal": 0, 
	            "calories": 802.075100205, 
	            "km": 2.249, 
	            "bmr": 164.075100205, 
	            "intensity": 1, 
	            "bg_calories": 127.953000784, 
	            "meters": 2249, 
	            "time": 10800, 
	            "bg_active_time": 1871, 
	            "steps": 3372, 
	            "bmr_calories": 164.075100205
	        }, 
	        "shared": true, 
	        "type": "workout", 
	        "band_ids": [], 
	        "user": {
	            "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	            "name": "Tester VisHealth", 
	            "short_name": "Tester", 
	            "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	            "last": "VisHealth", 
	            "type": "user", 
	            "first": "Tester"
	        }, 
	        "date": 20130612, 
	        "sub_type": 1, 
	        "reaction": null, 
	        "time_updated": 1371044854, 
	        "route": "", 
	        "app_generated": false, 
	        "time_created": 1371006048, 
	        "is_manual": true, 
	        "is_complete": true, 
	        "goals": {
	            "steps": 10000, 
	            "workout_time": null
	        }
	    }
	}

### workouts/%evtXid%/snapshot ###

从 user/%userXid%/social 结果中的 **"data"."feed"."xid"**; 从 user/%userXid%/workouts 结果中的 **"data"."items"."xid"** 获得 %evtXid% ， 用于调用 workouts/%evtXid%/snapshot 。

并非所有的 workouts/%evtXid%/snapshot 都会返回详细的数据，一些锻炼方式，如：步行、跑步等，使用 snapshot 能够返回细节运动数据；而另一些锻炼方式，如：瑜伽，则没有细节运动数据。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/workouts/EJpCkyAtwoPa1a-leTNHQg/snapshot  #瑜伽，无详情
	https://jawbone.com/nudge/api/workouts/EJpCkyAtwoPXN30hjKufWg/snapshot?bucket=600  #步行，有详情

**Params：**

	'bucket' : bucket # 运动数据汇总时间颗粒度，以秒为单位，最小取值为 60 

**Return :**

无详情的“瑜伽”结果示例如下：

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372473235
	    }, 
	    "data": []
	}

有详情的“步行”结果示例如下：

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372473234
	    }, 
	    "data": [
	        [
	            1371006588, 
	            0
	        ], 
	        [
	            1371007188, 
	            262.6
	        ], 
	        [
	            1371007788, 
	            356.4
	        ], 
	        [
	            1371008388, 
	            0
	        ], 
	        [
	            1371008988, 
	            537.0
	        ], 
	        [
	            1371009588, 
	            712.2
	        ], 
	        [
	            1371010188, 
	            320.8
	        ], 
	        [
	            1371010788, 
	            229.0
	        ], 
	        [
	            1371011388, 
	            0
	        ], 
	        [
	            1371011988, 
	            164.0
	        ], 
	        [
	            1371012588, 
	            115.4
	        ], 
	        [
	            1371013188, 
	            102.6
	        ], 
	        [
	            1371013788, 
	            38.2
	        ], 
	        [
	            1371014388, 
	            39.8
	        ], 
	        [
	            1371014988, 
	            292.0
	        ], 
	        [
	            1371015588, 
	            54.0
	        ], 
	        [
	            1371016188, 
	            0
	        ], 
	        [
	            1371016788, 
	            106.0
	        ], 
	        [
	            1371017388, 
	            42.0
	        ]
	    ]
	}

---
[返回](how-to-fetch-jawbone-data-unofficial-api.md)
