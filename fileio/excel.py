## excel
from forest._importable import LazyImport


xlrd = LazyImport("import xlrd", "PACKAGE xlrd — retrieving information from a spreadsheet, derived from 'import xlrd', from https://github.com/python-excel/xlrd, Documentation: https://xlrd.readthedocs.io/en/latest/?badge=latest")
open_workbook = LazyImport("from xlrd import open_workbook", "FUNCTION xlrd.open_workbook — open a spreadsheet file for data extraction, derived from 'from xlrd import open_workbook', from https://github.com/python-excel/xlrd, Documentation: https://xlrd.readthedocs.io/en/latest/api.html")
xlwt = LazyImport("import xlwt", "PACKAGE xlwt — library for writing data and formatting information to older Excel files, derived from 'import xlwt', from https://github.com/python-excel/xlwt, Documentation: https://xlwt.readthedocs.io/en/latest/")
easyxf = LazyImport("from xlwt import easyxf", "FUNCTION xlwt.easyxf — a function to create and configure XFStyle objects, derived from 'from xlwt import easyxf', from https://github.com/python-excel/xlwt, Documentation: https://xlwt.readthedocs.io/en/latest/api.html")
openpyxl = LazyImport("import openpyxl", "PACKAGE openpyxl — library to read/write Excel 2010 xlsx,xlsm files, derived from 'import openpyxl', from https://bitbucket.org/openpyxl/openpyxl/src/default/, Documentation: https://openpyxl.readthedocs.io/en/stable/")
Workbook = LazyImport("from openpyxl import Workbook", "CLASS openpyxl.Workbook — a class that represents a workbook, derived from 'from openpyxl import Workbook', from https://bitbucket.org/openpyxl/openpyxl/src/default/, Documentation: https://openpyxl.readthedocs.io/en/stable/api/openpyxl.workbook.workbook.html#openpyxl.workbook.workbook.Workbook")
Worksheet = LazyImport("from openpyxl.worksheet.worksheet import Worksheet", "CLASS openpyxl.worksheet.worksheet.Worksheet — a class that represents a sheet in a workbook, derived from 'from openpyxl.worksheet.worksheet import Worksheet', from https://bitbucket.org/openpyxl/openpyxl/src/default/, Documentation: https://openpyxl.readthedocs.io/en/stable/api/openpyxl.worksheet.worksheet.html#openpyxl.worksheet.worksheet.Worksheet")
load_workbook = LazyImport("from openpyxl import load_workbook")
