## Import Packages
import unittest
from unittest.mock import patch, MagicMock
from src.service.service import (
    update_item_svc,
)
from src.models.Items import ItemBase

## Define test cases
class TestUpdateItemService(unittest.TestCase):

    @patch("src.service.service.get_db")
    @patch("src.service.service.update_item")
    def test_update_item_ItemUpdatedSuccessful(self, mock_update_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking read_item() function
        mock_response = {"detail": None, "data": []}
        mock_update_item.return_value = mock_response

        ## Input item
        item = ItemBase(
            name="Fish", description="Fish from Ghana", price=100, in_stock=True
        )

        ## Call update_item_svc() function
        response = update_item_svc(2, item)

        ## Assert
        self.assertEqual(response["message"], "Item updated successfully. Thank you!")
        self.assertIs(type(response["message"]), str)
        self.assertGreater(len(response["data"]), 0)

    @patch("src.service.service.get_db")
    @patch("src.service.service.update_item")
    def test_update_item_ItemNotFound(self, mock_update_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking read_item() function
        mock_response = {"detail": "empty", "data": []}
        mock_update_item.return_value = mock_response

        ## Input item
        item = ItemBase(
            name="Fish", description="Fish from Ghana", price=100, in_stock=True
        )

        ## Call update_item_svc() function
        response = update_item_svc(2, item)

        ## Assert
        self.assertEqual(response["message"], "Item not found. Thank you!")
        self.assertIs(type(response["message"]), str)
        self.assertEqual(len(response["data"]), 0)

    