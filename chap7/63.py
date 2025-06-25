import sys
sys.stdin=open('input.txt','r')

def DFS(x):
    print(x)
    DFS(x-1)
    

if __name__ == '__main__':
    n = int(input())
    DFS(n)