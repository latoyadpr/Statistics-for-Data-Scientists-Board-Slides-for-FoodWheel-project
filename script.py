import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt

# Load the orders data
orders = pd.read_csv('orders.csv')

# Inspect the first few rows
print(orders.head())

# Load the restaurants data
restaurants = pd.read_csv('restaurants.csv')

# Inspect the restaurants dataframe
print(restaurants.head())

# Group count by cuisine
cuisine_counts = restaurants.groupby('cuisine').count()
print(cuisine_counts)

# Create a pie chart
plt.pie(
    cuisine_counts['id'],  # Use the count of restaurants for each cuisine
    labels=cuisine_counts.index,  # Use cuisine names as labels
    autopct='%1.1f%%'  # Display percentages
)

# Add a title
plt.title('Cuisine Distribution on FoodWheel')

# Make the pie chart a perfect circle
plt.axis('equal')

# Display the chart
plt.show()

# Create a new column 'month' by extracting the month from the 'date' column
orders['month'] = orders['date'].apply(lambda x: x.split('-')[0])

# Group the orders by 'month' and calculate the average order amount
avg_order = orders.groupby('month')['price'].mean()

# Calculate the standard deviation for each month
std_order = orders.groupby('month')['price'].std()

# Inspect the results
print("Average Order Amount per Month:")
print(avg_order)
print("\nStandard Deviation of Order Amount per Month:")
print(std_order)


# Group orders by customer_id and calculate the total amount spent by each customer
customer_amount = orders.groupby('customer_id')['price'].sum()

# Create a histogram
plt.hist(
    customer_amount,  # Data to plot
    range=(0, 200),   # Range of the histogram
    bins=40           # Number of bins
)

# Label the x-axis
plt.xlabel('Total Spent')

# Label the y-axis
plt.ylabel('Number of Customers')

# Add a title
plt.title('Distribution of Total Amount Spent by Customers')

# Display the histogram
plt.show()


# View the unique neighborhoods
unique_neighborhoods = restaurants['neighborhood'].unique()
print("Unique Neighborhoods:")
print(unique_neighborhoods)

# Calculate the value counts of the neighborhood variable
neighborhood_counts = restaurants['neighborhood'].value_counts()
print("\nNeighborhood Counts:")
print(neighborhood_counts)

# Create a list of the neighborhood count values
neighborhood_count_values = neighborhood_counts.tolist()
print("\nList of Neighborhood Count Values:")
print(neighborhood_count_values)
