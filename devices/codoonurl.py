#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'iascchen@gmail.com'

webHost = "http://www.codoon.com/"
apiHost = "http://api.codoon.com/"
staticHost = "http://static.codoon.com/"

apiHome = "%s%s" % ( apiHost , "api/")

# auth
def getTokenUrl():
    return "%s%s" % ( apiHost , "token" )

def getVerifyCredentialsUrl():
    return "%s%s" % ( apiHome , "verify_credentials" )

def getVersionRunUrl():
    return "%s%s" % ( staticHost , "app/android/version_run.xml" )

def getMiscMobileUrl():
    return "%s%s" % ( webHost , "misc/mobile_index" )

def getUserStatisticUrl():
    return "%s%s" % ( webHost , "data_v/get_user_statistic" )

def getUserMedalUrl():
    return "%s%s" % ( apiHome , "get_user_medal" )

def getUserGrowingPointUrl():
    return "%s%s" % ( apiHome , "get_user_growing_point_related" )

def getMobilePortraitsUrl():
    return "%s%s" % ( apiHome , "get_mobile_portraits" )

def getPeopleSurroundingUrl():
    return "%s%s" % ( apiHome , "people_surrounding" )

def getGpsHighestRecordUrl():
    return "%s%s" % ( apiHome , "gps_highest_record" )

def getGpsStatisticUrl():
    return "%s%s" % ( apiHome , "gps_statistic" )

def getAirQualityUrl():
    return "%s%s" % ( apiHome , "get_air_quality" )

def getSportsProgramManifestUrl():
    return "%s%s" % ( apiHome , "sports_program_manifest_for_codoon" )

def getSportsProgramDetailUrl():
    return "%s%s" % ( apiHome , "sports_program_detail" )

def getSingleLogUrl():
    return "%s%s" % ( apiHome , "get_single_log" )

def getRouteLogUrl():
    return "%s%s" % ( apiHome , "get_route_log" )

def getTrackerSummaryUrl():
    return "%s%s" % ( apiHome , "get_tracker_summary" )

def getTrackerDataUrl():
    return "%s%s" % ( apiHome , "get_tracker_data" )

def getTrackerGoalUrl():
    return "%s%s" % ( apiHome , "get_tracker_goal" )

def getSleepDataUrl():
    return "%s%s" % ( apiHome , "get_sleep_data" )




