
phone_book = {}


n = int(input())


for i in range(n):
    query = input().split()
    
    if query[0] == 'add':
        # If the query is to add a new contact, update the phone book
        phone_book[query[1]] = query[2]
    elif query[0] == 'del':
        # If the query is to delete a contact, check if it exists in the phone book and remove it
        if query[1] in phone_book:
            del phone_book[query[1]]
    elif query[0] == 'find':
        # If the query is to find a contact, check if it exists in the phone book and print the name or "not found"
        if query[1] in phone_book:
            print(phone_book[query[1]])
        else:
            print("not found")
