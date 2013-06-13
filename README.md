# VisHealth

VisHealth is a open source project of data visualization for sports monitor and health care, which is developed in python 2.7.3.
we want to integrate some wearable devices data, visualize them for better sports and health suggestion.

## License Info
GPLv3

## Release Info

20130613
Firstly, VisHealth implemented jawbone up band un-official api. these functions are hacked from Jawbone up App.
Can used in Jawbone Server version : v.1.34
Reference : [eric-blue](http://eric-blue.com/2011/11/28/jawbone-up-api-discovery/), the "healthCredits" method can't be accessed. [alexburrell](https://github.com/alexburrell/up-for-status-board])

## Using it

### Jawbone UP
If you want to use this api, please open /devices/jawboneup.py，then change the main method, filled the account info with your Jawbone account， then you can run the main method and read the return json file in folder "data/jawboneup"
```pythont
account = { "email" : "iascchen@gmail.com" , "passwd" : "yourpassword" }
```

## Contact Me
Email ： iascchen AT gmail.com or iasc AT 163.com
Sina Weibo ： [@问天鼓](http://www.weibo.com/u/2090594487）


