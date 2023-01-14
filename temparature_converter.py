print('Written By Hüseyin Berk Keskin')

def choice_celcius():
    celcius=int(input("Celcius cinsinden sicaklik giriniz: "))
    kelvin = float(273.15+celcius)
    fahrenheit = float((celcius*(9/5))+32)
    return "{} celcius sicakligi, {} kelvin'e ve {} fahrenheit'a esittir".format(celcius,kelvin,fahrenheit)


def choice_kelvin():
    kelvin=int(input("Kelvin cinsinden sicaklik giriniz: "))
    celcius = float(kelvin-273.15)
    fahrenheit = float(((kelvin-273.15)*(9/5))+32)
    return "{} kelvin sicakligi, {} celcius'a ve {} fahrenheit'a esittir".format(kelvin,celcius,fahrenheit)

def choice_fahrenheit():
    fahrenheit=int(input("Fahrenheit cinsinden sicaklik giriniz: "))
    kelvin = float((fahrenheit-32)*(9/5)+273.15)
    celcius = float((fahrenheit-32)*(9/5))
    return "{} fahrenheit sicakligi, {} kelvin'e ve {} celcius'a esittir".format(fahrenheit,kelvin,celcius)

while True:
    print("Cevirilecek sicaklik çeşininin numarasini yaziniz")
    print("1. Celcius")
    print("2. Kelvin")
    print("3. Fahrenheit")
    print("4. Exit")
    choice = input('Tip: ')

    if choice=='1' or choice==1 or choice=='1. Celcius' or choice=='celcius' or choice=='Celcius':
        print(choice_celcius())
    elif choice=='2' or choice==2 or choice=='2. Kelvin' or choice=='kelvin' or choice=='Kelvin':
        print(choice_kelvin())
    elif choice=='3' or choice==3 or choice=='3. Fahrenheit' or choice=='fahrenheit' or choice=='Fahrenheit':
        print(choice_fahrenheit())
    elif choice=='4' or choice==4 or choice=='4. Exit' or choice=='exit' or choice=='Exit':
        break
    else:
        print("Invalid choice.")