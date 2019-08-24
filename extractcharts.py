from props import *
from definereqs import meansfilenumbers, definereqs
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as offline
from selenium import webdriver
import os


def save_png(imagepath, imagename, figure, width, height):
    offline.plot(figure, image='svg', auto_open=False,
                 image_width=width, image_height=height)
    driver = webdriver.PhantomJS(executable_path="./phantomjs")
    driver.set_window_size(width, height)
    driver.get('temp-plot.html')
    os.system("mkdir -p " + imagepath)
    driver.save_screenshot(imagepath + imagename)
    os.system("rm -rf temp-plot.html")

def dbscomparefigure(databases, values_names, values, values_title, chart_title):
    dt = []
    for i in range(0, len(values)):
        dt += [go.Bar(name=values_names[i], x=databases,
                      y=values[i], text=values[i], textposition='auto')]
    figure = go.Figure(data=dt)
    figure.update_xaxes(title_text="<b>Databases</b>")
    figure.update_yaxes(title_text="<b>%s</b>" % values_title)
    figure.update_layout(title_text="<b>%s</b>" % chart_title)
    figure.update_layout(barmode='group')
    return figure
# save_png('./','p.png', dbscomparefigure(COMPARINGDBS, ['read','load'],  [[1,3],[2,4]], 'values title', 'chart title'), CHARTWIDTH, CHARTHEIGHT)
# save_png('./','p.png', dbscomparefigure(COMPARINGDBS, ['read'],  [[1,3]], '', 'chart title'), CHARTWIDTH, CHARTHEIGHT)


def dbcompare_createchart(resultsbasepath, databases, workload, rccount, opcount, thrdcount):
    meanfilepath = None
    resultsfilepath = CHARTRESULTPATH
    all_results = []
    for req in definereqs(workload)[2]:
        all_results += [[req, []]]
    for db in databases:
        resultsfilepath += (db + '-')
        means = meansfilenumbers(
            resultsbasepath, db, workload, rccount, opcount, thrdcount)
        i = 0
        for mean in means:
            all_results[i][1] += [mean[1]]
            i += 1
    resultsfilepath = list(resultsfilepath)
    resultsfilepath[-1] = '/'
    resultsfilepath = ''.join(resultsfilepath)
    resultsfilepath = resultsfilepath + workload + '/' + 'rc-' + \
        str(rccount) + 'op' + str(opcount) + '/' + 'tc-' + str(thrdcount) + '/'

    throughputs = all_results[0][1]
    save_png(resultsfilepath, all_results[0][0][1]+'.png', dbscomparefigure(databases, [all_results[0][0][1]], [
             throughputs], 'Throughput (ops/sec)', 'Workload'+workload+" | Records = " + str(rccount) + " | Operations = "+str(opcount)), CHARTWIDTH, CHARTHEIGHT)

    values = [all_results[1][1], all_results[2][1], all_results[3][1]]
    names = [all_results[1][0][1], all_results[2][0][1], all_results[3][0][1]]
    save_png(resultsfilepath, all_results[1][0][0]+'.png', dbscomparefigure(
        databases, names, values, all_results[1][0][0] + ' (us)', 'Workload'+workload+" | Records = " + str(rccount) + " | Operations = "+str(opcount)), CHARTWIDTH, CHARTHEIGHT)

    if len(all_results) <= 4:
        return

    values = [all_results[4][1], all_results[5][1], all_results[6][1]]
    names = [all_results[4][0][1], all_results[5][0][1], all_results[6][0][1]]
    save_png(resultsfilepath, all_results[4][0][0]+'.png', dbscomparefigure(
        databases, names, values, all_results[4][0][0] + ' (us)', 'Workload'+workload+" | Records = " + str(rccount) + " | Operations = "+str(opcount)), CHARTWIDTH, CHARTHEIGHT)

def recordeffectfigure(databases, records, values, values_title, chart_title):
    dt = []
    for i in range(0, len(values)):
        dt += [go.Scatter(x=records, y=values[i], name=databases[i])]
    figure = go.Figure(data=dt)
    figure.update_xaxes(title_text="<b>Records/Opertation Count</b>")
    figure.update_yaxes(title_text="<b>%s</b>" % values_title)
    figure.update_layout(title_text="<b>%s</b>" % chart_title)
    return figure

def recordsizeeffectonthroughput_createchart(resultsbasepath, databases, workload, thrdcount, rec_op_set):
    meanfilepath = None
    resultsfilepath = CHARTRESULTPATH
    for db in databases:
        resultsfilepath += (db + '-')
    resultsfilepath = list(resultsfilepath)
    resultsfilepath[-1] = '/'
    resultsfilepath = ''.join(resultsfilepath)
    resultsfilepath = resultsfilepath + workload + '/' + 'tc-' + str(thrdcount) + '/'
    x = []    
    y = []
    for i in range(0, len(databases)):
        y += [[]]
        for (rec, op) in rec_op_set:
            x += [rec]
            y[i] += [op*1000/meansfilenumbers(CHARTSREFRENCE, databases[i], workload, rec, op, thrdcount)[0][1]]
    save_png(resultsfilepath, 'exectimeVSopcount.png', recordeffectfigure(databases, x, y, 'Total Execution Time (ms)', 'Workload'+wl), CHARTWIDTH, CHARTHEIGHT)

for comparing_dbs in COMPARINGDBS_SET:
    for wl in CHARTSWLSREFRENCE:
        for thrd in CHARTTHREADCOUNTS:
            for (reccount, opcount) in CHARTCOUNTSREFRENCE:
                dbcompare_createchart(
                    CHARTSREFRENCE, comparing_dbs, wl, reccount, opcount, thrd)
        recordsizeeffectonthroughput_createchart(CHARTSREFRENCE, comparing_dbs, wl, thrd, CHARTCOUNTSREFRENCE)