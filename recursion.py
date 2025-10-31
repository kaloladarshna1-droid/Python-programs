menu = {"Home" :{},
        "Products" : {
            "Electronics" : {
                "phone" :{},
                "Laptops" :{},
            
            }
        },
            "Clothing" : {               
                "Mens" : {},
                "Women" : {}
            },
            "About" : {},
            "Contact Us" : {}

        }

def print_menu (menu,indent = 0) :

    for item in menu :
        print(" "*indent + f"-{item}")
        print_menu(menu[item],indent +1 )

print_menu(menu)