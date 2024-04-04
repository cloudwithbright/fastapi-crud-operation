import unittest
from fastapi.testclient import TestClient
from main import app, get_db, engine, Base, Item

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)

    def test_create_item(self):
        response = self.client.post("/items/", json={"name": "Test Item", "price": 10.99, "description": "An item", "in_stock": True, "id": 1})
        self.assertEqual(response.status_code, 200)
        item_data = response.json()
        self.assertEqual(item_data["name"], "Test Item")

    def test_read_item(self):
        item = Item(name="Test Item", price=10.99, description= "An item", in_stock=True, id=1)
        with get_db() as db:
            db.add(item)
            db.commit()

        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        item_data = response.json()
        self.assertEqual(item_data["name"], "Test Item")

    # Add more unit tests for other endpoints

if __name__ == "__main__":
    unittest.main()
