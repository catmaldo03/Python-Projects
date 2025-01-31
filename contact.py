f = open('contactList.csv','a+')
instructions = 0
def create_contact(f):
    name = input("Enter name:")
    phone = input("Enter phone:")
    email = input("Enter email:")
    f.write(name + ',' + phone + ',' + email + '\n')
def view_all_contacts(f):
    f.seek(0)
    print(f.read())
def search_contact(f):
    name = input("Enter name:")
    f.seek(0)
    for line in f:
        if name in line:
            print(line)
            print("Contact found")
            print(f.readline())
def delete_contact(f):
    name = input("Enter name:")  
    f.seek(0)
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    flag = False 
    for line in lines:
        if name not in line:  
            f.write(line)
        else:
            flag = True
    if flag == False:
        print("Contact not found")
    else:
        print("Contact Deleted")

while instructions != 5:
    print("Select what you want to do:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    instructions = int(input())
    if instructions == 1:
        create_contact(f)
    elif instructions == 2:
        view_all_contacts(f)
    elif instructions == 3:
        search_contact(f)
    elif instructions == 4:
        delete_contact(f)
    elif instructions == 5:
        print("Exiting...")
f.close()