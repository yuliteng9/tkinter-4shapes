import requests
import tkinter as tk

response = requests.get("http://api.covid19api.com/summary")

window = tk.Tk()
window.geometry("800x400")
window.title("Covid stats")

for index in response.json()["Countries"]:
    if index["Country"] == "Canada":
        print(index)



window.mainloop()
