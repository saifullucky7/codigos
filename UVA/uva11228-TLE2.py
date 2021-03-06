# -*- coding: utf-8 -*-
'''
Leonardo Deliyannis Constantin
UVa 11228 - Transportation system.
'''

from math import hypot
from sys import stdin, stdout

class UnionFind:
    def __init__(self, N):
        self.p = [i for i in range(0, N)]
        self.rank = [0 for i in range(0, N)]
    def findSet(self, i):
        x = i
        while(x != self.p[x]):
            x = self.p[x]
        self.p[i] = x
        return self.p[i]
    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)
    def unionSet(self, i, j):
        if not self.isSameSet(i, j):
            x = self.findSet(i)
            y = self.findSet(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

class point:
    pass

def kruskal(N, R, els):
    roads = 0
    rails = 0
    states = 0
    els.sort()
    UF = UnionFind(N)
    for edge in els:
        if not UF.isSameSet(edge[1], edge[2]):
            UF.unionSet(edge[1], edge[2])
            if(edge[0] <= R):
                roads += edge[0]
            else:
                states += 2 if states == 0 else 1
                rails += edge[0]
    if states == 0: 
        states = 1
    return states, roads, rails

class Buffer:
    def __init__(self):
        pass
    def bufferize(self):
        self.idx = 0
        self.data = [line for line in stdin.readlines()]
    def read(self):
        self.idx += 1
        return self.data[self.idx-1]

def main():
    format = "Case #%d: %d %d %d"
    br = Buffer()
    br.bufferize()
    T = int(br.read())
    for tc in range(1, T+1):
        N, R = [int(n) for n in br.read().split()]
        v = []
        els = []
        for i in range(0, N):
            p = point()
            p.x, p.y = [int(n) for n in br.read().split()]
            v.append(p)
            for j in range(0, i):
                d = hypot(v[i].x - v[j].x, v[i].y - v[j].y)
                els.append((d, i, j))
        states, roads, rails = kruskal(N, R, els)
        roads = int(roads + 0.5)
        rails = int(rails + 0.5)
        s = "Case #" + str(tc) + ': '
        s += ' '.join([str(i)
            for i in [states, roads, rails]])
        s += '\n'
        stdout.write(s)

main()
