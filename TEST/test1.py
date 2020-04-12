"""
friends([("Ivan", "Maria"),
         ("Ella", "Ivan"),
         ("Ivan", "Oleg")]) == \

{"Ivan"  : {"Maria", "Ella", "Oleg"},
 "Ella"  : {"Ivan"},
 "Maria" : {"Ivan"},
 "Oleg"  : {"Ivan"},
}
"""


def friends(pairs):
    friends = dict()
    for i in pairs:
        for j in i:
            if j not in friends:
                friends[j] = set()
    for friend in friends:
        for pair in pairs:
            if pair[0] == friend:
                friends[friend].add(pair[1])
            if pair[1] == friend:
                friends[friend].add(pair[0])
    return friends