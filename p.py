import numpy as np
import pickle as pk
import pandas as pd


f1=open("liner_reg.pkl","rb")
model=pk.load(f1)

with open("column.pkl", "rb") as file:
    saved_columns = pk.load(file)

