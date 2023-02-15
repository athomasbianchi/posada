import pandas as pd
import pymongo

wb = pd.read_csv('./batters.csv', index_col=["PlayerId"])

# 'Name', 'Team', 'G', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'R',
# 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SF', 'SH', 'GDP', 'SB', 'CS', 'AVG',
# 'BB%', 'K%', 'BB/K', 'OBP', 'SLG', 'wOBA', 'OPS', 'ISO', 'Spd', 'BABIP',
# 'UBR', 'wSB', 'wRC', 'wRAA', 'wRC+', 'BsR', 'Fld', 'Off', 'Def', 'WAR',
# 'ADP', 'InterSD', 'InterSK', 'IntraSD', 'PlayerId'
wb["pts"] = wb["H"] + wb["2B"] + wb["3B"] * 2 + wb["HR"] * 3 + wb["RBI"] + wb["R"] + wb["HBP"] + wb["BB"] + wb["SB"] * 2

wb = wb.sort_values('points', ascending=False)

  # wb.to_csv('./batters_points.csv')