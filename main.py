class Observable:
    def __init__(self):
        self.observers = []
        self.str = ""

    def setStr(self, str):
        self.str = str
        self.update_observers(str)

    def getStr(self):
        return self.str
        
    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def update_observers(self, str):
        for observer in self.observers:
            observer.update(str)

class Observer:
    def __init__ (self, id):
        self.id = id

    def update(self, str):
        print("Observer: ", self.id)
        print(f"A frase tem {self.qtyPalavras(str)} palavras")
        print(f"A frase tem {self.qtyParCaracteres(str)} palavras com quantidade par de caracteres")
        print(f"A frase tem {self.qtyComecaMaiuscula(str)} palavras que começam com letra maiúscula")

    def qtyPalavras(self, str):
        return len(str.split(" "))
    
    def qtyParCaracteres(self, str):
        return len([palavra for palavra in str.split(" ") if len(palavra) % 2 == 0])

    def qtyComecaMaiuscula(self, str):
        return len([palavra for palavra in str.split(" ") if palavra[0].isupper()])



if __name__ == "__main__":

    observable = Observable()
    observable.add_observer(Observer(1))
    observable.add_observer(Observer(2))
    observable.add_observer(Observer(3))

    frase = input("Digite uma frase\n").strip()

    observable.setStr(frase)

    print(observable.getStr())