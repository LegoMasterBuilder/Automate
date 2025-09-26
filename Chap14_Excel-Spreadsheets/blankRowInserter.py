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
    N, M = int(sys.argv[1]), int(sys.argv[2])
    spreadsheet = sys.argv[3]
    # N = 3
    # M = 2
    # spreadsheet = './Automate_the_Boring_Stuff_3e_onlinematerials/example3.xlsx'

    wb1 = openpyxl.load_workbook(spreadsheet)
    sheetOrig = wb1['Sheet1']
    wb2 = openpyxl.Workbook()
    sheetNew = wb2['Sheet']

    for row in range(1, N):
        for col in range(1, sheetOrig.max_column + 1):
            column_letter = str(get_column_letter(col))
            row_number = str(row)
            cell_loc = column_letter + row_number
            if row == N:
                sheetNew[cell_loc] = " "
                break
            else: 
                sheetNew[cell_loc] = sheetOrig[cell_loc].value

    for row in range(N, sheetOrig.max_row + M+1):
        for col in range(1, sheetOrig.max_column + 1):
            column_letter = str(get_column_letter(col))
            row_number_old = str(row)
            row_number_new = str(row + M)
            cell_loc_old = column_letter + row_number_old
            cell_loc_new = column_letter + row_number_new
            sheetNew[cell_loc_new] = sheetOrig[cell_loc_old].value
            

    # Save changes to a .xlsx file.
    wb2.save('editBlank.xlsx')

except IndexError:
    print("Incomplete input. Please try again.")

except FileNotFoundError:
    print("File input not found. Please try again.")