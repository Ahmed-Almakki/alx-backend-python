#!/usr/bin/env python3
""" Parameterize a unit test"""
from utils import access_nested_map, get_json
import unittest
from unittest.mock import MagicMock, Mock, patch
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ test cases for function acces_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
                          ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               exp: Any) -> None:
        self.assertEqual(access_nested_map(nested_map, path), exp)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """ test the exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test__get_json(self, test_url: str,
                       test_payload: Mapping, mocck) -> None:
        req = MagicMock()
        req.status_code = 200
        req.json.return_value = test_payload
        mocck.return_value = req.get(test_url)
        result = get_json(test_url)
        mocck.assert_called_once_with(test_url)
