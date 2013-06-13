#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'iascchen@gmail.com'

apiHost = "https://jawbone.com/"
# apiHome = "%s%s" % ( apiHost , "nudge/api/v.1.34/")
apiHome = "%s%s" % ( apiHost , "nudge/api/")
imageHome = "%s%s" % ( apiHost , "image")

# auth
def getLoginUrl():
    return "%s%s" % ( apiHost , "user/signin/login" )

def getLogin2Url():
    return "%s%s" % ( apiHome , "users/login" )

# this function is useless, return 404
def getHealthCreditsUrl( userXid  = "@me"):
    return "%s%s" % ( apiHome ,  ("users/%s/healthCredits" %  userXid ))

def getUserScoresUrl(  userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/score" % userXid) )

def getUserSocialFeedUrl( userXid  = "@me"):
    return "%s%s" % ( apiHome ,  ("users/%s/social" % userXid ))

def getEventUrl( type , userXid  = "@me"):
    ret = {
        "move": lambda : getMoveUrl(userXid),
        "workout": lambda : getWorkoutUrl(userXid),
        "sleep": lambda : getSleepsUrl(userXid),
        "meal": lambda : getMealUrl(userXid),
        "mood": lambda : getMoodsUrl(userXid)
        }[type]()
    return ret

def getUserMoodUrl(userXid = "@me"):
    return "%s%s" % ( apiHome , ("users/%s/mood" % userXid ))

def getUserBandUrl( userXid  = "@me"):
    return "%s%s" % ( apiHome ,  ("users/%s/band" %  userXid ))

def getUserSleepsUrl( userXid  = "@me"):
    return "%s%s" % ( apiHome ,  ("users/%s/sleeps" %  userXid ))

def getUserWorkoutsUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/workouts" % userXid ))

def getUserAliasesUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/aliases" % userXid) )

def getUserFriendsUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/friends" % userXid) )

def getUserActivitesURL( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/events" % userXid) )

def getUserAcknowledgeUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/acknowledgement" % userXid) )

def getUserGoalsUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/goals" % userXid) )

def getUserTrendsUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/trends" % userXid) )

def getUserSettingsUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/settings" % userXid) )

def getUserTimeZoneUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/timezone" % userXid) )

def getUserProfileUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/profile" % userXid) )

def getUserProfilePhotoUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/photo" % userXid) )

def getUserFeedUrl( userXid = "@me" ):
    return "%s%s" % ( apiHome , ( "users/%s/feed" % userXid) )

def getMoveUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "moves/%s" % evtXid) )

def getMealUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "meals/%s" % evtXid ) )

def getMoodsUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "mood/%s" % evtXid) )

def getSleepsUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "sleeps/%s" % evtXid) )

def getWorkoutUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "workouts/%s" % evtXid) )

def getDeleteAliasesUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "aliases/%s" % evtXid) )

def getFeedItemUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "feeditems/%s" % evtXid) )

def getSleepsSnapshotUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "sleeps/%s/snapshot" % evtXid ))

def getWorkoutSnapshotUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "workouts/%s/snapshot" % evtXid ))

def getMovesSnapshotUrl( evtXid ):
    return "%s%s" % ( apiHome , ( "moves/%s/snapshot" % evtXid ))

# --------------------------
# these urls is not used now

def getContactsUploadUrl():
    return "%s%s" % ( apiHome , "users/@me/externalFriends/addressbook" )

def getExternalFriendsUrl( paramString):
    return "%s%s" % ( apiHome , ( "users/%s/externalFriends" % paramString) )

def getFacebookTokenUpdateUrl():
    return "%s%s" % ( apiHome , "users/@me/auth/facebook")

def getGeoCodeLocationURL():
    return "%s%s" % ( apiHome , "places/" )

def getMutualFriendsUrl( paramString):
    return "%s%s" % ( apiHome , ( "users/%s/mutualFriends" % paramString) )

def getTeammateSearchUrl( paramString, paramInt):
    return "%s%s" % ( apiHome , ( "users/@me/search?q=%s&page_size=%d" % ( paramString, paramInt )) )









