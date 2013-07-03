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

if __name__ == "__main__":
    datapath = "../data/jawboneup/"

    trans = Json2Csv()
    trans.parseJawboneBand( path = datapath , filename = "users_band_start" )
    trans.parseJawboneTrends( path = datapath , filename = "users_trends-day" )
