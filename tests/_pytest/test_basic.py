import pytest
import requests
from datetime import datetime

def test_request_work():
    url = 'http://www.baidu.com'
    res = requests.get(url)
    assert res.status_code == 200


def test_elho(smtp):
    response,msg = smtp.ehlo()
    assert response == 250
    assert 0