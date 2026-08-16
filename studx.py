gpa = []
count = 0
while usersdatas.lower() != 'q':

    usersdatas = input(f"class({count+1}):")
    for value in usersdatas.split():
        if value == "end":
            break
        usersdata = float(value)
        if 0 < usersdata <= 4.00:
            gpa.append(usersdata)
        else:
            print("invavid data")
    count += 1
