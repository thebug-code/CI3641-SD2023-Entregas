import unittest
from io import StringIO
from unittest.mock import patch
from vtable import VTable


class TestVTable(unittest.TestCase):
    def test_vtable1(self):
        vtable = VTable()
        vtable.add(None, "A", ["f", "g"])
        self.assertEqual(vtable.vtables, {"A": {"f": "A", "g": "A"}})

    def test_vtable2(self):
        vtable = VTable()
        vtable.add(None, "A", ["f", "g"])
        vtable.add("A", "B", ["h"])
        self.assertEqual(
            vtable.vtables,
            {"A": {"f": "A", "g": "A"}, "B": {"h": "B", "f": "A", "g": "A"}},
        )

    def test_vtable3(self):
        vtable = VTable()
        vtable.add(None, "A", ["f", "g"])
        vtable.add("A", "B", ["f", "h"])
        self.assertEqual(
            vtable.vtables,
            {"A": {"f": "A", "g": "A"}, "B": {"f": "B", "h": "B", "g": "A"}},
        )

    def test_vtable4(self):
        vtable = VTable()
        vtable.add(None, "A", ["f", "g"])
        vtable.add("A", "B", ["f", "g"])
        self.assertEqual(
            vtable.vtables, {"A": {"f": "A", "g": "A"}, "B": {"f": "B", "g": "B"}}
        )

    def test_vtable5(self):
        vtable = VTable()
        vtable.add(None, "A", ["foo", "baz"])
        vtable.add("A", "B", ["foo"])
        vtable.add("B", "C", ["bar"])
        self.assertEqual(
            vtable.vtables,
            {
                "A": {"foo": "A", "baz": "A"},
                "B": {"foo": "B", "baz": "A"},
                "C": {"bar": "C", "foo": "B", "baz": "A"},
            },
        )

    def test_vtable6(self):
        vtable = VTable()
        vtable.add(None, "A", ["foo", "baz", "bar"])
        vtable.add("A", "B", ["foo"])
        vtable.add("B", "C", ["bar"])
        self.assertEqual(
            vtable.vtables,
            {
                "A": {"foo": "A", "baz": "A", "bar": "A"},
                "B": {"foo": "B", "baz": "A", "bar": "A"},
                "C": {"bar": "C", "foo": "B", "baz": "A"},
            },
        )

    def test_vtable7(self):
        vtable = VTable()
        vtable.add(None, "A", ["foo", "baz"])
        vtable.add("A", "B", ["foo"])
        vtable.add("B", "C", [])
        self.assertEqual(
            vtable.vtables,
            {
                "A": {"foo": "A", "baz": "A"},
                "B": {"foo": "B", "baz": "A"},
                "C": {"foo": "B", "baz": "A"},
            },
        )

    def test_derived_class_already_exists(self):
        vtable = VTable()
        input = ["CLASS A f g", "CLASS A f h", "SALIR"]

        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            with patch("builtins.input", side_effect=input):
                vtable.run_simulation()
                output = fake_out.getvalue()
                success_count = output.count(
                    "La tabla de metodos virtuales de A fue creada con exito\n"
                )
                error_count = output.count("La clase derivada ya existe\n")
                self.assertEqual(success_count, 1)
                self.assertEqual(error_count, 1)

    def test_base_class_does_not_exist(self):
        vtable = VTable()
        input = ["CLASS A f g", "CLASS B : C f h", "SALIR"]

        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            with patch("builtins.input", side_effect=input):
                vtable.run_simulation()
                output = fake_out.getvalue()
                success_count = output.count(
                    "La tabla de metodos virtuales de A fue creada con exito\n"
                )
                error_count = output.count("La clase base no existe\n")
                self.assertEqual(success_count, 1)
                self.assertEqual(error_count, 1)

    def test_base_class_and_derived_are_the_same(self):
        vtable = VTable()
        input = ["CLASS A f g", "CLASS A : A f h", "SALIR"]

        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            with patch("builtins.input", side_effect=input):
                vtable.run_simulation()
                output = fake_out.getvalue()
                success_count = output.count(
                    "La tabla de metodos virtuales de A fue creada con exito\n"
                )
                error_count = output.count(
                    "La clase derivada y la clase base son la misma\n"
                )
                self.assertEqual(success_count, 1)
                self.assertEqual(error_count, 1)

    def test_repeated_methods(self):
        vtable = VTable()
        input = ["CLASS A f f g", "SALIR"]

        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            with patch("builtins.input", side_effect=input):
                vtable.run_simulation()
                output = fake_out.getvalue()
                error_count = output.count("Los metodos no son distintos\n")
                self.assertEqual(error_count, 1)


def run_tests():
    """
    Metodo para inicializar los test
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVTable)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    run_tests()
