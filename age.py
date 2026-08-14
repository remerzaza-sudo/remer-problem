from datetime import date
storageData = []
storageYear = []
storageMonth = []
names = []

resultage = []
resultmonth = []

yearnow = date.today().year
monthnow = date.today().month

#asking user to get userdata
i = 0
while i < 5:
    rawdata = input("Enter name, year, month>")
    if rawdata == "q":
        run = False
    else:
        i+=1
    name, year, month = rawdata.split()
    storageYear.append(int(year))
    storageMonth.append(int(month))
    names.append(name)

for Yearborn, monthborn in zip(storageYear, storageMonth):
    userage = yearnow - Yearborn
    resultage.append(userage)

    if monthborn <= monthnow:
        monthage = monthnow - monthborn
    else:
        monthage = (monthnow + 12) - monthborn
    resultmonth.append(monthage)

    
for name,year,month in zip(names, resultage, resultmonth):
    print(f"{name} {year:^5} {month:^5}")


#all day made by resper!

    



    


