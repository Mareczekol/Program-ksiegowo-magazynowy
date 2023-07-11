account = 0
magazyn = {}
actions = []

while True:
    print("Dostepne opcje:")
    print("saldo")
    print("sprzedaz")
    print("zakup")
    print("konto")
    print("lista")
    print("magazyn")
    print("przeglad")
    print("koniec")

    command = input("Wybierz opcje: ")
# tworzenie salda ( dodawanie i odejmowanie podanej wartości)
    if command == "saldo":
        amount = float(input("Wprowadz kwote: "))
        if amount < 0 and abs(amount) > account:
            print("Nie można odjąć więcej niż jest na koncie")
        else:
            account += amount
            actions.append(("saldo", amount))
            print("Saldo zaktualizowane")

# komenda sprzedaż
    elif command == "sprzedaz":
        product_name = input("Wprowadz nazwe produktu: ")
        price = int(input("Wprowadz cene: "))
        quantity = int(input("Wprowadz ilosc: "))
        if product_name not in magazyn:
            print("Brak produktu w magazynie")
        elif price <= 0 or quantity <= 0:
            print("Podaj prawidłową cenę i ilość")
        elif magazyn[product_name][1] < quantity:
            print("Nie ma wystarczającej ilości produktu w magazynie")
        else:
            account += price * quantity
            magazyn[product_name][1] -= quantity
            actions.append(("sprzedaz", product_name, price, quantity))
            print("Sprzedaz wykonana")

# komenda zakup
    elif command == "zakup":
        product_name = input("Wprowadz nazwe produktu: ")
        price = int(input("Wprowadz cene: "))
        quantity = int(input("Wprowadz ilosc: "))
        if price <= 0 or quantity <= 0:
            print("Nieprawidłowa cena lub ilosc")
        elif account < price * quantity:
            print("Nie wystarczające środki na koncie")
        else:
            if product_name not in magazyn:
                magazyn[product_name] = [price, quantity]
            else:
                magazyn[product_name][1] += quantity
            account -= price * quantity
            actions.append(("zakup", product_name, price, quantity))
            print("Zakup wykonany")

# wyswietlanie stanu konta
    elif command == "konto":
        print(f"Stan konta: {account}")
# komenda lista
    elif command == "lista":
        print("Stan magazynu:")
        # wyświetlanie stanu magazynu
        for product, details in magazyn.items():
            print(f"Produkt: {product}, Cena: {details[0]}, "
                  f"Ilosc: {details[1]}")
# komenda magazyn
    elif command == "magazyn":
        product_name = input("Wprowadz nazwe produktu: ")
        # jesli jest w magazynie to pokaz nazwe, cene i ilosc
        if product_name in magazyn:
            print(f"Produkt: {product_name}, Cena: {magazyn[product_name][0]}, "
                  f"Ilosc: {magazyn[product_name][1]}")
        else:
            print("Brak produktu w magazynie")

