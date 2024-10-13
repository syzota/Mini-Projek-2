def hitung():
    panjang = float(input("Masukkan panjang dari persegi panjang: "))
    lebar = float(input("Masukkan lebar dari persegi panjang: "))

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    if panjang > 0 and lebar > 0:
        print(f"Luasnya: {luas}")
        print(f"Kelilingnya: {keliling}")
    else:
        print("Nilai harus lebih dari 0.")

hitung()