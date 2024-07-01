import requests
import json
import datetime
from prettytable import PrettyTable

def api(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    key = '7f628240c7ecf2c3259ea4a64034d24a'
    url = api_url + "appid=" + key + "&q=" + city_name
    return requests.get(url).json()
    
def get():
    city = input("Enter a city: ")
    return city

def table_format(api, name):
    info = datetime.datetime.now()
    date = str(info).split()
    start_datetime = datetime.datetime.strptime(str(info), '%Y-%m-%d %H:%M:%S.%f')
    day = start_datetime.strftime('%A')

    cloud = api['weather'][0]['description']
    # temp_min = api['main']['temp_min']
    
    
    
    
    time = date[1].split(".")
    temp_max = api['main']['temp_max']
    tn = round(18543/int(temp_max))
    tx = round(5179/int(temp_max))
    icon = api['weather'][0]['icon']
    
    table = PrettyTable()
    table.field_names = ["City", "Day", "Date", "Time", "Cloud", "Temp °F", "Temp °C", "Icon"]
    table.add_row([name, day, date[0], time[0], cloud, tn, tx, icon])
    print(table)
 
if __name__ == "__main__":
    name =get()
    apis = api(name)
    table_format(apis, name)
    
    

