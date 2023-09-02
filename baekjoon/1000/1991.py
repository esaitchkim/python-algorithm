"""1991.py
트리 순회
https://www.acmicpc.net/problem/1991
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

tree = {}

N = int(input())
for _ in range(N):
    parent, l_child, r_child = input().rstrip().split()
    tree[parent] = [l_child, r_child]


def preorder(tree, node):
    print(node)
    l_child, r_child = tree[node]
    if l_child != '.':
        preorder(tree, l_child)
    if r_child != '.':
        preorder(tree, r_child)


def inorder(tree, node):
    l_child, r_child = tree[node]
    if l_child != '.':
        inorder(tree, l_child)
    print(node)
    if r_child != '.':
        inorder(tree, r_child)


def postorder(tree, node):
    l_child, r_child = tree[node]
    if l_child != '.':
        postorder(tree, l_child)
    if r_child != '.':
        postorder(tree, r_child)
    print(node)


preorder(tree, 'A')
print('\n')

inorder(tree, 'A')
print('\n')

postorder(tree, 'A')
print('\n')
