storing =[]
velocitys = []
fuelperkilometer = []

distance = int(input("Distnace>"))
run =True
while run:
    raw = input("Fuel used, hour, minute>")
    if raw == "q":
        run = False
    else:
        fuel, h ,m = raw.split()
        storing.append(raw.split())

for i in storing:
    fuelrate = distance / int(i[0])
    # print(round(fuelrate, 2))
    fuelperkilometer.append(fuelrate)

for i in storing:
    meterdistance = distance * 1000
    time = (int(i[1]) * 3600) + (int(i[2]) * 60)
    velocity = (meterdistance / time) * 3.6
    # print(round(velocity,2))
    velocitys.append(velocity)

for car in range(len(storing)):
    print(f"Car({car}) {round(fuelperkilometer[car], 2)}km/l {round(velocitys[car],2)} Km/h")
  
