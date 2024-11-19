# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-55kQ_JrYi3v6lFAt3NTKx0tCd031xBz
"""

import pandas as pd
baza={
    "FISH":["Qadamova Zulayxo", "Xalilov Durbek", "Abdullayeva G", "Jo'rayeva G", "Turdimatov M", "Erkinova Mohlaroyim", "Parpiyev O'rmonjon", "Parpiyeva Muhabbatxon", "Erkinov Asadbek", "Erkinova Nilufarxon"],
    "Manzil": ["Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar"],
    "Yoshi": ["26", "60", "26", "40", "60", "19", "46", "44", "23", "19"],
    "Ish joyi":["TATUFF", "TATUFF", "TATUFF", "TATUFF", "TATUFF", "TATUFF", "UMID servis", "Tadbirkor", "Injinir mexanik", "Hamshira"],
    "Jinsi": ["ayol", "erkak", "ayol", "ayol", "erkak", "ayol", "erkak", "ayol", "erkak", "ayol"]

}

db=pd.DataFrame(baza)
print(db)

filtr1=db[db["Ish joyi"]=="TATUFF"]
print(filtr1)

filtr2=db[(db["Ish joyi"]=="TATUFF") & (db["Jinsi"]=="ayol")]
print(filtr2)