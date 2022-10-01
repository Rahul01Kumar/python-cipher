import pandas as pd
yr1={'QTR1':44500,'QTR2':50000,'Q3':58322,'Q4':85000}
yr2={'A':85888,'B':85663,'QTR4':99866}
diSales1={1:yr1,2:yr2}
df3=pd.DataFrame(diSales1)
print(df3)
