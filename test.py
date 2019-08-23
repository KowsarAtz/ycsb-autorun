from extractcharts import *

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"), text=y, textposition='auto',
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data",
               hovertext=["Text A", "Text B", "Text C"]),
    secondary_y=False
)
# fig.add_trace(
#     go.Bar(x=[1, 5], y=[0.5, 3.5], name="yaxis2 data"),
#     secondary_y=True
# )

fig.update_xaxes(title_text="<b>xaxis</b> title")

fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondory</b> yaxis title", secondary_y=True)


save_png('./','p.png', fig, 2000, 1000)