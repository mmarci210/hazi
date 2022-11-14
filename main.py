try:
    with open("hazi.txt",encoding="UTF-8") as my_file:
        tartalom = my_file.readlines()
    file1 = open("hz.txt", "w") 

    s = 2
    list = []
    nono = "aáeéoóöőuúüűií.:?!-_%="
    a =""
    for sor in tartalom:
        sor = sor.rstrip()
        if sor != "":
            s = s+1
            if s == 3:
                ##print(sor)
                list.append(sor)
                for x in sor:
                  if x not in nono:
                      a += x
                file1.write(a+"\n")
                s = 0
                print(a)
                a = ""


    file1.close()
    my_file.close()
except FileNotFoundError:
    print("Nem jó!")