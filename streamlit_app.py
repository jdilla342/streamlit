import streamlit as st
st.title("Online Retail")
## !!! date options
date = st.sidebar.selectbox(
            "Select a Invoice Date Range",
            [
              "'2010-12-01' and '2011-01-01'", 
              "'2010-12-01' and '2010-12-15'"              
            ])
## !!! product options           
product = st.sidebar.selectbox(
            "Select a Product",
            [
              'CHOCOLATE HOT WATER BOTTLE', 
              'GREY HEART HOT WATER BOTTLE', 
              'JUMBO BAG PINK POLKADOT', 
              'WHITE METAL LANTERN'
            ])

## Take in the query
df_series = pd.read_sql(timeSeries_query, engine)
df_series['InvoiceDate'] = pd.to_datetime(df_series['InvoiceDate']) 

## Line chart 
plt.rc('figure', figsize=(10, 5))
fig, ax = plt.subplots()

sns.lineplot(data=df_series, x='InvoiceDate', y='Total_Sale_Amt', hue='Description', style='Description', 
             linewidth=0.8, marker='o')
start, end = ax.get_xlim()
plt.xticks(ticks=np.arange(start, end, 2), ## 2 days apart
           rotation=45, ha='right')
