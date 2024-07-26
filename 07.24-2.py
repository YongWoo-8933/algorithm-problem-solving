"""
백준 15684 사다리 조작 (골드3)

1. 남은 K횟수에 따른 visited table을 만들어놓고 BFS진행하면 됨
2. 각 이동시 k가 남아있다면 말이동하는 경우까지 q에 추가
"""
from sys import stdin
from collections import deque

N, M, H = map(int, stdin.readline().split())
