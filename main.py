from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather_now():
  url = "https://devapi.qweather.com/v7/weather/now?location=101030100&key=afc9647291ad4e3e993aa97899b177d7"
  res = requests.get(url).json()
  weather = res['now']
  fxLink = res['fxLink']
  return weather['text'], int(weather['temp']), int(weather['feelsLike']), weather['windDir'],weather['windScale']+'级',weather['humidity']+'%',fxLink

def get_weather_today():
  url = "https://devapi.qweather.com/v7/weather/3d?location=101030100&key=afc9647291ad4e3e993aa97899b177d7"
  res = requests.get(url).json()
  weather = res['daily'][0]
  return weather['textDay'],weather['textNight'], int(weather['tempMax']),int(weather['tempMin']),weather['windDirDay']+weather['windScaleDay']+'级',weather['windDirNight']+weather['windScaleNight']+'级',weather['humidity']+'%',weather['precip'],int(weather['uvIndex'])

def get_weather_indices():
  url = "https://devapi.qweather.com/v7/indices/1d?type=0&location=101030100&key=afc9647291ad4e3e993aa97899b177d7"
  res = requests.get(url).json()
  indices = res['daily']
  return indices[0]['name']+':'+indices[0]['category'],indices[0]['text'],indices[2]['name']+':'+indices[2]['category'],indices[2]['text'],indices[12]['name']+':'+indices[12]['category'],indices[12]['text'],indices[6]['name']+':'+indices[6]['category'],indices[6]['text'],indices[8]['name']+':'+indices[8]['category'],indices[8]['text'],indices[7]['name']+':'+indices[7]['category'],indices[7]['text'],indices[15]['name']+':'+indices[15]['category'],indices[15]['text'],indices[5]['name']+':'+indices[5]['category'],indices[5]['text']

def get_weather_air():
  url = "https://devapi.qweather.com/v7/air/now?location=101030100&key=afc9647291ad4e3e993aa97899b177d7"
  res = requests.get(url).json()
  air = res['now']
  return air['category'],int(air['aqi']), air['pm2p5']+' μg/m³'


def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp", verify=False)
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

#def get_words2():
#  words2 = requests.get("https://saying.api.azwcl.com/saying/get", verify=False)
#  if words2.status_code != 200:
#    return get_words2()
#  return words2.json()['data']['content'],words2.json()['data']['author']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)

def get_random_color2():
  return "#%06x" % random.randint(0, 0xFFFFFF)

def get_random_color3():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color4():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color5():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color6():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color7():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color8():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color9():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color10():
  return "#%06x" % random.randint(0, 0xFFFFFF)

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
weatherTextNow, temperature, feelsLike,wind ,windScale, humidity,link   = get_weather_now()
weatherTextDay, weatherTextNight,tempMax,tempMin,windDay,windNight,humidityToday,precip,uvIndex = get_weather_today()
yundong,yundongText,chuanyi,chuanyiText,huazhuang,huazhuangText,guomin,guominText,ganmao,ganmaoText,shushi,shushiText,fangshai,fangshaiText,lvyou,lvyouText = get_weather_indices()
airText,aqi,pm25=get_weather_air()

#text, author = get_words2()

data = {
        "weatherTextNow":{"value":weatherTextNow},
        "temperature":{"value":temperature,"color": "#FF0000" if temperature >= 35 else "#FF9900" if 30<=temperature<35 else "#00FF00" if  15<=temperature<30 else "#00BFFF" if temperature<15 else "#0000CD"},
        "feelsLike":{"value":feelsLike,"color": "#FF0000" if feelsLike >= 35 else "#FF9900" if 30<=feelsLike<35 else "#00FF00" if  15<=feelsLike<30 else "#00BFFF" if feelsLike<15 else "#0000CD"},
        "wind":{"value":wind},
        "windScale":{"value":windScale},
        "humidity":{"value":humidity},
        "link":{"value":link},
        "weatherTextDay":{"value":weatherTextDay},
        "weatherTextNight":{"value":weatherTextNight},
        "tempMin":{"value":tempMin,"color": "#FF0000" if tempMin >= 35 else "#FF9900" if 30<=tempMin<35 else "#00FF00" if  15<=tempMin<30 else "#00BFFF" if tempMin<15 else "#0000CD"},
        "tempMax":{"value":tempMax,"color": "#FF0000" if tempMax >= 35 else "#FF9900" if 30<=tempMax<35 else "#00FF00" if  15<=tempMax<30 else "#00BFFF" if tempMax<15 else "#0000CD"},
        "windDay":{"value":windDay},
        "windNight":{"value":windNight},
        "humidityToday":{"value":humidityToday},
        "precip":{"value":precip},
        "uvIndex":{"value":uvIndex,"color":"#00FF00" if uvIndex<=2 else "#FFFF00" if 2<uvIndex<=4 else "#FF9900" if 4<uvIndex<=6 else "#FF0000" if 6<uvIndex<=9 else "#9900CC" },
        "air":{"value":airText,"color":"#00FF00" if airText=="优" else "#FF9900" if airText=="良" else "#FF0000" },
        "aqi":{"value":aqi},
        "pm25":{"value":pm25},
        "yundong":{"value":yundong},"yundongText":{"value":yundongText+" ", "color":get_random_color3()},
        "chuanyi":{"value":chuanyi},"chuanyiText":{"value":chuanyiText+" ", "color":get_random_color4()},
        "huazhuang":{"value":huazhuang},"huazhuangText":{"value":huazhuangText+" ", "color":get_random_color5()},
        "guomin":{"value":guomin},"guominText":{"value":guominText+" ", "color":get_random_color6()},
        "ganmao":{"value":ganmao},"ganmaoText":{"value":ganmaoText+" ", "color":get_random_color7()},
        "shushi":{"value":shushi},"shushiText":{"value":shushiText+" ", "color":get_random_color8()},
        "fangshai":{"value":fangshai},"fangshaiText":{"value":fangshaiText+" ", "color":get_random_color9()},
        "lvyou":{"value":lvyou},"lvyouText":{"value":lvyouText+" ", "color":get_random_color10()},
  
  
        "love_days":{"value":get_count()},
        "birthday_left":{"value":get_birthday()},
        "words":{"value":get_words()+" ", "color":get_random_color()},
      #  "words2":{"value":text+' —— '+ author+"  ", "color":get_random_color2()}
       }
res = wm.send_template(user_id, template_id, data)
print(res)
