import pandas as pd
import json 


with open("orders.json", "r") as file:
    orders = json.load(file)