#week 2 and 3

#Iine[8]:

import pandas as pd
import openpyxl


# Iine[9]:


xls = pd.ExcelFile('yelp.xlsx')


# Iine[10]:


type(xls)


# Iine[11]:


df = xls.parse('yelp_data')


# Iine[123]:


df


# Iine[13]:


df.shape


# Iine[14]:


len(df)


# Iine[15]:


type(df)


# Iine[16]:


df.columns


# Iine[17]:


df.count()


# Iine[18]:


df.dtypes


# Iine[19]:


df.describe()


# Iine[20]:


df.head()


# Iine[21]:


df["name"]


# Iine[22]:


atts=["name","city_id","state_id"]


# Iine[23]:


df_states = xls.parse('states')


# Iine[24]:


df_states.head()


# Iine[25]:


df.head()


# Iine[26]:


df.head(100)


# In[27]:


df = df.drop_duplicates()


# In[28]:


df[atts].head(100)


# In[29]:


df_cities = xls.parse('cities')


# In[30]:


df_cities.head()


# In[31]:


df = pd.merge(left=df, right=df_cities, how='inner', left_on='city_id', right_on='id')


# In[32]:


df.head()


# In[33]:


df = pd.merge(left=df, right=df_cities, how='inner', left_on='city_id', right_on='id')


# In[34]:


df.shape


# In[35]:


del df['id_x']


# In[36]:


del df['id_y']


# In[37]:


df.head()


# In[38]:


df[100:200]


# In[39]:


index = len(df) - 1
last_business = df[index:]
last_business['name']


# In[40]:


df[-1:]['name']


# In[41]:


rest  = df['name'] == 'The Dragon Chinese Cuisine'
df[rest]


# In[42]:


df[rest]['take_out']


# In[43]:


cat_0_bars = df["category_0"] == "Bars"
cat_1_bars = df["category_1"] == "Bars"
df[cat_0_bars| cat_1_bars]


# In[44]:


cat_0_bars = df["category_0"] == "Bars"
cat_1_bars = df["category_1"] == "Bars"
carnegie = df["city_x"]  == "Carnegie"
df[(cat_0_bars | cat_1_bars) & carnegie]


# In[45]:


cat_0 = df["category_0"] == "Bars"
cat_1 = df["category_1"] == "Bars"
carnegie = df["city_y"] == "Carnegie"
carnegie = df["city_x"]  == "Carnegie"
df[(cat_0 | cat_1 ) & carnegie]


# In[46]:


lv = df["city_x"] == "Las Vegas"
cat_0_bars = df["category_0"] == "Dive Bars"
cat_1_bars = df["category_1"] == "Dive Bars"
divebars_lv = df[lv & (cat_0_bars | cat_1_bars)]


# In[47]:


len(divebars_lv)


# In[48]:


stars = divebars_lv["stars"] >= 4.0
divebars_lv_4star_rating = divebars_lv[stars]


# In[49]:


divebars_lv_4star_rating


# In[50]:


import random


# In[51]:


rand_int = random.randint(0,len(divebars_lv_4star_rating)-1)
rand_divebar = divebars_lv_4star_rating[rand_int : rand_int + 1]
rand_divebar


# In[52]:


rand_int = random.randint(0,len(divebars_lv_4star_rating)-1)
rand_divebar = divebars_lv_4star_rating.iloc[rand_int]
rand_divebar


# In[53]:


cat_0 = df["category_0"].str.contains("Nail Salon")


# In[54]:


cat_1 = df["category_1"].str.contains("Nail Salon")


# In[55]:


henderson = df["city_x"] == "Henderson"


# In[56]:


df[(cat_0 | cat_1) & henderson]["review_count"].sum


# In[59]:


cat_0 = df["category_0"].str.contains("Auto Repair")
cat_1 = df["category_1"].str.contains("Auto Repair")
pitts = df["city_x"] == 'Pittsburgh'
df[(cat_0 | cat_1) & pitts]["stars"].mean()


# In[60]:


df["city_x"].unique()


# In[114]:


df["category_0"].nunique()


# In[62]:


df["categories"] = df["category_0"].str.cat(df["category_1"], sep = ',')


# In[121]:


df["categories"] = df["category_0"].str.cat(df["category_1"], sep=',')


# In[67]:


df[df["category_1"].str.contains("pizza")]


# In[124]:


df["rating"] = df["stars"] * 2


# In[68]:


df.head()


# In[76]:


def convert_to_rating(x):
    return(str(x)+ "out of 10")


# In[77]:


df["rating"] = df["rating"].apply(convert_to_rating)


# In[72]:


df.head()


# In[81]:


df.groupby(['city_x']).groups.keys()


# In[82]:


len(df.groupby(['city_x']).groups["Las Vegas"])


# In[83]:


import numpy as np
df.groupby(['city_x']).agg([np.sum, np.mean, np.std])["stars"]


# In[84]:


pivot_city = pd.pivot_table(df,index=["city_x"])


# In[85]:


pivot_city


# In[86]:


type(pivot_city)


# In[90]:


pivot_state_take = pd.pivot_table(df,index=["state_id", "take_out"])


# In[92]:


pivot_state_take


# In[96]:


bars_rest = df["category_0"].isin(["Bars", "Resraurants"])
df_bars_rest = df[bars_rest]


# In[97]:


df_bars_rest


# In[99]:


pivot_state_cat = pd.pivot_table(df_bars_rest, index = ["state_id", "city_x", "category_0"])


# In[101]:


pivot_state_cat[["review_count", "stars"]]


# In[102]:


import numpy as np
pivot_agg = pd.pivot_table(
    df,index=["state_id","city_x"],
    values=["review_count"],
    aggfunc=[np.sum]
)
pivot_agg


# In[103]:


pivot_a2 = pd.pivot_table(
    df,index=["state_id","city_x"],
    values=["review_count"],
    columns=["take_out"],
    aggfunc=[np.sum]
)
pivot_a2


# In[107]:


pivot_agg3 = pd.pivot_table(
df,index=["state_id","city_x"],
columns=["take_out"],
aggfunc={"review_count":np.sum,"stars":np.mean}
)
pivot_agg3



