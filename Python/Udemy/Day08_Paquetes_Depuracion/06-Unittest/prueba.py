import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):  ## Es obligatorio que tenga "test" en el inicio
        palabra = "-"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "-a")

if __name__ == "__main__":
    unittest.main()