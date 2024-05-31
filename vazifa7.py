# import qrcode
# import random
# import string

# def qr_kod_chiqarish(uzunlik=8):
#     harflar = string.ascii_letters + string.digits
#     return ''.join(random.choice(harflar) 
#     for _ in range(uzunlik))

# def qr_kod_generatsiya():
#     satr = qr_kod_chiqarish()
#     link = f"https://github.com/{satr}"
    
#     fayl_nomi = f"{satr}.png"
    
#     img = qrcode.make(link)
#     img.save(fayl_nomi)
    
#     return link, fayl_nomi
# link, fayl_nomi = qr_kod_generatsiya()
# print(f"Link: {link}")
# print(f"Fayl nomi: {fayl_nomi}")

