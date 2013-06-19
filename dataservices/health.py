#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'iascchen@gmail.com'

import requests
import logging
import unittest

# The World Health Organization Child Growth Standards
# http://www.who.int/childgrowth/standards/en/
class WHOService:
    whoHome = "http://www.who.int/childgrowth/standards"
    bodyMatrixP1 = {"/" : ["wfa" , "lhfa" , "bfa" , "wfh" , "wfl"] ,
                    "/second_set/" : ["hcfa", "acfa", "ssfa" , "tsfa"  ] }
    bodyMatrixP2 = ["boys" , "girls"]
    bodyMatrixP3 = ["p" , "z"]

    def __init__(self):
        logging.basicConfig(filename='../logs/log.txt', level=logging.DEBUG)

    def saveTextData(self, filename, data):
        f = open("../data/WHO/%s" % filename, "w")
        f.write(data)
        f.close()

    def download(self):
        for p2 in self.bodyMatrixP2:
            for p3 in self.bodyMatrixP3:
                for p1_k in self.bodyMatrixP1.keys():
                    for p1_v in self.bodyMatrixP1[p1_k]:
                        file = "%s_%s_%s_exp.txt" % (p1_v , p2 ,p3)
                        url = "%s%s%s" % (self.whoHome , p1_k, file)
                        print file , url
                        response = requests.get(url)
                        self.saveTextData(file , response.content )

class WHOServiceTest(unittest.TestCase):
    service = WHOService()

    def test_download(self):
        self.service.download()

class BmiCalculator:
    children_data = { "M":"boys_bmi.txt" , "F":"girls_bmi.txt"}
    girls_data = "girls_bmi.txt"
    adults_data = "adults_bmi.txt"

    levelName = ["Underweight", "Normal", "Overweight", "Obese Class I" , "Obese Class II"]
    # adultDetailName = ["偏轻", "健康", "超重", "严重超重", "极度超重"]
    childrenAgeBmi = {"M" : {} , "F" : {}}
    adultsBmi = {}

    def __init__( self ):
        for k in self.children_data.keys():
            f = open( self.children_data[k] , "r")
            for line in f.readlines() :
                if line.startswith("#") :
                    continue

                row = line[:-1].split( "," )
                self.childrenAgeBmi[k].update( { row[0] : [ float(row[1]), float(row[2]), float(row[3]) ]})
            f.close()
            # print self.childrenAgeBmi

        f = open( self.adults_data , "r")
        for line in f.readlines() :
            if line.startswith("#") :
                continue

            row = line[:-1].split( "," )
            self.adultsBmi.update( {row[0] : [ float(row[1]), float(row[2]), float(row[3]), float(row[4]) ]})
        f.close()
        # print adultsBmi

    # unit is meter and kg
    def bmiCalc( self, height, weight ):
        bmi = weight / height ** 2
        return bmi

    def getBmiLevel(self, dataset , bmi):
        level = 0
        for i in range( 0 , len(dataset) ):
            if bmi > dataset[i]:
                level = i + 1
                continue
            else:
                level = i
                break

        return level

    def bmiAdult( self, height, weight , area = "China" ):
        bmi = self.bmiCalc(height, weight)
        level = self.getBmiLevel( self.adultsBmi[area] , bmi)
        return {"bmi": "%.2f" % bmi, "level": level}

    def bmiChild( self, height, weight, gender, age ):
        bmi = self.bmiCalc(height, weight)
        if(( age < 2) | (age > 20)):
            return "Age must >= 2 and <= 20"
        else:
            agekey = "%d" % age
            level = self.getBmiLevel( self.childrenAgeBmi[gender][agekey] , bmi)
            return {"bmi": "%.2f" % bmi, "level": level}

class BmiCalculatoTest(unittest.TestCase):
    calc = BmiCalculator()

    def test_bmiAdult(self):
        # China, 18.5, 24, 27, 30
        testdata = [
            ( "China", 1.70 , 90 , 4 ),
            ( "China", 1.70 , 80 , 3 ),
            ( "China", 1.70 , 70 , 2 ),
            ( "China", 1.70 , 60 , 1 ),
            ( "China", 1.70 , 50 , 0 ) ]

        for d in testdata:
            level = self.calc.bmiAdult(height=d[1], weight=d[2] , area=d[0])
            self.assertEquals( level["level"] , d[3] )

    def test_bmiChild(self):
        # 2, 14.4, 18, 19.1
        # 10, 14, 19.9, 22.9
        # 15, 16.3, 24, 28.1
        # 20, 17.8, 26.5, 31.8
        testdata = [
            ( 2, 1.00 , 12 , 0 ),
            ( 10, 1.50 , 55 , 3 ),
            ( 15, 1.70 , 70 , 2 ),
            ( 20, 1.70 , 70 , 1 ) ]

        for d in testdata:
            level = self.calc.bmiChild(height=d[1], weight=d[2] , gender = "F" ,age=d[0])
            self.assertEquals( level["level"] , d[3] )

        testdata = [
            ( "1", 4.5 , 0.3  ),
            ( "21", 1.70 , 60 ) ]

        for d in testdata:
            level = self.calc.bmiChild(height=d[1], weight=d[2] , gender = "F" ,age=d[0])
            self.assertEquals( level , "Age must >= 2 and <= 20" )

if __name__ == "__main__":
    unittest.main(  )