import streamlit as st

import pandas as pd


import plotly.express as px

#------------------------------------------------------------------------------------------
url="https://raw.githubusercontent.com/NUJEL-NIGS-NS/streamlit1/master/pages/1year_onl.csv"
df=pd.read_csv(url)
st.sidebar.header("pages")
fi = px.pie(df, values="Outwards",
             names="Product"
            )

st.plotly_chart(fi)

st.title("Analysis Of Each Product")
pro= st.selectbox("Product",
               options=df['Product'].unique())
d1=df.query("Product== @pro")
fig_s=px.bar(d1,
          y="Outwards",
          x="State",
        orientation="v",
        color="Particulars",barmode = 'group'

          )
st.plotly_chart(fig_s)
st.title("Statewise PieChart")

sta= st.selectbox("State",
                   options=df['State'].unique()

                   )
d = df.query("State ==@sta")
fig = px.pie(d, values="Outwards",
             names="Product",
             hole=.3)

st.plotly_chart(fig)

st.title("Sales Datewise and Productwise")
my=st.multiselect("Month and Year",options=df['Date'].unique())
po=st.multiselect("Product",options=df['Product'].unique())

d11=df.query("Date==@my and Product== @po")
fig_3=px.bar(d11,
          y="Outwards",
          x="State",
        orientation="v",
        color="Particulars"

          )

st.plotly_chart(fig_3)
