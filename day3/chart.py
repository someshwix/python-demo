#openpyxl:
import openpyxl
#import bar  chart class from openpyxl.chart from sub module
from openpyxl.chart import BarChart,Reference
wb=openpyxl.Workbook()
sheet=wb.active 
for i in range(10):
    sheet.append([i])

values = Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)    
chart=BarChart()
chart.add_data(values)
chart.tittle="BAR-chart"
chart.x_axis.tittle="x_AXIS"
chart.y_axis.tittle="Y_AXIS"
sheet.add_chart(chart,"E5")
wb.save("barchart.xlsx")
print("Bar chart created ... open barchart.xlsx")