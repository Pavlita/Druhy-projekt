import random

obsazena_pole = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

hracX = "X"
hracO = "O"

def vytiskni_hraci_plochu(obsazena_pole):
    print("+---+---+---+")
    print('| ' +obsazena_pole[0] + ' | ' + obsazena_pole[1] + ' | ' + obsazena_pole[2] + ' |')
    print("+---+---+---+")
    print('| ' +obsazena_pole[3] + ' | ' + obsazena_pole[4] + ' | ' + obsazena_pole[5] + ' |')
    print("+---+---+---+")
    print('| ' +obsazena_pole[6] + ' | ' + obsazena_pole[7] + ' | ' + obsazena_pole[8] + ' |')
    print("+---+---+---+")


def uloz_hracuv_tah(hrac, pole):
    if pole < 1 or pole > 9:
        print("==================================")
        print("Zadejte pozici 1-9")
        print("==================================")
        return False
    elif obsazena_pole[pole - 1] != " ":
        print("==================================")
        print("Pole je obsazeno .. ")
        return False
    else:
        obsazena_pole[pole - 1] = hrac
        return True


def zkontroluj_konec(obsazena_pole):
    for i in obsazena_pole:
        if i == " ":
            return False

    return True


def vypis_vitezstvi(obsazena_pole, hrac):
    print("==================================")
    vytiskni_hraci_plochu(obsazena_pole)
    print("==================================")
    print(f"Konec hry HRAC {hrac} vítězí !!!")
    print("==================================")


def zkontroluj_vyhru(obsazena_pole):
    if obsazena_pole[0] == obsazena_pole[1] == obsazena_pole[2] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[0])
        return True
    elif obsazena_pole[3] == obsazena_pole[4] == obsazena_pole[5] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[3])
        return True
    elif obsazena_pole[6] == obsazena_pole[7] == obsazena_pole[8] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[6])
        return True
    elif obsazena_pole[0] == obsazena_pole[3] == obsazena_pole[6] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[0])
        return True
    elif obsazena_pole[1] == obsazena_pole[4] == obsazena_pole[7] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[1])
        return True
    elif obsazena_pole[2] == obsazena_pole[5] == obsazena_pole[8] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[2])
        return True
    elif obsazena_pole[0] == obsazena_pole[4] == obsazena_pole[8] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[0])
        return True
    elif obsazena_pole[2] == obsazena_pole[4] == obsazena_pole[6] != " ":
        vypis_vitezstvi(obsazena_pole, obsazena_pole[2])
        return True
    else:
        return False



if __name__ == '__main__':
    # uvitani
    print("Vítej v tic-tac-toe!")
    print("===============================")
    print("PRAVIDLA HRY:")
    print("Každý hráč vybírá jedno místo")
    print("z hrací plochy 3x3. Vítězem se")
    print("stává ten, který první zkompletuje")
    print("3 své znaky v řadě:")
    print(" * horizontálně")
    print(" * vertikálně")
    print(" * diagonálně")
    print("Hrací pole mají tyhle čísla: ")
    obsazena_pole = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    vytiskni_hraci_plochu(obsazena_pole)

    print("===============================")
    print(" Hra začíná")
    print("-------------------------------")

    hrac = random.choice([hracO, hracX])
    obsazena_pole = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    while True:

        vytiskni_hraci_plochu(obsazena_pole)

        try:
            print("==================================")
            hracova_volba = int(input(f"HRAC {hrac} | zadej svoji volbu: "))
            print("==================================")
        except ValueError:
            print("==================================")
            print("!!! volba musi byt cislo 1-9 !!!")
            print("==================================")
            continue

        if uloz_hracuv_tah(hrac, hracova_volba):
            if zkontroluj_vyhru(obsazena_pole):
                break
            if zkontroluj_konec(obsazena_pole):
                vytiskni_hraci_plochu(obsazena_pole)
                print("==================================")
                print("Všechna pole jsou už obsazena - nikdo nevítězí.")
                print("==================================")

                break
            hrac = hracX if hrac == hracO else hracO
        else:
            print("Volba nemohla být použita ..")
            print("==================================")
