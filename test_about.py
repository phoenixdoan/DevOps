from app import app

def test_about_load_correctly():
    test_client = app.test_client()
    response = test_client.get('/about')
    assert response.status_code == 200
    assert b"About Vertical Tank Maintenance" in response.data #This about title is displayed on page
    assert b"Lorem" in response.data                           #there is lorem on the page
    assert b"ipsum" in response.data                           #there is ipsum on the page
   

