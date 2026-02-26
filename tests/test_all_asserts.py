import unittest
SERVER = "server_b"
class AllAssertest(unittest.TestCase):
    def test_assert_Equal(self):
        self.assertEqual(10,10)
        self.assertEqual("Hola","Hola")

    def test_assert_true(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no soy un numero")

    def test_assert_in(self):
        self.assertIn(10, [2,4,6,8,10])
        self.assertNotIn(5, [2,4,6,8,10])

    def test_assert_dicts(self):
        user = {"name":"Luis","lastName":"Martinez"}
        self.assertDictEqual(user,{"name":"Luis","lastName":"Martinez"})
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )

    @unittest.skip("trabajo en progreso, será habilitada despues")
    def test_skip(self):
        self.assertEqual("Hola","Chao")

    @unittest.skipIf(SERVER == "server_b", "Saltada por no estar en el servidor")
    def test_skip_if(self):
        self.assertEqual(10,10)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,100)