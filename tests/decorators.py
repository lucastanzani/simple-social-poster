from typing import Tuple
from unittest import TestCase

import dotenv

import src.social_poster
from src.social_poster.config.decorators import *

dotenv.load_dotenv(".env.test")
poster = src.social_poster


@at_most_one_defined_true("second", "third")
def test_1(first: int, second: bool = False, third: bool = False):
	return "OK"


@all_defined("first", "second", "third")
def test_2(first: int, second: bool = False, third: bool = False):
	return "OK"


@all_defined("first", "second")
@at_most_one_defined_true("first", "second")
def test_3(first: bool, second: bool = False, third: bool = False):
	return "OK"


@exactly_one_defined("second", "third", "first")
def test_4(first: int = 0, second: bool = False, third: bool = False):
	return "OK"


class TestInstagramE2E(TestCase):

	def test_at_most_one_defined_true(self):
		self.assertRaises(TypeError, test_1, first=False, second=True, third=True)
		self.assertRaises(TypeError, test_1, first=True, second=True, third=True)

		self.assertEqual(test_1(first=True, second=False, third=False), "OK")
		self.assertEqual(test_1(first=True, second=True, third=False), "OK")

		self.assertEqual(test_1(first=True, second=False, third=False), "OK")
		self.assertEqual(test_1(first=True, second=True, third=False), "OK")

		self.assertRaises(TypeError, test_3, first=True, second=True, third=False)
		self.assertRaises(TypeError, test_3, first=True, second=True, third=True)

		self.assertEqual(test_3(first=True, second=False, third=False), "OK")
		self.assertEqual(test_3(first=True, second=False, third=True), "OK")

		self.assertEqual(test_3(first=False, second=True, third=True), "OK")
		self.assertEqual(test_3(first=False, second=True, third=False), "OK")

		self.assertEqual(test_3(first=False, second=False, third=False), "OK")
		self.assertEqual(test_3(first=False, second=False, third=True), "OK")

	def test_all_defined(self):
		self.assertRaises(TypeError, test_2, first=False)
		self.assertRaises(TypeError, test_2, second=False)
		self.assertRaises(TypeError, test_2, third=False)
		self.assertRaises(TypeError, test_2, first=False, second=True)
		self.assertRaises(TypeError, test_2, first=False, third=True)
		self.assertRaises(TypeError, test_2, second=False, third=True)

		self.assertEqual(test_2(first=False, second=False, third=False), "OK")
		self.assertEqual(test_2(first=False, second=False, third=True), "OK")
		self.assertEqual(test_2(first=False, second=True, third=True), "OK")
		self.assertEqual(test_2(first=False, second=True, third=False), "OK")
		self.assertEqual(test_2(first=True, second=False, third=False), "OK")
		self.assertEqual(test_2(first=True, second=False, third=True), "OK")
		self.assertEqual(test_2(first=True, second=True, third=False), "OK")
		self.assertEqual(test_2(first=True, second=True, third=True), "OK")

		self.assertRaises(TypeError, test_3, first=True, second=True, third=False)
		self.assertRaises(TypeError, test_3, first=True, second=True, third=True)

	def test_exactly_one_defined(self):
		self.assertEqual(test_4(first=0), "OK")
		self.assertEqual(test_4(second=False), "OK")
		self.assertEqual(test_4(third=True), "OK")

		self.assertRaises(TypeError, test_4, first=0, second=False)
		self.assertRaises(TypeError, test_4, first=0, second=True)
		self.assertRaises(TypeError, test_4, first=1, second=False)
		self.assertRaises(TypeError, test_4, first=1, second=True)
		self.assertRaises(TypeError, test_4, second=False, third=True)
		self.assertRaises(TypeError, test_4, second=False, third=False)
		self.assertRaises(TypeError, test_4, second=True, third=False)
		self.assertRaises(TypeError, test_4, second=True, third=True)
		self.assertRaises(TypeError, test_4, first=0, third=True)
		self.assertRaises(TypeError, test_4, first=0, third=False)
		self.assertRaises(TypeError, test_4, first=1, third=False)
		self.assertRaises(TypeError, test_4, first=1, third=True)
		self.assertRaises(TypeError, test_4, first=1, second=True, third=True)
		self.assertRaises(TypeError, test_4, first=1, second=True, third=False)
		self.assertRaises(TypeError, test_4, first=1, second=False, third=True)
		self.assertRaises(TypeError, test_4, first=1, second=False, third=False)
		self.assertRaises(TypeError, test_4, first=0, second=True, third=True)
		self.assertRaises(TypeError, test_4, first=0, second=True, third=False)
		self.assertRaises(TypeError, test_4, first=0, second=False, third=True)
		self.assertRaises(TypeError, test_4, first=0, second=False, third=False)
