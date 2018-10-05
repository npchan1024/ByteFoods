from UserAnalysisFunctions import *

# First Data Insight - Average Purchase Window!
# This script will find the average purchase window time for a specific user/product pairing
# That data will be useful to understand how often to restock that particular product
# Can possibly be generalized for each separate product
# Average active customer count can be multiplied by this number to find the number to stock
filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv'
userhash = "64LcsIctWnPrGaXfcW+gPRBJq5akh84HNEuUWbemoFZT8YOwmWpMjNDfRzyllfGGKXo37iHtiLOrIEW6XAePrw=="
prodid = 2605
# give a more easy to read name instead of df
dataframe = preProcess(filename)

# later on make this a function that you can input the df.card_hash for

# Supply variable for the access outside - check that dataframe is the right format first

datauser = getUserDataframe(dataframe, userhash)
datauserproduct = getSmallDataProduct(datauser, prodid)
datasorted = datauserproduct.sort_values(by=['date_time'])
datasorted = datasorted.reset_index()
datediff = shortAvgPurchaseWindow(datasorted)
print("Product:" + str(prodid))
print("User:" + userhash)
print("Average Purchase Window Time: " + str(datediff))

# Split output into two numbers
# we can use the date difference to understand the "lifetime" of the product
# And then use the count to get the average purchase frequency
# This metric could be useful for our second analysis


# Additional thing I can do with this - do it across all products for this one user
# Then plot the values
# Or do across all users of one product - different number for each user of course.

# Get an array of each unique user id?




# Inefficient to call this for EACH user, but do it first, fix it later.



# Average active customer count - second data insight
# I will have to explore the data a bit first before I come up with how I want to get this value.
# Look at my same small basecase first

# Explore the complete data for one single product, and use that to figure out an analysis






# Data Insight 3 - Something we should use statistics or something more mathematically relevant on