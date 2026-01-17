import matplotlib.pyplot as plt
import numpy as np

# ---------------- New Sales Data ----------------
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
products = ['Product W', 'Product X', 'Product Y', 'Product Z']
regions = ['North', 'South', 'East', 'West']

# Generate random sales data for each product by quarter
np.random.seed(456)  # Different seed for new data
sales_data = np.random.randint(15000, 60000, (len(products), len(quarters)))

# Regional market share (new random percentages summing to 100)
market_share = np.array([30, 30, 25, 15])

# Customer age distribution (new random numbers)
age_groups = ['18-25', '26-35', '36-45', '46-55', '55+']
customers = np.random.randint(100, 400, len(age_groups))

# Price vs Sales correlation (new random values)
prices = np.array([30, 50, 70, 90])
units_sold = np.array([4200, 3100, 2200, 800])

# ---------------- Plotting ----------------
fig, axes = plt.subplots(3, 3, figsize=(20, 14))
markers = ['o', 's', '^', 'D']
colors = ['purple', 'teal', 'brown', 'pink']

# 1. Line plot - Quarterly sales for all products
for i, product in enumerate(products):
    axes[0,0].plot(quarters, sales_data[i],
                   marker=markers[i], color=colors[i],
                   linewidth=2, markersize=6, label=product)
axes[0,0].set_title('Quarterly Sales Trend', fontsize=14, fontweight='bold')
axes[0,0].set_xlabel('Quarters', fontsize=12)
axes[0,0].set_ylabel('Sales ($)', fontsize=12)
axes[0,0].legend(fontsize=10)
axes[0,0].grid(True)

# 2. Bar chart - Total sales per product
axes[0,1].set_title("Total Sales by Product", fontsize=14, fontweight='bold')
axes[0,1].set_xlabel("Product Names", fontsize=12)
axes[0,1].set_ylabel("Total Sales ($)", fontsize=12)
total_sales = np.sum(sales_data, axis=1)
bars = axes[0,1].bar(products, total_sales, color=colors)
for bar in bars:
    height = bar.get_height()
    axes[0,1].text(bar.get_x() + bar.get_width()/2., height + 1000,
                   f'${height:,.0f}', ha='center', va='bottom', fontsize=9)
axes[0,1].grid(axis='y', alpha=0.3)

# 3. Pie chart - Regional market share
axes[0,2].set_title("Regional Market Share", fontsize=14, fontweight='bold')
max_share_idx = np.argmax(market_share)
explode = [0, 0, 0, 0]
explode[max_share_idx] = 0.1
axes[0,2].pie(market_share, labels=regions, explode=explode,
              autopct='%1.1f%%', shadow=True, labeldistance=1.05)

# 4. Customer age distribution
axes[1,0].set_title("Customer Age Distribution", fontsize=14, fontweight='bold')
axes[1,0].set_xlabel("Age Groups", fontsize=12)
axes[1,0].set_ylabel("Number of Customers", fontsize=12)
axes[1,0].bar(age_groups, customers, color='lightgreen')
axes[1,0].grid(axis='y', alpha=0.3)

# 5. Scatter plot - Price vs Units Sold
axes[1,1].set_title("Price vs Sales Correlation", fontsize=14, fontweight='bold')
axes[1,1].set_xlabel("Price ($)", fontsize=12)
axes[1,1].set_ylabel("Units Sold", fontsize=12)
for i, product in enumerate(products):
    axes[1,1].scatter(prices[i], units_sold[i], color=colors[i], s=100, label=product)
slope, intercept = np.polyfit(prices, units_sold, 1)
trend_line = slope * np.array(prices) + intercept
axes[1,1].plot(prices, trend_line, color='red', linestyle='--', linewidth=2, label='Trend Line')
axes[1,1].legend(fontsize=10)
axes[1,1].grid(True)

# 6. Horizontal bar chart - Product performance
axes[1,2].set_title("Product Performance Ranking", fontsize=14, fontweight='bold')
axes[1,2].set_xlabel("Total Sales ($)", fontsize=12)
axes[1,2].set_ylabel("Products", fontsize=12)
bars = axes[1,2].barh(products, total_sales, color=colors)
for bar in bars:
    width = bar.get_width()
    axes[1,2].text(width + 500, bar.get_y() + bar.get_height()/2,
                   f'${width:,.0f}', ha='left', va='center', fontsize=9)
axes[1,2].grid(axis='x', alpha=0.3)

# 7. Creative empty subplots
creative_texts = ['Future Growth', 'Market Insights', '2026 Projections']
for j, text in enumerate(creative_texts):
    axes[2,j].text(0.5, 0.5, text, ha='center', va='center', fontsize=14, style='italic',
                   transform=axes[2,j].transAxes)
    axes[2,j].set_facecolor('lightgray')

# 8. Main title
fig.suptitle("Annual Sales Report 2025", fontsize=20, fontweight='bold', y=0.98)

# 9. Layout adjustments
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.tight_layout(pad=3.0, w_pad=2.0, h_pad=2.0)

# 10. Save and show
plt.savefig('sales_report_clone.png', dpi=300, bbox_inches='tight')
plt.show()


