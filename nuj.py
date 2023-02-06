import streamlit as st

import pandas as pd


import plotly.express as px
st.set_page_config(page_title="Sales Analysis",
                   page_icon="data:image/jpeg;base64,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",
                   layout="wide"
                   )
#------------------------------------------------------------------------------------------
url="https://raw.githubusercontent.com/NUJEL-NIGS-NS/streamlit1/master/rivcl.csv"
df=pd.read_csv(url)
st.title("Sales PieChart Total")
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
