import xlsxwriter

out_work_book = xlsxwriter.Workbook("names.xlsx")
out_sheet = out_work_book.add_worksheet()

names = ["Tom", "Hardy"]
values = [70, 90]

out_sheet.write("A1", "Names")
out_sheet.write("B1", "Scores")

for y in range(len(names)):
    out_sheet.write(y + 1, 0, names[y])
    out_sheet.write(y + 1, 1, values[y])

# Fixed: was missing closing parenthesis
out_sheet.write_formula("D2", "=SUM(B2:B4)")

out_work_book.close()