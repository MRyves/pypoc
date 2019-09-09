# coding=utf-8

# 1 - imports
from base import Session
from test import Test

# 2 - extract a session
session = Session()

# 3 - extract all movies
tests = session.query(Test).all()

for test in tests:
    print(f'Test: {test.id}')
