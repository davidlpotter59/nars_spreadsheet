#!/usr/bin/env python
import pandas as pd
import os
import time
import datetime

datestr = time.strftime("%Y%m%d_%H%M%S")

# Calculate the last day of the previous month to get the Accounting Date
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
accdate = lastMonth.strftime("%Y%m%d")

xlsx_file = accdate + "_" + datestr+"_nars_spreadsheet.xlsx"
input_file = "nars.csv"

if os.path.exists(xlsx_file):
    os.remove(xlsx_file)
    
nars_df = pd.read_csv(input_file, sep='|', header=0, encoding = "ISO-8859-1")

#  fixing bad eff date and exp date
nars_df['eff_date'] = pd.to_datetime(nars_df['eff_date'], format = "%m/%d/%Y", errors="coerce")
nars_df['exp_date'] = pd.to_datetime(nars_df['exp_date'], format = "%m/%d/%Y", errors="coerce")

# had to search for DELOS using the .contains since the client location contains a space 
delos_df = nars_df[nars_df['client_location'].str.contains("104")] 
starr_df = nars_df[nars_df.client_location=='SILC']
axis_df = nars_df[nars_df.client_location=="AX1"]
gsn_df = nars_df[nars_df.client_location=="SC2"]
bad_df = nars_df.query('eff_date == "NaT"' or 'exp_date == "NaT"')

with pd.ExcelWriter(xlsx_file) as writer:  
    nars_df.to_excel(writer, sheet_name="All - Detail")
    delos_df.to_excel(writer, sheet_name='DELOS - Detail')
    starr_df.to_excel(writer, sheet_name='STARR - Detail')
    axis_df.to_excel(writer, sheet_name='AXIS - Detail')
    gsn_df.to_excel(writer, sheet_name='GSN - Detail')
    bad_df.to_excel(writer, sheet_name='Bad Records')

print("Output Completed")