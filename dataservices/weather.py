#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'iascchen@gmail.com'

from lxml import etree
from datetime import date
import requests
import json
import logging
import unittest

class WeatherService:
    # This service use Panguso.com weather service
    panguAfHost = "http://af.panguso.com/"
    myHeaders = None

    devUserAgent = "panguso_boce"
    citiesID = None

    def __init__(self):
        logging.basicConfig(filename='../logs/log.txt', level=logging.DEBUG)
        self.myHeaders = {"User-Agent": self.devUserAgent}

    def logCommand(self, command, retJson, headers ):
        # tmp = { "cmd" : command , "ret" : json.dumps(retJson) , "hed" : headers }
        # logging.debug( tmp )

        logging.debug(json.dumps(retJson))

    def saveJsonData(self, filename, data):
        f = open("../data/panguso/%s" % filename, "w")
        f.write(json.dumps(data, indent=4))
        f.close()

    def saveXmlData(self, filename, data):
        f = open("../data/panguso/%s" % filename, "w")
        doc = etree.fromstring(data)
        f.write(etree.tostring(doc, pretty_print=True))
        f.close()

    def excuteGetRequst(self, command, params=None):
        print "Get : ", command
        response = requests.get(command, params=params, headers=self.myHeaders)
        content = response.json
        self.logCommand(command, content, response.headers)

        if( 200 != response.status_code):
            print "StatusCode : ", response.status_code

        return content

    # cityId use weather.com.cn CityID, for example : http://m.weather.com.cn/data/101010100.html
    # Tac is telephone area code
    def get_weather(self, cityName=None, cityId=None, tac=None):
        command = "%s%s" % ( self.panguAfHost, "weather/query" )
        request_data = {"city": cityName, "cityid": cityId, "tac": tac}
        return self.excuteGetRequst(command, params=request_data)

    def loadCitiesID(self, filename="weather_city.txt"):
        if ( self.citiesID == None):
            self.citiesID = {}
            f = open(filename, "r")
            for line in f.readlines():
                if line.startswith("#"):
                    continue

                row = line[:-1].split(":")
                self.citiesID.update({row[1]: row[0]})
            f.close()
        # print self.citiesID

    # TODO , implement multithread
    def get_all_weather(self, filename="weather_city.txt"):
        self.loadCitiesID(filename)

        datestr = "%s" % date.today()
        command = "%s%s" % ( self.panguAfHost, "weather/query" )

        weathers = { "date" : datestr , "data" : []}
        for id in sorted( self.citiesID.keys()):
            request_data = {"cityid": id}
            retjson = self.excuteGetRequst(command, params=request_data)
            weathers["data"].append( retjson )

        filename = "/weather_all_%s.json" % datestr
        # print weathers
        self.saveJsonData(filename=filename, data=weathers)

class WeatherServiceTest(unittest.TestCase):
    device = WeatherService()

    def test_get_weather(self):
        ret = self.device.get_weather(cityName="北京")
        self.device.saveJsonData(filename="/weather.json", data=ret)
        # print ret["cityExt"]["city"], ret["cityExt"]["cityid"]
        self.assertEquals(ret["cityExt"]["city"], u"北京")
        self.assertEquals(ret["cityExt"]["cityid"], "101010100")

        ret = self.device.get_weather(cityName="朝阳")
        self.device.saveJsonData(filename="/weather_2.json", data=ret)
        # print ret["cityExt"]["city"], ret["cityExt"]["cityid"]
        self.assertEquals(ret["cityExt"]["city"], u"朝阳")
        self.assertEquals(ret["cityExt"]["cityid"], "101010300")

        ret = self.device.get_weather(cityId="101071201")
        self.device.saveJsonData(filename="/weather_3.json", data=ret)
        # print ret["cityExt"]["city"], ret["cityExt"]["cityid"]
        self.assertEquals(ret["cityExt"]["city"], u"朝阳")
        self.assertEquals(ret["cityExt"]["cityid"], "101071201")

        ret = self.device.get_weather(tac="021")
        self.device.saveJsonData(filename="/weather_4.json", data=ret)
        # print ret["cityExt"]["city"], ret["cityExt"]["cityid"]
        self.assertEquals(ret["cityExt"]["city"], u"上海")
        self.assertEquals(ret["cityExt"]["cityid"], "101020100")

    def test_get_all_weather(self):
        self.device.get_all_weather( )
        pass

if __name__ == "__main__":
    unittest.main()