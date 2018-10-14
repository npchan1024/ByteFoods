from UserAnalysisFunctions import *

# Data Insight 2
# Statistical analysis for our 2nd insight - find probability of a user dropping a product
# Might be able to use our previous insight in a different form for this - might need to look at specific user

# 114 users total that are "recurring" customers, defined as buying the product 3 or more times
# We want to predict - whether or not a "current" latest user will purchase the product again

# This is more like an extension of previous insight
# If the user hasn't purchased the item for 2 standard deviations after the previous purchase, consider the user done?
# Add standard deviation to previous insight table

# Quick example, lets look at the most frequent customer of product 2605

# This is a rewritten avg purchase window function
# We actually need all the values in between to get standard deviation

# Input should be a time since last purchase, output should be probability that the user dropped the item.

print("Data Insight 2 - Customer retention prediction")

# input dataframe should be data from just one user for one product.
# We already have "datasorted" from earlier, which is for product 2606 for one user.

filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv'
userhash = "64LcsIctWnPrGaXfcW+gPRBJq5akh84HNEuUWbemoFZT8YOwmWpMjNDfRzyllfGGKXo37iHtiLOrIEW6XAePrw=="
prodid = 2605
resultFile = 'C:/Users/NPC/Desktop/Career/Bytefoods/purchaseWindow.csv'

# preProcess will throw out all null values first
dataframe = preProcess(filename)

# later on make this a function that you can input the df.card_hash for

# Supply variable for the access outside - check that dataframe is the right format first

# For single user, single product as an example
print("Data Insight 1 - purchase count, item life, and average purchase window")

datauser = getUserDataframe(dataframe, userhash)
datauserproduct = getSmallDataProduct(datauser, prodid)
datasorted = datauserproduct.sort_values(by=['date_time'])
datasorted = datasorted.reset_index()





# To simplify a bit, just pass in the sorted series of datetime objects
print(datasorted)
window2, sd2 = avgPurchaseWindowSD(datasorted["date_time"])

print("Average time between purchases: " + str(window2))
print("Standard deviation of time between purcahses: " + str(sd2))
# Lets say it's been 4 days since the user purchased the product.
# Have to be able to input 4 as a timedelta object, so the calculations are done in the same units
timeinput = pd.to_timedelta('3 days 07:05:01')

# see if I need this to be numeric instead of timedelta to do probability
p2 = calculateProbability(timeinput, window2, sd2)
print("Comparison of this delay to average delay for this customer")
print(p2)

# This is a high standard deviation compared to the mean
# Exploring the data, there are some gaps of up to 10 days, and some very small gaps
# Difference will have very small values if the customer buys two copies of the item in the same purchase
# Add a filter for this later.