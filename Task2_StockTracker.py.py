def run_stock_tracker():
    # Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 140.0,
        "MSFT": 390.0,
        "AMZN": 170.0
    }
    
    portfolio = {}
    
    print("--- Stock Portfolio Tracker ---")
    print("Available stocks in system: AAPL, TSLA, GOOGL, MSFT, AMZN")
    
    # User inputs stock names and quantity
    while True:
        stock_name = input("\nEnter the stock ticker (or type 'done' to finish): ").upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print("Stock not found in our system. Please choose from the available list.")
            continue
            
        try:
            quantity = float(input(f"Enter the quantity of {stock_name} shares: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
                
            # Add to portfolio (or update if already entered)
            if stock_name in portfolio:
                portfolio[stock_name] += quantity
            else:
                portfolio[stock_name] = quantity
                
        except ValueError:
            print("Invalid input. Please enter a numerical value for quantity.")
            
    # Display total investment value
    total_investment = 0.0
    
    # Prepare the output text for both the console and the text file
    summary_text = "--- Your Portfolio Summary ---\n"
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_investment += value
        
        line_item = f"Stock: {stock} | Quantity: {qty} | Current Price: ${price} | Total Value: ${value}\n"
        summary_text += line_item
        
    final_total = f"\nGrand Total Investment Value: ${total_investment}"
    summary_text += final_total + "\n"
    
    # Print the summary to the console
    print(f"\n{summary_text}")
    
    # Save the result in a .txt file
    if portfolio:
        save_choice = input("Would you like to save this summary to a text file? (y/n): ").lower()
        if save_choice == 'y':
            try:
                with open("portfolio_summary.txt", "w") as file:
                    file.write(summary_text)
                print("Success! Your portfolio has been saved to 'portfolio_summary.txt'.")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    run_stock_tracker()