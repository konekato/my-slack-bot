from slackbot.bot import listen_to
import urllib.request
import json

citycode = '130010' # 東京
response= urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
response = json.loads(response.decode('utf-8'))

def get_message_location():
    message_location = response['location']['city']
    message_location += 'の天気は、\n'
    message_location += '\n'

    return message_location

def get_messages_forecast_by_days():
    messages_forecast = ['『今日』の情報はありませんでした。\n\n', '『明日』の情報はありませんでした。\n\n', '『明後日』の情報はありませんでした。\n\n']
    day_from_today = 0
    for r in response['forecasts']:
        messages_forecast[day_from_today] = '『' + r['dateLabel'] + '(' + r['date'] + ')』\n'
        messages_forecast[day_from_today] += '天気：' + r['telop'] + '\n'
        messages_forecast[day_from_today] += '最低気温：'
        if r['temperature']['min']:
            messages_forecast[day_from_today] += r['temperature']['min']['celsius']
        else:
            messages_forecast[day_from_today] += '情報無し'
        messages_forecast[day_from_today] += '　最高気温：'
        if r['temperature']['max']:
            messages_forecast[day_from_today] += r['temperature']['max']['celsius']
        else:
            messages_forecast[day_from_today] += '情報無し'
        messages_forecast[day_from_today] += '\n'
        messages_forecast[day_from_today] += '\n'
        day_from_today += 1
    
    return messages_forecast

def get_message_description():
    message_description = '『詳細』\n'
    message_description += response['description']['text']
    message_description += '\n'

    return message_description

def fetch_message_forecast_of(day):
    message = ''
    messages_forecasts = get_messages_forecast_by_days()

    if day == '今日':
        message += messages_forecasts[0]
    elif day == '明日':
        message += messages_forecasts[1]
    elif day == '明後日':
        message += messages_forecasts[2]
    return message

def fetch_message_forecast_description():
    message = get_message_description()
    return message

def fetch_message_forecast_all():
    message = get_message_location()
    messages_forecasts = get_messages_forecast_by_days()

    for forecasts in messages_forecasts:
        message += forecasts
    message += get_message_description()
    return message

@listen_to('今日')
def forecast_today(message):
    message.send(fetch_message_forecast_of('今日'))

@listen_to('明日')
def forecast_tomorrow(message):
    message.send(fetch_message_forecast_of('明日'))
    
@listen_to('明後日')
def forecast_day_after_tomorrow(message):
    message.send(fetch_message_forecast_of('明後日'))

@listen_to('詳細')
def forecast_description(message):
    message.send(fetch_message_forecast_description())

@listen_to('予報')
def forecast_all(message):
    message.send(fetch_message_forecast_all())