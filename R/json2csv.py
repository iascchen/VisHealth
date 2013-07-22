#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'chenhao'

import json

class Json2Csv:
    def list2string(self , list ):
        ret = ""
        for l in list:
            ret = "%s,%s" % (ret , l)
        return "%s\n" % ret[1:]

    def parseJawboneBand(self , path , filename ):
        fn = "%s%s.json" % ( path , filename )
        ofn = "%s.csv" % ( filename )

        input = open( fn , 'r' )
        str = input.read()
        v = json.loads(str)

        output = open( ofn , 'w' )
        ticks = v["data"]["ticks"]

        tmps = ticks[0]["value"]
        headerKeys = sorted(tmps , key=lambda tmps:tmps[0] )
        header = self.list2string(headerKeys)
        print header
        output.write( header )

        for tick in ticks:
            # str = self.list2string(tick["value"].values())
            stmp = ""
            for key in headerKeys:
                stmp = "%s,%s" % ( stmp , tick["value"][ key ])

            str = "%s\n" % ( stmp[1:] )
            print str
            output.write( str )

    def parseJawboneTrends(self , path , filename ):
        fn = "%s%s.json" % ( path , filename )
        ofn = "%s.csv" % ( filename )

        input = open( fn , 'r' )
        str = input.read()
        v = json.loads(str)

        output = open( ofn , 'w' )
        datas = v["data"]["data"]

        tmps = datas[0][1]
        headerKeys = sorted(tmps , key=lambda tmps:tmps[0] )
        header = "datestr,%s" % self.list2string(headerKeys)
        print header
        output.write( header )

        for d in datas:
            tmps = d[1]
            stmp = ""
            for key in headerKeys:
                stmp = "%s,%s" % ( stmp , tmps[ key ])

            str = "%s,%s\n" % (d[0] ,  stmp[1:])
            print str
            output.write( str )

    def filterFileds(self , keys , ignoreSet ):
        tmpkeys = keys
        for k in ignoreSet:
            tmpkeys.remove(k)
        return sorted( tmpkeys )

    def parseJawboneSleeps(self , path , filename ):
        ignoredFieldSet = ("app_generated", "time_updated" , "band_ids" , "shared", "snapshot_image" , "networks" ,
                           "user" , "details" , "xid" , "title" , "type")
        ignoredDetailsFieldSet = ( "body" , "tz")

        fn = "%s%s.json" % ( path , filename )
        ofn = "%s.csv" % ( filename )

        input = open( fn , 'r' )
        str = input.read()
        v = json.loads(str)

        output = open( ofn , 'w' )
        datas = v["data"]["items"]

        tmps = datas[0]
        print tmps.keys()
        headerKeys = self.filterFileds( tmps.keys() , ignoredFieldSet )
        header = self.list2string(headerKeys)[:-1]
        print header

        tmpDetails = datas[0]["details"]
        detailsHeaderKeys = self.filterFileds( tmpDetails.keys() , ignoredDetailsFieldSet )
        header = "%s,%s" % (header , self.list2string(detailsHeaderKeys))
        print header

        output.write( header )

        for tmps in datas:
            stmp = ""
            for key in headerKeys:
                stmp = "%s,%s" % ( stmp , tmps[ key ])

            tmpsDetails = tmps["details"]
            for key in detailsHeaderKeys:
                stmp = "%s,%s" % ( stmp , tmpsDetails[ key ])

            str = "%s\n" % (stmp[1:])
            print str
            output.write( str )

if __name__ == "__main__":
    datapath = "../data/jawboneup/"

    trans = Json2Csv()
    # trans.parseJawboneBand( path = datapath , filename = "users_band_start" )
    # trans.parseJawboneTrends( path = datapath , filename = "users_trends-day" )

    trans.parseJawboneBand( path = datapath , filename = "users_band_1hour" )
    trans.parseJawboneSleeps( path = datapath , filename = "users_sleeps_1hour" )
