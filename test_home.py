from app import app

def test_home_load_correctly():
    test_client = app.test_client()
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to VTM!" in response.data                 #The 'welcome to VTM!' is displayed on page
    assert b"Lorem" in response.data                           #there is lorem on the page
    assert b"ipsum" in response.data                           #there is ipsum on the page
    assert b"above_ground_vertical_tanks.jpg" in response.data #The tank image is loaded 


