def biodata(tahun_lahir, namaku, asal):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahun_lahir
    print(f"Perkenalkan Nama Saya: {namaku}")
    print(f"Umur saya: {umur}")
    print(f"Saya adalah angkatan: {tahun_sekarang}")
    print(f"Asal saya dari: {asal}")
tahun_lahir = int(input())
namaku = input()
asal = input()
biodata(tahun_lahir, namaku, asal)