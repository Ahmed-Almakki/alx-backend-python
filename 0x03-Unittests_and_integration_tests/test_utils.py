#!/usr/bin/env python3
""" Parameterize a unit test"""
from utils import access_nested_map
import unittest
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
