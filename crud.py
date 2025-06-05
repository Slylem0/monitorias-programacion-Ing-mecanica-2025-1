#clase 1 // 5/06/25
#pablo nicolas marin 2459440
#Ing industrial

#Un CRUD se define en Create - Read - Update - Delate

#imaginemos que tenemos que hacer un programa para Univalle, donde se tengan que guardar estudiantes con los siguientes datos
#Nombre, codigo, promedio}

estudiantes = []
student = []

def main():
    x = True
    while(x):
        print("Welcome dear user, this is a CRUD of Univalle :D, select the options ")
        print("1.Create User \n2.Show users\n3.Update User\n4.Delate user\n5.Exit")
        option = int(input(":"))
        if option == 1:
            create()
        if option == 2:
            read()
        if option == 3:
            update()
        if option == 4:
            pass
        if option == 5:
            x = False
        else:
            print("Please select a valid option")
        
        

def create():
    name = str(input("Pls write ur name: "))
    student.append(name)
    code = int(input("pls digit ur code: "))
    student.append(code)
    average = float(input("pls digit ur average: "))
    student.append(average)
    print("\n")
    estudiantes.append(student.copy())
    student.clear()


def read():
    for i in range(len(estudiantes)):
        print("______________________")
        print("Student #" + str(i+1))
        for j in range(0,3):
            print(estudiantes[i][j])
        print("______________________")

def update():
    for i in range(len(estudiantes)):
        print("______________________")
        print("Student #" + str(i+1))
        for j in range(0,3):
            print(estudiantes[i][j])
        print("______________________")

    print ("Wich user u want to modificate: ")
    pos = int(input(":"))
    name = str(input("Pls write the new name of the user : "))
    student.append(name)
    code = int(input("pls digit the new code: "))
    student.append(code)
    average = float(input("pls digit the new  average: "))
    student.append(average)
    print("\n")

    estudiantes[pos-1]= (student.copy())
    student.clear()


if __name__ == "__main__":
    main()

