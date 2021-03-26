# Syarat Mendaftar Kursus Online
print("Berapa Usia Anda?")
usia = int(input())
if usia >= 21:
    print("Apakah anda sudah lulus ujian kualifikasi (Y/T)")
    kualifikasi = input()
    if kualifikasi == "Y":
        print("Anda dapat mendaftar di kursus")
    else:
        print("Anda tidak dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")



