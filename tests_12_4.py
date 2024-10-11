import logging
import unittest
from run_exc import Runner, Tournament

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner = Runner('Sveta',-5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            runner = Runner(12354)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner1 = Runner('Vika')
        runner2 = Runner('Stesha')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance,runner2.distance)


