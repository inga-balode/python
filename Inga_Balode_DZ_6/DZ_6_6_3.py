import sys

def show_from_to(start, end):
    with open('bake.csv', 'r', encoding='utf-8') as f:
        for i in range(int(start)-1):
            f.readline()
        for i in range(int(start)-1, int(end)):
            print(f.readline().strip())



if __name__ == "__main__":
    show_from_to(sys.argv[1], sys.argv[2])