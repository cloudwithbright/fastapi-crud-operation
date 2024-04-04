import unittest
from sqlalchemy import create_engine
from main import app, Base, Item
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.client = TestClient(app)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)

    def test_create_item(self):
        response = self.client.post("/items/", json={"name": "Test Item", "price": 10.99})
        self.assertEqual(response.status_code, 200)
        item_data = response.json()
        self.assertEqual(item_data["name"], "Test Item")

    def test_read_item(self):
        item = Item(name="Test Item", price=10.99)
        with self.SessionLocal() as db:
            db.add(item)
            db.commit()

        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        item_data = response.json()
        self.assertEqual(item_data["name"], "Test Item")

if __name__ == "__main__":
    unittest.main()
