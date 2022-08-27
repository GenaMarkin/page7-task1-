import random


def main():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    print('round 1:', x)
    print('round 2:', y)
    print('round 3:', z)
    return x + y + z


David_sum = 0
Yosef_sum = 0
for i in range(10):
    print('Yosef tries: ')
    t = main()
    if t % 2 == 0:
        Yosef_sum += 1
    print('David tries: ')
    f = main()
    if f % 2 == 0:
        David_sum += 1
print('Yosef sum is: ', Yosef_sum)
print('David sum is: ', David_sum)
