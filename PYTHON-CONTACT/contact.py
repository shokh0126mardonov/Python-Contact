from printer import print_status,print_all_contact

def add_contact(contacts:list[dict]):
    
    first_name = input("first name : ")
    last_name = input("last name : ")
    phone = input("number : ").replace(" ","")
    group = input("group (family,friends,work,other): ")
    
    if first_name.isalpha() and last_name.isalpha() and phone.isdigit() and group in ("family","friends","work","other" ):
        contacts.append({
            "first_name" : first_name,
            "last_name"  : last_name,
            "phone"   : phone,
            "group"   : group,
        })
        print_status("success")
    else:
        print_status("error")

def show_all_contact(contacts:list[dict]):
    
    if contacts:
        print_all_contact(contacts)
    else:
        print("kontakt mavjud emas")
        

def search_contact(contacts):
    search = input("search : ").lower()
    
    result = list(filter(
        lambda contact: search in contact.values(),contacts
    ))
    
    if result:
        print(result)
    else:
        print_status("error")
            
def delete_contact(contacts):
    
    delete = input("delete : ").lower().replace(" ","")
    
    for contact in contacts:
        for value in contact.values():
            if value.replace(" ","").lower() == delete:
                print_status("success")
                contacts.remove(contact)
    else:print_status('error')     

def update_contact(contacts):
    
    old_value = input("mavjud malumotni kiriting ")
    new_value = input("yangi malumotni  kiriting ")
    
    for contact in contacts:
        for key,value in contact.items():
            if old_value == value:
                contact[key] = new_value
        else:
                print_status('error') 