import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 400
WIDTH = 500

#def buttontrigger():
 #   print("Button Clicked")

#def entrytrigger(entry):
 #   print(f"Entry:{entry}")


#api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={your api key}
def format_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        condition = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        feel = weather['main']['feels_like']

        output = 'City: %s \nCountry: %s \nCondition: %s \nTemperature: %s Celsius \n Real Feel: %s Celsius' %(city,country,condition,temperature,feel)

    except:
        output = 'Problem Obtaining Weather Information'

    return output

def get_weather(city):
    weather_key = "INSERT API KEY"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'appid':weather_key,'q':city, 'units': 'Metric'}
    response = requests.get(url, params = params)
    weather =response.json()
    #print(weather)
    label['text'] = format_weather(weather)




root = tk.Tk()




canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)  #rectangular area intended for drawing pictures or other complex layouts
canvas.pack()

background = tk.PhotoImage(file = 'AvocadoBoi_5-26-2020_32179910.png')
background_label = tk.Label(root, image = background)
background_label.place(relwidth = 1, relheight = 1)

#top frame
frame = tk.Frame(root, bg = "#80c1ff", bd = 3)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40) #text form syntax
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Test Button", bg = "gray", command = lambda: get_weather(entry.get())) #place a button inside root container
button.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)

#bottom frame
bot_frame = tk.Frame(root, bg = "#80c1ff", bd = 3)
bot_frame.place(relx = 0.5, rely = 0.3, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(bot_frame, font = 60)
label.place(relwidth = 1, relheight = 1)

root.mainloop()