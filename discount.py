def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount_percent)
        
        if final_price == price:
            print(f"No discount applied. Final price: ${final_price}")
        else:
            print(f"Final price after applying {discount_percent}% discount: ${final_price}")
    
    except ValueError:
        print("Please enter valid numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()



   