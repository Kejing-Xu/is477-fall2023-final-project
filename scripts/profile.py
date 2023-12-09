import os
import pandas as pd
from ydata_profiling import ProfileReport

path = "profiling"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
# Create a new directory because it does not exist
    os.makedirs(path)

os.rename('data/iris/iris.data','data/iris/iris.csv')
df=pd.read_csv('data/iris/iris.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/report.html")