import random
def main():
    sayi = random.randint(1,100)
    hak = 5
    tahmin : int

    while hak > 0:
        hak = hak - 1
        tahmin = int(input("Tahmininizi giriniz : "))

        if sayi == tahmin:
            print("Tebrikler, bildiniz.")
            break

        if sayi > tahmin:
            print("yukarı")
        else:
            print("aşağı")

        if hak == 0:
            print(f"Hakkınız bitti. Tutulan sayı {sayi}.")
            break

if __name__ == "__main__"
    main()
