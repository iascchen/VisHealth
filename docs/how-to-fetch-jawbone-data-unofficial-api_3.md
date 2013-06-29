# 获取Jawbone UP中的个人数据（二）非官方API #

# 3. 睡眠情况细节——Sleeps #

Jawbone 最吸引我的功能之一，就是能够记录睡眠情况。除了前面介绍的 user/%userXid%/social 等用户行为概述 API 之外，与睡眠相关的 API 还有以下几个：
	
	user/%userXid%/sleeps
	sleeps/%evtXid%
	sleeps/%evtXid%/snapshot

从 user/%userXid%/social 结果中的 "data"."feed"."xid"; 从 user/%userXid%/sleeps 结果中的 "data"."items"."xid" 获得 %evtXid% ， 用于调用 sleeps/%evtXid% 和 sleeps/%evtXid%/snapshot 。

![Meals](imgs/jawbone_up_4.png)

### user/%userXid%/sleeps ###

这个 API 能够返回个人的睡眠概括数据列表。在Jawbone UP 的手机应用界面中并没有对应的界面输出。

Request：
	
	GET
	https://jawbone.com/nudge/api/users/@me/sleeps?start_time=1370707200&end_time=1370966399&limit=100
	https://jawbone.com/nudge/api/users/RGaCBFg9CsDYVvm2kchbcw/sleeps?start_time=1370707200&end_time=1370966399&limit=100

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
	        "time": 1371960979
	    }, 
	    "data": {
	        "items": [
	            {
	                "time_updated": 1370730602, 
	                "xid": "EJpCkyAtwoPx-NDQaWEnSw", 
	                "band_ids": [
	                    "23424880A48CD061"
	                ], 
	                "title": "7 \u5c0f\u65f6 55 \u5206\u949f", 
	                "type": "sleep", 
	                "time_created": 1370699857, 
	                "sub_type": 0, 
	                "date": 20130609, 
	                "app_generated": false, 
	                "time_completed": 1370730588, 
	                "details": {
	                    "body": 0, 
	                    "smart_alarm_fire": 0, 
	                    "awakenings": 2, 
	                    "light": 12406, 
	                    "mind": 0, 
	                    "asleep_time": 1370700119, 
	                    "deep": 16136, 
	                    "awake": 2189, 
	                    "duration": 30731, 
	                    "tz": "Asia/Shanghai", 
	                    "quality": 99, 
	                    "awake_time": 1370729557
	                }, 
	                "is_manual": false, 
	                "shared": false, 
	                "snapshot_image": "/nudge/image/e/1370730602/EJpCkyAtwoPx-NDQaWEnSw.png", 
	                "networks": [], 
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
	                "time_completed": 1370812786, 
	                "xid": "EJpCkyAtwoNhHfcKmXhLDQ", 
	                "band_ids": [
	                    "23424880A48CD061"
	                ], 
	                "title": "6 \u5c0f\u65f6 40 \u5206\u949f", 
	                "type": "sleep", 
	                "time_created": 1370787934, 
	                "networks": [], 
	                "is_manual": false, 
	                "app_generated": false, 
	                "time_updated": 1370812792, 
	                "user": {
	                    "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	                    "name": "Tester VisHealth", 
	                    "short_name": "Tester", 
	                    "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	                    "last": "VisHealth", 
	                    "type": "user", 
	                    "first": "Tester"
	                }, 
	                "date": 20130610, 
	                "shared": false, 
	                "snapshot_image": "/nudge/image/e/1370812792/EJpCkyAtwoNhHfcKmXhLDQ.png", 
	                "sub_type": 0, 
	                "details": {
	                    "body": 0, 
	                    "smart_alarm_fire": 0, 
	                    "awakenings": 0, 
	                    "light": 13966, 
	                    "mind": 0, 
	                    "asleep_time": 1370788739, 
	                    "deep": 10080, 
	                    "awake": 806, 
	                    "duration": 24852, 
	                    "tz": "Asia/Shanghai", 
	                    "quality": 78, 
	                    "awake_time": 1370812534
	                }
	            }, 
	            {
	                "time_updated": 1370957154, 
	                "xid": "EJpCkyAtwoPgu7Y5xcoEUw", 
	                "band_ids": [
	                    "23424880A48CD061"
	                ], 
	                "title": "4 \u5c0f\u65f6 23 \u5206\u949f", 
	                "type": "sleep", 
	                "time_created": 1370880162, 
	                "sub_type": 0, 
	                "is_manual": false, 
	                "app_generated": false, 
	                "time_completed": 1370898180, 
	                "details": {
	                    "body": 0, 
	                    "smart_alarm_fire": 0, 
	                    "awakenings": 2, 
	                    "light": 11393, 
	                    "mind": 0, 
	                    "asleep_time": 1370881499, 
	                    "deep": 4408, 
	                    "awake": 2217, 
	                    "duration": 18018, 
	                    "tz": "Asia/Shanghai", 
	                    "quality": 46, 
	                    "awake_time": 1370898162
	                }, 
	                "date": 20130611, 
	                "shared": false, 
	                "snapshot_image": "/nudge/image/e/1370957154/EJpCkyAtwoPgu7Y5xcoEUw.png", 
	                "networks": [], 
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
	                "time_completed": 1370908500, 
	                "xid": "EJpCkyAtwoMIuTGkAPvdTw", 
	                "band_ids": [
	                    "23424880A48CD061"
	                ], 
	                "title": "1 \u5c0f\u65f6 7 \u5206\u949f", 
	                "type": "sleep", 
	                "time_created": 1370902821, 
	                "networks": [], 
	                "is_manual": false, 
	                "app_generated": false, 
	                "time_updated": 1370957155, 
	                "details": {
	                    "body": 0, 
	                    "smart_alarm_fire": 0, 
	                    "awakenings": 0, 
	                    "light": 1680, 
	                    "mind": 0, 
	                    "asleep_time": 1370903099, 
	                    "deep": 2340, 
	                    "awake": 1659, 
	                    "duration": 5679, 
	                    "tz": "Asia/Shanghai", 
	                    "quality": 12, 
	                    "awake_time": 1370907021
	                }, 
	                "date": 20130611, 
	                "shared": false, 
	                "snapshot_image": "/nudge/image/e/1370957155/EJpCkyAtwoMIuTGkAPvdTw.png", 
	                "sub_type": 2, 
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
	        "size": 4
	    }
	}


### sleeps/%evtXid% ###

从 user/%userXid%/social 结果中的 **"data"."feed"."xid"**; 从 user/%userXid%/sleeps 结果中的 **"data"."items"."xid"** 获得 %evtXid% ， 用于调用 sleeps/%evtXid% 。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/sleeps/EJpCkyAtwoOBmMCiBEugow

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1371960968
	    }, 
	    "data": {
	        "time_updated": 1370995674, 
	        "xid": "EJpCkyAtwoOBmMCiBEugow", 
	        "band_ids": [
	            "23424880A48CD061"
	        ], 
	        "title": "9 \u5c0f\u65f6 55 \u5206\u949f", 
	        "type": "sleep", 
	        "user": {
	            "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	            "name": "Tester VisHealth", 
	            "short_name": "Tester", 
	            "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	            "last": "VisHealth", 
	            "type": "user", 
	            "first": "Tester"
	        }, 
	        "comments": {
	            "items": [], 
	            "size": 0
	        }, 
	        "sub_type": 0, 
	        "is_manual": false, 
	        "app_generated": false, 
	        "time_completed": 1370995140, 
	        "emotions": {
	            "items": [], 
	            "size": 0
	        }, 
	        "time_created": 1370958101, 
	        "date": 20130612, 
	        "shared": false, 
	        "snapshot_image": "/nudge/image/e/1370995674/EJpCkyAtwoOBmMCiBEugow.png", 
	        "networks": [], 
	        "goals": {
	            "total": 27000, 
	            "bedtime": null, 
	            "deep": null
	        }, 
	        "details": {
	            "body": 0, 
	            "smart_alarm_fire": 1370988000, 
	            "awakenings": 1, 
	            "light": 20652, 
	            "mind": 0, 
	            "asleep_time": 1370958959, 
	            "deep": 15093, 
	            "awake": 1294, 
	            "duration": 37039, 
	            "tz": "Asia/Shanghai", 
	            "quality": 100, 
	            "awake_time": 1370995001
	        }
	    }
	}

