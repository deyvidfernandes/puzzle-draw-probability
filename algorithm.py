import math

class GameCore:
    def __init__(self, elements):
        self.elements = elements
        self.perfectGame = math.factorial(elements) / math.pow(elements, elements)
        self.counter = 0
        self.winProb = None
        self.scenarios = 1

    def iterate(self, function, n):
        calc = 0
        n += 1
        for i in range(n - 1):
            calc += function(i + 1)
        return calc

    def calcWinProb(self, attempts, on_progress=None):
        def calcOrder(startPos, factorSum, maxDepth, depth):
            probSum = 0
            depth += 1
            
            for x in range(startPos, self.elements - 1):
                self.counter += 1
                if on_progress:
                    on_progress(self.counter / self.scenarios)
                numerator = x + 1
                innerFactor = (numerator / self.elements) * factorSum
                probSum += self.perfectGame * innerFactor
                if depth < maxDepth:
                    probSum += calcOrder(numerator - 1, innerFactor, maxDepth, depth)
                if numerator == self.elements - 1:
                    return probSum

        self.counter = 1
        self.scenarios = self.getScenarios(attempts - 1)
        if attempts < self.elements:
            self.winProb = 0
            self.counter = 0
            return
        elif attempts == self.elements:
            self.winProb = self.perfectGame
            return

        attempts -= self.elements
        self.winProb = calcOrder(0, 1, attempts, 0) + self.perfectGame
        
    def getScenarios(self, attempts):
        orders = attempts - self.elements
        if orders == 1:
            return self.iterate(lambda n: n, self.elements)
        elif orders == 0:
            return self.elements
        elif orders >= 2:
            orders -= 1
        if orders == 1:
            return self.iterate(lambda z: self.iterate(lambda n: n, z), self.elements)

        def orderLoop(x, lastOrder, orders, depth):
            if orders == 1:
                return lastOrder(self.elements)
            else:
                newOrder = lambda z: self.iterate(lastOrder, z)
                calc = newOrder(x)
                depth += 1
                if depth < orders:
                    return orderLoop(x, newOrder, orders, depth)
                return calc
        
        return orderLoop(self.elements, lambda z: self.iterate(lambda n: n, z), orders, 0)

class GameUI:
    def __init__(self, elements):
        self.game = GameCore(elements)

    def displayWinProb(self):
        print("\n------- CONCLUÍDO -------")
        outputstr = "{:.2%}".format(self.game.winProb)
        print(f"Chance de vencer o jogo: {outputstr}")
        print(f"Cenários simulados: {self.game.counter}\n")

    def run(self):
        while True:
            try:
                userInput = int(input("Número de tentativas: "))
                self.game.calcWinProb(userInput, self.printProgress)
                self.displayWinProb()
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    
    def printProgress(self, progress):
        print(f"Progresso: {progress:.2%}", end="\r")

if __name__ == "__main__":
    GameUI(6).run()
