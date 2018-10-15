from UserAnalysisFunctions import *

# Data Insight 2
# Statistical analysis for our 2nd insight - find probability of a user dropping a product
# We want to predict - whether or not a "current" user will purchase a specific product again
# Based on their previous times between purchases

# Quick example, lets look at the most frequent customer of product 2605

# This is a rewritten avg purchase window function
# We actually need all the values in between to get standard deviation

# Input should be a time since last purchase, output should be probability that the user dropped the item.

print("Data Insight 2 - Customer retention prediction")

# input dataframe should be data from just one user for one product.
# We already have "datasorted" from earlier, which is for product 2606 for one user.

filename = "C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv"
userhash = "64LcsIctWnPrGaXfcW+gPRBJq5akh84HNEuUWbemoFZT8YOwmWpMjNDfRzyllfGGKXo37iHtiLOrIEW6XAePrw=="
prodid = 2605


# preProcess will throw out all null values first
dataframe = preProcess(filename)

# later on make this a function that you can input the df.card_hash for

# Supply variable for the access outside - check that dataframe is the right format first

# For single user, single product as an example

datauser = getUserDataframe(dataframe, userhash)
datauserproduct = getSmallDataProduct(datauser, prodid)
datasorted = datauserproduct.sort_values(by=["date_time"])
datasorted = datasorted.reset_index()
window2, sd2 = avgPurchaseWindowSD(datasorted["date_time"])

print("Average time between purchases: " + str(window2))
print("Standard deviation of time between purcahses: " + str(sd2))

# Change the time window here, this is the time since the last purcahse:
timeinput = pd.to_timedelta('4 days')

# see if I need this to be numeric instead of timedelta to do probability
p2 = calculateProbability(timeinput, window2, sd2)
print("Comparison of this delay to average delay for this customer")
print(p2)


