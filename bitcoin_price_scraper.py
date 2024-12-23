import yfinance as yf
from datetime import datetime  
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")  # Set the backend to TkAgg for interactive plotskAgg

# Define the Bitcoin ticker
btc_ticker = "BTC-USD"

# Set the start and end dates
start_date = "2014-09-17" #oldest data available for BTC-USD price on yahoo finance
end_date = datetime.today().strftime("%Y-%m-%d")  # Today's date in YYYY-MM-DD format

#end_date = "2023-12-21"  
print("End Date:", end_date)  

# Fetch historical data as dataframe
btc_data = yf.download(btc_ticker, start=start_date, end=end_date)

# Display the data
print(btc_data)

# Save to CSV (optional)
btc_data.to_csv("bitcoin_price_history.csv")



# Plot the closing price

import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use("seaborn-v0_8")

if not btc_data.empty:
    plt.figure(figsize=(12, 6))  # Set a larger figure size
    plt.plot(btc_data["Close"], label="Bitcoin Closing Price", color="dodgerblue", linewidth=2)

    # Add a title and axis labels
    plt.title("Bitcoin Price History", fontsize=16, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)

    # Rotate date labels for readability
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)

    # Add a grid
    plt.grid(visible=True, linestyle="--", linewidth=0.5)

    # Add a legend
    plt.legend(fontsize=12)

    # Show the plot
    plt.tight_layout()
    plt.show()
else:
    print("No data to plot!")