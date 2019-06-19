import xlwt
from xlwt import Workbook
import link

links=link.links()

wb = Workbook()
sheet1=wb.add_sheet('links','font: bold 1')

sheet1.write(0,0,'Links')
length=len(links)
for i in range(length):
    sheet1.write(i+1,0,links[i])

wb.save('data.xls')