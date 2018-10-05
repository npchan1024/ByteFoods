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

# experiment with just one product's data first
fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
dataproduct = dataframe.loc[(dataframe.product_id == 2605), fields]
dataproduct = dataproduct.sort_values(by=['card_hash','date_time'])
userlist = list(set(dataproduct.card_hash))

# dataproduct is now a sorted dataframe
# if we loop through every row... we could just update our result dataframe with each entry
# what is an efficient way to do that?  loop through and just pick the entry and exit values?
# This is like my IFTA algorithm, when the user id changes, log the value.

# For now lets just do the inefficient version, can improve on it after.

# inefficient version - use whole dataframe (dataproduct) for each user...

# Create a dataframe of the size of userlist
# Add a column for each of the results we want

# qweq = pd.DataFrame(userlist, columns=["card_hash"])
# qweq["item_life"] = ""
# qweq["purchase_count"] = ""
# # For this one, see if I can just do a vectorized operation of item_life // purchase_count later
# qweq["avg_window"] = ""


# Different dataframe construction
userResult = pd.DataFrame(columns=["card_hash", "item_life", "purchase_count", "avg_window"])

# Follow this to insert row by row
# https://stackoverflow.com/questions/17091769/python-pandas-fill-a-dataframe-row-by-row


# loop through qweq/userlist and get the smaller dataframe for each user
# then do shortAvgPurchaseWindow(dataframe), make it output both values and store it in qweq

# loop through qweq, and be inserting as we go - otherwise, fill the result dataframe as we go?
index = 0
for user in userlist:
    small = getUserDataframe(dataproduct, user)
    timedelta, count, avg = shortAvgPurchaseWindow(small)
    #insert each of the values
    userResult.loc[index] = pd.Series({'card_hash': user, 'item_life': timedelta, 'purchase_count': count, 'avg_window': avg})
    index += 1

# datauser = getUserDataframe(dataframe, userhash)
# datauserproduct = getSmallDataProduct(datauser, prodid)
# datasorted = datauserproduct.sort_values(by=['date_time'])
# datasorted = datasorted.reset_index()
#
# datausersorted = datauser.sort_values(['product_id','date_time'])
#
# # Test looping through data
# for index, row in datausersorted.iterrows():
#     print(row)

# What is a good way to visualize this result?  Do we also want an overall average?  Variance?  Weight by count?
print(userResult)

# datausersorted.to_csv("C:/Users/NPC/Desktop/Career/Bytefoods/userexplore.csv")