import pytest
from ToDoList import ToDoList

@pytest.fixture

def todolist():
    todolist = ToDoList()
    return todolist

def testCanCallList(todolist):
    todolist

def testCanAddItem(todolist):
    # link = ToDoList()
    todolist.addItem('Fill Dog Dish')
    assert todolist.addItem('Fill Dog Dish') == 'Fill Dog Dish'

def testCanAddMultipleItems(todolist):
    # link = ToDoList()
    items = ['Make Coffee', 6, True, {"sink": "broken"}]
    assert todolist.addMultItems(items) == ['Make Coffee', 6, True, {"sink": "broken"}]

def testRemoveFirstItem(todolist):
    # link = ToDoList()
    items = ['Make Coffee', 6, True, {"sink": "broken"}]
    todolist.addMultItems(items)
    assert todolist.removeFirstItem() == [6, True, {"sink": "broken"}]

def testRemoveLastItem(todolist):
    # link = ToDoList()
    items = ['Make Coffee', 6, True, {"sink": "broken"}]
    todolist.addMultItems(items)
    assert todolist.removeLastItem() == ['Make Coffee', 6, True]

def testRemoveSpecificItem(todolist):
    # link = ToDoList()
    items = ['Make Coffee', 6, True, {"sink": "broken"}]
    todolist.addMultItems(items)
    assert todolist.removeSpecificItem(6) == ['Make Coffee', True, {"sink": "broken"}]