import justpy as jp
import pandas
from pytz import utc
from datetime import datetime

data = pandas.read_csv("amazon.csv", parse_dates = ["reviews.date"], low_memory=False)

data["Month"] = data["reviews.date"].dt.strftime("Y: %Y M: %m")
month_avg_c = data.groupby(["Month", "name"])["reviews.rating"].mean(["reviews.rating"]).unstack()

chart_type = """
{
    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },
    title: {
        floating: true,
        align: 'center',
        text: ''
    },
    subtitle: {
        floating: true,
        align: 'center',
        y: 30,
        text: ''
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: ''
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Soviet Union fell,<br>Germany united'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    series: [{}],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis on Amazon Data (Ratings)", classes = "text-h1 text-center q-pa-md")
    h2 = jp.QDiv(a = wp, text = "Average of Ratings left on each Product Grouped by Months", classes = "text-h5 text-center q-pa-md")
    hc = jp.HighCharts(a = wp, options = chart_type)
    hc.options.chart.inverted = False
    hc.options.xAxis.categories = list(month_avg_c.index)
    hc_data = [{"name": v1, "data": [v2 for v2 in month_avg_c[v1]]} for v1 in month_avg_c.columns]
    hc.options.title.text = "Amazon's own product Ratings"
    hc.options.series = hc_data
    return wp

jp.justpy(app)