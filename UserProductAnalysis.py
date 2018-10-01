import pandas as pd

filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv'
userhash = "64LcsIctWnPrGaXfcW+gPRBJq5akh84HNEuUWbemoFZT8YOwmWpMjNDfRzyllfGGKXo37iHtiLOrIEW6XAePrw=="

df = pd.read_csv(filename, sep=",")

# later on make this a function that you can input the df.card_hash for
du = df.loc[(df.card_hash == userhash), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]

#dus = du.sort_values(by=['product_id', 'date_time'])
#print(dus)

# check out product_id 2605 for this guy first
# write something that does this for any product input later

# function should be something like "analyze user/product"
# should loop through every product in that user's list, and then find that frequency data and output for each product
# see if there is a better way to do this in aggregate, or if I do need to just break the dataframe into smaller ones

# first, do it for one product for this user - 2605
prodid = 2605
dup = du.loc[(du.product_id == prodid), ["kiosk_id", "date_time"]]
dupsort = dup.sort_values(by=['date_time'])

# reset indexes, makes it so we can loop through easier
dupsort = dupsort.reset_index()
print(dupsort)

# this is just 45 rows of data - lets find the average time in between each purchase?
# the first and second purchase have a long time in between, not sure how to account for it
# make this into a function... next.



# date difference in PANDAS?
# output it as one column, will be size n-1


# Interestingly, there is a shortcut in the math....
# Take difference of first and last purchase, and then divide by the number of purchases
# What losses are there if we do this approximation - outlier data isn't accounted for


# only important thing is to throw out outliers (customer went on vacation or something)

# Think about this a little more, how do we tell if the user is "dropping off" at the end?

# Series data structure
# What tools in PANDAS is there for time series?

# First datetime


d1 = dupsort.loc[0][2]
d2 = dupsort.loc[1][2]
# The dates are somehow being treated as strings - how do we treat it as a date?
print(d2-d1)
