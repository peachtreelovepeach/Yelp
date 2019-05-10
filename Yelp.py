# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:47:08 2019

@author: yvain
"""
#Library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3


business = pd.read_csv("yelp_business.csv")
#business_attributes = pd.read_csv("yelp_business_attributes.csv")
#business_hours = pd.read_csv("yelp_business_hours.csv")
#check_in = pd.read_csv("yelp_checkin.csv")
reviews = pd.read_csv("yelp_review.csv")
#tip = pd.read_csv("yelp_tip.csv")
#user = pd.read_csv("yelp_user.csv")


#print(business.info())
#print(list(business))
##business columns:['business_id', 'name', 'neighborhood', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'categories']


#######
##Rating
####### 
#Get the distribution of the ratings
x=business['stars'].value_counts()
x=x.sort_index()
#plot
plt.figure(figsize=(8,4))
ax= sns.barplot(x.index, x.values, alpha=0.8)
plt.title("Star Rating Distribution")
plt.ylabel('# of businesses', fontsize=12)
plt.xlabel('Star Ratings ', fontsize=12)

#adding the text labels
rects = ax.patches
labels = x.values
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')

plt.show()

'''
Most of the rateings are 3.5 and 4.0. Approximitly normal distribution.
Let's see what features the 5 star business have 
and what's the difference between 5 star and 4.5
'''

#use sqlite 
def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

connect('yelp data.db')


# Select all entries of 5 stars
c.execute("""SELECT * FROM yelp_business
           WHERE stars = '5.0'""")
fivestars = c.fetchall()
print(fivestars[1])


c.execute("""SELECT text, business_id FROM yelp_review
          GROUP BY business_id
          """)
review = c.fetchall()
print(review[1])
'''
Table information




def close(conn):
    """ Commit changes and close connection to the database """
    # conn.commit()
    conn.close()


def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = cursor.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]


def table_col_info(cursor, table_name, print_out=False):
    """ Returns a list of tuples with column informations:
    (id, name, type, notnull, default_value, primary_key)
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()

    if print_out:
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    return info


def values_in_col(cursor, table_name, print_out=True):
    """ Returns a dictionary with columns as keys
    and the number of not-null entries as associated values.
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()
    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0
    for col in col_dict:
        c.execute('SELECT ({0}) FROM {1} '
                  'WHERE {0} IS NOT NULL'.format(col, table_name))
        # In my case this approach resulted in a
        # better performance than using COUNT
        number_rows = len(c.fetchall())
        col_dict[col] = number_rows
    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))
    return col_dict


if __name__ == '__main__':

    sqlite_file = 'my_first_db.sqlite'
    table_name = 'my_table_3'

    conn, c = connect(sqlite_file)
    total_rows(c, table_name, print_out=True)
    table_col_info(c, table_name, print_out=True)
    # next line might be slow on large databases
    values_in_col(c, table_name, print_out=True)

    close(conn)
'''


















 #Which city get most reviews
 #Get the distribution of the ratings
 x=business['city'].value_counts()
 x=x.sort_values(ascending=False)
 x=x.iloc[0:20]
 plt.figure(figsize=(16,4))
 ax = sns.barplot(x.index, x.values, alpha=0.8, color='blue')
 plt.title("Which city has the most reviews?")
 locs, labels = plt.xticks()
 plt.setp(labels, rotation=45)
 plt.ylabel('# businesses', fontsize=12)
 plt.xlabel('City', fontsize=12)

 #adding the text labels
 rects = ax.patches
 labels = x.values
 for rect, label in zip(rects, labels):
     height = rect.get_height()
     ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')

 plt.show()

 '''
 Vegas has most reviews
 Look into vegas next
 '''



# # categories_list = list(business.categories.unique())
# # #print(categories_list)

# # ##Mexican food category list
# # mex_cate = ['Mexican']
# # mex_busn = business[business['categories'].str.contains('|'.join(mex_cate))]
