#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")


# In[5]:


print (soup.prettify)


# In[20]:


table = soup.find_all("table")[1]
print (table.prettify)


# In[29]:


game_titles = table.find_all(scope = "col")
print (table_titles)


# In[31]:


table_titles = [title.text.strip() for title in game_titles]
print (table_titles)


# In[33]:


cleaned_titles = [col.replace('[a]', '') for col in table_titles]
print(cleaned_titles)


# In[34]:


import pandas as pd


# In[35]:


df = pd.DataFrame(columns = cleaned_titles)

df


# In[83]:


table_rows = table.find_all("tr")[1:]
print(table_rows)


# In[98]:


# Iterate through each row and extract data
for row in table_rows:
    # Extract the year from the <th> tag within the <tr> tag
    year_tag = row.find("th")
    if year_tag:
        # Store the year text if available
        year = year_tag.text.strip()
    
    # Extract the data in <td> tags
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Add the year as the first element in the row data
    if individual_row_data:  # Make sure we have row data to avoid adding empty lists
        individual_row_data.insert(0, year)
    
    # Print or store the row data
    #print(individual_row_data)
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[99]:


df


# In[106]:


import pandas as pd
import matplotlib.pyplot as plt

# Group by 'Genre' and count the occurrences
genre_counts = df['Genre'].value_counts()

plt.figure(figsize=(12, 6))
plt.bar(genre_counts.index, genre_counts.values, color='skyblue')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Distribution of Game Genres for the Best Games of the Year')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()
plt.show()


# In[ ]:




