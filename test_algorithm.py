from algorithm import GameCore

algo = GameCore(6)

def test_prob():
   assert(algo.calcWinProb(5),  0.00)
   assert(algo.calcWinProb(6),  1.54)
   assert(algo.calcWinProb(7),  5.40)
   assert(algo.calcWinProb(8),  11.40)
   assert(algo.calcWinProb(9),  18.90)
   assert(algo.calcWinProb(10), 27.18)

def test_cases():
   assert(algo.getScenarios(5),  0)
   assert(algo.getScenarios(6),  1)
   assert(algo.getScenarios(7),  6)
   assert(algo.getScenarios(8),  21)
   assert(algo.getScenarios(9),  56)
   assert(algo.getScenarios(10), 126)

      