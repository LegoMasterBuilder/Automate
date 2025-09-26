#blankRowInserter.py

# Create a program blankRowInserter.py that takes two integers and a filename 
# string as command line arguments. Let’s call the first integer N and the 
# second integer M. Starting at row N, the program should insert M blank rows 
# into the spreadsheet. For example, when the program is run like this:

# python blankRowInserter.py 3 2 myProduce.xlsx

import sys, openpyxl
from openpyxl.utils import get_column_letter

try:
    # Set row N and M blank rows.
    # N, M = int(sys.argv[1]), int(sys.argv[2])
    # spreadsheet = sys.argv[3]
    N = 3
    M = 2
    spreadsheet = './Automate_the_Boring_Stuff_3e_onlinematerials/example3.xlsx'

    wb = openpyxl.load_workbook(spreadsheet)
    sheet = wb.active
    factor = 0

    for row in range(1, N):
        for col in range(1, sheet.max_column + 1):
            column_letter = str(get_column_letter(col))
            row_number = str(row + factor)
            cell_loc = column_letter + row_number
            if row == N:
                break
            else: 
                print(row)
                # print(sheet[cell_loc])
                # sheet.cell(row=row, column=col).value = sheet[cell_loc]

    for row in range(N+M, sheet.max_row + M+1):
        for col in range(1, sheet.max_column + 1):
            column_letter = str(get_column_letter(col))
            row_number = str(row + factor)
            cell_loc = column_letter + row_number
            while M > 0:
                M -= 1
                print("blank")
            print(row)
            

    # Save changes to a .xlsx file.
    wb.save('blankRowInserted.xlsx')

except IndexError:
    print("Incomplete input. Please try again.")

# except FileNotFoundError:
#     print("File input not found. Please try again.")