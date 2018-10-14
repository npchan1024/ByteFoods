from UserAnalysisFunctions import *

print("Data Insight 3 - Product retention prediction in Kiosk")
# Data Insight 3
# Probability of a product being out of rotation
# Similar analysis to 2, but for a specific product stocked at a single kiosk

# Get dataframe data from one kiosk, one product before putting it through the function

filename = 'C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv'
userhash = "64LcsIctWnPrGaXfcW+gPRBJq5akh84HNEuUWbemoFZT8YOwmWpMjNDfRzyllfGGKXo37iHtiLOrIEW6XAePrw=="
prodid = 2605
resultFile = 'C:/Users/NPC/Desktop/Career/Bytefoods/purchaseWindow.csv'

# preProcess will throw out all null values first
dataframe = preProcess(filename)


datakiosk = getKioskDataframe(dataframe, 750, 4061)
sortedkiosk = datakiosk.sort_values(by=['date_time'])
window3, sd3 = avgPurchaseWindowSD(sortedkiosk["date_time"])

timeinput2 = pd.to_timedelta('2 days 07:05:01')
print("Average time between purchases: " + str(window3))
print("Standard deviation of time between purcahses: " + str(sd3))
p3 = calculateProbability(timeinput2, window3, sd3)
print("Comparison of this delay to average delay for this product in this kiosk")
print(p3)

# Similar issues as I thought of in second data insight
# Item can be bought very quickly in succession, average time between purchase not a good metric