def calculate_stock(n):
    stock = 1024
    stocks = [stock]
    for week in range(2, n + 2):
        stock -= (20 + week)
        if week % 4 == 0:
            stock += 500
        stocks.append(stock)
    return stocks

def display_stock_forecast(n):
    stocks = calculate_stock(n)
    for week in range(1, n + 1):
        print(f"Semaine {week} : stock {stocks[week - 1]}")
    print("\na. Prévisions de stock")
    print("b. Stock maximal")
    print("(q pour quitter)")

def find_max_stock(n):
    stocks = calculate_stock(n)
    max_stock = max(stocks)
    week_max_stock = stocks.index(max_stock)
    return max_stock, week_max_stock

def main():
    print("a. Prévisions de stock")
    print("b. Stock maximal")
    print("(q pour quitter)")
    
    while True:
        choice = input().strip().lower()

        if choice == 'q':
            break
        elif choice == 'a':
            try:
                n = int(input("Choisissez une semaine : "))
                display_stock_forecast(n)
            except ValueError:
                print("Veuillez entrer un numéro de semaine valide.")
        elif choice == 'b':
            try:
                n = int(input("Choisissez une semaine : "))
                max_stock, week_max_stock = find_max_stock(n)
                print(f"Stock max égal à {max_stock} , atteint en semaine {week_max_stock + 1}")
                print("\na. Prévisions de stock")
                print("b. Stock maximal")
                print("(q pour quitter)")
            except ValueError:
                print("Veuillez entrer un numéro de semaine valide.")
        else:
            print("Choix incorrect, recommencez")

if __name__ == "__main__":
    main()