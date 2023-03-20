import pytest
from selene import browser
import csv


@pytest.fixture()
def download_csv():
    with open('/tests/addresses_1.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


            #os.getcwd()+'/picture1.jpg'
