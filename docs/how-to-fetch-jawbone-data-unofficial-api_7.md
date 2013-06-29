# 获取Jawbone UP中的个人数据（二）非官方API #

# 7. 其他个人信息 #

## Acknowledgement ##

### user/%userXid%/acknowledgement ###

返回此用户基本情况。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/acknowledgement
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/acknowledgement

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432025
	    }, 
	    "data": {
	        "primary_team_xid": "", 
	        "last": "VisHealth", 
	        "name": "Tester VisHealth", 
	        "short_name": "Tester", 
	        "settings": {
	            "share_move": true, 
	            "share_eat": false, 
	            "profile_privacy": "friends", 
	            "share_sleep": false, 
	            "share_mood": true
	        }, 
	        "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	        "user_is_friend": true, 
	        "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "user_received_invite": false, 
	        "type": "user", 
	        "user_sent_invite": false, 
	        "first": "Tester"
	    }
	}

## Aliases ##

### user/%userXid%/aliases ###

返回此用户曾经使用的设备的 aliases。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/aliases
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/aliases

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432033
	    }, 
	    "data": {
	        "items": [
	            {
	                "alias": "iasc@163.com", 
	                "xid": "N0-rp7AnP9M08aMT-OA", 
	                "type": 10
	            }, 
	            {
	                "alias": "222c3254103c38485395bbd4ac128b7178881322cab796992ab5e", 
	                "xid": "N0-rp7AnP9PIh301Ymg", 
	                "type": 15
	            }, 
	            {
	                "alias": "6a7c367a58f9152e2312dc4f238f85515716c6a29b7632a0b298e", 
	                "xid": "N0-rp7AnP9NlJCay_uA", 
	                "type": 15
	            }, 
	            {
	                "alias": "iasc@163.com", 
	                "xid": "N0-rp7AnP9PBkXp3_43", 
	                "type": 1
	            }, 
	            {
	                "alias": "d191b684f6627fd3c15a17976d3a5bdfadd7e0b081d88c36d678e", 
	                "xid": "N0-rp7AnP9MEyTr4M-s", 
	                "type": 15
	            }
	        ], 
	        "size": 5
	    }
	}

## Friends ##

### user/%userXid%/friends ###

返回此用户的好友。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/friends
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/friends

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432036
	    }, 
	    "data": {
	        "requests": {
	            "items": [], 
	            "size": 0
	        }, 
	        "friends": {
	            "items": [], 
	            "size": 0
	        }, 
	        "unacknowledged_count": 0
	    }
	}

## Goals ##

### user/%userXid%/goals ###

返回此用户的健身目标。具体数值什么逻辑俺也没搞明白。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/goals
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/goals

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432020
	    }, 
	    "data": {
	        "move": 3500, 
	        "sleep": 21600, 
	        "eat": 2
	    }
	}

## Photo ##

### user/%userXid%/photo ###

返回此用户的照片。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/photo
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/photo

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432043
	    }, 
	    "data": {
	        "primary_team_xid": "", 
	        "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "name": "Tester VisHealth", 
	        "short_name": "Tester", 
	        "settings": {
	            "share_move": true, 
	            "share_eat": false, 
	            "profile_privacy": "friends", 
	            "share_sleep": false, 
	            "share_mood": true
	        }, 
	        "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	        "user_is_friend": true, 
	        "last": "VisHealth", 
	        "user_received_invite": false, 
	        "type": "user", 
	        "user_sent_invite": false, 
	        "first": "Tester"
	    }
	}

## Profile ##

### user/%userXid%/profile ###

