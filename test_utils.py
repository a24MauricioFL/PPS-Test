# Importar o módulo unittest
import unittest
import utils

# Crear unha clase TestUtils que estenda de unittest.TestCase
class TestUtils(unittest.TestCase):
    def test_e_primo(self):
        """Comproba se a función is_prime funciona correctamente."""
        self.assertFalse(utils.is_prime(4))
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertFalse(utils.is_prime(8))
        self.assertFalse(utils.is_prime(10))
        self.assertTrue(utils.is_prime(7))
        self.assertEqual(
            utils.is_prime(-3),
            "Os números negativos non están permitidos"
        )

if __name__ == "__main__":
    unittest.main()