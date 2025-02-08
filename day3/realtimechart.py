"""The assignment is to connect with the openweathermap api and receive the weather data for seven day
Then save the weather data to an excel file and create a chart of the weather."""

import requests
import logging
from datetime import datetime, timedelta,UTC
import openpyxl
from openpyxl.chart import BarChart, Reference

logging.basicConfig(filename="weather.log", level=logging.DEBUG, filemode="w",
                    format="Weather assignment - %(asctime)s - %(name)s - %(levelname)s - %(message)s")

def get_day(shift_seconds):
    """This function get UTC time and return Weekday abbreviated name"""
    utc_origin = datetime.now(UTC)
    # Calculate the shifted time
    shifted_time = utc_origin + timedelta(seconds=shift_seconds)
    shifted_day = shifted_time.strftime("%a")
    return shifted_day

def get_weather_from_api():
    """This function calls openweathermap and get next seven day forecast max temperature data"""
    #Mumbai url ="https://api.openweathermap.org/data/2.5/forecast/daily?lat=19.02&lon=72.51&cnt=7&appid=ca3f6d6ca3973a518834983d0b318f73"
    url = "https://api.openweathermap.org/data/2.5/forecast/daily?lat=17.04&lon=78.47&cnt=7&appid=ca3f6d6ca3973a518834983d0b318f73"
    response = requests.get(url)
    logging.info("response code from OpenWeatherMap %s", response.status_code)
    if response.ok:
        date = response.headers['Date']
        data=response.json()
        temp_data = []
        for i in range(7):
            day = get_day(data['list'][i]['dt'])
            min_temp = (data['list'][i]['temp']['min'])
            max_temp = (data['list'][i]['temp']['max'])
            temp_data.append((day,min_temp, max_temp))
        return date, temp_data
    else:
        logging.error("Sorry Bad response")

def createChart(date, temp_data):
    """Creates chart using the provided data and return the created file"""
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Weather Forecasts"
    max_temp, min_temp = -999999, 999999
    for i in range(len(temp_data)):
        sheet.append(temp_data[i])
        min_temp = min(min_temp, temp_data[i][1])
        max_temp = max(max_temp, temp_data[i][2])

    value = Reference(sheet, min_col=1, min_row=1, max_col=3, max_row=7)
    categories = Reference(sheet, min_col=1, min_row=1, max_row=7)
    chart = BarChart()
    chart.add_data(value)
    chart.set_categories(categories)
    chart.categoryNames = categories
    chart.type = "col"
    chart.style = 10
    chart.title = f"Weather forecast for Mumbai as of {date}"
    chart.x_axis.title = "Day"
    chart.y_axis.title = "Temperature"
    chart.gapWidth = 30
    chart.y_axis.scaling.min = min_temp-5
    chart.y_axis.scaling.max = max_temp+5
    chart.legend = None  # Remove the default legend
    sheet.add_chart(chart, "E4")
    wb.save("weather_forecast.xlsx")
    logging.info("Chart weather_forecast.xlsx created for %s", date)


if __name__ == "__main__":
    date, temp_data = get_weather_from_api()
    createChart(date, temp_data)