import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load and prepare data
df = pd.read_csv("sales_data_for_powerbi.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Compute KPIs
total_revenue = df["Revenue"].sum()
total_units = df["Units_Sold"].sum()

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Sales Analytics Dashboard"

app.layout = html.Div([
    html.H1("📊 Sales Analytics Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.H3("Total Revenue"),
            html.P(f"${total_revenue:,.2f}", style={"fontSize": "24px", "color": "green"})
        ], className="card"),

        html.Div([
            html.H3("Total Units Sold"),
            html.P(f"{total_units:,}", style={"fontSize": "24px", "color": "blue"})
        ], className="card"),
    ], style={"display": "flex", "justifyContent": "space-around", "marginBottom": "30px"}),

    dcc.Graph(
        figure=px.line(df, x="Date", y="Revenue", title="Revenue Over Time")
    ),

    dcc.Graph(
        figure=px.bar(df, x="Product Category", y="Units_Sold", color="Product Category",
                      title="Units Sold by Product Category")
    ),

    html.Label("Select Region:"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{"label": r, "value": r} for r in df["Region"].unique()],
        value=df["Region"].unique()[0]
    ),
    dcc.Graph(id='region-revenue')
])

@app.callback(
    dash.dependencies.Output('region-revenue', 'figure'),
    [dash.dependencies.Input('region-dropdown', 'value')]
)
def update_region_chart(region):
    filtered = df[df["Region"] == region]
    fig = px.line(filtered, x="Date", y="Revenue", title=f"Revenue Over Time — {region}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
