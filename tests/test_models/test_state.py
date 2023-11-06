import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_attributes(self):
        """
        Verificar que los atributos de State se inicializan correctamente.
        """
        state = State()
        self.assertEqual(state.name, "")
        self.assertIsInstance(state.name, str)

    def test_inheritance(self):
        """Verificar que State hereda de BaseModel."""
        state = State()
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
