# Setni yaratish, gulli qavslar yordamida setni o'qitish
numerliSet={1,2,3,4,5,6,7,8,9}
print(type(numerliSet),numerliSet)

#set() maxsus konstruktor yordamida yaratish
numerliSetkonstruktor=set([1,2,3,4,5,6,7])
print(numerliSetkonstruktor)
#DIQQAT set ni indeksi yo'q
# Setni listga aylantirish
numerliSetkonstruktor=list(numerliSetkonstruktor)
print(numerliSetkonstruktor)  #set listga aylandi
# setda bir xil elementlar bo'lmaydi
mevalar={"olma","olma", "anor","gilos", "olma","anor"}
print(mevalar)  # natija {'gilos', 'olma', 'anor'} chiqadi
#tekshirish setda tartib muhimmas
mevalar1={'gilos', 'olma', 'anor'}
mevalar={"olma","olma", "anor","gilos", "olma","anor"}
if mevalar==mevalar1:
    print('Teng')
else:
    print('Teng emas')
    