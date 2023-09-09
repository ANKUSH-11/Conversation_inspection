import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import functions
import data_df
import nltk


st.sidebar.title("conversation_inspection")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = data_df.df(data)
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    # stats Area
    tag_mem = st.sidebar.selectbox("Show analysis wrt", user_list)
    if st.sidebar.button("Show Analysis"):
        num_messages = functions.Total_mssge(tag_mem, df)
        words = functions.num_words(tag_mem, df)
        num_media_messages = functions.num_med(tag_mem, df)
        st.title("Top statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header("media shared")
            st.title(num_media_messages)
        # monthly_timeline
        st.title("Monthly Timeline")
        timeline = functions.month_active(tag_mem, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color="red")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily_timeline
        st.title("Daily Timeline")
        daily_timeline = functions.daily_active(tag_mem, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color="black")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        # activity
        st.title('Activity Map')
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most busy day")
            busy_day = functions.active_weekly(tag_mem, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("Most busy month")
            busy_month = functions.active_monthly(tag_mem, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="red")
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        st.title("Weekly activity map")
        user_heatmap = functions.hm_act(tag_mem, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
        # finding the busiest users in the(group level)

        if tag_mem == 'Overall':
            st.title('Most busy users')
            x = functions.busy_us_1(tag_mem, df)
            new_df = functions.busy_us_2(tag_mem, df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # WorldCloud
        st.title("Wordcloud")
        df_wc = functions.w_c(tag_mem, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
        # most common words
        cw_df = functions.most_cw(tag_mem, df)
        fig, ax = plt.subplots()
        ax.barh(cw_df[0], cw_df[1])
        plt.xticks(rotation='vertical')
        st.title("most common words")
        st.pyplot(fig)
        # Area Chart
        st.title('Area_chart')
        x = functions.busy_us_1(tag_mem, df)
        new_df = functions.busy_us_2(tag_mem, df)
        fig, ax = plt.subplots()
        ax.stackplot(x.index, x.values, color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        #Area Chart2
        st.title('Chart')
        new_df = functions.busy_us_2(tag_mem, df)
        sorted_df = new_df.sort_values(by='count')
        x =[]
        x=sorted_df['user'].astype(str)
        y =[]
        y =sorted_df['count'].astype(str)
        fig, ax = plt.subplots()
        ax.stackplot(x[-10:],y[-10:], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

"""
        new_df = pd.DataFrame(df, columns=["date", "user", "message"])
        from nltk.sentiment.vader import SentimentIntensityAnalyzer

        sentiments = SentimentIntensityAnalyzer()
        new_df["sentiment"] = new_df["message"].apply(lambda message: sentiments.polarity_scores(message))
        new_df["positive"] = new_df["sentiment"].apply(lambda score: score["pos"])
        new_df["negative"] = new_df["sentiment"].apply(lambda score: score["neg"])
        new_df["neutral"] = new_df["sentiment"].apply(lambda score: score["neu"])
        new_df = new_df.drop("sentiment", axis=1)
        new_df.head(10)"""