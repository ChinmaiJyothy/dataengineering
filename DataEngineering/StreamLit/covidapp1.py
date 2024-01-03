import streamlit as st
import pandas as pd
import plotly.express as px

file_path = 'C:\\Users\\CHIMURA\\Desktop\\DataEngineering\\all-states-history.csv'
covid_data = pd.read_csv(file_path)

page = st.sidebar.selectbox("Choose a page", ["Overview", "Death", "Hospitalization", "Testing", "Positive Cases", "Recovered"])

st.title("COVID-19 Data Visualization Dashboard")

if page == "Overview":
    st.write("## Overview Page")
    
    # Add general overview visualizations here

    # Display the data table for the overview page
    st.write("### Raw Data")
    st.dataframe(covid_data)
    
elif page == "Death":
    st.write("## Death Page")
    fig_death = px.line(covid_data, x="date", y=["death", "deathIncrease"], labels={"value": "Count", "variable": "Type"}, title="Death Trends")
    st.plotly_chart(fig_death)

    fig_death_probable = px.line(covid_data, x="date", y="deathProbable", title="Probable Death Trends")
    st.plotly_chart(fig_death_probable)

elif page == "Hospitalization":
    st.write("## Hospitalization Page")
    fig_hospitalized = px.line(covid_data, x="date", y=["hospitalizedCurrently", "hospitalizedIncrease"], labels={"value": "Count", "variable": "Type"}, title="Hospitalization Trends")
    st.plotly_chart(fig_hospitalized)

    fig_icu = px.line(covid_data, x="date", y=["inIcuCurrently", "inIcuCumulative"], labels={"value": "Count", "variable": "Type"}, title="ICU Trends")
    st.plotly_chart(fig_icu)

elif page == "Testing":
    st.write("## Testing Page")
    # Add visualizations for testing-related fields
    fig_testing = px.line(covid_data, x="date", y=["totalTestsViral", "positiveTestsViral"], labels={"value": "Count", "variable": "Type"}, title="Testing Trends")
    st.plotly_chart(fig_testing)

elif page == "Positive Cases":
    st.write("## Positive Cases Page")
    # Add visualizations for positive cases-related fields
    fig_positive_cases = px.line(covid_data, x="date", y=["positive", "positiveIncrease"], labels={"value": "Count", "variable": "Type"}, title="Positive Cases Trends")
    st.plotly_chart(fig_positive_cases)

elif page == "Recovered":
    st.write("## Recovered Page")
    # Add visualizations for recovered-related fields
    fig_recovered = px.line(covid_data, x="date", y="recovered", title="Recovered Trends")
    st.plotly_chart(fig_recovered)

# Information about the dataset
st.sidebar.title('About the Dataset')
st.sidebar.info('This dataset contains COVID-19 related data overall.')

# Show the last update date
st.sidebar.info(f'Last Updated: {covid_data["date"].max()}')
