
import pandas as pd
# Python doesn't recognize \ as a file location splitter, so I have to use /

filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/sampledata.csv'


# Learn about what datatype the output for read_csv from pandas is, how to manipulate it, etc
df = pd.read_csv(filename, sep=",")
print(df)

print(df.loc[3][2])

# Column 2 has the hash
# Row 3 is the 4th entry (remember indexes start at 0)

# This is a PANDAS DataFrame




# create subset of data of one product
# pick this product 4167
dp4167 = df.loc[(df.product_id == 4167), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]
# Think about how to simplify the card_hash into a smaller value to use?  Easier to see


print(dp4167)


# find subset of data of one user
# pick this user pFCsO21elMCmPzQ4S0ASZesbTnPjb75q6sB4KEwR/SHlZJ4XlKB3wssrWb1cTRVYjEraXRaQssMiFUKXjJ0r3Q==
du1= df.loc[(df.card_hash == "pFCsO21elMCmPzQ4S0ASZesbTnPjb75q6sB4KEwR/SHlZJ4XlKB3wssrWb1cTRVYjEraXRaQssMiFUKXjJ0r3Q=="), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]
print(du1)

# Make a function/script that sorts the data by user, and does some analysis







# create subset of data of one kiosk
# Pick this kiosk - 548
dk548= df.loc[(df.kiosk_id == 548), ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]]
print(dk548)




