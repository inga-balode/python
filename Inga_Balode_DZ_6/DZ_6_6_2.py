import sys

with open('bake.csv', 'r', encoding='utf-8') as f:
    end = sum(1 for row in f)

def show_from(start):
    with open('bake.csv', 'r', encoding='utf-8') as f:
        for i in range(int(start)-1):
            f.readline()
        for i in range(int(start)-1, end):
            print(f.readline().strip())



if __name__ == "__main__":
    show_from(sys.argv[1])