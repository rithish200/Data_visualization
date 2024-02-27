import justpy as jp
import pandas
from pytz import utc
from datetime import datetime

data = pandas.read_csv("amazon.csv", parse_dates = ["reviews.date"], low_memory=False)

data["Month"] = data["reviews.date"].dt.strftime("Y: %Y M: %m")
month_avg = data.groupby(["Month"]).mean(["reviews.rating"])

chart_type = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Amazon Ratings on Various Products'
    },
    subtitle: {
        text: 'Grouped by Months'
    },
    xAxis: {
        reversed: false,
        title: {
        enabled: true,
        text: 'Weeks'
        },
        labels: {
        format: '{value}'
        },
        accessibility: {
        rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
        text: 'Average Rating'
        },
        labels: {
        format: '{value}'
        },
        accessibility: {
        rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: ' Average of {point.y} Stars on this month'
    },
    plotOptions: {
        spline: {
        marker: {
            enable: false
        }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
        [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis on Amazon Data (Ratings)", classes = "text-h1 text-center q-pa-md")
    br = jp.Br(a = wp)
    hc = jp.HighCharts(a = wp, options = chart_type)
    hc.options.chart.inverted = False
    hc.options.xAxis.categories = list(month_avg.index)
    hc.options.title.text = "Amazon's own product Ratings"
    hc.options.series[0].name =  "Rating"  
    hc.options.series[0].data = list(month_avg["reviews.rating"])
    return wp

jp.justpy(app)