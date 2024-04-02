# Defining stocks at given times with a tuple
stock_prices = [
        ('09:00', 100.00),
        ('09:30', 102.50),
        ('10:00', 105.25),
        ('10:30', 103.75),
        ('11:00', 101.80),
        ('11:30', 99.50),
        ('12:00', 98.00)
        ]   

# Defining a function
def analyze_stocks(stock_prices):
    
    # Creating new objects
    highest_price = float('-inf')
    lowest_price = float('inf')
    total_price = 0
    start_time = None
    end_time = None
    
    for time, price in stock_prices:
        # Check for highest price
        if price > highest_price:
            highest_price = price
            highest_time = time

        # Check for lowest price
        if price < lowest_price:
            lowest_price = price
            lowest_time = time

        # Update total price
        total_price += price

        # Update start and end time
        if start_time is None:
            start_time = time
        end_time = time

    # Calculate average price
    average_price = total_price / len(stock_prices)

    # Calculate total trading duration
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    total_trading_hours = end_hour - start_hour + (end_minute - start_minute) / 60

    # Print results
    print("Highest Price: ${:.2f} at {}".format(highest_price, highest_time))
    print("Lowest Price: ${:.2f} at {}".format(lowest_price, lowest_time))
    print("Average Price: ${:.2f}".format(average_price))
    print("Total Trading Duration: {:.2f} hours".format(total_trading_hours))
    
# Calling the analyze_stocks function
analyze_stocks(stock_prices)