'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
# input 
harga_awal = 370000
diskon = 15

# code
harga_diskon = (diskon/100)*harga_awal
harga_akhir = harga_awal-harga_diskon
print(f'jumlah yang harus dibayar customer adalah {harga_akhir}')