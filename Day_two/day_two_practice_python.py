# reading and reading/writing data from and to excel in python
import openpyxl

wb = openpyxl.load_workbook("data.xlsx")
ws = wb['Sheet1']
s = ws['B2'].value
print(s)
# OR

s = ws.cell(row=3, column=3).value
print(s)

# OR
data = ws['A1':'C5']
for i in range(len(data)):
    for j in range(len(data[0])):
        print((data[i][j]).value)

for a, b, c in data:
    print(str(a.value) + " " + str(b.value) + " " + str(c.value))
