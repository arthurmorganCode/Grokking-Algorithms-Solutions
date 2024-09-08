from collections import deque

def  search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + ' is mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False








def person_is_seller(name):
    return name[-5:] == 'Mango'









graph = {
    'Alice': ['David', 'Eve', 'Charlie Mango', 'Bob'],
    'Bob': ['Charlie Mango', 'Frank'],
    'Charlie Mango': ['Alice', 'Eve', 'David'],
    'David': ['Eve', 'Charlie Mango', 'Bob', 'Frank'],
    'Eve': ['David'],
    'Frank': ['Bob', 'Alice', 'David', 'Charlie Mango']
}

search('Alice')