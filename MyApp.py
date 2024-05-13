# import streamlit as st
# import streamlit as yt
# import pandas as pd

import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from temperature;', ttl=600)

# Print results.
st.write("The temperature Data")
for row in df.itertuples():

    st.write(f"{row.new_id} has a : {row.Temperature} on :{row.Date}:")


# st.write(""" # Human development Index""")
#
# df = pd.read_excel("HDI data.xlsx")
#
# if st.button('Open Data 1'):
#     st.write('Table is displayed')
#     st.table(df)
# else:
#     st.write('Table is hidden')
#
# yt.write(""" # Production yield Prediction""")
#
# yd = pd.read_csv("yield.csv")
#
# if yt.button('Open Data 2'):
#         yt.write('Table is displayed')
#         yt.table(yd)
# else:
#         yt.write('Table is hidden')
