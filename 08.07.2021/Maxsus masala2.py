shaxslar = [
    {
        "ism": "Shoxzod",
        "yoshi": 20,
        "jinsi": "erkak"
    },
    {
        "ism": "Oybek",
        "yoshi": 22,
        "jinsi": "erkak"
    },
    {
        "ism": "Bunyod",
        "yoshi": 22,
        "jinsi": "erkak"
    },
    {
        "ism": "Madinabonu",
        "yoshi": 13,
        "jinsi": "ayol"
    }
]
for shaxs in shaxslar:
    if shaxs["jinsi"]=="erkak":
        print(shaxs["ism"])
shaxs.update({"manzili": "Jizzax", "tel": "+99 894 646 24 99"})
print(shaxs)