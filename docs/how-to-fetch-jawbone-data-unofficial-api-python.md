# 获取Jawbone UP中的个人数据（三）Python实现 #

---

Author : iascchen(at)gmail(dot)com

Date : 2013-06-29

新浪微博 : [@问天鼓](http://www.weibo.com/iascchen)

---

利用Python实现了 Jawbone UP 的 API。对应API详细说明参见 [获取Jawbone UP中的个人数据（二）非官方API](how-to-fetch-jawbone-data-unofficial-api.md)

## 代码地址 ##

[https://github.com/iascchen/VisHealth/](https://github.com/iascchen/VisHealth/)

使用 devices/jawboneup.py 即可。

## 依赖包 ##

[requests](http://docs.python-requests.org/en/latest/)

## 源代码说明 ##

jawboneurl.py 为 Jawbone UP 服务请求 URL 入口生成工具。

jawboneup.py 为Jawbone UP 非官方 API 的 Python 实现代码。它的 main 方法是使用这些API的示例。
	
1. Jawbone UP API 被封装在 class DeviceJawboneUp 中
2. 获取Jawbone 的数据之前，首先登录。登录成功之后，能够获得用于维持会话的 Token。这个Token将被存放为 DeviceJawboneUp 实例中的 nudgeHeaders 变量中，每次向服务器的请求，都需要将 nudgeHeaders 的加载在 HTTP Header 中提供。
3. 登录之后，user 的 Xid， 身份认账 token 这两个参数，也会被存储于 DeviceJawboneUp 实例中的 auth_info 变量中。
4. 如果函数调用之后，各函数会返回所收到的JSON文件。如果调用失败，会抛出异常，或打出 Error Code 。

## 代码示例 ##

为了方便理解，下面对原来main中的代码进行了最简化改写，去掉了一些不必要的为了输出和验证的代码。

---

### Part 1.	登陆 ###

这两种登陆方法都可用，任选其一即可，Jawbone UP 2 的应用中使用的是 users/login 。

**函数说明：**

	get_users_login(self , email , password )
	get_auth_info(self , email , password )
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    device = DeviceJawboneUp ()

	# API users/login
    device.get_users_login(account["email"], account["passwd"])
    print device.auth_info
    
	# API user/signin/login
    device.get_auth_info(account["email"], account["passwd"])
    print device.auth_info
    
### Part 2.	用户行为概况  ###

**函数说明：**

	# 返回 datestr 日期那天的数据。
	# userXid , 取值可以有两种形式： 
	# 	@me ，用于访问自己的信息; 
	# 	可以使用 login 返回的 "user"."xid" 访问自己的信息。或者可以利用从朋友查找中获取的 User XID值，查询他人的信息（推测，未实验）。
	# datestr 格式为yyyymmdd. 缺省 datestr = None，返回今日数据。

	get_users_score(self , userXid = "@me", datestr = None) 
	
	# 返回 datestr 日期之前的用户事件，最多返回 limit 条。
	# datestr，用户事件的截止日期。格式为yyyymmdd. 缺省 datestr = None，返回截止日期为今日.
	# limit，整数，缺省为20。用于限制返回多少条结果	

	get_users_social(self , userXid = "@me", datestr = None , limit = 20)

	# 获得从当前日期向前的用户事件，最多返回 limit 条。

	get_users_feed(self , userXid = "@me", limit = 10)

	# 获得从某用户事件的详情 。

    get_feeditems(self , evtXid )

	# users/%userXid%/events 是个非常有用的函数。利用这个函数，能够获取当前用户的所有 Event， 包括已经被删除的用户事件。同时，这个 API 还有 types 参数，能够限制只返回特定类别 Event。
	# startDate, 开始日期，格式为yyyymmdd
	# types, 选择哪种类型的事件。取值为 : 1 workout, 2 meal, 3 sleep, 4 move, 5 mood, 7 body。需要显示多个类型，可以将类型取值用逗号连接。不设置则包括所有类型。此处取值为逆向工程得出，不一定全面。
	# limit, 最多返回多少条记录，缺省为20。
	# listDeleted, 取值为 True， False。缺省为 False。

	get_users_events(self  ,userXid = "@me" , startDate = None, types = None , limit = 20 , listDeleted = True )

	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

	startDate = "20130609"
    endDate =  "20130612"

    device = DeviceJawboneUp ()
	
	# login
    device.get_users_login(account["email"], account["passwd"])

	# users/%userXid%/score
    score = device.get_users_score( datestr = startDate )
    score = device.get_users_score( )
    
    # users/%userXid%/social
    social = device.get_users_social( datestr = startDate)
    social = device.get_users_social( )
    
    feeds = social["data"]["feed"]
    for feed in feeds:
        try:
            print feed["type"], feed["title"]
            ret = device.get_event( feed["type"] , feed["xid"])
        except:
            pass

    # users/%userXid%/feed
    userfeeds = device.get_users_feed( limit = 5 )

    feeds = userfeeds["data"]["feed"]
    for feed in feeds:
        try:
            print feed["type"], feed["title"]
            feeditem = device.get_feeditems(  feed["activity_xid"] )
        except:
            pass

    # users/%userXid%/events 
    events = device.get_users_events( startDate = startDate, listDeleted = True , limit = 10 )
    device.displayEvents( events)
    
    tys = ["1" , "3"]
    eventsintypes = device.get_users_events( limit = 10 , types = ','.join(tys) , listDeleted = True )
    device.displayEvents( eventsintypes )

    # check event type
    for t in range(1, 10) :
        ret = device.get_users_events( types = t , limit = 10 , listDeleted = True )
        items = ret["data"]["items"]
        if( (items != None) & (len(items) > 0) ):
            print t , items[0]["type"]

### Part 3. Sleeps ###

**函数说明：**

	# 获得 [ startTime , endTime ] 期间之内的睡眠情况。
	# userXid , 取值可以有两种形式： 
	# 	@me ，用于访问自己的信息; 
	# 	可以使用 login 返回的 "user"."xid" 访问自己的信息。或者可以利用从朋友查找中获取的 User XID值，查询他人的信息（推测，未实验）。
	# startTime, 为 long 型时间，即从1970年以来的秒数
	# endTime, 为 long 型时间，即从1970年以来的秒数
	# limit, 最多返回结果条数限制

	get_users_sleeps(self  , startTime , endTime , userXid = "@me", limit = 100)

	# 某次睡眠信息情况。
	# evtXid，例如可以从 user/%userXid%/social 结果中得到的的 "data"."feed"."xid" 获得 %evtXid%

	get_sleeps(self , evtXid )

	# 某次睡眠的按时间状态详情。

	get_sleeps_snapshot(self , evtXid )

	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

	startDate = "20130609"
    sDate = time.strptime(startDate, "%Y%m%d")
    start = long( time.mktime(sDate) )

	endDate = "20130612"
    eDate = time.strptime(endDate, "%Y%m%d")
    end = long( time.mktime(eDate) )

    device = DeviceJawboneUp ()

	# login
    device.get_users_login(account["email"], account["passwd"])

	# users/%userXid%/events in type 3 is sleep 
	usersleeps = device.get_users_events( types = "3" , limit = 10 , listDeleted = False )
    
	# user/%userXid%/sleeps
    usersleeps = device.get_users_sleeps( startTime = start , endTime = end , limit = 100)

	# display sleeps
	items = usersleeps["data"]["items"]
	for item in items:
		xid = item["xid"]
		print item["type"], " " , xid

        sleep = device.get_sleeps( evtXid = xid )
        sleepsnap = device.get_sleeps_snapshot( evtXid = xid )


### Part 4. Moves ###

**函数说明：**

	# 某次运动信息情况。
	# evtXid，例如可以从 user/%userXid%/social 结果中得到的的 "data"."feed"."xid" 获得 %evtXid%

	get_moves(self , evtXid )

	# 某次运动的按时间状态详情。
	# bucket，运动数据汇总时间颗粒度，以秒为单位，最小取值为 60 

	get_moves_snapshot(self , evtXid , bucket = 100 )
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

	startDate = "20130609"
    sDate = time.strptime(startDate, "%Y%m%d")
    start = long( time.mktime(sDate) )

    device = DeviceJawboneUp ()

	# login
    device.get_users_login(account["email"], account["passwd"])

	# users/%userXid%/events in type 4 is moves 
	moves = device.get_users_events( types = "4" , limit = 10 , listDeleted = False )

	# display moves
	items = moves["data"]["items"]
	for item in items:
		xid = item["xid"]
        print item["type"], " " , xid

        move = device.get_moves( evtXid = xid )
        movesnap = device.get_moves_snapshot( evtXid = xid )

### Part 5. Workouts  ###

**函数说明：**

	# 获得 [ startTime , endTime ] 期间之内的锻炼情况。
	# userXid , 取值可以有两种形式： 
	# 	@me ，用于访问自己的信息; 
	# 	可以使用 login 返回的 "user"."xid" 访问自己的信息。或者可以利用从朋友查找中获取的 User XID值，查询他人的信息（推测，未实验）。
	# startTime, 为 long 型时间，即从1970年以来的秒数
	# endTime, 为 long 型时间，即从1970年以来的秒数
	# limit, 最多返回结果条数限制

	get_users_workouts(self  , startTime , endTime , userXid = "@me", limit = 100)

	# 某次锻炼信息情况。
	# evtXid，例如可以从 user/%userXid%/social 结果中得到的的 "data"."feed"."xid" 获得 %evtXid%

	get_workouts(self , evtXid )

	# 某次锻炼的按时间状态详情。并非所有的 workouts/%evtXid%/snapshot 都会返回详细的数据，一些锻炼方式，如：步行、跑步等，使用 snapshot 能够返回细节运动数据；而另一些锻炼方式，如：瑜伽，则没有细节运动数据。
	# bucket，运动数据汇总时间颗粒度，以秒为单位，最小取值为 60 

	get_workouts_snapshot(self , evtXid , bucket = 100 )

	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

	startDate = "20130609"
    sDate = time.strptime(startDate, "%Y%m%d")
    start = long( time.mktime(sDate) )

    device = DeviceJawboneUp ()

	# login
    device.get_users_login(account["email"], account["passwd"])

	# users/%userXid%/events in type 1 is workouts 
	workouts = device.get_users_events( types = "1" , limit = 10 , listDeleted = False )
    
	# user/%userXid%/workouts
    workouts = device.get_users_workouts( startTime = start , endTime = None , limit = 10)

	# display workouts
	items = workouts["data"]["items"]
	for item in items:
		xid = item["xid"]
        print item["type"], " " , xid

        workout = device.get_workouts( evtXid = xid )
        workoutsnap = device.get_workouts_snapshot( evtXid = xid , bucket = 600 )

### Part 6. Meals & Mood  ###

**函数说明：**

	# 获得用户最近一次Moods情况。
	# userXid , 取值可以有两种形式： 
	# 	@me ，用于访问自己的信息; 
	# 	可以使用 login 返回的 "user"."xid" 访问自己的信息。或者可以利用从朋友查找中获取的 User XID值，查询他人的信息（推测，未实验）。

	get_users_moods(self  ,userXid = "@me")
	
	# evtXid，例如可以从 user/%userXid%/social 结果中得到的的 "data"."feed"."xid" 获得 %evtXid%

	# 某次饮食信息情况。
	get_meals(self , evtXid )
	# 某次Mood信息情况。
	get_moods(self , evtXid )

**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    device = DeviceJawboneUp ()

	# login
    device.get_users_login(account["email"], account["passwd"])

	# Meal
    meals = device.get_users_events( types = "2" , limit = 10 , listDeleted = True )

    items = meals["data"]["items"]
	for item in items:
		xid = item["xid"]
        print item["type"], " " , xid

        meal = device.get_meals( evtXid = xid )

    # Moods
	# user/%userXid%/moods
    currentmood = device.get_users_moods( device.auth_info["xid"] )    
	xid = currentmood["data"]["xid"]
    mood = device.get_moods( evtXid = xid )

	# user/%userXid%/events in type 5 is mood
    moods = device.get_users_events( types = "5" , limit = 10 , listDeleted = True )

    items = moods["data"]["items"]
	for item in items:
		xid = item["xid"]
        print item["type"], " " , xid

        mood = device.get_moods( evtXid = xid )

    # Body, 
	# user/%userXid%/events in type 7 is body , such as weight data from other App named Withings
    body = device.get_users_events( types = "7" , limit = 10 , listDeleted = True )
    items = body["data"]["items"]
    for item in items:
        print item["type"], " " , item["xid"]

### Part 7. Other User Proiles  ###

**函数说明：**

	# userXid , 取值可以有两种形式： 
	# 	@me ，用于访问自己的信息; 
	# 	可以使用 login 返回的 "user"."xid" 访问自己的信息。或者可以利用从朋友查找中获取的 User XID值，查询他人的信息（推测，未实验）。

	get_users_acknowledgement(self , userXid = "@me")

	get_users_aliases(self , userXid = "@me")

	get_users_friends(self , userXid = "@me")

	get_users_goals(self , userXid = "@me")

	get_users_profile(self , userXid = "@me")

	get_users_photo(self , userXid = "@me")

	get_users_settings(self , userXid = "@me")

	get_users_timezone(self , userXid = "@me")
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    device = DeviceJawboneUp ()

	# login
    device.get_users_login(account["email"], account["passwd"])

    # display privicy setting
    acknowledgement = device.get_users_acknowledgement(  )
	acknowledgement = device.get_users_acknowledgement( device.auth_info["xid"] )

    # alias
	aliases = device.get_users_aliases(  )
    aliases = device.get_users_aliases( device.auth_info["xid"] )

    # friends
    friends = device.get_users_friends( )
    friends = device.get_users_friends( device.auth_info["xid"] )
   
    # what's you had done ?
    goals = device.get_users_goals( )
    goals = device.get_users_goals( device.auth_info["xid"] )
    
    # user profiles
    profile = device.get_users_profile( )
	profile = device.get_users_profile( device.auth_info["xid"] )
    
	photo = device.get_users_photo( )
	photo = device.get_users_photo( device.auth_info["xid"] )
    
    # setting for up hardware
    setting = device.get_users_settings( )
	setting = device.get_users_settings( device.auth_info["xid"] )

    timezone = device.get_users_timezone( )
	setting = device.get_users_settings( device.auth_info["xid"] )

### Part 8. Trends & Band ###

**函数说明：**

	# 返回用户运动的历史统计。
	# endDate , 统计截止日期，格式为 yyyymmdd
	# bucketSize, 取值为 : d 日 , w 周, m 月
	# inRange ,  取值似乎只能为 d 按天
	# rangeDuration，返回的最大的区间，与 range 有关。

    get_users_trends(self, userXid = "@me" , endDate = None , bucketSize = "d", inRange = "d" , rangeDuration = 730 ):

	# 时间颗粒度为分钟，显示用户上传的详细运动和能量消耗数据。
	# startTime, 为 long 型时间，即从1970年以来的秒数
	# endTime, 为 long 型时间，即从1970年以来的秒数

	get_users_band(self , startTime , endTime , userXid = "@me"):

**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }
	
	startDate = "20130609"
    sDate = time.strptime(startDate, "%Y%m%d")
    start = long( time.mktime(sDate) )

	endDate = "20130612"
    eDate = time.strptime(endDate, "%Y%m%d")
    end = long( time.mktime(eDate) )

    device = DeviceJawboneUp ()

	# login
    device.get_users_login(account["email"], account["passwd"])

    # trends
	
    monthtrends = device.get_users_trends( endDate =  None , inRange = "d" , bucketSize = "m"  )
    weektrends = device.get_users_trends( endDate =  None , inRange = "d" , bucketSize = "w"  )
    daytrends = device.get_users_trends( endDate =  None , inRange = "d" , bucketSize = "d"  )
    daytrends = device.get_users_trends( endDate =  endDate , inRange = "d" , bucketSize = "d"  )
    
    # Band
    band = device.get_users_band( startTime = start , endTime = end )

## 其他 ##

其他还有一些社交类、饮食类 API 与用户行为数据相关性不大，不再进行分析。

祝各位玩的开心！