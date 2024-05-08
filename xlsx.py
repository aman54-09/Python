"""import xlsxwriter
workbook = xlsxwriter.Workbook('D:\\aman\\abc.xls')
worksheet=workbook.add_worksheet()
chart = workbook.add_chart({'type':'column'})
data = [ [1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15] ]
worksheet.write_column('A1', data[0])
worksheet.write_column('B1', data[1])
worksheet.write_column('C1', data[2])
chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
chart.add_series({'values': '=Sheet1!$C$1:$C$5'})
worksheet.insert_chart('A7', chart)
workbook.close()"""



import xlsxwriter
workbook=xlsxwriter.Workbook("D:\\aman\\abc.xls")
worksheet=workbook.add_worksheet()
worksheet.set_column('A:A',20)
bold=workbook.add_format({'bold': True})

worksheet.write('A1', 'Hello')
worksheet.write('A2', 'world', bold)
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)
worksheet.insert_image('B5', 'mango.jpg')
workbook.close()
                
