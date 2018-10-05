import pandas as pd
from scipy.stats.distributions import norm
import numpy as np

def preProcess(filename):

    # check that filename is not null
    # clean out null data

    dataframe = pd.read_csv(filename, sep=",")
    dataframe = dataframe.dropna()
    return dataframe

# dataframe must have five fields of "kiosk_id", "product_id", "card_hash", "date_time", "fc_number"
def getUserDataframe(dataframe, userhash):
    # For now, these are the only fields.  Can make fields an input parameter to make this useful with other datasets.
    fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
    datauser = dataframe.loc[(dataframe.card_hash == userhash), fields]
    return datauser

# This is meant to pass a single user's dataframe in and get analysis for a single product
# Only returning kiosk id and date_time because we don't need the rest, can change this later


def getKioskDataframe(dataframe, kioskid, prodid):
    fields = ["kiosk_id", "product_id", "card_hash", "date_time", "fc_number"]
    datakiosk = dataframe.loc[(dataframe.kiosk_id == kioskid) & (dataframe.product_id == prodid), fields]
    return datakiosk

def getSmallDataProduct(dataframe, prodid):
    # for now data format is assumed to be valid
    dataproduct = dataframe.loc[(dataframe.product_id == prodid), ["kiosk_id", "date_time"]]
    return dataproduct

# need to pass in a dataframe with just kiosk_id and date_time... is there a way to redefine these dataframes?
def shortAvgPurchaseWindow(dataframe):
    # More universal to use this if I can make any field an input instead of just "date_time"
    # Can save time if we already know the dataframe is sorted, but oh well

    # This returns 0 days if it's the only purchase!

    # Find latest date_time
    maxdate = pd.to_datetime(max(dataframe["date_time"]))
    # Find earliest date_time
    mindate = pd.to_datetime(min(dataframe["date_time"]))
    # Find number of values
    # This shortcut is okay because we're supposed to divide by n
    # For my next function, I will have to add conditionals to deal with there only being 1 entry
    count = dataframe["date_time"].count()
    # Difference/number of values = avg time between purchases
    timedelta = maxdate-mindate
    avgPurchaseWindow = (maxdate-mindate)//count
    # Convert to something more displayable?
    return timedelta, count, avgPurchaseWindow

# has to take in a reindexed sorted series of datetimes
# creates a list of differences, and then finds standard deviation and mean
def avgPurchaseWindowSD(series):
    count = series.count()
    dateseries = pd.to_datetime(series)
    maxdate = max(dateseries)
    # Find earliest date_time
    mindate = min(dateseries)
    # Find number of values - this will be number of entries in date difference array

    # Might not need this, just use series count - 1

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


        # find standard deviation of series (1-end)
        #sd = diffseries.std()
        sd = np.std(diffseries)
        # find mean of series
        #avg = diffseries.mean()
        avg = np.mean(diffseries)

        # this is being returned as a series instead of a timedelta, figure out why
    # Phase 2 would be to take out outliers - 1st purchase and 2nd purchase are usually further than usual
    avgtimedelta = avg["date_time"]
    sdtimedelta = sd["date_time"]

    return avgtimedelta, sdtimedelta


# This is assuming a normal distribution.
# Does PANDAS already have a function for this?
def calculateProbability(time, avg, sd):
    if sd == pd.to_timedelta(0):
        print("Standard deviation is 0, not enough data points, returning p = 0")
        p = 0
    else:
        z = (time - avg)/sd
        p = norm.cdf(z)
    return p