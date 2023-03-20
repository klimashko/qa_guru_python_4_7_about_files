import pytest
from selene import browser
import os
import csv


@pytest.fixture()
def download_csv():
    with open(os.getcwd()+'/addresses_1.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)



