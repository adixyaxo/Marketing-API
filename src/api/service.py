from src.config.database import DF
from typing import Literal

def removeDuplicates(Column:str):
    CT = list(DF[Column])
    NonDup = []

    for type in CT:
        if type not in NonDup:
            NonDup.append(type)
    return NonDup



def getOptions():
    opt:dict[str:list] = {}
    columns = DF.columns.tolist()
    columns.remove("Conversion_Rate")
    columns.remove("Acquisition_Cost")
    columns.remove("ROI")
    columns.remove("Clicks")
    columns.remove("Impressions")
    columns.remove("Engagement_Score")
    columns.remove("Date")
    columns.remove("Campaign_ID")
    for column in columns:
        opt[column] = removeDuplicates(column)
    return opt

DF.get("Conversion_Rate").unique()

'''
Things we can find out
Total No of campaigns per company  - exact no

no of per type of campaign per company - choice based
gender based - choice based
Customer segment based - choice based
Location Based - choice based
channel used - choice based
Lanuage Based - choice based


age based - range based
duration based - range based
conversion rate based - range based
ROI based - range based
Clicks Based - range based
Impressions based - range based
Engagement Score based - range based
Date based - range based
'''
