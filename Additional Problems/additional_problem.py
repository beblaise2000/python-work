import pandas as pd

# Given data
prices = [80, 88, 100, 90, 80, 65, 60, 50, 40, 35]
shares_short_scratchy = 100
initial_margin_requirement_scratchy = 1.5
maintenance_margin_requirement_scratchy = 1.3
shares_bought_itchy = 10
borrowed_amount_itchy = 400
initial_margin_requirement_itchy = 0.5
maintenance_margin_requirement_itchy = 0.3

# Part A: Scratchy's Short Position
def calculate_scratchy_margins(prices, shares_short, initial_margin_req, maintenance_margin_req):
    margin_account = []
    value_of_short_position = []
    maintenance_margin = []
    initial_margin_account = initial_margin_req * shares_short * prices[0]
    margin_account.append(initial_margin_account)
    
    for price in prices:
        short_position = shares_short * price
        maintenance_margin_needed = short_position * maintenance_margin_req
        value_of_short_position.append(short_position)
        maintenance_margin.append(maintenance_margin_needed)
        
        if margin_account[-1] < maintenance_margin_needed:
            margin_account.append(maintenance_margin_needed)
        else:
            margin_account.append(margin_account[-1] - (short_position - value_of_short_position[-1]))
    
    return pd.DataFrame({
        "Day": list(range(1, len(prices) + 1)),
        "Price": prices,
        "Value of Short Position": value_of_short_position,
        "Required Maintenance Margin": maintenance_margin,
        "Margin Account": margin_account[:-1]
    })

# Part B: Itchy's Position
def calculate_itchy_margins(prices, shares_bought, borrowed_amount, maintenance_margin_req):
    total_value_of_shares = []
    equity = []
    maintenance_margin = []
    
    for price in prices:
        total_value = shares_bought * price
        equity_value = total_value - borrowed_amount
        maintenance_margin_needed = total_value * maintenance_margin_req
        total_value_of_shares.append(total_value)
        equity.append(equity_value)
        maintenance_margin.append(maintenance_margin_needed)
    
    return pd.DataFrame({
        "Day": list(range(1, len(prices) + 1)),
        "Price": prices,
        "Total Value of Shares": total_value_of_shares,
        "Equity": equity,
        "Required Maintenance Margin": maintenance_margin
    })

# Calculating Scratchy's and Itchy's margins
scratchy_df = calculate_scratchy_margins(prices, shares_short_scratchy, initial_margin_requirement_scratchy, maintenance_margin_requirement_scratchy)
itchy_df = calculate_itchy_margins(prices, shares_bought_itchy, borrowed_amount_itchy, maintenance_margin_requirement_itchy)

print(scratchy_df)
print(itchy_df)

scratchy_df, itchy_df
