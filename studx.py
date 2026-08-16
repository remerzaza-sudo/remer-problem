rawgpa = []
count = 0
usersdatas = ""
run = False
print("Enter your GPA data (type 'n' to move to the next class or 'q' to quit):")
while not run:
    usersdatas = input(f"class({count+1}):")
    for value in usersdatas.split():
        if value == "q":
            run = True
            break
        elif value == "n":
            break
        usersdata = float(value)
        if 0 < usersdata <= 4.00:
            num = [value]
            rawgpa.append(num)
        else:
            print("invalid data")
    count += 1




    