### sleeps/%evtXid%/snapshot ###

从 user/%userXid%/social 结果中的 **"data"."feed"."xid"**; 从 user/%userXid%/sleeps 结果中的 **"data"."items"."xid"** 获得 %evtXid% ， 用于调用 sleeps/%evtXid%/snapshot 。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/sleeps/EJpCkyAtwoOBmMCiBEugow/snapshot

**Params：**

	无

**Return :**

睡眠详情为记录不同睡眠状态的开始时间。时间序列中的 1 = awake, 2 = light , 3 = deep。

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1371960969
	    }, 
	    "data": [
	        [
	            1370958101, 
	            1
	        ], 
	        [
	            1370959001, 
	            2
	        ], 
	        [
	            1370959901, 
	            3
	        ], 
	        [
	            1370962001, 
	            2
	        ], 
	        [
	            1370966201, 
	            3
	        ], 
	        [
	            1370967101, 
	            2
	        ], 
	        [
	            1370968301, 
	            3
	        ], 
	        [
	            1370969201, 
	            2
	        ], 
	        [
	            1370971601, 
	            3
	        ], 
	        [
	            1370972501, 
	            2
	        ], 
	        [
	            1370973701, 
	            3
	        ], 
	        [
	            1370974301, 
	            2
	        ], 
	        [
	            1370975501, 
	            3
	        ], 
	        [
	            1370976701, 
	            2
	        ], 
	        [
	            1370979701, 
	            3
	        ], 
	        [
	            1370981501, 
	            2
	        ], 
	        [
	            1370983901, 
	            3
	        ], 
	        [
	            1370985401, 
	            2
	        ], 
	        [
	            1370986601, 
	            3
	        ], 
	        [
	            1370987501, 
	            2
	        ], 
	        [
	            1370987801, 
	            1
	        ], 
	        [
	            1370988401, 
	            2
	        ], 
	        [
	            1370989601, 
	            3
	        ], 
	        [
	            1370992001, 
	            2
	        ], 
	        [
	            1370993201, 
	            3
	        ], 
	        [
	            1370994701, 
	            2
	        ], 
	        [
	            1370995001, 
	            1
	        ]
	    ]
	}

---
[返回](how-to-fetch-jawbone-data-unofficial-api.md)
