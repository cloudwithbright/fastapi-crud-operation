## Import Packages
import unittest
from unittest.mock import patch, MagicMock
from src.service.service import (
    read_item_svc,
    read_items_svc,
)
from src.models.Items import ItemBase


## Define test cases
class TestGetItemService(unittest.TestCase):

    @patch("src.service.service.get_db")
    @patch("src.service.service.read_items")
    def test_read_items_ItemFound(self, mock_read_items, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking create_item() function
        mock_response = {"detail": None, "data": []}
        mock_read_items.return_value = mock_response

        ## Call read_items_svc
        response = read_items_svc()

        ## Assert
        self.assertEqual(response["message"], "Item found. Thank you!")
        self.assertIs(type(response["message"]), str)

    @patch("src.service.service.get_db")
    @patch("src.service.service.read_items")
    def test_read_items_ItemNotFound(self, mock_read_items, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking create_item() function
        mock_response = {"detail": "empty", "data": []}
        mock_read_items.return_value = mock_response

        ## Call read_items_svc
        response = read_items_svc()

        ## Assert
        self.assertEqual(response["message"], "No Item found. Thank you!")
        self.assertIs(type(response["message"]), str)
        self.assertListEqual(response["data"], [])
        self.assertEqual(len(response["data"]), 0)

    @patch("src.service.service.get_db")
    @patch("src.service.service.read_item")
    def test_read_item_ItemFound(self, mock_read_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking read_item() function
        mock_response = {"detail": "empty", "data": []}
        mock_read_item.return_value = mock_response

        ## Call read_item_svc
        response = read_item_svc(1)

        ## Assert
        self.assertEqual(response["message"], "Item found. Thank you!")
        self.assertIs(type(response["message"]), str)

    @patch("src.service.service.get_db")
    @patch("src.service.service.read_item")
    def test_read_item_ItemNotFound(self, mock_read_item, mock_get_db):

        ## Mock get_db() function
        mock_db_connection = MagicMock()
        mock_get_db.return_value = iter([mock_db_connection])

        ## Mocking read_item() function
        mock_response = None
        mock_read_item.return_value = mock_response

        ## Call read_item_svc
        response = read_item_svc(10)

        ## Assert
        self.assertEqual(response["message"], "Item not found. Thank you!")
        self.assertIs(type(response["message"]), str)
        self.assertIs(type(response["data"]), list)
        self.assertListEqual(response["data"], [])