
import pandas as pd
# Python doesn't recognize \ as a file location splitter, so I have to use /

#filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/sampledata.csv'
filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv'

# Learn about what datatype the output for read_csv from pandas is, how to manipulate it, etc
df = pd.read_csv(filename, sep=",")
#print(df)

print(df.loc[3][2])

# Column 2 has the hash
# Row 3 is the 4th entry (remember indexes start at 0)

# This is a PANDAS DataFrame



#remove data with fc_number = null




# create subset of data of one product
# pick this product 4167
dp4167 = df.loc[(df.product_id == 4167), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]
# Think about how to simplify the card_hash into a smaller value to use?  Easier to see


print(dp4167)


# analyze just the most frequent user
# find the user with the most entries first, then use that subset

user_counts = df["card_hash"].value_counts()
print(user_counts)

# pick this user pFCsO21elMCmPzQ4S0ASZesbTnPjb75q6sB4KEwR/SHlZJ4XlKB3wssrWb1cTRVYjEraXRaQssMiFUKXjJ0r3Q==
du1= df.loc[(df.card_hash == "pFCsO21elMCmPzQ4S0ASZesbTnPjb75q6sB4KEwR/SHlZJ4XlKB3wssrWb1cTRVYjEraXRaQssMiFUKXjJ0r3Q=="), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]
print(du1)


# Most common user: pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidlZpC1Md3ilg1NvM19ip8WAvilcMdy8siy5whPtAKA==
du2= df.loc[(df.card_hash == "pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidlZpC1Md3ilg1NvM19ip8WAvilcMdy8siy5whPtAKA=="), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]

# Make a function/script that sorts the data by user, and does some analysis







# create subset of data of one kiosk
# Pick this kiosk - 548
# 625 rows of data for this kiosk - lets look into that in a bit more detail first?

# For this one kiosk, lets first just look at the most common product, and analyze the time that product is bought

# Maybe we can look at products with the same category, and see if one fades out as another fades in?
# If this is the case, we can apply that analysis to other kiosks, too
dk548= df.loc[(df.kiosk_id == 548), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]
print(dk548)

dk548sortdate = dk548.sort_values(by=["date_time"])
print(dk548sortdate)

dk548sortprod = dk548.sort_values(by=["product_id", "date_time"])
print(dk548sortprod)

