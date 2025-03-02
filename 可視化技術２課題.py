import streamlit as st 
import pandas as pd 
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import ipywidgets as widgets 
import seaborn as sns
from ipywidgets import interact
plt.rcParams['font.family'] = 'Meiryo' 

st.subheader('コメント総数可視化') 

dflive=pd.read_csv("ライブコメントスクレイピング(西園21~22章)（分析用）.csv")
df_ban=pd.read_csv("Banコメントデータ(西園21~22章)（分析用）.csv")

def plot_plot(time,col):
    dflive["投稿時間"]=pd.to_datetime(dflive['投稿時間'])
    dflive_re=dflive.set_index('投稿時間')
    dflive_re=dflive_re.resample(time).count()
    dflive_re=dflive_re.drop(["ユーザ名","コメント","コメント文字数","コメントID"],axis="columns")
    dflive_re.columns=["総コメント総数"]
    df_ban["投稿時間"]=pd.to_datetime(df_ban['投稿時間'])
    df_ban_new_re=df_ban.set_index('投稿時間')
    df_ban_new_re=df_ban_new_re.resample(time).count()
    df_ban_new_re=df_ban_new_re.drop(["ユーザ名","コメント","コメント文字数","コメントID"],axis="columns")
    dflive_re["削除コメント総数"]=df_ban_new_re
    sns.lineplot(dflive_re[col])
    plt.show()
i = widgets.Dropdown(value='総コメント総数', options=["総コメント総数","削除コメント総数"],description="データ") 
t=widgets.Dropdown(value="30T", options=["10T","30T","H","2H"],  description="時間間隔")
st.pyplot(interact(plot_plot,time=t,col=i) )

def plot_plot(time):
    dflive["投稿時間"]=pd.to_datetime(dflive['投稿時間'])
    dflive_re=dflive.set_index('投稿時間')
    dflive_re=dflive_re.resample(time).count()
    dflive_re=dflive_re.drop(["ユーザ名","コメント","コメント文字数","コメントID"],axis="columns")
    dflive_re.columns=["総コメント総数"]
    df_ban["投稿時間"]=pd.to_datetime(df_ban['投稿時間'])
    df_ban_new_re=df_ban.set_index('投稿時間')
    df_ban_new_re=df_ban_new_re.resample(time).count()
    df_ban_new_re=df_ban_new_re.drop(["ユーザ名","コメント","コメント文字数","コメントID"],axis="columns")
    dflive_re["削除コメント総数"]=df_ban_new_re
    fig, ax = plt.subplots() 
    ax.plot(dflive_re["総コメント総数"]/dflive_re["総コメント総数"].sum()) 
    ax.plot(dflive_re["削除コメント総数"]/dflive_re["削除コメント総数"].sum())
    plt.show() 
t=widgets.Dropdown(value="30T", options=["10T","30T","H","2H"],  description="時間間隔")
st.pyplot(interact(plot_plot,time=t) )