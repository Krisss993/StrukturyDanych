import pandas as pd

df = pd.DataFrame({
    '1st':1,
    '2nd':2
}, index=['index1'])



df = pd.read_csv(r'D:\PycharmProjects\StrukturyDanych\StrukturyDanychAlgorytmyKtoreMusiszZnac\WorldUniversityRanking\cwurData.csv')
print(df)


print(df.columns)

# print(df[(df['country'] == 'Poland') & (df['year'] == 2015)])

print(df.query("country == 'Poland' & year == 2015 & (publications > 700 | patents > 300)"))

