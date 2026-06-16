import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")

df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

yearly_sales = df.groupby("year")["sales"].sum()

print(yearly_sales)

yearly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Sales Trend by Year")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("images/sales_by_year.png")

print("Yearly sales chart saved!")

plt.show()