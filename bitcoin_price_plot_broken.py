import matplotlib.pyplot as plt

# Add moving averages
btc_data["SMA_30"] = btc_data["Close"].rolling(window=30).mean()
btc_data["SMA_90"] = btc_data["Close"].rolling(window=90).mean()

# Plot the data
if not btc_data.empty:
    plt.figure(figsize=(14, 7))  # Larger figure size
    plt.plot(btc_data["Close"], label="Bitcoin Closing Price", color="dodgerblue", linewidth=2)
    plt.plot(btc_data["SMA_30"], label="30-Day SMA", color="orange", linestyle="--", linewidth=2)
    plt.plot(btc_data["SMA_90"], label="90-Day SMA", color="green", linestyle="--", linewidth=2)

    # Add shading for volatility
    plt.fill_between(btc_data.index, btc_data["Low"], btc_data["High"], color="lightblue", alpha=0.2, label="Daily Range")

    # Highlight significant dates
    plt.axvline("2021-04-14", color="red", linestyle="--", label="BTC All-Time High")

    # Add labels, title, and legend
    plt.title("Bitcoin Price History", fontsize=18, fontweight='bold')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(fontsize=12)
    plt.grid(visible=True, linestyle="--", linewidth=0.5)

    # Show the plot
    plt.tight_layout()
    plt.show()
else:
    print("No data to plot!")