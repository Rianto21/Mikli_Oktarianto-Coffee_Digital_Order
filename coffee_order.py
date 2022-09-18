belum_pesan = 'y'
while belum_pesan == 'y':
  input("===============================\nSELAMAT DATANG DI JOCOFFEE\nKLIK APA SAJA UNTUK MELANJUTKAN\n===============================")
  check = input("Apakah anda ingin memesan kopi? (y/n)")
  if(check in('ya', 'yes', 'Ya', 'y', 'Y')):
    daftar_pesanan = []
    while True:
      pesanan = input("--------------\nMasukan nama menu: ")
      daftar_pesanan.append(pesanan)
      print(f"pesanan anda berupa {pesanan} sudah ditambahkan ke dalam daftar pesanan")
      lanjut_pesan = input("ingin memesan lagi? (y/n)")
      if(lanjut_pesan in('ya', 'yes', 'Ya', 'y', 'Y')): 
        continue
      elif(lanjut_pesan in('tidak', 'no', 'Tidak', 'No', 'n', 'N')):
        print(f"terimakasih telah memesan berikut adalah pesanan anda\n{', '.join(daftar_pesanan)}")
        daftar_pesanan.clear()
        belum_pesan = 'n'
        break
      else:
        input("sistem error silahkan tekan enter untuk melanjutkan")
  else:
    continue