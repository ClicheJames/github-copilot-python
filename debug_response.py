from starter.app import app

with app.test_client() as client:
    response = client.get('/new?clues=35')
    print(response.status_code)
    print(response.get_data(as_text=True))
