# exempel från YT guide "https://www.youtube.com/watch?v=sogNluduBQQ"
# pip install streamlit för att komma åt biblioteket
# via kommando "streamlit run python-filens-namn.py" så öppnas webbapplikationen i browsern och man får en lokal URL att interagera med

# Import the necessary libraries

import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Create file uploader object
upload_file = st.file_uploader('Upload a file containing earthquake data')

# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:

    # Read the file to a dataframe using pandas
    df = pd.read_csv(upload_file)

    # Create a section for the dataframe statistics
    st.header('Statistics of Dataframe')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.write(df.head())

    # Create a section for matplotlib figure
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig)