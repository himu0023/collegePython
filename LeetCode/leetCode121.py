def bestProfit(stock):
    max_profit = 0
    min_price = stock[0]

    for price in stock:
        profit = price - min_price 

        if profit > max_profit:
            max_profit = profit

        if price < min_price:
            min_price = price

    return max_profit

prices = [9,1,2,5,8,7]

money = bestProfit(prices)
print(f"maximun profit: {money}")