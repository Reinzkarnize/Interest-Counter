while True:
    # Penghitung Bunga

    print('=' * 35)
    print('Operasi Matematika')
    print('  1. Hitung Besar Bunga         [Rp]')
    print('  2. Hitung Persentase Bunga \t [%]')
    print('=' * 35)

    operasi = input('Pilih operasi (1/2): ')
    if operasi == '1':
        print('Menghitung besar bunga')
    if operasi == '2':
        print('Menghitung Persentase Bunga')

    if operasi == '1':
        tabungan = eval(input('Masukkan besar tabungan(Rp):'))
        persbunga = eval(input('Masukkan pensentase bunga(%):'))
    elif operasi == '2':
        bunga = eval(input('Masukkan bunga yang didapat(Rp):'))
        tabungan = eval(input('Masukkan besar tabungan(Rp):'))

    print('=' * 35)
    if operasi == '1':
        hasil = int(tabungan * persbunga / 100)
        print(f'Bunga yang di dapat adalah {hasil} Rupiah')
    if operasi == '2':
        hasil = bunga / tabungan * 100
        print(f'Persentase Bunga yang di dapat adalah {hasil} %')
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
