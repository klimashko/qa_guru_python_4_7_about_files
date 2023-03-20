import pytest
import os




@pytest.fixture()
def clean_resources():
    resources = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")
    for filename in os.listdir(resources):
        if filename.endswith(".zip"):
            file_path = os.path.join(resources, filename)
            os.remove(file_path)




