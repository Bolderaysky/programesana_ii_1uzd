from statistics import mean 

Admin = []
Viesis = []

if __name__ == "__main__":
    AdminFile = open("admin.txt", "r")
    tmp = AdminFile.readlines()
    AdminFile.close()

    for i in range(len(tmp)):
        Admin.append(tmp[i].split(";"))
        Admin[i][3] = int(Admin[i][3].rstrip("\n"))


    ViesisFile = open("viesis.txt", "r")
    tmp = ViesisFile.readlines()
    ViesisFile.close()

    for i in range(len(tmp)):
        Viesis.append(tmp[i].split(";"))
        Viesis[i][3] = int(Viesis[i][3].rstrip("\n"))

    tmp = []

    for i in range(len(Admin)):
        tmp.append(Admin[i][3])

    AverageAge = mean(tmp)
    MinAge = min(tmp)
    MaxAge = max(tmp)

    print(f"""
------------------------------------------------
Average administrator's age is {round(AverageAge, 2)}
The youngest administrator is {MinAge} years old
The elder administrator is {MaxAge} years old

Count of administrators is {len(Admin)}
Count of guests is {len(Viesis)}
------------------------------------------------""")

    print(*(Admin + Viesis), sep = "\n")