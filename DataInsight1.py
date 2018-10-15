from UserAnalysisFunctions import *

# Data Insight 1
# This script will find the average purchase window time for a specific user/product pairing
# That data will be useful to understand how often to restock that particular product
# As an example, it performs the operation for a smaller set of data first and prints it to screen

# replace this filename with the location of the dataframe you want to run
filename = "C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv"
userhash = "64LcsIctWnPrGaXfcW+gPRBJq5akh84HNEuUWbemoFZT8YOwmWpMjNDfRzyllfGGKXo37iHtiLOrIEW6XAePrw=="
prodid = 2605

# This is where the result csv will be saved, change the location accordingly
resultFile = 'C:/Users/NPC/Desktop/Career/Bytefoods/purchaseWindow.csv'

# preProcess will throw out all null values first
dataframe = preProcess(filename)

# For single user, single product as an example
print("Data Insight 1 - purchase count, item life, and average purchase window")

# Create dataframe of data from just that specific user and product ID 2605
datauser = getUserDataframe(dataframe, userhash)
datauserproduct = getSmallDataProduct(datauser, prodid)
datasorted = datauserproduct.sort_values(by=['date_time'])
datasorted = datasorted.reset_index()


datediff, count, window = shortAvgPurchaseWindow(datasorted)
print("Product:" + str(prodid))
print("User:" + userhash)
print("Item Life: " + str(datediff))
print("Purchase Count: " + str(count))
print("Average Purchase Window Time: " + str(window))


# For all customers of one product, right now product id is set to 2605:
fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
# Create smaller dataframe of only data on product 2605
dataproduct = dataframe.loc[(dataframe.product_id == prodid), fields]
dataproduct = dataproduct.sort_values(by=['card_hash', 'date_time'])
dataproduct = dataproduct.reset_index()
userlist = list(set(dataproduct.card_hash))

# Result dataframe
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