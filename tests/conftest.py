import pytest
from selene import browser
import csv


@pytest.fixture()
def download_csv():
    with open('C:/Users/klima/PycharmProjects/qa_guru_python_4_7_about_files/tests/addresses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
