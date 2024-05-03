from dash import Dash,html,dash_table,dcc
import plotly.express as px
import  pandas as pd
app=Dash(__name__)

data=pd.read_csv("C:\\Users\\admin\\Downloads\\Global YouTube Statistics.csv",encoding="latin1")

country_data = data.groupby('Country').agg({'subscribers': 'sum', 'video views': 'sum'}).reset_index()

# Create choropleth map figure
fig = px.choropleth(country_data, 
                    locations='Country', 
                    locationmode='country names', 
                    color='subscribers',
                    hover_name='Country', 
                    projection='natural earth',
                    title='Total Subscribers by Country')

# App layout
app.layout = html.Div([
    html.Div(children="cs data"),
    dash_table.DataTable(data.to_dict("records"),page_size=10),
    html.H1("Choropleth Map Dashboard"),
    dcc.Graph(figure=fig)  # Display choropleth map
])

if __name__=="__main__":
    app.run(debug=True)