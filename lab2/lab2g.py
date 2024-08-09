#!/usr/bin/env python3

#Author: Jemark Amon
#Author ID: jamon@myseneca.ca
#DateCreated: 2024-06-05
import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])
    
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')