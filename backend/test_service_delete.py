## Import Packages
import unittest
from unittest.mock import patch, MagicMock
from src.service.service import (
    delete_item_svc,
)

## Define test cases
class TestDeleteItemService(unittest.TestCase):

    @patch("src.service.service.get_db")
    @patch("src.service.service.delete_item")
    def test_delete_item_ItemDeletedSuccessfully(self, mock_delete_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking delete_item() function
        mock_response = {"detail": None, "data": []}
        mock_delete_item.return_value = mock_response

        ## Call delete_item() function
        response = delete_item_svc(1)

        # Assert
        self.assertEqual(response["message"], "Item deleted successfully. Thank you!")
        self.assertIs(type(response["message"]), str)
        self.assertGreater(len(response["data"]), 0)

    @patch("src.service.service.get_db")
    @patch("src.service.service.delete_item")
    def test_delete_item_ItemNotFound(self, mock_delete_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking delete_item() function
        mock_response = {"detail": "empty", "data": []}
        mock_delete_item.return_value = mock_response

        ## Call delete_item() function
        response = delete_item_svc(1)

        # Assert
        self.assertEqual(response["message"], "Item not found. Thank you!")
        self.assertIs(type(response["message"]), str)
        self.assertEqual(len(response["data"]), 0)