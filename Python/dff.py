import pandas as pd
import numpy as np
staff=pd.Series([30,36,52])
salaries=pd.Series([152222,7529847,74246558])
school={'people':
        staff,'amount':salaries}
ob=pd.DataFrame(school)
ob1=pd.DataFrame(ob)
print(ob1)
