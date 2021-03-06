import json
import os
a = input("enter the website's name by which you will like to call it: ")
b = input(f"enter the {a}'s web address: ")
dic = {}
dic[a] = b
try:
    with open("websites.json", "r+") as file:
        data = json.load(file)
        if next(iter(dic)) not in data.keys():
            data.update(dic)
            file.seek(0)
            json.dump(data, file)
            print(data)
        else:
            print("the recipient's name is already registered.\do you want to overwrite it.")
            s = input()
            s.lower()
            if "y" in s:
                data.update(dic)
                file.seek(0)
                json.dump(data, file)
                print(data)
            elif "n" in s:
                print("Okay!")
            else:
                print("not recognised")
except FileNotFoundError as fe:
    with open("websites.json", "w+") as file:
        json.dump(dic, file)