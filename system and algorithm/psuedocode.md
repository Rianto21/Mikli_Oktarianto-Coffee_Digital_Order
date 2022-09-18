STORE "belum_pesan" with string "y"
WHILE "belum_pesan" == "y"
  PRINT "SELAMAT DATANG DI JOCOFFEE KLIK APA SAJA UNTUKMELANJUTKAN"
  STORE "check" with STRING FROM INPUT "Apakah anda ingin memesan kopi? (y/n)"
  IF "check" == "y"
    STORE "daftar_pesanan" with LIST
    WHILE TRUE
      STORE "pesanan" with STRING FROM INPUT "Masukan Nama Menu: "
      ADD "pesanan" TO LIST"daftar_pesanan"
      PRINT "Pesanan berupa {pesanan} telah ditambahkan ke dalam daftar"
      STORE "lanjut_pesan" with STRING FROM INPUT "ingin memesan lagi? (y/n)"
      IF "lanjut_pesan" == "y"
        CONTINUE
      ELIF "lanjut_pesan == "n"
        PRINT "Terimakasih telah memesan berikut daftar pesanan anda {daftar_pesanan}"
        CLEAR LIST "daftar_pesanan"
        STORE "belum_pesan" with STRING "t"
        BREAK
      ELSE
        PRINT "Sistem Error Masukan Input dengan Benar!"
  ELSE
    CONTINUE