from pymongo import MongoClient


client=MongoClient("mongodb://localhost:27017")
db=client["okul_yönetim"]
print("veritabani olusturuldu veya mevcutsa bağlanildi")

ogrenciler=db["ogrenciler"]
ogrenciler.delete_many({})
ogrenci={"ad":"nur","yas":21,"bolum":"yazilim muhendisliği"}
ogrenciler.insert_one(ogrenci)
for ogrenci in ogrenciler.find():
    print(ogrenci)
ogrenci_listesi=[
    {"ad":"Ali","yas":21,"bolum":"bilgisayar muhendisliği"},
    {"ad":"Ayşe","yas":22,"bolum":"elektrik muhendisliği"},
    {"ad":"Neşe","yas":22,"bolum":"yazilim muhendisliği"}
]
ogrenciler.insert_many(ogrenci_listesi)
print("ogrencilerin bilgileri".center(100,"-"))
for ogrenci in ogrenciler.find():
    print(ogrenci)
print("yasi 22 olan ogrenciler".center(100,"-"))
for ogrenci in ogrenciler.find({"yas":22}):
    print(ogrenci)
result=ogrenciler.find_one({"ad":"Ayşe"})
print("Ayşeye ait  bilgiler :")
print(result)
ogrenciler.update_one({"ad":"Ayşe"},{"$set":{"yas":24}})
print("ayşenin yaşi değiştirildi")
result=ogrenciler.find_one({"ad":"Ayşe"})
print("Ayşenin guncel bilgisi")
print(result)
ogrenciler.update_many({"bolum":"yazilim muhendisliği"},{"$set":{"yas":25}})
for ogrenci in ogrenciler.find():
    print(ogrenci)
print("yaslarin kucukten buyuge dogru sıralama")
for ogrenci in ogrenciler.find().sort("yas",1):
    print(ogrenci)
print("-"*100)
for ogrenci in ogrenciler.find().sort([("bolum",1),("yas",-1)]):
    print(ogrenci)
for ogrenci in ogrenciler.find().sort("yas",1).limit(2):
    print(ogrenci)

for  ogrenci in ogrenciler.find().sort("bolum",1).limit(3):
    print(ogrenci)
for ogrenci in ogrenciler.find({"ad":{"$regex":"^A"}}):
    print(ogrenci)
for ogrenci in ogrenciler.find({"ad":{"$regex":"e$"}}):
    print(ogrenci)
print("*"*100)
for ogrenci in ogrenciler.find({"bolum":{"$regex":"muhendisliği"}}):
    print(ogrenci)
for ogrenci in ogrenciler.find({"bolum":{"$regex":"yazilim"}}):
    print(ogrenci)

for ogrenci in ogrenciler.find({"ad":{"$regex":"ayşe","$options":"i"}}):
    print(ogrenci)
print("*"*100)
for ogrenci in ogrenciler.find({"ad":{"$regex":"^a","$options":"i"}}).sort("yas",-1).limit(3):
    print(ogrenci)
