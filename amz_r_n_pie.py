import justpy as jp
import pandas
from pytz import utc
from datetime import datetime

data = pandas.read_csv("amazon.csv", parse_dates = ["reviews.date"], low_memory=False)

count_ratings = data.groupby(["name"])["reviews.rating"].count()

chart_type = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '{point.name}: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis on Amazon Data (Ratings)", classes = "text-h1 text-center q-pa-md")
    h2 = jp.QDiv(a = wp, text = "Grouped by Number of Ratings left on each Product", classes = "text-h5 text-center q-pa-md")
    hc = jp.HighCharts(a = wp, options = chart_type)
    hc.options.xAxis.categories = list(count_ratings.index)
    hc_data = [{"name": v1, "y": v2} for v1, v2 in zip(count_ratings.index, count_ratings)]
    hc.options.title.text = "Amazon's own product Ratings"
    hc.options.series[0].data = hc_data
    return wp

jp.justpy(app)
