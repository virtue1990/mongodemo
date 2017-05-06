import pytest

@pytest.fixture
def smtp():
    '''
    for some test
    '''
    import smtplib
    sm = smtplib.SMTP('smtp.gmail.com')
    # def fin():
    #     print 'teardowm smtp'
    #     sm.close()
    # request.addfinalizer(fin)
    return sm