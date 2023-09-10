import pandas as pd
from wordcloud import WordCloud ,STOPWORDS, ImageColorGenerator
from collections import Counter
import emoji
import matplotlib.pyplot as plt
#import nltk
#nltk.download()




def Total_mssge(tag_mem,df):
   if tag_mem !='Overall':
        df1=df[df['user'] == tag_mem]
        #fetch the number of messages
        num_messages =df1.shape[0]
        #fetch the total number of words
        return num_messages

   else:
        num_messages= df.shape[0]
        return num_messages



def num_words(tag_mem,df):
    if tag_mem != 'Overall':
        df1 = df[df['user'] == tag_mem]
        words=[]
        for message in df1['message']:
            words.extend(message.split())
        return len(words)
    else:

        words = []
        for message in df['message']:
            words.extend(message.split())
        return len(words)
def num_med(tag_mem,df):
    if tag_mem != 'Overall':
       df1 = df[df['user']==tag_mem]
       new_df=df1[df1['message']=='<Media omitted>\n']
       med_messages = new_df.shape[0]
       return med_messages
    else:
       med_messages=df[df['message']=='<Media omitted>\n'].shape[0]
       return med_messages

def busy_us_1(tag_mem,df):
       new_df= df['user'].value_counts().head()
       x=new_df
       return x
def busy_us_2(tag_mem,df):
        x = df['user'].value_counts()
        y = df.shape[0]
        z = (x / y) * 100
        data = z.reset_index().rename(columns={'index': 'name', 'users': 'percent'})
        df1 = pd.DataFrame(data)
        new_df = df1.round(2)
        return new_df
def w_c(tag_mem,df):

    if tag_mem !='Overall':
        df1=df[df['user']==tag_mem]
        wc =WordCloud(width=500,height=500,min_font_size=10,background_color='white')
        df_wc =wc.generate(df1['message'].str.cat(sep=" "))

        return df_wc
    else:
        wc =WordCloud(width=500,height=500,min_font_size=10,background_color='white')
        df_wc =wc.generate(df['message'].str.cat(sep=" "))
        return df_wc
def most_cw(tag_mem,df):
    if tag_mem != 'Overall':
        df = df[df['user'] == tag_mem]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    for message in temp['message']:
        words.extend(message.split())
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def month_active(tag_mem,df):
    if tag_mem != 'Overall':
        df = df[df['user'] == tag_mem]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + '-' + str(timeline['year'][i]))
    timeline['time']= time
    return timeline
def daily_active(tag_mem,df):
    if tag_mem!='Overall':
       df=df[df['user']==tag_mem]
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline
def active_weekly(tag_mem,df):
    if tag_mem != 'Overall':
        df = df[df['user'] == tag_mem]
    return  df['day_name'].value_counts()
def active_monthly(tag_mem,df):
         if tag_mem != 'Overall':
            df = df[df['user'] == tag_mem]
         return df['month'].value_counts()
def hm_act(tag_mem,df):
    if tag_mem != 'Overall':
        df = df[df['user'] == tag_mem]
    user_heatmap=df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)
    return user_heatmap





















