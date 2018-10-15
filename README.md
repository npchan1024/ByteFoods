# ByteFoods
Bytefoods Data Engineer Exercise

# Data Insight 1 - Average Purchase Window, Item Life, and Purchase Count

File: DataInsight1.py


To run this, you will have to change the filename variable to the location of your source dataset.

The result csv file will be saved in the location specified by resultFile, so change where you want the result to be saved.


For the first example, I picked a specific userhash (64Lcs...) and product ID (2605) to analyze.

The first part of this script will print out three insight numbers for that user/product.


The Item Life is the time between the earliest and latest purchase of that product for that user.

The Purchase Count is the number of times that user has purchased that product total.

The Average Purchase Window is the average amount of time in between each purchase of that product for that user (example - user A buys milk on average 2 times a week).

The second part of the script runs this for all users of one specific product (2605), and saves the resulting dataframe in a csv file.



For this first example, we find that there is an average of around 1 day and 21 hours between purchases of product 2605 for this user.  This information tells us to restock the product every 2 days.

The second part of the script runs this for all users of one specific product (2605), and saves the resulting dataframe in a csv file.  The data on all users can let us know when to restock the product.


# Data Insight 2 - Chance User drops Product

File: DataInsight2.py

To run this, you will have to change the filename variable to the location of your source dataset.

This script will calculate the average time window in between purchases of a specific product by a specific user across all Kiosks they visit, and also the standard deviation of the time differences.
This can be used to make a prediction on whether or that product is still active for that user.
If that user has not purchased that product in a certain number of days (example used is 4 days), how "unusual" is it for this user?

The number we receive is 0.75.  What this means is that not having purchased the product for 4 days is outside of 75% of the expected behavior of the user.

If you want to try different user ids, different products, or a different time window, change the variables accordingly.


# Data Insight 3 - Chance Kiosk drops Product

File: DataInsight3.py

To run this, you will have to change the filename variable to the location of your source dataset.

This script will calculate the average time window in between purchases of a specific product at a specific Kiosk, and also the standard deviation of the time differences.
Then, with an input of the time since the last purchase of that item, we want to predict how far this is from the usual expected outcome for that item.

Similar to Data Insight 2, the .86 that this returns means that the this product not having been purchased for 1.5 days is outside of 86% of expected purchase for this product.

If you want to try different product ids, different kiosks, or a different time window, change the variables accordingly.


# Handling New Data

I thought a bit about handling new data, and I found it a bit difficult to keep the standard deviation and difference numbers consistent.
With new data, it seems a bit easier to just merge the new dataset into the dataframe, and then proceed with the calculation.

This is less efficient than I would like it to be, and I am considering other possibilities.

I included a function called mergeNewData at the bottom of my UserAnalysisFunctions pack, which merges a new csv into an existing dataframe.


