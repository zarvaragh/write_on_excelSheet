import xlsxwriter

out_work_book = xlsxwriter.Workbook('names.xlsx')
outSheet = out_work_book.add_worksheet()

#declare Data
names = ['Tom', 'Hardy']
values = [70, 90]

#write Headers
outSheet.write('A1', 'Names')
outSheet.write('B1', 'Scores')

#write data to file 
# outSheet.write(1, 0 , names[0]) # 1 s representing the y axis and 0 is x. so y comes first
for y in range(len(names)):
    # outSheet.write(y, x, names[])
    outSheet.write(y+1, 0, names[y])


#Write a formula for a cell 
outSheet.write_formula('D2', "=SUM(B2:B4")

out_work_book.close()
