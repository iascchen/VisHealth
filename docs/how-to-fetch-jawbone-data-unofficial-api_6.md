# 获取Jawbone UP中的个人数据（二）非官方API #

# 6. Meals 和 Mood #

从 user/%userXid%/social 结果中的 "data"."feed"."xid" 获得 %evtXid% ， 用于调用 meals/%evtXid%， moods/%evtXid% 。

## Meals ##

### meals/%evtXid% ###

觉得饮食是Jawbone UP中比较鸡肋的功能，实在是懒得输入吃的是什么。与饮食相关的 API 有：

![Meals](imgs/IMG_1618.PNG)

	meals/%evtXid%

**Request：**
	
	GET
	https://jawbone.com/nudge/api/meals/EJpCkyAtwoMKaoaitjJHmg

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372431991
	    }, 
	    "data": {
	        "image": null, 
	        "time_created": 1370732127, 
	        "emotions": {
	            "items": [], 
	            "size": 0
	        }, 
	        "networks": [], 
	        "place_name": "", 
	        "time_completed": 1370732127, 
	        "xid": "EJpCkyAtwoMKaoaitjJHmg", 
	        "title": "Fried Egg \u548c Noodle Soup", 
	        "comments": {
	            "items": [], 
	            "size": 0
	        }, 
	        "note": "Fried Egg \u548c Noodle Soup", 
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
	        "shared": false, 
	        "type": "meal", 
	        "place_lon": 0.0, 
	        "user": {
	            "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	            "name": "Tester VisHealth", 
	            "short_name": "Tester", 
	            "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	            "last": "VisHealth", 
	            "type": "user", 
	            "first": "Tester"
	        }, 
	        "place_lat": 0.0, 
	        "date": 20130609, 
	        "sub_type": 1, 
	        "reaction": null, 
	        "time_updated": 1370732333, 
	        "items": {
	            "items": [
	                {
	                    "category_xid": "", 
	                    "image": null, 
	                    "multiplier_max": 5, 
	                    "multiplier_min": 0.1, 
	                    "carbohydrate": 3.88000011444, 
	                    "trans_fat": 0.0, 
	                    "measurement": "\u514b", 
	                    "saturated_fat": 0.270000010729, 
	                    "protein": 1.67999994755, 
	                    "xid": "vQ_cgl_cir2Bvy58ezYtBQ", 
	                    "sodium": 459.0, 
	                    "vitamin_c": 0, 
	                    "vitamin_a": 0, 
	                    "unsaturated_fat": 0.689999997616, 
	                    "sugar": 0.109999999404, 
	                    "type": "plate", 
	                    "fiber": 0.300000011921, 
	                    "description": "", 
	                    "potassium": 0.0, 
	                    "fat": 0.0, 
	                    "serving_xid": "DKFM_lU5qlg", 
	                    "sub_type": 2, 
	                    "monounsaturated_fat": 0.0, 
	                    "name": "Noodle Soup", 
	                    "calories": 31.0, 
	                    "polyunsaturated_fat": 0.0, 
	                    "calcium": 10.0, 
	                    "amount": 100.0, 
	                    "iron": 0, 
	                    "cholesterol": 3.0, 
	                    "food_xid": "ZAeHWmUphFM"
	                }, 
	                {
	                    "multiplier_min": 0.1, 
	                    "image": null, 
	                    "multiplier_max": 5, 
	                    "category_xid": "", 
	                    "carbohydrate": 0.879999995232, 
	                    "trans_fat": 0.0, 
	                    "measurement": "\u514b", 
	                    "saturated_fat": 4.29400014877, 
	                    "protein": 13.6300001144, 
	                    "xid": "vQ_cgl_cir2HK0LrwH-8iQ", 
	                    "sodium": 204.0, 
	                    "vitamin_c": 0, 
	                    "vitamin_a": 0, 
	                    "unsaturated_fat": 9.00599956512, 
	                    "sugar": 0.829999983311, 
	                    "type": "plate", 
	                    "fiber": 0.0, 
	                    "description": "", 
	                    "potassium": 0.0, 
	                    "fat": 0.0, 
	                    "serving_xid": "ac02AZA36z8", 
	                    "sub_type": 2, 
	                    "monounsaturated_fat": 0.0, 
	                    "name": "Fried Egg", 
	                    "calories": 201.0, 
	                    "polyunsaturated_fat": 0.0, 
	                    "calcium": 60.0, 
	                    "amount": 100.0, 
	                    "iron": 0, 
	                    "cholesterol": 457.0, 
	                    "food_xid": "QH1xyEjt3wc"
	                }
	            ], 
	            "size": 2
	        }, 
	        "place_type": "", 
	        "app_generated": false, 
	        "goals": {
	            "carbs": null, 
	            "fiber": null, 
	            "sodium": null, 
	            "sat_fat": null, 
	            "calcium": null, 
	            "unsat_fat": null, 
	            "cholesterol": null, 
	            "protein": null, 
	            "sugar": null
	        }
	    }
	}

## Mood ##

### user/%userXid%/mood ###

返回用户最近一次发表的 Mood。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/mood
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/mood

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432018
	    }, 
	    "data": {
	        "time_updated": 1370915387, 
	        "xid": "EJpCkyAtwoOzV4mpWxU5uA", 
	        "title": "\u8868\u73b0\u597d\u5440", 
	        "time_created": 1370915345, 
	        "app_generated": false, 
	        "details": {
	            "tz": "Asia/Shanghai"
	        }, 
	        "date": 20130611, 
	        "shared": true, 
	        "type": "mood", 
	        "sub_type": 3, 
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
	}

### mood/%evtXid% ###

与 Moods 相关的 API 有：

![Moodss](imgs/IMG_1619.PNG)

**Request：**
	
	GET
	https://jawbone.com/nudge/api/mood/EJpCkyAtwoOzV4mpWxU5uA

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432005
	    }, 
	    "data": {
	        "time_updated": 1370915387, 
	        "xid": "EJpCkyAtwoOzV4mpWxU5uA", 
	        "title": "\u8868\u73b0\u597d\u5440", 
	        "user": {
	            "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	            "name": "Tester VisHealth", 
	            "short_name": "Tester", 
	            "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	            "last": "VisHealth", 
	            "type": "user", 
	            "first": "Tester"
	        }, 
	        "emotions": {
	            "items": [], 
	            "size": 0
	        }, 
	        "app_generated": false, 
	        "details": {
	            "tz": "Asia/Shanghai"
	        }, 
	        "time_created": 1370915345, 
	        "date": 20130611, 
	        "shared": true, 
	        "type": "mood", 
	        "sub_type": 3, 
	        "comments": {
	            "items": [], 
	            "size": 0
	        }
	    }
	}

---
[返回](how-to-fetch-jawbone-data-unofficial-api.md)
