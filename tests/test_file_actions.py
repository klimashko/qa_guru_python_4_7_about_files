import pytest
from PyPDF2 import PdfReader
from selene import browser
import os
import csv
from zipfile import ZipFile
import io
import PyPDF2



def test_zip_csv():
    with open('addresses_1.csv') as file:
        # second_row_csv_file = csv.reader(file)[1]
        # print(second_row_csv_file)

    with ZipFile(os.path.join(os.path.dirname(__file__), "resources", "addresses_1_csv.zip"), "w") as my_zip:
        my_zip.write('addresses_1.csv')
    with ZipFile('resources/addresses_1_csv.zip') as myzip:
        with myzip.open('addresses_1.csv', 'r') as csv_file:
            print(csv.reader(csv_file)[0])




# def test_zip_xlsx():
#     with ZipFile(os.path.join(os.path.dirname(__file__), "resources", "sample2_xlsx.zip"), "w") as my_zip:
#          my_zip.write("sample2.xlsx")
#     with ZipFile("resources/sample2_xlsx.zip") as myzip:
#         read_xlsx = myzip.read("sample2.xlsx")
#         print(type(read_xlsx))
#
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


