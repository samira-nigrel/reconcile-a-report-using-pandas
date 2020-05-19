# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path,sep=",")
df['state']=df['state'].str.lower()
df['total']=df['Jan']+df['Feb']+df['Mar']
#df.loc['sum_row']= df.sum(numeric_only=True, axis=0)
sum_row = df.sum(numeric_only=True, axis=0)
df_final = df.append(sum_row,ignore_index=True)
#print(df_final.tail())
# Code ends here


# --------------
import requests

# Code starts here
url="https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response=requests.get(url)
df1=pd.read_html(response.content)[0]
#print(df1.head(15))
df1=df1.loc[11:]
header=df1.loc[11]
df1=df1.loc[12:]
df1.columns=header
df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping=df1.set_index('United States of America')['US'].to_dict()
df_final.insert(loc=6, column='abbr',value='Nan')
df_final['abbr']=df_final['state'].map(mapping)
# Code ends here


# --------------
# Code stars here
df_final['abbr'][df_final.state=='mississipi'] ="MS"
df_final['abbr'][df_final.state=='tenessee'] ="TN"
# Code ends here


# --------------
# Code starts here

# Calculate the total amount
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))

# Code ends here


# --------------
# Code starts here

# Calculate the sum
sum_row = df_sub[["Jan", "Feb", "Mar", "total"]].sum()

df_sub_sum = pd.DataFrame(data=sum_row).T
#apply $ to the sum 
df_sub_sum = df_sub_sum.applymap(lambda x: "${:,.0f}".format(x))

# append the sum
print(formatted_df)
final_table = formatted_df.append(df_sub_sum)
print(final_table)
# rename the index
final_table = final_table.rename(index={0: "Total"})
print(final_table)

# Code ends here    


# --------------
# Code starts here
df_sub['total']=df_sub['Jan']+df_sub['Feb']+df_sub['Mar']
df_sub.plot.pie(y='total',figsize=(5,5))

# Code ends here


