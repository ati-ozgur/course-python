# to be able to use following code
# I need to install the packages using pip
# pip install altair
# pip install altair_viewer
import pandas as pd
import altair as alt



df = pd.read_csv('seattle-weather.csv')
chart = alt.Chart(df)

alt.Chart(df).mark_circle().encode(
    x=alt.X('temperature', bin=True),
    y=alt.Y('wind', bin=True),
    size='count()'
).show()

