from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14 Pro Max", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79987654321"),
    Smartphone("Xiaomi", "Redmi Note 11S", "+79112233445"),
    Smartphone("Huawei", "P50 Pro", "+79556677889"),
    Smartphone("OnePlus", "10T", "+79445566778")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")