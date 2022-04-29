from app import app

def test_estimate_calculation():
    test_client = app.test_client()
    data = {"radius":"180","height":"360"}
    response = test_client.post('/generate_estimate',data=data)
    assert response.status_code == 200                       # Request succedes
    assert b"141300" in response.data                        # check if result is in the response
    


