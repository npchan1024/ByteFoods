from UserAnalysisFunctions import *

# The two inputs for my function should be a userhash?
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
print("Average Purchase Window Time:")
print(datediff)


