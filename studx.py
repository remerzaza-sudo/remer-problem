gpa = []
count = 0
usersdatas = ""
run = False
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
            gpa.append(usersdata)
        else:
            print("invavid data")

    count += 1
