# 获取咕咚运动移动应用中的数据——Python实现 #

---

Author : iascchen(at)gmail(dot)com

Date : 2013-07-18

新浪微博 : [@问天鼓](http://www.weibo.com/iascchen)

---

利用Python实现了咕咚 Codoon 运动的 API。对应API详细说明参见 [获取咕咚运动移动应用中的数据——非官方API](how-to-fetch-codoon-data-unofficial-api_all.md)

## 代码地址 ##

[https://github.com/iascchen/VisHealth/](https://github.com/iascchen/VisHealth/)

使用 devices/codoon.py 即可。

## 依赖包 ##

[requests](http://docs.python-requests.org/en/latest/) 当前使用版本为 1.2.3

## 源代码说明 ##

codoonurl.py 为 Codoon 服务请求 URL 入口生成工具。

codoon.py 为 Codoon 运动非官方 API 的 Python 实现代码。它的 main 方法是使用这些API的示例。
	
1. Codoon API 被封装在 class DeviceCodoon 中
2. Codoon App 一般通过 HTTP 协议与 api.codoon.com 通讯。在进行其他访问之前，必须先登录。可以用 Codoon 网注册用户通过 HTTP Basic 协议进行登陆。正确登录之后，这个 Token 将被存放为 DeviceCodoon 实例中的 codoonHeaders 变量中，每次向服务器的请求，都需要将 codoonHeaders 的加载在 HTTP Header 中提供。Codoon App 还支持利用新浪微博、腾讯微博、人人网的用户，通过OAuth协议登录（这几种登录方式本文并未论述）。
3. 访问Codoon其他站，需要进行 SSO，这个SSO需要用到 Cookies， 调用 get_misc_mobile( ) 方法后，如果正确返回，包含用户信息的 Cookies 将放在 DeviceCodoon 实例中的 codoonCookies 变量中。
4. 如果函数调用之后，各函数会返回所收到的JSON文件。如果调用失败，会抛出异常，或打出 Error Code 。

### HTTP Basic 认证后的 HTTP Header ###

需要将认证时的所获得 access_token 值设置到 HTTP Header：**Authorization** 里，即可保持会话。除此之外，还需要将**Charset**设置为 UTF-8。如：

	Authorization : Bearer  4836c512060faa34793730959daa901f
    Charset : UTF-8


### 带参数的请求 ###

需要向 Server 端提交参数的请求，需要采用 POST 方式传参。比较特殊的是，在 Codoon 的接口中，需要将参数需要转化为 JSON 之后，放在 POST 体中再提交。

下面的 Python 代码作为参考示例：

	startDate = "2013-06-01"
    endDate =  "2013-06-30"
	command = "http://api.codoon.com/api/gps_statistic"

	request_data = {"from_date" : fromDate , "to_date" : toDate}
	response = requests.post(command , data = json.dumps(request_data),  headers = self.codoonHeaders )
    content = json.loads(response.content)

## 代码示例 ##

为了方便理解，下面对原来main中的代码进行了最简化改写，去掉了一些不必要的为了输出和验证的代码。

---

### Part 1.	登陆 ###

可以用 Codoon 网注册用户通过 HTTP Basic 协议进行登陆。

Codoon App 还支持利用新浪微博、腾讯微博、人人网的用户，通过OAuth协议登录（这几种登录方式本文并未论述）。

**函数说明：**
	
	# 登录
	get_users_login(self , email , password )

	# 获得用户基本信息凭证
	verify_credentials(self)
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    device = DeviceCodoon ()

    # login
    logined = device.get_users_login(account["email"], account["passwd"])
	print device.auth_info

	credentials = device.verify_credentials()

### Part 2.	用户运动成就  ###

**函数说明：**

	# 返回用户的成就信息
	get_user_growing_point_related(self)
	
	# 返回用户的运动纪
	gps_highest_record(self)

	# 用户所获得的奖章
	get_user_medal(self)

	# 统计信息
	# 日期格式为： yyyy-mm-dd, 如：2013-06-01
    gps_statistic(self , fromDate , toDate)
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

	startDate = "2013-06-01"
    endDate =  "2013-06-30"

    device = DeviceCodoon ()
	
	# login
    device.get_users_login(account["email"], account["passwd"])

	# records
    growingPoint = device.get_user_growing_point_related( )
	
	# 纪录
    record = device.gps_highest_record( )
	# 奖章
    medal = device.get_user_medal( )
	# 统计
    statistic = device.gps_statistic( startDate , endDate )

### Part 3. 运动历史 ###

**函数说明：**

	# productId 为本机 IMEI 号，写个假的也可以	
	# count 应该是最大返回结果
	# excluded 缺省值为""， 格式不明
	# page 翻页信息
	# isPart 是否返回GPS位置点记录： 1 概述信息, 0 返回带有GPS位置点的记录
	get_route_log(self , productId , count = 100 , excluded = "" , page = 1 , isPart = 1 )

	# routeId 来自于 get_route_log 返回结果中的 "data"."route_id"
	get_single_log(self , routeId)

**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    imei = "000000000000000"

    device = DeviceCodoon ()

	# login
    device.get_users_login(account["email"], account["passwd"])

	# 获得用户的运动历史列表	
	routes = device.get_route_log( productId = imei , isPart = 0 )

    routes = device.get_route_log( productId = imei )
	
	# 获得具体每次的运动轨迹
	for r in routes["data"]:
    	routeId = r["route_id"]
    	route = device.get_single_log( routeId = routeId )

### Part 4. 智能配件API（疑似） ###

**函数说明：**

	get_mobile_portraits(self )

	get_tracker_goal(self)

	# endDate 截止日期，日期格式如：2013-06-30
	# daysBack 整数，向前回溯多少天。
	get_tracker_summary(self, endDate, daysBack )

	# datestr，日期格式如：2013-06-01
	get_tracker_data(self , datestr)

	# datestr，日期格式如：2013-06-01
	get_sleep_data(self, datestr)
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    endDate =  "2013-06-30"
    checkDate = "2013-06-17"

    device = DeviceCodoon ()

	# login
    device.get_users_login(account["email"], account["passwd"])
	
	# mobile_portraits
	portraits = device.get_mobile_portraits( )
	
	# tracker_goal
    tgoal = device.get_tracker_goal(  )
    
	# tracker_summary
    tsummary = device.get_tracker_summary( endDate = endDate, daysBack = 3)
    
	# tracker_data
    tdata = device.get_tracker_data( checkDate )
    
	# sleep_data
    sleep = device.get_sleep_data( checkDate )

### Part 5. 其他  ###

**函数说明：**

	# 约跑
	# point 地理位置，形式为两个浮点数组成的字符串。如："36.5,112.32"
	# gender 性别 : 1 Male, 0 Female. Gender is not 0 or 1, will return all
    # hobby 缺省设置为 ""，返回所有结果。服务端似乎有Bug，如果 hobby 为中文, 会返回 500 error, :(
	# page 整数，页码 
	people_surrounding(self , point , gender = 2 , hobby = None , page = 1)

	# 运动计划
	# programIds 很奇葩的是被**排除在外**的 Program ID 列表，例如：如果设置为 "3,4" ，将会返回不包括ID为 3，4 的列表
    sports_program_manifest_for_codoon(self, programIds)
	
	# programId， 来自 sports_program_manifest_for_codoon 中的 "data"."id"
    sports_program_detail(self , programId)

	# 空气质量
	# cityName, 中文城市名
	get_air_quality(self, cityName = None):

	version_run_xml(self):

	# 向 sso.codoon.com 进行认证，获得Cookies, 如果需要访问 www.codoon.com 的资源，就需要使用它。
    def get_misc_mobile( self ):

	# 访问 http://www.codoon.com/data_v/get_user_statistic
	# 得到的返回 JSON 形如： { "calorie": 82.45851, "days": 3.0, "km": 1.55822135 }
    def get_user_statistic( self ):
	
**参考代码：**

	account = { "email" : "your@email" , "passwd" : "yourpassword" }

    point = "36.5,112.32"

    device = DeviceCodoon ()

    # login
    logined = device.get_users_login(account["email"], account["passwd"])

    # 约跑
    # Maybe Server Bug : if hobby is Chinese , server will return 500 error, :(
    # ret = device.people_surrounding( point = point , gender = "1" , hobby = "跑步" , page = 1) will return 500
    peoples = device.people_surrounding( point = point , gender = "1" , hobby = "") # Male

    peoples = device.people_surrounding( point = point , gender = 2 , hobby = "" , page = 1) # All

    # program
    programs = device.sports_program_manifest_for_codoon( programIds = "3,4" ) # will return the record which ID is NOT 3 and 4
    
    programs = device.sports_program_manifest_for_codoon( programIds = "" )

	for p in programs["data"]:
    	programId = p["id"]
    	program = device.sports_program_detail( programId = programId )

    # air quality
    air = device.get_air_quality( cityName = "北京" )

    # Latest App version
    versionInfo = device.version_run_xml()

    # access other info from codoon site
    device.get_misc_mobile( )
	# will return JSON such as { "calorie": 82.45851, "days": 3.0, "km": 1.55822135 }
    wwwStatistic = device.get_user_statistic( ) 

---

祝各位玩的开心！