#!/usr/bin/env python
import pandas as pd
import os
import time
import datetime

datestr = time.strftime("%Y%m%d_%H%M%S")

# Calculate the last day of the previous month for the Accounting Date
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
accdate = lastMonth.strftime("%Y%m%d")
print(accdate)

xlsx_file = accdate + "_" + datestr+"_nars_panda.xlsx"
input_file = "nars.csv"

if os.path.exists(xlsx_file):
    os.remove(xlsx_file)
# else:
#     print("Can not delete the file as it doesn't exists")
    
nars_df = pd.read_csv(input_file, sep='|', header=0, encoding = "ISO-8859-1")


# had to search for DELOS using the .contains since the client location contains a space 
delos_df = nars_df[nars_df['client_location'].str.contains("104")] 
starr_df = nars_df[nars_df.client_location=='SILC']
axis_df = nars_df[nars_df.client_location=="AX1"]
gsn_df = nars_df[nars_df.client_location=="SC2"]

with pd.ExcelWriter(xlsx_file) as writer:  
    nars_df.to_excel(writer, sheet_name="All - Detail")
    delos_df.to_excel(writer, sheet_name='DELOS - Detail')
    starr_df.to_excel(writer, sheet_name='STARR - Detail')
    axis_df.to_excel(writer, sheet_name='AXIS - Detail')
    gsn_df.to_excel(writer, sheet_name='GSN - Detail')

print("Complete")