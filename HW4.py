class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int) -> dict:
        self.stock -= quantity
        if self.stock < 0:
            print("Ошибка, отрицательное количество товара на складе.")
            pass
        else:
            print(f"Количество незарезервированного товара {
                  self.name}, оставшегося на складе после заказа - {self.stock}")
            return self

    def __repr__(self) -> dict:
        return str(self.__dict__)


class Order:
    def __init__(self, products: dict):
        self.products = products

    def add_product(self, product: str, quantity: int) -> dict:
        global products_storage
        for i in range(0, len(products_storage)):
            if products_storage[i].name == product:
                if quantity <= int(products_storage[i].stock):
                    print(
                        f"Товар {product} успешно добавлен в заказ в количестве {quantity}")
                    a = {product: quantity}
                    return a
                else:
                    print(f"Недостаточно {product} на складе. Товар был добавлен в корзину в количестве {
                          products_storage[i].stock}")
                    a = {product: products_storage[i].stock}
                    return a
        print(f"Ошибка. Товара {product} не существует")
        pass

    def calculate_total(self) -> float:
        price_of_product = 0
        summ = 0
        global products_storage
        for i in range(0, len(self.products)):
            for name, amount in self.products.items():
                if name == products_storage[i].name:
                    price_of_product = int(amount) * \
                        float(products_storage[i].price)
                    summ += price_of_product
        print(f"Итоговая стоимость заказа - {summ}")
        return summ

    def remove_product(self, product: str, quantity: int) -> dict:
        for name, amount in self.products.items():
            if name == product:
                a = int(amount) - int(quantity)
                if a > 0:
                    self.products['amount'] = a
                    return self.products
                elif a == 0:
                    del self.products[name]
                    return self.products
                else:
                    print(
                        f"Указано неверное количество (можно удалить не более {amount}).")
                    del self.products[name]
                    print(f"Товар {name} был полностью удален.")
                    return self.products
        if product not in self.products.keys():
            print("Ошибка. Такого товара нет в корзине.")
            return self.products

    def return_product(self, product: str, quantity: int) -> dict:
        global products_storage
        for i in range(0, len(products_storage)):
            # print(products_storage[i].stock)
            if product == products_storage[i].name:
                new_amount = int(products_storage[i].stock) + int(quantity)
                products_storage[i].stock = new_amount
                # products_storage[i] = new_product_info
                print(f"Количество {product} вернулось на склад: {quantity}.")
        return products_storage

    def __repr__(self):
        return self

    def __str__(self):
        return str(self.products)


