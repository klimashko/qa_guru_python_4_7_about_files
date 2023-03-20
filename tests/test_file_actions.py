import pytest
from PyPDF2 import PdfReader
from selene import browser
import os
import csv
from zipfile import ZipFile
import io
import PyPDF2
import codecs
from openpyxl import load_workbook




# def test_zip_csv():
#     with open('addresses_1.csv') as file:
#         rows = [row for row in csv.reader(file)]
#         first_row_in_csv_file = rows[0]
#
#
#     with ZipFile(os.path.join(os.path.dirname(__file__), "resources", "addresses_1_csv.zip"), "w") as my_zip:
#         my_zip.write('addresses_1.csv')
#     with ZipFile('resources/addresses_1_csv.zip') as myzip:
#         with myzip.open('addresses_1.csv', 'r') as csv_file:
#             rows_from_zip = [row for row in csv.reader(codecs.iterdecode(csv_file, 'utf-8'))]
#             first_row_in_csv_file_from_zip = rows_from_zip[0]
#
#     assert first_row_in_csv_file_from_zip == first_row_in_csv_file, 'First row not matched'




def test_zip_xlsx():
    with open('sample2.xlsx') as file:
        cell = load_workbook('sample2.xlsx').active.cell(row=1, column=2).value
        print(cell)


    with ZipFile(os.path.join(os.path.dirname(__file__), "resources", "sample2_xlsx.zip"), "w") as new_zip:
         new_zip.write("sample2.xlsx")
    with ZipFile("resources/sample2_xlsx.zip") as myzip:
        with myzip.open('sample2.xlsx', 'r') as xlsx_file:
            cell_xlsx_file_from_zip = load_workbook(xlsx_file).active.cell(row=1, column=2).value
            print(cell_xlsx_file_from_zip)


    assert cell == cell_xlsx_file_from_zip


# def test_zip_pdf():
#     num_pages_pdf_file = len(PdfReader('example3.pdf').pages)
#     text_1page_pdf_file = PdfReader('example3.pdf').pages[0].extract_text()
#
#
#     with ZipFile(os.path.join(os.path.dirname(__file__), "resources", "example3_pdf.zip"), "w") as my_zip:
#         my_zip.write('example3.pdf')
#     with ZipFile('resources/example3_pdf.zip') as my_zip:
#         with my_zip.open('example3.pdf', 'r') as pdf_file:
#             num_pages_pdf_file_from_zip = len(PdfReader(pdf_file).pages)
#             print(PdfReader(pdf_file).pages[0].extract_text())
#             text_1page_pdf_file_from_zip = PdfReader(pdf_file).pages[0].extract_text()
#
#
#     assert num_pages_pdf_file_from_zip == num_pages_pdf_file, "Number of pages does not match"
#     assert text_1page_pdf_file_from_zip == text_1page_pdf_file, "Beginning text not the same"
#
#
#


