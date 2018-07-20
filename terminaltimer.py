import time
import sys

class ProgressBar:
    def __init__(self, goal, step):
        self.goal = goal
        self.current = 0
    
    def step(self):
        if self.current < self.goal:
            self.current = self.current + 1
    
    def generate_bar(self):
        return "[" + ("#" * self.current) + (" " * (self.goal - self.current)) + "]"

    def run(self):
        for i in xrange(goal):
            sys.stdout.write("\r " + self.generate_bar())
            self.step()
            time.sleep(step)
