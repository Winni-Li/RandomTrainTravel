# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:16:41 2024

@author: Winni_Lee
"""

import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import messagebox

# 爬取台鐵車站資料
def get_station_list():
    url ="https://sheethub.com/tra.gov.tw/臺鐵車站代號"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假設車站名在table中
    stations = []
    table = soup.find('table')
    for row in table.find_all('tr')[1:]:
        station = row.find_all('td')[1].text.strip()
        stations.append(station)

    return stations

# 隨機選取車站
def pick_random_stations(station_list, num_stations=3):
    return random.sample(station_list, num_stations)

# 簡單的GUI介面
def create_interface():
    window = tk.Tk()
    window.title("小旅行規劃")

    # 標題
    label = tk.Label(window, text="隨機選取區間車站的小旅行", font=("Arial", 16))
    label.pack(pady=10)

    # 按鈕
    def on_click():
        stations = get_station_list()
        picked_stations = pick_random_stations(stations)
        messagebox.showinfo("隨機小旅行", f"您選擇的車站是：\n" + "\n".join(picked_stations))

    button = tk.Button(window, text="生成小旅行", command=on_click)
    button.pack(pady=20)

    window.mainloop()

create_interface()
