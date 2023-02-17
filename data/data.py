import pandas as pd
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")
wb = pd.read_csv(
    './batters.csv',
    # index_col=["PlayerId"]
    )

# 'Name', 'Team', 'G', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'R',
# 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SF', 'SH', 'GDP', 'SB', 'CS', 'AVG',
# 'BB%', 'K%', 'BB/K', 'OBP', 'SLG', 'wOBA', 'OPS', 'ISO', 'Spd', 'BABIP',
# 'UBR', 'wSB', 'wRC', 'wRAA', 'wRC+', 'BsR', 'Fld', 'Off', 'Def', 'WAR',
# 'ADP', 'InterSD', 'InterSK', 'IntraSD', 'PlayerId'
wb["pts"] = wb["H"] + wb["2B"] + wb["3B"] * 2 + wb["HR"] * 3 + wb["RBI"] + wb["R"] + wb["HBP"] + wb["BB"] + wb["SB"] * 2

wb.sort_values('pts', ascending=False)

  # wb.to_csv('./batters_points.csv')
# TODO remove duplicates
  # TODO fix issue with PlayerId
  # TODO split push to database
  # TODO someday use venv

client = MongoClient(
    "mongodb+srv://ybucks:" + config["PASSWORD"] + "@cluster0.nz88yey.mongodb.net/?retryWrites=true&w=majority")

db = client["2023"]
collection = db["Scoring"]

data_dic = wb.to_dict("records")

collection.insert_many(data_dic)