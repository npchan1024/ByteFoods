import pandas as pd
from scipy.stats.distributions import norm
import numpy as np

# this imports the file and drops all blank entries from the dataset
def preProcess(filename):

    dataframe = pd.read_csv(filename, sep=",")
    dataframe = dataframe.dropna()
    return dataframe

# this retrieves a dataframe of just one user's data
def getUserDataframe(dataframe, userhash):
    fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
    datauser = dataframe.loc[(dataframe.card_hash == userhash), fields]
    return datauser

# returns a dataframe with just data on one product in one kiosk
def getKioskDataframe(dataframe, kioskid, prodid):
    fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
    datakiosk = dataframe.loc[(dataframe.kiosk_id == kioskid) & (dataframe.product_id == prodid), fields]
    return datakiosk


# creates a small dataframe with only the kiosk_id and date_time of the inputted purchases, for one specific product
def getSmallDataProduct(dataframe, prodid):
    dataproduct = dataframe.loc[(dataframe.product_id == prodid), ["kiosk_id", "date_time"]]
    return dataproduct


# This function calculates the item lifetime, purchase count, and purchase window for one user for one product
def shortAvgPurchaseWindow(dataframe):
    # Find latest date_time
    maxdate = pd.to_datetime(max(dataframe["date_time"]))
    # Find earliest date_time
    mindate = pd.to_datetime(min(dataframe["date_time"]))
    # Find number of values

    count = dataframe["date_time"].count()
    # This shortcut is okay because we're supposed to divide by n    count = dataframe["date_time"].count()
    # Difference/number of values = avg time between purchases
    timedelta = maxdate-mindate
    avgPurchaseWindow = (maxdate-mindate)//count
    # Convert to something more displayable?
    return timedelta, count, avgPurchaseWindow

# This function takes in a reindexed sorted series of datetimes
# Creates a list of differences, and then finds standard deviation and mean
def avgPurchaseWindowSD(series):
    count = series.count()
    dateseries = pd.to_datetime(series)
    maxdate = max(dateseries)
    # Find earliest date_time
    mindate = min(dateseries)
    # Find number of values - this will be number of entries in date difference array

    # Total difference/number of values = avg time between purchases
    timedelta = maxdate-mindate

    if (series.count() - 1) == 0:
        avg = timedelta
        sd = 0
    else:
        # Shortcut done by vectorized subtraction
        firstdate = dateseries[0:count-1]
        firstdate = firstdate.reset_index()
        seconddate = dateseries[1:count]
        seconddate = seconddate.reset_index()
        diffseries = seconddate - firstdate

        # Standard Deviation
        sd = np.std(diffseries)

        # Mean
        avg = np.mean(diffseries)

    # Convert back to the correct format
    avgtimedelta = avg["date_time"]
    sdtimedelta = sd["date_time"]

    return avgtimedelta, sdtimedelta


# This calculation assumes normal distribution
# Basically a z-score calculation
def calculateProbability(time, avg, sd):
    if sd == pd.to_timedelta(0):
        print("Standard deviation is 0, not enough data points, returning p = 0")
        p = 0
    else:
        z = (time - avg)/sd
        p = norm.cdf(z)
    return p

# For new data - for now, just merge new data in before running the function
# I can't think of the best way to maintain data integrity with my current processes
# Without having to rerun the entire dataset again.

# Calculating standard deviation requires calculating a new mean

# Calculating the average difference time can work if we save the first data point and the count somewhere
# But processing it should be linear (get first and last point, get count, do the operation)
# So you might as well just rerun it.


# This function imports stuff from the new file into an already existing dataframe
# Just merge it first (check that it's the same data type, has the same columns, etc)
# After running this, then sort appropriately for each of the insights
def mergeNewData(filename, dataframe):

    newdataframe = pd.read_csv(filename, sep=",")
    newdataframe = newdataframe.dropna()

    # This doesn't break if the dataframes don't have the same fields
    # But running it on different types of datasets might not be useful
    list_ = []
    list_.append(dataframe)
    list_.append(newdataframe)
    output = pd.concat(list_)
    # need to reindex the data after, or leave that for after sorting

    return output


