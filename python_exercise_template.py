# import pandas, numpy

import pandas as pd
import numpy as np

# Create the required data frames by reading in the files
# filename ='SaleData.xlsx'
# df = pd.read_excel(filename,sheet_name='Sales Data')


# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
	ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe
    sales_newsum = df.groupby(["Region","year","Item"]).sum()
    return sales_newsum

from datetime import date
# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe
    a=[]
    for i in range(0,len(df['OrderDate'])):
      a.append((date.today() - df['OrderDate'].iloc[i].date()).days)
    df1=pd.DataFrame(a,df['OrderDate'])
    df1.columns =['days_diff'] 
    return df1

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe
    list = df.values.tolist()
    manager =[]
    sales_man ={}
    temp=[]
    for row in list[0:]:
        if row[2] not in manager:
            manager += [row[2]]
        if row[2] in sales_man.keys():
            if row[3] not in sales_man.get(row[2]):
                temp = sales_man.get(row[2])
                temp=temp+[row[3]]
                sales_man[row[2]]=temp;
        else:
            sales_man[row[2]]=[row[3]]
    sales_man_list =[]
    for _ in sales_man.keys():
        sales_man_list+=[sales_man.get(_)]
    d= {'Managers':manager,'Sales_man':sales_man_list}
    dfq4 = pd.DataFrame(data = d)
    return dfq4

def unique(list): 
    x = np.array(list) 
    return np.unique(x)
data = pd.read_excel("SaleData.xlsx")
# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    mylist = data['Region'].tolist()
    k=unique(mylist)
    k1=k
    l=[]
    for i in range(len(k)):
        l.append(0)
    g=dict(zip(k,l) )   
    for row in list[1:]:
        if row[1] in g:
            g[row[1]]=g[row[1]]+1
    l=[]
    for i in range(len(k)):
        l.append(0)
    g1=dict(zip(k,l))
    for row in list[1:]:
        if row[1] in g1:
            g1[row[1]]=g1[row[1]]+row[7]
    values = [] 
    items = g.items()  
    for item in items: 
        values.append(item[1])
    values1 = [] 
    items = g1.items()  
    for item in items: 
        values1.append(item[1])
    d= {'Region':k,'salesman_count':values,'total_sales':values1}
    dfq4 = pd.DataFrame(data = d)
    return dfq4


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    calc_sum=df.groupby("Manager").sum()
    pt=calc_sum.loc[:, ['Sale_amt']]
    dfk=pd.DataFrame(pt)
    total=df.Sale_amt.sum()
    group=df.groupby("Manager")
    dfkk=pd.DataFrame(zip(group.Manager.unique(),(group.Sale_amt.sum()/total*100)),columns=["Manager","Percentage"])
    return dfkk

# df = pd.read_csv('imdb.csv',escapechar='\\',encoding='utf-8')
# Q7 get imdb rating for fifth movie of dataframe

def fifth_movie(df):
    df1=df.sort_values(by=['year'])
    df1.head()
    rating=df1.iloc[[4]]['imdbRating'].iloc[0]
    return rating

# Q8 return titles of movies with shortest and longest run time
def movies(df):
    maxDuration_title=df[df[df['type']=='video.movie']['duration'].max()==df['duration']]['title'].iloc[0]
    minDuration_title = df[df[df['type']=='video.movie']['duration'].min()==df['duration']]['title'].iloc[0]
    return [minDuration_title,maxDuration_title]

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
    df2=df.sort_values(['year','imdbRating'],ascending=[True,False])
    return df2

def dur(a):
  if a>1800 and a<10800:
    return True
  else :
    return False

# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
    return df[df['duration'].apply(lambda x:dur(x))]

# df = pd.read_csv("diamonds.csv")  

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here
    d1=df
    d1=d1.drop_duplicates(keep=False) 
    return len(df)-len(d1)

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
    d2= df.dropna(subset=['carat', 'cut'])
    return d2
    
# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here
    data_numerics_only = df.select_dtypes(exclude=['object'])
    return data_numerics_only

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here
    df['z'] = pd.to_numeric(df['z'],errors='coerce')
    new_df1 = df.select_dtypes([np.number])
    df["volume"]=np.where(df["depth"]>60,(df['x']*df['y']*df['z']),8)
    return (df['volume'])


# Q15 impute missing price values with mean
def impute(df):
	# write code here
    d3 =df
    d3['price'] =d3['price'].fillna(d3['price'].mean())       
    return d3['price']
