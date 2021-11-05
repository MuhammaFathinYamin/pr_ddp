maksimal = int(input("Masukkan maks jumlah kebawah: "));
for kebawah in range (0,maksimal):
    for kesamping in range (0, kebawah+1):
        print("* ", end="")
    print("")