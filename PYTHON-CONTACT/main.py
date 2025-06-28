from sys import exit
from printer import print_menu
from contact import add_contact, show_all_contact,search_contact,delete_contact,update_contact

def main():
    contacts: list[dict] = [{
        'first_name':'Shohjahon',
        'last_name':"Mardonov",
        "phone":'94 081 01 26',
        'group':"family"
        }]
    
    while True:
        print_menu()
        
        choice = int(input("Menudan birini tanlang :"))
        
        if choice == 1:
            add_contact(contacts)
        
        elif choice == 2:
            show_all_contact(contacts)
        
        elif choice == 3:
            search_contact(contacts)
        
        elif choice == 4:
            delete_contact(contacts)
        
        elif choice == 5:
            update_contact(contacts)
        
        else:
            exit(0)
            

if __name__ == "__main__":
    main()