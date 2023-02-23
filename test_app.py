import pytest
import os
from fastapi.testclient import TestClient
from app import app
client = TestClient(app)

def test_read_main():

    file_path = "Addison King Bed.jpg"
    if file_path:
        files = open(file_path, 'rb')
        response = client.post("/",files={"file": files})
        assert response.status_code == 200
        print(6)
    else:
        pytest.fail("Scratch file does not exists.")


test_read_main()
