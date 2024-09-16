import time
import datetime
import math
import sys

wktu = datetime.datetime.now()

def loading_animation(duration):
    start_time = time.time()
    dots = [".", "..", "..."]
    
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            break
        
        for dot in dots:
            print(f"\rLoading{dot}", end='', flush=True)
            time.sleep(0.5)
        
        print("\rLoading   ", end='', flush=True)
        time.sleep(0.1)

    print("\r" + " " * 10, end='', flush=True)
    print("\r", end='', flush=True)

def print_menu():
    print("\n=== Kalkulator Sederhana ===")
    print(f"[ Halo [{nama}], {wktu}] ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Akar Kuadrat")
    print("6. Eksponen")
    print("7. Logaritma")
    print("8. Keluar")
    print("=============================")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error!\nPembagian dengan 0 tidak diperbolehkan."

def sqrt(x):
    return math.sqrt(x)

def exponent(x, y):
    return math.pow(x, y)

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error!\nNilai logaritma tidak valid."

def calculator():
    while True:
        print_menu()
        choice = input("Pilih operasi ([1][2][3][4][5][6][7][8]): ").strip()

        if choice == '8':
            return

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
            except ValueError:
                print("Harap masukkan angka yang benar.")
                continue

        if choice == '1':
            print(f"Hasil: {add(num1, num2)}")
        elif choice == '2':
            print(f"Hasil: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Hasil: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Hasil: {divide(num1, num2)}")
        elif choice == '5':
            try:
                num = float(input("Masukkan Angka: "))
                print(f"Hasil: {sqrt(num)}")
            except ValueError:
                print("Harap masukkan angka yang benar.")
                continue
        elif choice == '6':
            try:
                base = float(input("Masukkan ANgka: "))
                exponent_value = float(input("Masukkan Eksponen: "))
                print(f"Hasil: {exponent(base, exponent_value)}")
            except ValueError:
                print("Harap masukkan angka yang benar.")
                continue
        elif choice == '7':
            try:
                num = float(input("Masukkan Angka: "))
                base = float(input("Masukkan Logaritma: "))
                print(f"Hasil: {logarithm(num, base)}")
            except ValueError:
                print("Harap masukkan angka yang benar.")
                continue
        else:
            print("Silakan coba lagi.")
            continue

def balik(nama):
    while True:
        print(f"{nama}, Apakah Anda yakin ingin keluar?\n")
        pilih = input("Y/N: ").strip().lower()

        if pilih == 'y':
            sys.exit()
        elif pilih == 'n':
            break
        else:
            print("Harap masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    loading_animation(6)
    nama = input("Silahkan Masukkan Nama : ")
    print(f"\rSelamat Datang {nama}!")
    time.sleep(2)
    
    while True:
        calculator()
        balik(nama)