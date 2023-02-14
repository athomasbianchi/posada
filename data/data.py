import pandas as pd

wb = pd.read_csv('./batters.csv')

# 'Name', 'Team', 'G', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'R',
# 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SF', 'SH', 'GDP', 'SB', 'CS', 'AVG',
# 'BB%', 'K%', 'BB/K', 'OBP', 'SLG', 'wOBA', 'OPS', 'ISO', 'Spd', 'BABIP',
# 'UBR', 'wSB', 'wRC', 'wRAA', 'wRC+', 'BsR', 'Fld', 'Off', 'Def', 'WAR',
# 'ADP', 'InterSD', 'InterSK', 'IntraSD', 'PlayerId'
def total_points(wb):

  
  wb["points"] = wb["H"] + wb["2B"] + wb["3B"] * 2 + wb["HR"] * 3 + wb["RBI"] + wb["R"] + wb["HBP"] + wb["BB"] + wb["SB"] * 2
  return wb

def log(wb):
  return wb["Name"].head(5)

print(wb.head())
print(wb.columns)
print(log(wb))
print(total_points(wb))
print(log(wb))
print(wb.columns)
wb = wb.sort_values('points', ascending=False)
print(log(wb))
print(wb[["Name", "H", "points"]])