import random

# Menghasilkan angka acak antara 1 dan 100
angka_acak = random.randint(1, 100)

# Menerima input dari pengguna dan menangani yang valid
def terima_tebak():
    while True:
        try:
            tebak = int(input("Tebak angka (1-100): "))
            if tebak < 1 or tebak > 100:
                print("Mohon masukkan angka antara 1 dan 100.")
            else:
                return tebak
        except ValueError:
            print("Mohon masukkan angka yang valid.")

# Memeriksa apakah angka yang ditebak pengguna benar, terlalu tinggi, atau terlalu rendah
tebak = terima_tebak()
while tebak != angka_acak:
    if tebak > angka_acak:
        print("terlalu tinggi")
    else:
        print("terlalu rendah")
    tebak = int(input("tebak lagi lah: "))

# menebak kembali jika angka benar
print("Tebakan lu benar bre! Angka yang lu tebak adalah", angka_acak)
