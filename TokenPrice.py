import time
import tkinter as tk
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

total_price = ""

browser = webdriver.Chrome()
browser.get("https://www.okx.com/vi/markets/prices")
time.sleep(1/10)

def price(token):
    try:
        button_find = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div[2]/i")
        button_find.click()
        button_cancel = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/span")
        time.sleep(1/10)
        input_find = browser.find_element(By.CSS_SELECTOR,"input[placeholder='Tìm kiếm']")
        input_find.send_keys(token)
        time.sleep(1/10)
        token_name = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[4]/table/tbody/tr[1]/td[1]/a/span[2]')
        token_price = browser.find_element(By.XPATH,'//html/body/div[1]/div/div/div/div[4]/table/tbody/tr[1]/td[2]')
        token_change = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[4]/table/tbody/tr[1]/td[3]/div')
        token_text = f'{token_name.text} : {token_price.text} | {token_change.text}\n'
        global total_price
        total_price = total_price + token_text
        button_cancel.click()
    except Exception as e:
        print(e)

def main():
    token_list = entry.get()
    token = token_list.split(' ')
    for i in token:
        price(i)
        time.sleep(1)
    output.delete(1.0, tk.END)
    global total_price
    now = datetime.datetime.now()
    formatted_time = now.strftime(" %H:%M:%S %d-%m-%Y")
    output.insert(1.0,f'Giá vào lúc {formatted_time} \n{total_price}')
    total_price = ""


window = tk.Tk()
window.title('Cập nhật giá coin ')
window.geometry('400x300')

label = tk.Label(window,text="Nhập tên token \n (Các token cách nhau bởi dấu cách)")
label.pack(pady = 10)

entry = tk.Entry(window, width=20)
entry.pack()

button = tk.Button(window,text = 'Tìm',width=10,command = main)
button.pack(pady = 10)

output = tk.Text(window,width=40,height=8)
output.pack()

window.mainloop()

