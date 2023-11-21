import unittest

from main import Observable, Observer

class MockObserver:
    def __init__(self):
        pass

    def __update__(self):
        pass

class TestObservable(unittest.TestCase):
    def setUp(self):
        self.observable = Observable()

    def test_setStr(self):
        self.observable.setStr("Hello")
        self.assertEqual(self.observable.getStr(), "Hello")

    def test_addObserver(self):
        observer = MockObserver()
        self.observable.add_observer(observer)
        self.assertIn(observer, self.observable.observers)

    def test_RemoveObserver(self):
        observer = MockObserver()
        self.observable.add_observer(observer)
        self.observable.remove_observer(observer)
        self.assertNotIn(observer, self.observable.observers)

class TestObserver(unittest.TestCase):
    def test_qtyPalavras(self):
        observer = Observer(1)
        str = "Frase de Teste bla bla bl"
        self.assertEqual(observer.qtyPalavras(str), 6)

    def test_qtyParCaracteres(self):
        observer = Observer(1)
        str = "Frase de Teste bla bla bl"
        self.assertEqual(observer.qtyParCaracteres(str), 2)

    def test_qtyComecaMaiuscula(self):
        observer = Observer(1)
        str = "Frase de Teste bla blaa bl"
        self.assertEqual(observer.qtyComecaMaiuscula(str), 2)

if __name__ == "__main__":
    unittest.main()