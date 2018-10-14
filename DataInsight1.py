from UserAnalysisFunctions import *

# Data Insight 1
# This script will find the average purchase window time for a specific user/product pairing
# That data will be useful to understand how often to restock that particular product
# Can possibly be generalized for each separate product
# Also starting to get more used to the tools PANDAS has


# Consider formatting as a function

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
datediff, count, window = shortAvgPurchaseWindow(datasorted)
print("Product:" + str(prodid))
print("User:" + userhash)
print("Item Life: " + str(window))
print("Purchase Count: " + str(count))
print("Average Purchase Window Time: " + str(window))


# For all customers of one product, right now product id is set to 2605:
fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
dataproduct = dataframe.loc[(dataframe.product_id == prodid), fields]
dataproduct = dataproduct.sort_values(by=['card_hash', 'date_time'])
userlist = list(set(dataproduct.card_hash))
userResult = pd.DataFrame(columns=["card_hash", "item_life", "purchase_count", "avg_window"])

index = 0
for user in userlist:
    small = getUserDataframe(dataproduct, user)
    timedelta, count, avg = shortAvgPurchaseWindow(small)
    #insert each of the values
    userResult.loc[index] = pd.Series({'card_hash': user, 'item_life': timedelta, 'purchase_count': count, 'avg_window': avg})
    index += 1

userResult = userResult.sort_values(by=['purchase_count', 'avg_window'], ascending = False)

# write result back to csv
userResult.to_csv(resultFile)
print("Wrote to csv file " + resultFile)