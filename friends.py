users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]
friendsList = []
def num_friends():
    '''
    Find number of friends for a given user
    '''  
    for item in users:
        jsonResult=[]
        name = None
        numberOfFriends = 0
        dict = item
        name = dict.get("name")
        for friendshipItem in friendship:
            if dict.get("id") == friendshipItem[0]:
                numberOfFriends +=1
            if dict.get("id") == friendshipItem[1]:
                numberOfFriends +=1
        jsonResult.append(name)
        jsonResult.append(numberOfFriends)
        friendsList.append(jsonResult)
    print("Number of friends each user has:")
    print(friendsList)   
    # TODO
    pass

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    friendsList.reverse()
    friendsList.sort(key=lambda x: x[1])
    friendsList.reverse()
    print("Sorting from most friends to least friends:")
    print(friendsList)
    # TOOD
    pass

num_friends()
sort_by_num_friends()