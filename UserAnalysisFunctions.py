import pandas as pd

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
    count = dataframe["date_time"].count()
    # Difference/number of values = avg time between purchases
    timedelta = maxdate-mindate
    avgPurchaseWindow = (maxdate-mindate)//count
    # Convert to something more displayable?
    return timedelta, count, avgPurchaseWindow

# Not done yet, will write a version to deal with outliers if I have time.
def realAveragePurchaseWindow(dataframe, userhash, prodid):
    # This should filter outliers and stuff, figure it out later.
    purchaseWindow = 0
    return purchaseWindow