class Store:
    def __init__(self, products: list):
        self.products = products

    def add_product(self, product: str) -> dict:
        self.products.append(product)
        return self.products

    def list_products(self) -> None:
        print("Всего на складе содержится: ")
        for i in range(0, len(products_storage)):
            if int(products_storage[i].stock) > 0:
                print(f"Товар - {products_storage[i].name} стоимостью {
                      products_storage[i].price}, остаток на складе {products_storage[i].stock} единиц.")

    def create_order(self):
        new_order = {}
        try:
            i = int(
                input(print("Введите количество позиций, которое хотите добавить в заказ. ")))
            while i > 0:
                name = input(print("Введите товар: ")).capitalize()
                if name not in new_order.keys():
                    amount = int(input(print("Введите количество: ")))
                    new_order.update({name: amount})
                    i -= 1
                else:
                    amount = int(input(print(f"Товар {
                                 name} уже есть в списке, количество будет обновлено. Введите новое количество: ")))
                    new_order[name] = amount
                    i -= 1
        except:
            print("Ошибка ввода данных!")
        return new_order


products_storage = []
# Базовые товары
product1 = Product("Ноутбук", 1000.0, 3)
product2 = Product("Смартфон", 500.0, 10)

# Обновили количество товара
product1 = product1.update_stock(2)


# Это список всех имеющихся продуктов
products_storage.append(product1)
products_storage.append(product2)


store = Store(products_storage)

# Создали магазин с продуктами по умолчанию

# Добавляем новые товары в магазин и в список всего, что содержится:


def new_products() -> dict:
    global products_storage
    try:
        number = int(
            input(print("Введите количество позиций для добавления на склад")))
    except:
        print("Ошибка ввода количества.")
    names = []
    for i in range(0, len(products_storage)):
        names.append(products_storage[i].name)
    while number > 0:
        name = (input(print("Введите название товара: "))).capitalize()
        if name in names:
            for i in range(0, len(products_storage)):
                if name == products_storage[i].name:
                    stock = int(input(print(
                        f"Такой товар уже есть на складе, количество будет обновлено. \n Введите новое количество товара {name}: ")))
                    product_n = Product(
                        name, products_storage[i].price, products_storage[i].stock)
                    new_amount = int(products_storage[i].stock) - stock
                    product_update = product_n.update_stock(new_amount)
                    products_storage[i] = product_update
                    number -= 1
                    break
        else:
            new_product = Product(name, float(input(print("Введите цену товара: "))), int(
                input(print("Введите количество товара: "))))
            products_storage = store.add_product(new_product)
            number -= 1
            names.append(name)
    return products_storage


"""products_storage = new_products()"""

# Обновили магазин
"""store = Store(products_storage)"""

# Показали все товары в списке. Данная операция встроена в create_order для удобства, чтобы не дублировать - закомментирована
# show_products = store.list_products()

# Создали заказ
order = store.create_order()

# Проверили позиции в create_order на правильность создания заказа через add_product и скорректировали итоговый заказ:


def change_correct(order: dict) -> dict:
    global products_storage
    added_order = Order(order)
    try:
        global true_order
        print(true_order)
    except:
        true_order = {}
    new_order_updated = {}
    for name, amount in order.items():
        if name in true_order.keys():
            print(
                "Такой товар уже есть в корзине. Если вы ходите изменить количество - сперва удалите его.")
        else:
            new_position = added_order.add_product(name, amount)
            if new_position is not None:
                true_order.update(new_position)
                new_order_updated.update(new_position)
    return true_order, new_order_updated


try:
    result_ord = list(change_correct(order))
    true_order = result_ord[0]

    upd = result_ord[1]
except:
    pass

# Обновили заказ в корзине
updated_order = Order(true_order)

# Посчитали сумму верного заказа
total = updated_order.calculate_total()

# Соотнесли заказанные товары и товары на складе, выявили остатки на складе:


def check(new_order) -> dict:
    global products_storage
    for name, amount in new_order.items():
        for i in range(0, len(products_storage)):
            if name == products_storage[i].name:
                product_info = Product(name, float(
                    products_storage[i].price), int(products_storage[i].stock))
                product_info.update_stock(amount)
                products_storage[i] = product_info
    return products_storage


products_storage = check(true_order)

# Проверяем остатки на складе после заказа
store = Store(products_storage)
store.list_products()

# РЕАЛИЗАЦИЯ ДОП ФУНКЦИОНАЛА

# Удаляем товар из корзины


def order_del() -> list:
    try:
        i = int(
            input(print("Введите количество позиций, которое хотите удалить из корзины: ")))
    except:
        print("Неверно указано количество позиций.")
        pass
    back_to_store_products = {}
    removed_prod = {}
    global updated_order
    while i > 0:
        name_del = str(input(print(
            "Введите название товара, который хотите удалить из корзины: "))).capitalize()
        try:
            stock_del = int(input(print("Введите количество: ")))

        except:
            print("Неверно указано количество товара.")
            pass
        if name_del in true_order.keys():
            if stock_del <= true_order[name_del]:
                back_to_store_products.update({name_del: stock_del})
                removed_prod = updated_order.remove_product(
                    name_del, stock_del)  # обновленный заказ в order
                updated_order = Order(removed_prod)
                print(f"В вашей корзине остались товары: {removed_prod}")
                i -= 1
            else:
                back_to_store_products.update({name_del: true_order[name_del]})
                removed_prod = updated_order.remove_product(
                    name_del, stock_del)
                # обновленный заказ в order
                updated_order = Order(removed_prod)
                print(f"В вашей корзине остались товары: {removed_prod}")
                i -= 1
        else:
            print("Ошибка. Такого товара нет в корзине.")
            i -= 1

    return removed_prod, back_to_store_products


try:
    result = list(order_del())
    updated_order = result[0]
    back_to_store_products = result[1]
except:
    pass

# Обновили заказ в корзине после удаления
updated_order = Order(updated_order)


def order_back(back_to_store_products: dict) -> dict:
    for name, amount in back_to_store_products.items():
        updated_store = updated_order.return_product(name, amount)
    return updated_store


products_storage = order_back(back_to_store_products)

# Обновили магазин
updated_store = Store(products_storage)
store.list_products()


while True:
    command = input(print("Выберите действие: \n 1 - Проверить товары на складе. \n 2 - Посмотреть корзину. \n 3 - Добавить товары на склад. \n 4 - Добавить товары в заказ.  \n 5 - Удалить товары из заказа. \n 6 - Остановить цикл."))
    if command == '1':
        updated_store = Store(products_storage)
        updated_store.list_products()
    elif command == '2':
        order = Order(updated_order)
        print(order)
    elif command == '3':
        products_storage = new_products()
    elif command == '4':
        updated_store = Store(products_storage)
        order = updated_store.create_order()
        result_ord = list(change_correct(order))
        true_order = result_ord[0]
        upd = result_ord[1]
        updated_order = Order(true_order)
        total = updated_order.calculate_total()
        products_storage = check(upd)
    elif command == '5':
        try:
            result = list(order_del())
            updated_order = result[0]
            back_to_store_products = result[1]
        except:
            pass
        updated_order = Order(updated_order)
        products_storage = order_back(back_to_store_products)
    elif command == '6':
        break
    else:
        print("Неизвестная команда.")
