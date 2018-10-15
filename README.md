# ByteFoods
Bytefoods data engineer exercise

Data Insight 1 - Average Purchase Window, Item Life, and Purchase Count
File: DataInsight1.py

To run this, you may have to change the filename to the location of your source dataset (by default I have included it in the ByteFoods folder).
The result csv file will be saved in the location specified by resultFile, so change where you want the result to be saved.

For the first example, I picked a specific userhash (64Lcs...) and product ID (2605) to analyze.

The first part of this script will print out three insight numbers for that user/product.

The Item Life is the time between the earliest and latest purchase of that product for that user.
The Purchase Count is the number of times that user has purchased that product total.
The Average Purchase Window is the average amount of time in between each purchase of that product for that user (example - user A buys milk on average 2 times a week).

The second part of the script runs this for all users of one specific product (2605), and saves the resulting dataframe in a csv file.


Data Insight 2 - Chance User drops Product
File: DataInsight2.py

To run this, you may have to change the filename to the location of your source dataset (by default I have included it in the ByteFoods folder).
This script will calculate the average time window in between purchases of a specific product by a specific user across all Kiosks they visit, and also the standard deviation of the time differences.  This can be used to make a prediction on whether or that product is still active for that user - if that user has not purchased that product in a certain number of days, is this behavior considered "unusual" for that user (indicating that they might not be interested in the product anymore).


Insight 3 - Chance Kiosk drops Product
File: DataInsight3.py

To run this, you may have to change the filename to the location of your source dataset (by default I have included it in the ByteFoods folder).
This script will calculate the average time window in between purchases of a specific product at a specific Kiosk, and also the standard deviation of the time differences.  This can be used to make a prediction on whether or not a product is no longer active - as in the likelihood that any current user at this kiosk will not purchase it again.