返回此用户的健身数据汇总。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/profile
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/profile

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432041
	    }, 
	    "data": {
	        "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "score": {
	            "mood": null, 
	            "move": {
	                "distance": 1.179, 
	                "longest_idle": 1860, 
	                "calories": 58.8214670439, 
	                "bmr_calories_day": 1298.23403661, 
	                "goals": {
	                    "steps": [
	                        1683.0, 
	                        10000
	                    ], 
	                    "workout_time": [
	                        0.0, 
	                        null
	                    ]
	                }, 
	                "longest_active": 305, 
	                "hidden": false, 
	                "bg_steps": 1683.0, 
	                "bmr_calories": 486.780843611, 
	                "active_time": 870.0
	            }, 
	            "sleep": {
	                "awakenings": 2, 
	                "light": 14015.0, 
	                "time_to_sleep": 241, 
	                "goals": {
	                    "total": [
	                        20934.0, 
	                        27000
	                    ], 
	                    "bedtime": [
	                        1439, 
	                        null
	                    ], 
	                    "deep": [
	                        6919.0, 
	                        null
	                    ]
	                }, 
	                "qualities": [
	                    62
	                ], 
	                "awake": 766.0, 
	                "hidden": false
	            }, 
	            "insights": {
	                "items": []
	            }, 
	            "meals": {
	                "num_meals": 0, 
	                "calories": 0.0, 
	                "num_drinks": 0, 
	                "goals": {
	                    "carbs": [
	                        0.0, 
	                        null
	                    ], 
	                    "fiber": [
	                        0.0, 
	                        null
	                    ], 
	                    "sodium": [
	                        0.0, 
	                        null
	                    ], 
	                    "sugar": [
	                        0.0, 
	                        null
	                    ], 
	                    "calcium": [
	                        0.0, 
	                        null
	                    ], 
	                    "unsat_fat": [
	                        0.0, 
	                        null
	                    ], 
	                    "cholesterol": [
	                        0.0, 
	                        null
	                    ], 
	                    "protein": [
	                        0.0, 
	                        null
	                    ], 
	                    "sat_fat": [
	                        0.0, 
	                        null
	                    ]
	                }, 
	                "hidden": false, 
	                "num_foods": 0
	            }, 
	            "user_metrics": {
	                "dob": 19760609, 
	                "gender": 1, 
	                "pal": null, 
	                "weight": 56.2, 
	                "height": 1.58
	            }
	        }, 
	        "friends": {
	            "items": [], 
	            "size": 0
	        }, 
	        "user": {
	            "primary_team_xid": "RGaCBFg9CsDOwAhjtgE4qA", 
	            "up_last_sync": 1372381740, 
	            "name": "Tester VisHealth", 
	            "short_name": "Tester", 
	            "image": "user/image/i/51b4916b03eb185d1c1948a5_RGaCBFg9CsDYVvm2kchbcw_137078820345_2781804_photo.jpeg", 
	            "user_is_friend": true, 
	            "xid": "RGaCBFg9CsDYVvm2kchbcw", 
	            "up_member_since": 1370439133, 
	            "last": "VisHealth", 
	            "user_received_invite": false, 
	            "type": "user", 
	            "user_sent_invite": false, 
	            "first": "Tester"
	        }, 
	        "mutual_friends": {}
	    }
	}

## Settings ##

### user/%userXid%/settings ###

返回此用户的软件设置，包括用户信息和一些设定。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/settings
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/settings

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432039
	    }, 
	    "data": {
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
	        "smart_alarm": [
	            {
	                "stopTimeMinsPastMidnight": 390, 
	                "dayMask": 62, 
	                "enable": true, 
	                "startTimeMinsPastMidnight": 370
	            }, 
	            {
	                "stopTimeMinsPastMidnight": 480, 
	                "dayMask": 65, 
	                "enable": true, 
	                "startTimeMinsPastMidnight": 460
	            }
	        ], 
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
	    }
	}

## Timezone ##

### user/%userXid%/timezone ###

返回此用户的时区。

**Request：**
	
	GET
	https://jawbone.com/nudge/api/user/@me/timezone
	https://jawbone.com/nudge/api/user/RGaCBFg9CsDYVvm2kchbcw/timezone

**Params：**

	无

**Return :**

	{
	    "meta": {
	        "code": 200, 
	        "message": "OK", 
	        "user_xid": "RGaCBFg9CsDYVvm2kchbcw", 
	        "time": 1372432044
	    }, 
	    "data": [
	        {
	            "date": 19700101, 
	            "tz": "Asia/Shanghai", 
	            "time": 0
	        }
	    ]
	}

---
[返回](how-to-fetch-jawbone-data-unofficial-api.md)
