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


for comparing_dbs in COMPARINGDBS_SET:
    for wl in CHARTSWLSREFRENCE:
        for (reccount, opcount) in CHARTCOUNTSREFRENCE:
            for thrd in CHARTTHREADCOUNTS:
                dbcompare_createchart(
                    CHARTSREFRENCE, comparing_dbs, wl, reccount, opcount, thrd)



# dbcompare_createchart('./ycsb-results-bothok-singlemongoMSSQL/', COMPARINGDBS, 'b', 1000, 1000, 1)
# resultsbasepath = CHARTRESULTPATH
# databases = COMPARINGDBS
# workload = 'a'
# rccount = opcount = 1000
# dbcompare_createchart('./ycsb-results-bothok-singlemongoMSSQL/', COMPARINGDBS, 'a', 1000, 1000, 4)
# for item in meansfilenumbers('./ycsb-results-mssqlok', 'mssql', 'e', 1000, 1000, 4):
#     print(item[0][0], item[0][1], item[1])
'''
- Throughput 765.1
SCAN AverageLatency 3166.4
SCAN 95thPercentileLatency 8216.3
SCAN 99thPercentileLatency 17151.0
INSERT AverageLatency 9026.2
INSERT 95thPercentileLatency 17567.0
INSERT 99thPercentileLatency 27636.3
'''
