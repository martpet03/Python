class Medicine:
    def __init__(self, med_id, med_name, manufacturer, price, quantity):
        self.med_id = med_id
        self.med_name = med_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def Dislay(self):
        return f"{self.med_id} {self.med_name} {self.manufacturer} {self.price} {self.quantity}"

    def __repr__(self):
        return f"{self.med_id} {self.med_name} {self.manufacturer} {self.price} {self.quantity}"
    
    def Search_by_name(self, name):
            for x in med_list:
                if name == x.med_name:
                    print(x)

                
    def Sale(self, name, quantity):
        for x in med_list:
            if name == x.med_name and x.quantity > quantity:
                print(x.quantity - quantity)

    def Purchase(self, name, quantity):
        for x in med_list:
            if x.med_name == name:
                print(quantity + x.quantity) 

med_list = []

while True:
    med_id = int(input("Enter med_id: "))
    if med_id == 0:
        break
    med_name = input("Enter name: ")
    manufacturer = input("Enter manufacturer: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    med_list.append(Medicine(med_id, med_name, manufacturer, price, quantity))

def Sort_Meds(med_list):
    return sorted(med_list, key = lambda x:x.med_name, reverse = False)

def minimal_quantity_from_manufacturer(manufacturer, med_list):
    meds_from_manufacturer = [x for x in med_list if x.manufacturer == manufacturer]
    return min(meds_from_manufacturer, key=lambda x: x.quantity)

#def minimal_quantity_from_manufacturer(med_lis, manufacturer):
    #med_lis2 = (min(med_lis, key = lambda i : i.quantity))
    #for x in med_lis:
        #if manufacturer == x.manufacturer: 
            #print(med_lis2)
            #break
medicine = Medicine(med_list, "Aspirin")
medicine.Search_by_name()
'''for x in med_list:
    x.Search_by_name("Aspirin")
    break'''

for x in med_list:
    x.Sale("Aspirin", 2)
    break

for x in med_list:
    x.Purchase("Efizol", 5)
    break

print(Sort_Meds(med_list))

print(minimal_quantity_from_manufacturer("Bayer", med_list))
