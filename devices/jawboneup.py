#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'iascchen@gmail.com'

import requests
import json
import jawboneurl
import logging
import hashlib
import time

class DeviceJawboneUp:
    auth_info = None
    nudgeHeaders = None

    def __init__(self):
        logging.basicConfig(filename = '../logs/log.txt', level = logging.DEBUG)

    def logCommand(self , command , retJson , headers ):
        # tmp = { "cmd" : command , "ret" : json.dumps(retJson) , "hed" : headers }
        # logging.debug( tmp )
        logging.debug( json.dumps(retJson) )

    def saveJsonData(self , filename, data):
        f = open("../data/jawboneup/%s" % filename, "w")
        f.write(json.dumps( data , indent = 4 ))
        f.close()

    def excuteRequst(self , command , params , headers):
        print command
        response = requests.get(command , params = params , headers = headers)
        content = json.loads(response.content)

        if( 200 != response.status_code):
            print "StatusCode : " , response.status_code

        self.logCommand( command , content , response.headers )
        return content

    def displayEvents(self , ret):
        items = ret["data"]["items"]
        for item in items:
            try:
                print item["type"], item["title"]
            except:
                pass
        try:
            deleted = ret["data"]["deleted"]
            for item in deleted:
                print "Deleted:" , item
        except:
            pass

    def getUserEventFunc(self , urlFunc, evtXid ):
        command = urlFunc( evtXid )
        return self.excuteRequst(command , params = None , headers = self.nudgeHeaders)

    def getUserEventsInPeriodFunc(self , urlFunc, startTime , endTime , userXid = "@me", limit = 100):
        command = urlFunc( userXid = userXid )
        request_data = {'start_time' : startTime, 'end_time' : endTime, 'limit' : limit }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    # logins
    def get_auth_info(self , email , password ):
        command = jawboneurl.getLoginUrl()
        print command
        request_data = { 'email': email, 'pwd':  password, 'service': 'nudge' }
        response = requests.post(command , request_data)
        content = json.loads(response.content)

        if( 200 != response.status_code):
            print response.status_code

        self.logCommand( command , content , response.headers )

        token = content["token"]
        if ( token != None) :
            xid = content["user"]["xid"]
            self.auth_info =  { 'xid': xid, 'token': token }
            self.nudgeHeaders = { 'x-nudge-token': token }
        else:
            self.auth_info = None

        return content

    def get_users_login(self , email , password ):
        command = jawboneurl.getLogin2Url()
        print command
        hCode = hashlib.sha1()
        hCode.update(password)
        hash = hCode.hexdigest()
        request_data = {'email' : email, 'hash_pwd' : hash }

        response = requests.post(command , request_data)
        content = json.loads(response.content)

        if( 200 != response.status_code):
            print response.status_code

        self.logCommand( command , content , response.headers )

        token = content["data"]["session_uid"]
        if ( token != None) :
            xid = content["data"]["user"]["xid"]
            self.auth_info =  { 'xid': xid, 'token': token }
            self.nudgeHeaders = { 'x-nudge-token': token }
        else:
            self.auth_info = None

        return content

    def get_users_score(self , userXid = "@me", datestr = None):
        command = jawboneurl.getUserScoresUrl( userXid )
        request_data = {'date' : datestr }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    def get_users_social(self , userXid = "@me", datestr = None , limit = 20):
        command = jawboneurl.getUserSocialFeedUrl( userXid )
        request_data = {'date' : datestr, 'limit' : limit }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    # this result is similar with get_users_social
    def get_users_feed(self , userXid = "@me", limit = 20):
        command = jawboneurl.getUserFeedUrl( userXid )
        request_data = {'limit' : limit }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    def get_event(self , type , evtXid):
        command = jawboneurl.getEventUrl( type , evtXid )
        return self.excuteRequst(command , params = None , headers = self.nudgeHeaders)

    def get_moves(self , evtXid ):
        return self.getUserEventFunc( jawboneurl.getMoveUrl , evtXid  )

    def get_meals(self , evtXid ):
        return self.getUserEventFunc( jawboneurl.getMealUrl , evtXid  )

    def get_moods(self , evtXid ):
        return self.getUserEventFunc( jawboneurl.getMoodsUrl , evtXid  )

    def get_workouts(self , evtXid ):
        return self.getUserEventFunc( jawboneurl.getWorkoutUrl , evtXid  )

    def get_sleeps(self , evtXid ):
        return self.getUserEventFunc( jawboneurl.getSleepsUrl , evtXid  )

    def get_alias(self , evtXid ):
        return self.getUserEventFunc( jawboneurl.getUserAliasesUrl , evtXid  )

    def get_users_sleeps(self  , startTime , endTime , userXid = "@me", limit = 100):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserSleepsUrl, startTime , endTime ,
            userXid = userXid, limit = limit)

    def get_users_workouts(self  , startTime , endTime , userXid = "@me", limit = 100):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserWorkoutsUrl, startTime , endTime ,
            userXid = userXid, limit = limit)

    def get_users_band(self  , startTime , endTime , userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserBandUrl, startTime , endTime ,
            userXid = userXid, limit = None)

    def get_users_moods(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserMoodUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_goals(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserGoalsUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_acknowledgement(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserAcknowledgeUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_aliases(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserAliasesUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_friends(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserFriendsUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_settings(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserSettingsUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_timezone(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserTimeZoneUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_profile(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserProfileUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    def get_users_photo(self  ,userXid = "@me"):
        return self.getUserEventsInPeriodFunc( jawboneurl.getUserProfilePhotoUrl, startTime = None, endTime = None,
            userXid = userXid, limit = None)

    # bucketSize value is : d , w , m
    # inRange = d
    def get_users_trends(self  ,userXid = "@me" , endDate =  None , bucketSize = "d", inRange = "d"  ,
                         rangeDuration = 730 ):
        command = jawboneurl.getUserTrendsUrl( userXid = userXid )
        request_data = {"end_date" : endDate , "bucket_size" : bucketSize, "range" : inRange ,
                        "range_duration" : rangeDuration }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    # types value is : 1 workout, 2 meal, 3 sleep, 4 move, 5 mood, 7 body, if don't set this value, include all of them
    def get_users_events(self  ,userXid = "@me" , startDate = None, types = None , limit = 20 , listDeleted = True ):
        command = jawboneurl.getUserActivitesUrl( userXid = userXid )
        request_data = {'start_date' : startDate, 'types' : types, 'limit' : limit , "list_deleted" : listDeleted }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    # Result : 1 = awake, 2 = light , 3 = deep
    def get_sleeps_snapshot(self , evtXid ):
        command = jawboneurl.getSleepsSnapshotUrl( evtXid )
        return self.excuteRequst(command , params = None , headers = self.nudgeHeaders)

    def get_workouts_snapshot(self , evtXid , bucket = 100 ):
        command = jawboneurl.getWorkoutSnapshotUrl( evtXid)
        request_data = { 'bucket' : bucket }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    def get_moves_snapshot(self , evtXid , bucket = 100 ):
        command = jawboneurl.getMovesSnapshotUrl( evtXid)
        request_data = { 'bucket' : bucket }
        return self.excuteRequst(command , params = request_data , headers = self.nudgeHeaders)

    def get_feeditems(self , evtXid ):
        command = jawboneurl.getFeedItemUrl( evtXid)
        return self.excuteRequst(command , params = None , headers = self.nudgeHeaders)

if __name__ == "__main__":
    account = { "email" : "your@email" , "passwd" : "yourpassword" }
    
    startDate = "20130609"
    sDate = time.strptime(startDate, "%Y%m%d")
    start = long( time.mktime(sDate) )

    endDate = "20130612"
    eDate = time.strptime(endDate, "%Y%m%d")
    end = long( time.mktime(eDate) )

    device = DeviceJawboneUp ()

    # Part 1, login
    login = device.get_auth_info(account["email"], account["passwd"])
    print device.auth_info
    device.saveJsonData( filename = "/user_signin_login.json" , data = login)

    login = device.get_users_login(account["email"], account["passwd"])
    print device.auth_info
    device.saveJsonData( filename = "/users_login.json" , data = login)

    # Part 2, User's behaviours info
    # users/%userXid%/score
    score = device.get_users_score( datestr = startDate )
    device.saveJsonData( filename = "/users_score-date.json" , data = score)
    score = device.get_users_score( )
    device.saveJsonData( filename = "/users_score.json" , data = score)

    # users/%userXid%/social
    social = device.get_users_social( datestr = startDate)
    device.saveJsonData( filename = "/users_social-date.json" , data = social)
    social = device.get_users_social( )
    device.saveJsonData( filename = "/users_social.json" , data = social)

    feeds = social["data"]["feed"]
    for feed in feeds:
        try:
            print feed["type"], feed["title"]
            ret = device.get_event( feed["type"] , feed["xid"])
        except:
            pass

    # users/%userXid%/feed
    userfeeds = device.get_users_feed( limit = None )
    device.saveJsonData( filename = "/users_feed.json" , data = userfeeds)
    userfeeds = device.get_users_feed( limit = 5 )
    device.saveJsonData( filename = "/users_feed-limit.json" , data = userfeeds)

    feeds = userfeeds["data"]["feed"]
    i = 0
    for feed in feeds:
        try:
            print feed["type"], feed["title"]
            feeditem = device.get_feeditems(  feed["activity_xid"] )
            device.saveJsonData( filename = "/users_feeditem_%d.json" % i , data = feeditem)
            i += 1
        except:
            pass

    # users/%userXid%/events
    events = device.get_users_events(  )
    device.displayEvents( events )
    device.saveJsonData( filename = "/users_events.json" , data = events)

    events = device.get_users_events( startDate = startDate, listDeleted = True )
    device.displayEvents( events)
    device.saveJsonData( filename = "/users_events-start_listdeleted.json" , data = events)

    events = device.get_users_events( limit = 10 , listDeleted = True )
    device.displayEvents( events)
    device.saveJsonData( filename = "/users_events-listdeleted_limit.json" , data = events)

    events = device.get_users_events( limit = 10 , listDeleted = False )
    device.displayEvents( events)
    device.saveJsonData( filename = "/users_events-limit.json" , data = events)

    events = device.get_users_events( startDate = startDate, listDeleted = True , limit = 10 )
    device.displayEvents( events)
    device.saveJsonData( filename = "/users_events-start_listdeleted_limit.json" , data = events)

    tys = ["1" , "3"]
    eventsintypes = device.get_users_events( limit = 10 , types = ','.join(tys) , listDeleted = True )
    device.displayEvents( eventsintypes )
    device.saveJsonData( filename = "/users_events-types_listdeleted_limit.json" , data = eventsintypes)

    # check event type
    for t in range(1, 10) :
        ret = device.get_users_events( types = t , limit = 10 , listDeleted = True )
        items = ret["data"]["items"]
        if( (items != None) & (len(items) > 0) ):
            print t , items[0]["type"]

    # Part 3 : sleeps
    # users/%userXid%/events in type 3 is sleep
    usersleeps = device.get_users_events( types = "3" , limit = 10 , listDeleted = False )

    # user/%userXid%/sleeps
    usersleeps = device.get_users_sleeps( startTime = start , endTime = end , limit = 10)
    device.saveJsonData( filename = "/users_sleeps.json" , data = usersleeps)

    # display sleeps
    items = usersleeps["data"]["items"]
    # for item in items:
    #    xid = item["xid"]
    #    print item["type"], " " , xid
    #    sleep = device.get_sleeps( evtXid = xid )
    #    sleepsnap = device.get_sleeps_snapshot( evtXid = xid )

    if( (items != None) & (len(items) > 0) ):
        xid = items[0]["xid"]
        print items[0]["type"], " " , xid

        sleep = device.get_sleeps( evtXid = xid )
        device.saveJsonData( filename = "/sleeps.json" , data = sleep)
        sleepsnap = device.get_sleeps_snapshot( evtXid = xid )
        device.saveJsonData( filename = "/sleeps_snapshot.json" , data = sleepsnap)

    # Part 4 : moves
    # users/%userXid%/events in type 4 is moves
    moves = device.get_users_events( types = "4" , limit = 10 , listDeleted = False )

    items = moves["data"]["items"]
    # for item in items:
    #    xid = item["xid"]
    #    print item["type"], " " , xid
    #    move = device.get_moves( evtXid = xid )
    #    movesnap = device.get_moves_snapshot( evtXid = xid )
    if( (items != None) & (len(items) > 0) ):
        xid = items[0]["xid"]
        print items[0]["type"], " " , xid

        move = device.get_moves( evtXid = xid )
        device.saveJsonData( filename = "/moves.json" , data = move)
        movesnap = device.get_moves_snapshot( evtXid = xid )
        device.saveJsonData( filename = "/moves_snapshot.json" , data = movesnap)

    # Part 5 : workouts
    # users/%userXid%/events in type 1 is workouts
    workouts = device.get_users_events( types = "1" , limit = 10 , listDeleted = False )

    # user/%userXid%/workouts
    workouts = device.get_users_workouts( startTime = start , endTime = None , limit = 10)
    device.saveJsonData( filename = "/users_workouts.json" , data = workouts)

    # display workouts
    items = workouts["data"]["items"]
    i = 0
    for item in items:
        xid = item["xid"]
        print item["type"], " " , xid
        workout = device.get_workouts( evtXid = xid )
        device.saveJsonData( filename = ("/workouts_%d.json" % i), data = workout)
        workoutsnap = device.get_workouts_snapshot( evtXid = xid , bucket = 600 )
        device.saveJsonData( filename = ("/workouts_snapshot_%d.json" % i) , data = workoutsnap)
        i += 1

        if i > 2 :
            break

    # Part 6 : Meals and Mood
    # Meal
    meals = device.get_users_events( types = "2" , limit = 10 , listDeleted = True )

    items = meals["data"]["items"]
    # for item in items:
    #    xid = item["xid"]
    #    print item["type"], " " , xid
    #    meal = device.get_meals( evtXid = xid )

    xid = items[0]["xid"]
    print items[0]["type"], " " , xid
    meal = device.get_meals( evtXid = xid )
    device.saveJsonData( filename = "/meals.json" , data = meal)

    # Moods
    # user/%userXid%/moods
    currentmood = device.get_users_moods( )
    device.saveJsonData( filename = "/users_moods.json" , data = currentmood)
    currentmood = device.get_users_moods( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_moods-xid.json" , data = currentmood)

    xid = currentmood["data"]["xid"]
    mood = device.get_moods( evtXid = xid )
    device.saveJsonData( filename = "/moods.json" , data = mood)

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
    device.saveJsonData( filename = "/bodies.json" , data = body)
    items = body["data"]["items"]
    for item in items:
        print item["type"], " " , item["xid"]
        # TODO

    # Part 7, other user profiles
    # acknowledgement
    acknowledgement = device.get_users_acknowledgement(  )
    device.saveJsonData( filename = "/users_acknowledgement.json" , data = acknowledgement)
    acknowledgement = device.get_users_acknowledgement( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_acknowledgement-xid.json" , data = acknowledgement)

    # alias
    aliases = device.get_users_aliases(  )
    device.saveJsonData( filename = "/users_aliases.json" , data = aliases)
    aliases = device.get_users_aliases( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_aliases-xid.json" , data = aliases)

    # friends
    friends = device.get_users_friends( )
    device.saveJsonData( filename = "/users_friends.json" , data = friends)
    friends = device.get_users_friends( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_friends-xid.json" , data = friends)

    # what's you had done ?
    goals = device.get_users_goals( )
    device.saveJsonData( filename = "/users_goals.json" , data = goals)
    goals = device.get_users_goals( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_goals-xid.json" , data = goals)

    # user profiles
    profile = device.get_users_profile( )
    device.saveJsonData( filename = "/users_profile.json" , data = profile)
    profile = device.get_users_profile( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_profile-xid.json" , data = profile)

    photo = device.get_users_photo( )
    device.saveJsonData( filename = "/users_photo.json" , data = photo)
    photo = device.get_users_photo( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_photo-xid.json" , data = photo)

    # setting for up hardware
    setting = device.get_users_settings( )
    device.saveJsonData( filename = "/users_settings.json" , data = setting)
    setting = device.get_users_settings( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_settings-xid.json" , data = setting)

    timezone = device.get_users_timezone( )
    device.saveJsonData( filename = "/users_timezone.json" , data = timezone)
    setting = device.get_users_settings( device.auth_info["xid"] )
    device.saveJsonData( filename = "/users_timezone-xid.json" , data = timezone)

    # Part 8 , trends and band
    # trends
    monthtrends = device.get_users_trends( endDate =  None , inRange = "d" , bucketSize = "m"  )
    device.saveJsonData( filename = "/users_trends-month.json" , data = monthtrends)
    weektrends = device.get_users_trends( endDate =  None , inRange = "d" , bucketSize = "w"  )
    device.saveJsonData( filename = "/users_trends-week.json" , data = weektrends)
    daytrends = device.get_users_trends( endDate =  None , inRange = "d" , bucketSize = "d"  )
    device.saveJsonData( filename = "/users_trends-day.json" , data = daytrends)
    daytrends = device.get_users_trends( endDate = endDate , inRange = "d" , bucketSize = "d"  )
    device.saveJsonData( filename = "/users_trends-day_endDate.json" , data = daytrends)

    # Band
    band = device.get_users_band( startTime = start , endTime = None)
    device.saveJsonData( filename = "/users_band_start.json" , data = band)
    band = device.get_users_band( startTime = start , endTime = end)
    device.saveJsonData( filename = "/users_band-start_end.json" , data = band)
    band = device.get_users_band( startTime = None , endTime = None)
    device.saveJsonData( filename = "/users_band.json" , data = band)

    # Can't access this function in server
    # ret = device.get_users_healthCredits( datestr = "20130606" , timezoneStr = -28800 ,
    #     move_goal = 0, sleep_goal = 0 , eat_goal = 0, check_levels  = 1)
