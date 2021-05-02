# Made By: Vishwas Sharma
# Styled up by FrosT
import requests
import datetime
from colorama import Fore,Style,Back

def wtr(city):
    complete_api_link = f"http://wttr.in/%7B{city}%7D?english=%7BLANG%7D&format=j1"
    api_link = requests.get(complete_api_link)
    result = api_link.json()
    timen = datetime.datetime.now()
    timec = timen.strftime('%d/%m/%Y, %H:%M')
 
    cu_temp = result['current_condition'][0]['temp_C']
    temp_max = result['weather'][0]['maxtempC']
    temp_min = result['weather'][0]['mintempC']
    feel = result['current_condition'][0]['FeelsLikeC']
    wea_desc = result['current_condition'][0]['weatherDesc'][0]['value']
    hmdt = result['current_condition'][0]['humidity']
    windk = result['current_condition'][0]['windspeedKmph']

    o = f'''{Fore.YELLOW}
           Showing Results For: {Fore.GREEN}{city.title()} on {timec}.        
                             {Fore.CYAN}Currently:
                                {Fore.GREEN}{cu_temp}⁰C

{Fore.YELLOW}Maximum Temperature: {Fore.GREEN}{temp_max}⁰C                     {Fore.YELLOW}Wind Speed: {Fore.GREEN}{windk}Kmph
{Fore.YELLOW}Minimum Temperature: {Fore.GREEN}{temp_min}⁰                      {Fore.YELLOW}Weather Description: {Fore.GREEN}{wea_desc}.
{Fore.YELLOW}Feels Like: {Fore.GREEN}{feel}⁰C                                  {Fore.YELLOW}Humidity: {Fore.GREEN}{hmdt}%
'''
    return o,cu_temp
    
if __name__ == "__main__":
    cy = input("Enter your city for it's weather: ")
    wet,tmp = wtr(cy)
    print(wet)
