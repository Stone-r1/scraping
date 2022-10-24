import tkinter 
import tkinter.messagebox
from tkinter import StringVar
import requests

class page:
    def __init__(self) -> None:

        self.main_page = tkinter.Tk()
        self.main_page.title('weather')
        self.main_page.resizable(False, False)
        self.main_page.iconbitmap('')
        self.main_page.geometry('300x295+1000+150')
        self.main_page.configure(bg='#1ad4ed')

        self.top_frame = tkinter.Frame(self.main_page)
        self.top_frame.config(bg='#1ad4ed')
        self.mid_frame = tkinter.Frame(self.main_page)
        self.mid_frame.config(bg='#1ad4ed')
        self.optional = tkinter.Frame(self.main_page)
        self.optional.config(bg='#1ad4ed')
        self.answer_frame = tkinter.Frame(self.main_page)
        self.answer_frame.config(bg='#1ad4ed')
        self.button_frame = tkinter.Frame(self.main_page)
        self.button_frame.config(bg='#1ad4ed')

        self.title_weather_label = tkinter.Label(self.top_frame, text='weather',
                                           fg='#1a72ed', font=('something', 24),
                                           width=25, height=1, bg='#1ad4ed')
        self.title_weather_label.pack(side='top')

        self.line = tkinter.Label(self.top_frame, text='________________________________________________________________',
                                   fg= '#178d9c', bg='#1ad4ed', font=('something', 30), height=1)
        self.line.pack(side='bottom')

        self.question_label = tkinter.Label(self.mid_frame, text='city:',
                                            fg='#1a72ed', font=('Purlisa', 12),
                                            width=15, height=1, bg='#1ad4ed')
        self.question_label.pack(side='left')

        self.entry_label = tkinter.Entry(self.mid_frame, text='write city', selectbackground='#3f8af2')
        self.entry_label.pack(side='right')

        self.line1 = tkinter.Label(self.optional, text='________________________________________________________________',
                                   fg= '#178d9c', bg='#1ad4ed', font=('something', 30), height=1)
        self.line1.pack(side='top')

        self.temp1 = tkinter.IntVar()
        self.weather1 = tkinter.IntVar()
        self.wind1 = tkinter.IntVar()

        self.temp1.set(0)
        self.weather1.set(0)
        self.wind1.set(0)

        self.choice_temp = tkinter.Checkbutton(self.optional, text='Temperature',
                                               variable=self.temp1, width= 12, bg='#1ad4ed',
                                               fg='#1a72ed', activebackground='#13bbd1')
        self.choice_temp.pack(side='left')

        self.choice_weather = tkinter.Checkbutton(self.optional, text='Weather',
                                                  variable=self.weather1, width= 9, bg='#1ad4ed',
                                                  fg='#1a72ed', activebackground='#13bbd1')
        self.choice_weather.pack(side='left')

        self.choice_wind = tkinter.Checkbutton(self.optional, text='Wind', variable=self.wind1,
                                               width=7, bg='#1ad4ed', fg='#1a72ed', 
                                               activebackground='#13bbd1')
        self.choice_wind.pack(side='left')

        self.line2 = tkinter.Label(self.button_frame, text='________________________________________________________________',
                                   fg= '#178d9c', bg='#1ad4ed', font=('something', 30), height=1)
        self.line2.pack(side='top')

        self.temp_answer = StringVar()
        self.temp_label = tkinter.Label(self.answer_frame, textvariable=self.temp_answer, 
                                        fg= '#03171a', bg='#1ad4ed', width=10, height=1)
        self.temp_label.pack(side='left')

        self.weather_answer = StringVar()
        self.weather_label = tkinter.Label(self.answer_frame, textvariable=self.weather_answer, 
                                           fg= '#03171a', bg='#1ad4ed', width=10, height=1)
        self.weather_label.pack(side='left')

        self.wind_answer = StringVar()
        self.wind_label = tkinter.Label(self.answer_frame, textvariable=self.wind_answer, 
                                        fg= '#03171a', bg='#1ad4ed', width=10, height=1)
        self.wind_label.pack(side='left')

        self.view_button = tkinter.Button(self.button_frame, text='View', width=20, bg='#1ad4ed',
                                          fg='#1a72ed', activebackground='#13bbd1', command=self.view)
        self.view_button.pack(side='left')
        
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', width=15, bg='#1ad4ed', 
                                         fg='#1a72ed', activebackground='#13bbd1', command=self.main_page.destroy)
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.optional.pack()
        self.answer_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def view(self):
        temp = self.temp1.get()
        weather = self.weather1.get()
        wind = self.wind1.get()

        city_name = self.entry_label.get()

        status_code_success_value = 200
        api_key = 'api_key'
        units = {'units': 'metric'}

        find_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}', params=units)
        if find_weather.status_code != status_code_success_value:
            tkinter.messagebox.showerror('Error', 'this city is not defined')
        elif find_weather.status_code == status_code_success_value:
            x = find_weather.json()

        if temp == 1 and weather == 1 and wind == 1:
            current_temperature = x['main']['temp']
            current_weather = x['weather'][0]['main']
            wind_speed = x['wind']['speed']
            return self.temp_answer.set(current_temperature), self.weather_answer.set(current_weather), self.wind_answer.set(wind_speed)
        elif temp == 1 and weather == 1:
            current_temperature = x['main']['temp']
            current_weather = x['weather'][0]['main']
            return self.temp_answer.set(current_temperature), self.weather_answer.set(current_weather)
        elif temp == 1 and wind == 1:
             current_temperature = x['main']['temp']
             wind_speed = x['wind']['speed']
             return self.temp_answer.set(current_temperature), self.wind_answer.set(wind_speed)
        elif temp == 1:
            current_temperature = x['main']['temp']
            return self.temp_answer.set(current_temperature)
        elif weather == 1 and wind == 1:
            current_weather = x['weather'][0]['main']
            wind_speed = x['wind']['speed']
            return self.weather_answer.set(current_weather), self.wind_answer.set(wind_speed)
        elif weather == 1:
            current_weather = x['weather'][0]['main']
            return self.weather_answer.set(current_weather)
        elif wind == 1:
            wind_speed = x['wind']['speed']
            return self.wind_answer.set(wind_speed)

page = page()