
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/Sleeksofficial/business-financial-analytics-portfolio/main/dashboards/sales_data_for_powerbi.csv")

# App
app = dash.Dash(__name__)

# KPIs
total_revenue = df["Revenue"].sum()
total_units = df["Units_Sold"].sum()

# Charts
line_chart = px.line(df, x="Date", y="Revenue", title="Revenue Over Time")
bar_chart = px.bar(df, x="Region", y="Revenue", title="Revenue by Region", color="Region")

# Layout
app.layout = html.Div(children=[
    html.H1("Sales Performance Dashboard"),
    html.Div([
        html.Div(f"Total Revenue: ${total_revenue:,.2f}", style={"padding": "10px", "fontSize": "20px"}),
        html.Div(f"Total Units Sold: {total_units:,}", style={"padding": "10px", "fontSize": "20px"}),
    ], style={"display": "flex", "justifyContent": "space-around"}),
    dcc.Graph(figure=line_chart),
    dcc.Graph(figure=bar_chart)
])

if __name__ == '__main__':
    app.run_server(debug=True)
