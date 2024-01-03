'''import streamlit as st
import pandas as pd
import plotly.express as px

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"               # Load COVID-19 dataset
df = pd.read_csv(url)

st.sidebar.title("COVID-19 Dashboard")
selected_metrics = st.sidebar.multiselect(
    "Select Metrics",
    ["total_cases", "new_cases", "total_deaths", "new_deaths", "total_vaccinations", "people_vaccinated"],
    default=["total_cases", "new_cases", "total_deaths"]
)                                                                               # Sidebar

country = st.sidebar.selectbox("Select Country", df["location"].unique())       # Filter by country

filtered_df = df[df["location"] == country]                                     # Filter data

st.title(f"COVID-19 Data Visualization - {country}")                            # Main content

st.header("Line Chart")                                                         # Line Chart
fig_line = px.line(
    filtered_df,
    x="date",
    y=selected_metrics,
    title=f"{', '.join(selected_metrics)} over time",
)
st.plotly_chart(fig_line)

st.header("Bar Chart")                                                          # Bar Chart
fig_bar = px.bar(
    filtered_df,
    x="date",
    y=selected_metrics,
    title=f"{', '.join(selected_metrics)} over time",
)
st.plotly_chart(fig_bar)

st.header("Data Table")                                                         # Table
st.write(filtered_df[selected_metrics])

st.header("Map")                                                                # Map
filtered_df[selected_metrics[0]] = filtered_df[selected_metrics[0]].fillna(0)   # Handling NaN values in the size property
fig_map = px.scatter_geo(
    filtered_df,
    locations="iso_code",
    size=selected_metrics[0],
    title=f"{selected_metrics[0]} across countries",
)
st.plotly_chart(fig_map)






import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Load the dataset
file_path = 'C:\\Users\\CHIMURA\\Desktop\\DataEngineering\\all-states-history.csv'
df = pd.read_csv(file_path)

# Title of the dashboard
st.title('COVID-19 Data Visualization Dashboard')

# Display the raw dataset
st.subheader('Raw Data')
st.write(df)

# Sidebar for filtering options
st.sidebar.title('Filter Options')

# Select a specific state
selected_state = st.sidebar.selectbox('Select a State', df['state'].unique())

# Filter the data based on the selected state
filtered_data = df[df['state'] == selected_state]

# Line chart for daily positive cases
st.subheader(f'Daily Positive Cases in {selected_state}')
st.line_chart(filtered_data[['date', 'positiveIncrease']].set_index('date'))

# Bar chart for daily deaths
st.subheader(f'Daily Deaths in {selected_state}')
st.bar_chart(filtered_data[['date', 'deathIncrease']].set_index('date'))

# Line chart for hospitalizations
st.subheader(f'Hospitalizations in {selected_state}')
st.line_chart(filtered_data[['date', 'hospitalizedCurrently']].set_index('date'))

# Additional visualizations can be added based on your preference

# Show data table for the selected state
st.subheader(f'Data Table for {selected_state}')
st.write(filtered_data)

# Information about the dataset
st.sidebar.title('About the Dataset')
st.sidebar.info('This dataset contains COVID-19 related data for each state.')

# Show the last update date
st.sidebar.info(f'Last Updated: {df["date"].max()}')

#Line chart for Total Positive Cases:
st.subheader(f'Total Positive Cases Over Time in {selected_state}')
st.line_chart(filtered_data[['date', 'positive']].set_index('date'))

#Line chart for Total Deaths:
st.subheader(f'Total Deaths Over Time in {selected_state}')
st.line_chart(filtered_data[['date', 'death']].set_index('date'))

#Bar chart for Daily Hospitalization Increases:
st.subheader(f'Daily Hospitalization Increases in {selected_state}')
st.bar_chart(filtered_data[['date', 'hospitalizedIncrease']].set_index('date'))

# Scatter plot for Positive Cases vs. Total Tests with color representing Positive Increase
st.subheader(f'Positive Cases vs. Total Tests in {selected_state}')
scatter_chart = (
    alt.Chart(filtered_data)
    .mark_circle()
    .encode(
        x='totalTestsViral',
        y='positive',
        color='positiveIncrease',
        tooltip=['totalTestsViral', 'positive', 'positiveIncrease']
    )
    .interactive()
)

st.altair_chart(scatter_chart, use_container_width=True)

'''

