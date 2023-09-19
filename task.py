def Choose():
    keep = True
    while keep:
        print("\n" + "1 - создать новый контакт; " 
              + "\n" + "2 - найти контакт;" 
              + "\n" + "3 - удалить контакт;" 
              + "\n" + "4 - изменить контакт (в процессе);" 
              + "\n" + "5 - вывести все контакты;" 
              + "\n" + "6 - выход;")
        
        choice = input("выберите действие: ")
        print()
        if choice == '1': New_Contact()
        elif choice == '2': Search_Contact()
        elif choice == '3': Delete_Contact()
        elif choice == '4': Change_Contact()
        elif choice == '5': Print_Contact()
        elif choice == '6': 
            keep = False
            print("до свидания.")
        else:
            print("это не вариант. поробуйте снова")



## 1 ++
def New_Contact (list_name = "phones.txt"):
    with open(list_name, 'a', encoding="UTF-8") as telephone_list:
        print("для того, чтобы добавить контакт:")
        surname = input("введите фамилию: ")
        name = input("введите имя: ")
        patronym = input("введите отчество: ")
        number = input("введите номер телефона: ")
     
        telephone_list.write(surname + ' ' + name + ' ' + patronym + ',    ' + number + '\n')
        print("\n"+"успешно добавлено." + "\n" +"возращаемся в меню.")



## 2 ++
def Search_Contact(list_name = "phones.txt"):
    with open(list_name, 'r', encoding="UTF-8") as telephone_list:
        print("введите информацию человека, которого хотите найти: ")
        surname = input("введите фамилию: ")
        name = input("введите имя: ")
        
        print()
        found = 0
        lines = telephone_list.readlines()

        for line in lines:
            splitted = line.split()
            if (surname == splitted[0] and name == splitted[1] ):
                print("мы его нашли: ")
                print(line)
                found = 1 

        if found == 1: 
            print("ура. "+ "\n" +"возращаемся в меню.")           
        else: 
            print("о нет. такого контакта не существует."+ "\n" +"возращаемся в меню.")



## 3 +
def Delete_Contact(list_name = "phones.txt"):
    print("введите информацию человека, контакт которого хотите удалить: ")

    surname = input("введите фамилию: ")
    name = input("введите имя: ")
    patronym = input("введите отчество: ")

    print()
    counter = 0

    with open(list_name, 'r', encoding='UTF-8') as telephone_list:
        lines = telephone_list.readlines()
        for line in lines:
            splitted = line.split()
            if (surname == splitted[0] and name == splitted[1] and (patronym in splitted[2])):
                counter += 1
    if counter == 0:
        print("таких не найдено."+ "\n" +"возращаемся в меню.")
    elif counter == 1:
        with open(list_name, 'w', encoding='UTF-8') as telephone_list:
            for line in lines:
                splitted = line.split()
                if (surname == splitted[0] and name == splitted[1] and (patronym in splitted[2])):
                    print("успешно удалено. ура."+ "\n" +"возращаемся в меню." + "\n")
                else:
                    telephone_list.write(line)          
    else:
            print("\n" +"о нет. их целых " , counter , ". мы не знаем, что делать." + "\n" +"возращаемся в меню."+ "\n")
            


## 4 +
def Change_Contact(list_name = "phones.txt"):
    print("введите информацию человека, контакт которого хотите изменить: " + "\n")
    surname = input("введите фамилию: ")
    name = input("введите имя: ")
    print()
    counter = 0

    with open(list_name, 'r', encoding='UTF-8') as telephone_list:
        lines = telephone_list.readlines()
        for line in lines:
            splitted = line.split()
            if (surname == splitted[0] and name == splitted[1]):
                counter += 1
    if counter == 0:
        print("таких не найдено."+ "\n" +"возращаемся в меню."+ "\n")
    elif counter == 1:
        with open(list_name, 'w', encoding='UTF-8') as telephone_list:
            for line in lines:
                splitted = line.split()
                if (surname == splitted[0] and name == splitted[1]):
                    print("\n" + "человечек найден." + "\n" + "старая информация: ")
                    print(line)
                    print()
                    new_surname = input("введите новую фамилию: ")
                    new_name = input("введите новое имя: ")
                    new_patronym = input("введите новое отчество: ")
                    new_number = input("введите новый номер: ")
                    line = (new_surname + ' ' + new_name + ' ' + new_patronym + ',    ' + new_number + '\n')
                    telephone_list.write(line)
                    print("\n" + "успешно изменено. ура." + "\n" "возращаемся в меню." + "\n")
                else:
                    telephone_list.write(line)
    else:
        print("\n" +"о нет. их целых " , counter , ". мы не знаем, что делать." + "\n" +"возращаемся в меню."+ "\n")

        

## 5 +
def Print_Contact(list_name = "phones.txt"):
    with open(list_name, 'r', encoding="UTF-8") as telephone_list:
        lines = telephone_list.readlines()

        for i in lines:
            print(i, end = ' ')
    print("возращаемся в меню.")
# -------------------------------------------------------


Choose()



