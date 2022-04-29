from app import app

def test_estimate_load_correctly():
    test_client = app.test_client()
    response = test_client.get('/estimate')
    assert response.status_code == 200
    assert b"Tank Painting Estimate" in response.data #This estimate title is displayed on page
    assert b"Total cost estimate" in response.data                           #there is lorem on the page
    assert b"Radius : " in response.data                           #there is Radius on the page
    assert b"Height : " in response.data                           #there is Height on the page
   

