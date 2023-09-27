import tkinter as tk
from modules.weather_app.weather_map import Weather_map
from modules.calculator.run_gui import Calculator
#import modules.weather_app.weather_map.Weather_map as Weather_map
import os


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1280x720")
        #self.func_dict = {'weather_map': lambda: [w := weather_map.Weather_map(), w.display_map_stations(), w.mainloop()]}
        print(self.__dir__())
        self.func_dict = {'weather_map': lambda: [self.refresh(), w := Weather_map(self.master),
                                                  w.display_map_stations()],
                          'calculator': lambda: [self.refresh(), c := Calculator(self.master),
                                                 c.menu()]}

    def display_buttons(self):
        for i,key in enumerate(self.func_dict):
            func = self.func_dict[key]
            btn = tk.Button(self, text=key, command=func)
            btn.grid(row=0, column=i)

        #key = 'weather_map'
        #func = self.func_dict[key]
        #btn = tk.Button(self, text=key, command=func)
        #weather_map = importlib.import_module("weather_app.weather_map")
        #os.chdir("weather_app/weather_map")
        #btn.command = lambda: print("hell oworld")#
        #btn.grid(row=0, column=0)

    def refresh(self):
        cols,rows = self.size()

        for widget in self.winfo_children():
            widget.destroy()
        print(cols,rows)


if __name__ == '__main__':
    a = App()
    a.display_buttons()
    a.mainloop()