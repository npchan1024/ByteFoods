from UserAnalysisFunctions import *

print("Data Insight 3 - Product retention prediction in Kiosk")
# Data Insight 3
# Probability of a product being out of rotation
# Similar analysis to 2, but for a specific product stocked at a single kiosk

filename = "C:/Users/NPC/Desktop/Career/Bytefoods/items_purchased.csv"
prodid = 4061
kioskid = 750

# preProcess will throw out all null values first
dataframe = preProcess(filename)


datakiosk = getKioskDataframe(dataframe, kioskid, 4061)
sortedkiosk = datakiosk.sort_values(by=['date_time'])
window3, sd3 = avgPurchaseWindowSD(sortedkiosk["date_time"])

#Change the time window here:  This is the time since the last purcahse
timeinput2 = pd.to_timedelta('1 days 12:00:00')

print("Average time between purchases: " + str(window3))
print("Standard deviation of time between purcahses: " + str(sd3))
p3 = calculateProbability(timeinput2, window3, sd3)
print("Comparison of this delay to average delay for this product in this kiosk")
print(p3)
