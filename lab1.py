class Table:
    def __init__(self, inventory_number, price, material, color):
        self.inventory_number = inventory_number
        self.price = price
        self.material = material
        self.color = color

    def change_inventory_number(self, new_inventory_number):
        self.inventory_number = new_inventory_number
        print(f"Інвентарний номер змінено на: {self.inventory_number}")

    def change_price(self, new_price):
        self.price = new_price
        print(f"Ціна змінена на: {self.price}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f'Інвентарний номер: {self.inventory_number}\n')
            file.write(f'Ціна: {self.price}\n')
            file.write(f'Матеріал: {self.material}\n')
            file.write(f'Колір: {self.color}\n')
        print(f"Дані столу збережено у файлі: {filename}")

def create_table():
    inventory_number = input("Введіть інвентарний номер: ")
    price = float(input("Введіть ціну: "))
    material = input("Введіть матеріал: ")
    color = input("Введіть колір: ")
    return Table(inventory_number, price, material, color)

def main():
    filename = 'tables.txt'

    table1 = create_table()
    table1.save_to_file(filename)

    new_inventory_number = input("Введіть новий інвентарний номер: ")
    table1.change_inventory_number(new_inventory_number)

    new_price = float(input("Введіть нову ціну: "))
    table1.change_price(new_price)

    table1.save_to_file(filename)

if __name__ == "__main__":
    main()
