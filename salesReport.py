import matplotlib.pyplot as plt
import numpy as np

# Generate sample sales data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
products = ['Product A', 'Product B', 'Product C', 'Product D']
regions = ['North', 'South', 'East', 'West']

# Sales data for each product by quarter
np.random.seed(123)
sales_data = np.random.randint(10000, 50000, (len(products), len(quarters)))

# Regional market share
market_share = np.array([35, 25, 20, 20])

# Customer age distribution
age_groups = ['18-25', '26-35', '36-45', '46-55', '55+']
customers = np.array([120, 350, 280, 150, 100])

# Price vs Sales correlation
prices = np.array([25, 40, 60, 80])
units_sold = np.array([4500, 3200, 1800, 900])

# Create figure with 3 rows and 3 columns using subplots - increased size
fig, axes = plt.subplots(3, 3, figsize=(20, 14))

# Define different markers and colors for each product
markers = ['o', 's', '^', 'D']  # circle, square, triangle, diamond
colors = ['blue', 'red', 'green', 'orange']

# 1. Position 0,0: Line plot - Quarterly sales for all products
for i, product in enumerate(products):
    axes[0,0].plot(quarters, sales_data[i], 
                   marker=markers[i], 
                   color=colors[i], 
                   linewidth=2,
                   markersize=6,
                   label=product)

axes[0,0].set_title('Quarterly Sales Trend', fontsize=14, fontweight='bold')
axes[0,0].set_xlabel('Quarters', fontsize=12)
axes[0,0].set_ylabel('Sales ($)', fontsize=12)
axes[0,0].legend(fontsize=10)  # Smaller legend font
axes[0,0].grid(True)

# 2. Position 0,1: Bar chart - Total sales per product
axes[0,1].set_title("Total Sales by Product", fontsize=14, fontweight='bold')
axes[0,1].set_xlabel("Product Names", fontsize=12)
axes[0,1].set_ylabel("Total Sales ($)", fontsize=12)

# Calculate total sales for each product (sum across quarters)
total_sales = np.sum(sales_data, axis=1)

# Create bar chart
bars = axes[0,1].bar(products, total_sales, color=colors)

# Add value labels on top of each bar with adjusted positioning
for bar in bars:
    height = bar.get_height()
    axes[0,1].text(bar.get_x() + bar.get_width()/2., height + 1000,  # Moved up slightly
                  f'${height:,.0f}',
                  ha='center', va='bottom', fontsize=9)  # Smaller font

axes[0,1].grid(axis='y', alpha=0.3)

# 3. Position 0,2: Pie chart - Regional market share
axes[0,2].set_title("Regional Market Share", fontsize=14, fontweight='bold')
max_market_share = np.argmax(market_share)
explode = [0, 0, 0, 0]
explode[max_market_share] = 0.1

# Create pie chart with adjusted label distance
axes[0,2].pie(market_share, labels=regions, explode=explode, autopct='%1.1f%%', 
              shadow=True, labeldistance=1.05)  # Increased label distance

# 4. Position 1,0: Bar chart - Customer age distribution
axes[1,0].set_title("Customer Age Distribution", fontsize=14, fontweight='bold')
axes[1,0].set_xlabel("Age Groups", fontsize=12)
axes[1,0].set_ylabel("Number of Customers", fontsize=12)
axes[1,0].bar(age_groups, customers, color='lightblue')
axes[1,0].grid(axis='y', alpha=0.3)

# 5. Position 1,1: Scatter plot - Price vs Units Sold
axes[1,1].set_title("Price vs Sales Correlation", fontsize=14, fontweight='bold')
axes[1,1].set_xlabel("Price ($)", fontsize=12)
axes[1,1].set_ylabel("Units Sold", fontsize=12)

# Create scatter plot with different colors for each product
for i, product in enumerate(products):
    axes[1,1].scatter(prices[i], units_sold[i], color=colors[i], s=100, label=product)

# Add trend line
slope, intercept = np.polyfit(prices, units_sold, 1)
trend_line = slope * np.array(prices) + intercept
axes[1,1].plot(prices, trend_line, color='red', linestyle='--', linewidth=2, label='Trend Line')

axes[1,1].legend(fontsize=10)  # Smaller legend font
axes[1,1].grid(True)

# 6. Position 1,2: Horizontal bar chart - Product performance
axes[1,2].set_title("Product Performance Ranking", fontsize=14, fontweight='bold')
axes[1,2].set_xlabel("Total Sales ($)", fontsize=12)
axes[1,2].set_ylabel("Products", fontsize=12)

# Create horizontal bar chart using total sales from earlier
bars = axes[1,2].barh(products, total_sales, color=colors)

# Add value labels on each bar with adjusted positioning
for bar in bars:
    width = bar.get_width()
    axes[1,2].text(width + 500, bar.get_y() + bar.get_height()/2,  # Reduced spacing
                  f'${width:,.0f}',
                  ha='left', va='center', fontsize=9)  # Smaller font

axes[1,2].grid(axis='x', alpha=0.3)

# 7. Creative section for empty subplots
creative_texts = ['Future Growth', 'Market Insights', '2025 Projections']
for j, text in enumerate(creative_texts):
    axes[2,j].text(0.5, 0.5, text, ha='center', va='center', fontsize=14,  # Smaller font
                   transform=axes[2,j].transAxes, style='italic')
    axes[2,j].set_facecolor('lightgray')  # Light background

# 8. Add main title
fig.suptitle("Annual Sales Report 2024", fontsize=20, fontweight='bold', y=0.98)

# 9. Adjust layout with multiple methods for best spacing
plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Increased spacing between subplots
plt.tight_layout(pad=3.0, w_pad=2.0, h_pad=2.0)  # Added padding parameters

# 10. Save and show
plt.savefig('sales_report.png', dpi=300, bbox_inches='tight')
plt.show()