import streamlit as st
import pandas as pd
import altair as alt

# Load the dataset
file_path = 'C:\\Users\\CHIMURA\\Desktop\\DataEngineering\\all-states-history.csv'
df = pd.read_csv(file_path)

# Function to display the raw data
def show_raw_data():
    st.subheader('Raw Data')
    st.write(df)

# Function to display the daily positive cases chart
def show_daily_positive_cases():
    st.subheader(f'Daily Positive Cases in {selected_state}')
    st.line_chart(filtered_data[['date', 'positiveIncrease']].set_index('date'))

# Function to display the daily deaths chart
def show_daily_deaths():
    st.subheader(f'Daily Deaths in {selected_state}')
    st.bar_chart(filtered_data[['date', 'deathIncrease']].set_index('date'))

# Function to display the hospitalizations chart
def show_hospitalizations():
    st.subheader(f'Hospitalizations in {selected_state}')
    st.line_chart(filtered_data[['date', 'hospitalizedCurrently']].set_index('date'))

# Function to display the total positive cases chart
def show_total_positive_cases():
    st.subheader(f'Total Positive Cases Over Time in {selected_state}')
    st.line_chart(filtered_data[['date', 'positive']].set_index('date'))

# Function to display the total deaths chart
def show_total_deaths():
    st.subheader(f'Total Deaths Over Time in {selected_state}')
    st.line_chart(filtered_data[['date', 'death']].set_index('date'))

# Function to display the daily hospitalization increases chart
def show_daily_hospitalization_increases():
    st.subheader(f'Daily Hospitalization Increases in {selected_state}')
    st.bar_chart(filtered_data[['date', 'hospitalizedIncrease']].set_index('date'))

# Function to display the scatter plot for positive cases vs. total tests
def show_scatter_plot():
    st.subheader(f'Positive Cases vs. Total Tests in {selected_state}')
    scatter_chart = (
        alt.Chart(filtered_data)
        .mark_circle()
        .encode(
            x='totalTestsViral',
            y='positive',
            color='positiveIncrease',
            tooltip=['totalTestsViral', 'positive', 'positiveIncrease']
        )
        .interactive()
    )
    st.altair_chart(scatter_chart, use_container_width=True)

# Title of the dashboard
st.title('COVID-19 Data Visualization Dashboard')

# Sidebar for filtering options
st.sidebar.title('Navigation')
page_options = ['Raw Data', 'Daily Positive Cases', 'Daily Deaths', 'Hospitalizations',
                 'Total Positive Cases', 'Total Deaths', 'Daily Hospitalization Increases', 'Scatter Plot']
selected_page = st.sidebar.radio('Select a Page', page_options)

# Select a specific state
selected_state = st.sidebar.selectbox('Select a State', df['state'].unique())

# Filter the data based on the selected state
filtered_data = df[df['state'] == selected_state]

# Display the selected page
if selected_page == 'Raw Data':
    show_raw_data()
elif selected_page == 'Daily Positive Cases':
    show_daily_positive_cases()
elif selected_page == 'Daily Deaths':
    show_daily_deaths()
elif selected_page == 'Hospitalizations':
    show_hospitalizations()
elif selected_page == 'Total Positive Cases':
    show_total_positive_cases()
elif selected_page == 'Total Deaths':
    show_total_deaths()
elif selected_page == 'Daily Hospitalization Increases':
    show_daily_hospitalization_increases()
elif selected_page == 'Scatter Plot':
    show_scatter_plot()

# Information about the dataset
st.sidebar.title('About the Dataset')
st.sidebar.info('This dataset contains COVID-19 related data for each state.')

# Show the last update date
st.sidebar.info(f'Last Updated: {df["date"].max()}')

