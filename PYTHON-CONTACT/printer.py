from termcolor import colored

def print_menu():
    menu_colores_version = colored("""
          ======= Menu =======
          1. Add contact
          2. Show contacts
          3. Search contacts
          4. Delete contact       
          5. Update contact
          6. Exit       
          """,'green')
    
    print(menu_colores_version)

def print_status(status:str):
    status_data = {
        "error":colored("error",'red'),
        "success":colored("muvaffaqiyatli bajarildi",'green')
    }
    
    print(status_data[status])

def print_contact(contact):
    print(f"name : {contact['first_name']} {contact['last_name']} phone : {contact['phone']} group : {contact['group']}")

def print_all_contact(contacts:list[dict]):
    print("All contact")
    for contact in contacts:
        print_contact(contact)
