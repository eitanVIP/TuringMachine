import random
from TuringMachine import TuringMachine
from Rule import Rule
import time


def rulesFromText(text: str):
    pass


def main():
    rules = [Rule.randomRule("A"), Rule.randomRule("B"), Rule.randomRule("C"), Rule.randomRule("D")]
    for rule in rules:
        rule.setNextRule(random.choice(rules), random.choice(rules))

    machine = TuringMachine(20, rules)
    machine.setPos(0)
    while not machine.isHalted():
        machine.execute()
        print(machine)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
