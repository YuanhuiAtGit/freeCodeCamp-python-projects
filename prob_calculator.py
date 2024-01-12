import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for item in balls.items():
            for _ in range(item[1]):
                self.contents.append(item[0])

            
    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        else:
            return random.sample(self.contents, n)
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    total_nice_draw = 0 
    
    for _ in range(num_experiments):
        balls = hat.draw(num_balls_drawn)
        drawn_balls = count(balls)
        if is_nice_draw(expected_balls, drawn_balls):
            total_nice_draw += 1
    
    prob = total_nice_draw / num_experiments
    
    return prob


def count(lst):
    count = {}
    for elem in lst:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    return count

def is_nice_draw(expected_balls, drawn_balls):
    is_nice = True
    for k in expected_balls:
        if k not in drawn_balls or drawn_balls[k] < expected_balls[k]:
            is_nice = False
            return is_nice
    return is_nice

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
