import unittest
from unittest import TestCase
from unittest import mock
from buddy import Buddy


class TestBuddy(TestCase):

    def test_init(self):
        buddy = Buddy(128)
        self.assertEqual(len(buddy.block_list), 8)
        self.assertEqual(buddy.block_list, [[], [], [], [], [], [], [], [(0, 127)]])
        self.assertEqual(len(buddy.name_list), 0)
        self.assertEqual(buddy.memory_block_num, 128)

    def test_wrong_init1(self):
        with self.assertRaises(ValueError):
            buddy = Buddy(-6)

    def test_wrong_init2(self):
        with self.assertRaises(ValueError):
            buddy = Buddy(101)
    
    def test_wrong_init3(self):
        with self.assertRaises(ValueError):
            buddy = Buddy('a')

    def test_buddy_alloc(self):
        buddy = Buddy(128)
        test_cases = [
            {"name": "Bloque 1", "size": 32, "expected_list": [[], [], [], [], [], [(32, 63)], [(64, 127)], []],
             "expected_list_names": True},
            {"name": "Block 2", "size": 7, "expected_list": [[], [], [], [(40, 47)], [(48, 63)], [], [(64, 127)], []],
             "expected_list_names": True},
            {"name": "Block 3", "size": 64, "expected_list": [[], [], [], [(40, 47)], [(48, 63)], [], [], []],
             "expected_list_names": True},
            {"name": "Block 4", "size": 56, "expected_list": [[], [], [], [(40, 47)], [(48, 63)], [], [], []],
             "expected_list_names": False},
            {"name": "Block Wrong size", "size": -1, "expected_list": [[], [], [], [(40, 47)], [(48, 63)], [], [], []],
             "expected_list_names": False},
        ]
        for test in test_cases:
            buddy.buddy_alloc(test["size"], test["name"])
            self.assertEqual(buddy.block_list, test["expected_list"])
            self.assertEqual(test["name"] in buddy.name_list, test["expected_list_names"])

    def test_free(self):
        buddy = Buddy(128)
        alloc_test_cases = [
            {"name": "Block 1", "size": 16, "expected_list": [[], [], [], [], [(16, 31)], [(32, 63)], [(64, 127)], []],
             "expected_list_names": True},
            {"name": "Block 2", "size": 16, "expected_list": [[], [], [], [], [], [(32, 63)], [(64, 127)], []],
             "expected_list_names": True},
            {"name": "Block 3", "size": 16, "expected_list": [[], [], [], [], [(48, 63)], [], [(64, 127)], []],
             "expected_list_names": True},
            {"name": "Block 4", "size": 16, "expected_list": [[], [], [], [], [], [], [(64, 127)], []],
             "expected_list_names": True},
        ]

        for test in alloc_test_cases:
            buddy.buddy_alloc(test["size"], test["name"])
            self.assertEqual(buddy.block_list, test["expected_list"])
            self.assertEqual(test["name"] in buddy.name_list, test["expected_list_names"])

        free_test_cases = [
            {"name": "Block 1", "expected_list": [[], [], [], [], [(0, 15)], [], [(64, 127)], []],
             "expected_list_names": False},
            {"name": "Block No Allocate", "expected_list": [[], [], [], [], [(0, 15)], [], [(64, 127)], []],
             "expected_list_names": False},
            {"name": "Block 3", "expected_list": [[], [], [], [], [(0, 15), (32, 47)], [], [(64, 127)], []],
             "expected_list_names": False},
            {"name": "Block 2", "expected_list": [[], [], [], [], [(32, 47)], [(0, 31)], [(64, 127)], []],
             "expected_list_names": False},
        ]
        for test in free_test_cases:
            buddy.buddy_free(test["name"])
            self.assertEqual(buddy.block_list, test["expected_list"])
            self.assertEqual(test["name"] in buddy.name_list, test["expected_list_names"])

    def test_display(self):
        buddy = Buddy(128)
        buddy.display()
        self.assertEqual(len(buddy.block_list), 8)
        self.assertEqual(buddy.block_list, [[], [], [], [], [], [], [], [(0, 127)]])
        self.assertEqual(len(buddy.name_list), 0)
        self.assertEqual(buddy.memory_block_num, 128)

    def test_run_simulation(self):
        buddy5 = Buddy(128)
        buddy5.buddy_alloc(32, "Bloque_0")
        invalid_input_test_cases = ["reservar sin parametros", "reservar bloque_0", "liberar sin parametros", "liberar 1220", "mostrar", "salir"]

        with mock.patch('builtins.input', side_effect=invalid_input_test_cases):
            buddy5.run_simulation()
            self.assertEqual(buddy5.memory_block_num, 128)
            self.assertEqual(buddy5.block_list, [[], [], [], [], [], [(32, 63)], [(64, 127)], []])
            self.assertEqual(len(buddy5.block_list), 8)
            self.assertEqual(len(buddy5.name_list), 1)


if __name__ == '__main__':
    unittest.main()
