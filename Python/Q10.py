import pandas as pd
import numpy as np
target={'Zone A':56000,'Zone B':70000,'Zone C':75000,'Zone D':60000}
sales={'Zone A':58000,'Zone B':68000,'Zone C':78000,'Zone D':61000}
salesDict={'Target':target,'Sales':sales}

saleDF=pd.DataFrame(salesDict)
print("Actual Dataframe is \n",saleDF)
#Adding columns-Order
saleDF.loc[:,'Orders']=[6000,6700,6200,6000]
print("Dataframe after adding column-order\n",saleDF)

#Adding Rows-Zone E
saleDF.loc['Zone E',:]=[65000,62000,5700]
print("DAtafrane after adding new-zone E\n",saleDF)
