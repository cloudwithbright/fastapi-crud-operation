## Import Packages
import unittest
from unittest.mock import patch, MagicMock
from src.service.service import (
    create_item_svc,
    ItemBase
)

## Define test cases
class TestAddItemService(unittest.TestCase):

    @patch("src.service.service.get_db")
    @patch("src.service.service.create_item")
    def test_add_item_ItemAdded(self, mock_create_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking create_item() function
        mock_response = {"detail": None, "data": []}
        mock_create_item.return_value = mock_response

        ## Input item
        item = ItemBase(
            name="Fish", description="Fish from Ghana", price=100, in_stock=True
        )

        ## Call create service functions
        response = create_item_svc(item)

        ## Assert
        self.assertIs(type(response["message"]), str)
        self.assertEqual(response["message"], "Item added successfully. Thank you!")

    @patch("src.service.service.get_db")
    @patch("src.service.service.create_item")
    def test_add_item_ItemExists(self, mock_create_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking create_item() function
        mock_response = {"detail": "empty", "data": []}
        mock_create_item.return_value = mock_response

        ## Input item
        item = ItemBase(
            name="Fish", description="Fish from Ghana", price=100, in_stock=True
        )

        ## Call create service functions
        response = create_item_svc(item)

        ## Assert
        self.assertListEqual(response["data"], [])
        self.assertIs(type(response["message"]), str)
        self.assertEqual(type(response["data"]), list)
        self.assertEqual(response["message"], "Item exists. Thank you!")