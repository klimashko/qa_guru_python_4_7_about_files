

#https://axiomabio.com/pdf/test.pdf
import pytest
from selene import browser
import csv

#https://stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2021/Download-data/bos2021ModC.csv

def test_download_csv():
    with open('C:/Users/klima/PycharmProjects/qa_guru_python_4_7_about_files/tests/addresses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)