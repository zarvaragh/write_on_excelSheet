# write_on_excelSheet

Write data and formulas to Excel spreadsheets from Python using `xlsxwriter`.

## Requirements

```bash
pip install xlsxwriter
```

## Usage

```bash
python write_on_excel.py
```

This creates `names.xlsx` with:

| Names | Scores |     | =SUM(B2:B4) |
|-------|--------|-----|-------------|
| Tom   | 70     |     |             |
| Hardy | 90     |     |             |

## What it demonstrates

- Writing headers and data rows with `worksheet.write(row, col, value)`
- Writing Excel formulas with `worksheet.write_formula(cell, formula)`
- Closing the workbook to flush the file to disk