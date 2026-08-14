storagePrice = []
percent = [70, 50, 30]
priceoffs = []

run = True

while run:
    price = input("price before off>")
    if price == 'q':
        run = False

    else:
        storagePrice.append(price)
print()

for prices in storagePrice:
    prices01 = int(prices) / 100
    print(f"{prices}", end=" ")
    for percents in percent:
        priceoff = prices01 * (100 - percents)
        print(f"{round(priceoff)}$",end=" ")
    print() 


 #appox. 1 hour
