import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data", hovertext=["Text A", "Text B", "Text C"] ),
    secondary_y=True
)
fig.add_trace(
    go.Bar(x=[1,5], y=[0.5, 3.5], name="yaxis2 data"),
    secondary_y=True
)

fig.update_xaxes(title_text="<b>xaxis</b> title")

fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondory</b> yaxis title", secondary_y=True)

fig.show()

# fig = go.Figure()

# fig.add_trace(
#     go.Scatter(
#         x=[0, 1, 2, 3, 4, 5],
#         y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
#     ))

# fig.add_trace(
#     go.Bar(
#         x=[0, 1, 2, 3, 4, 5],
#         y=[1, 0.5, 0.7, -1.2, 0.3, 100]
#     ))

# fig.show()