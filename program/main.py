from datetime import date

RED = "\033[31m"
RESET = "\033[0m"
ascii_art = (r"""

          :::::::::  :::::::::::   :::::::::  :::::::::::  :::      :::            ::::::::::        :::::       :::    :::
         :+:    :+:     :+:      :+:     :+:     :+:      :+:      :+:            :+:     :+:      :+:   :+:    :+:    +;:
        +:+    +:+     +:+      +:+     +:+     +:+      +:+      +:+            +:+       7:+   +:+      7:+  :+;    +:/
       +#++:++#+      +#+      +#++:+#+:       +#+      :+#++::++#+:            +:+        +:7  +:##+::+##+:    ##++\:*
      +#+    +#+     +#+      +#+     +#+     +#+      +#+      +#+            +#+        +#?  +#+      7#+     +#+p
     #+#    #+#     #+#      ##:     #$:     #+$      #+#      #+#            #+#       #+#   #+#      #+#     #+#
    #########   ######$$:   ###     ##$     ##$      $##      $##            ##########$:    #$#      #$#     ##%

                    """)
print(ascii_art)

pre_month = 0
user = []
is_running = True
today = date.today()

def main():
    while is_running:
        raw = input("Enter name, years and mounth(q to quit): ")

        if raw.lower() == "q":
            break

        name, year, month = raw.split()
        if len(name) >= 12:
            print(f"{RED}username is greater than 12!{RESET}")
            continue
        elif year.isdigit() != True or year.isdecimal() != True:
            print(f"{RED}Year can't contain string sorry :( {RESET}")
            continue
        elif month.isdigit() != True:
            print(f"{RED}This program not support \"text\" in month sorry :({RESET}")
            continue


        year = int(year)
        month = int(month)


        age = today.year - year
        if month < today.month:
            pre_month = today.month - month

        elif month > today.month:
            age -=1
            pre_month = (today.month + 12) - month
        elif month == today.month:
            pre_month = month - today.month
            user.append({"name": name.lower(), "age": age, "pre_month": pre_month})

    for i in user:
        print(f"name:{i["name"]} age:{i["age"]} month:{i["pre_month"]}")


if __name__ == '__main__':
    main()
