from operation import add_product , view_products , total , valid_choice
from storage import load_shop


def main():
  product_list =  load_shop()


  while True:
        choice =  valid_choice()
        if choice == 1:
           add_product(product_list)
        elif choice == 2:
            if not product_list :
                print("product list empty!!")
            else :
                view_products(product_list)
        elif choice == 3:
            print(f'the total is {total(product_list)}')
        elif choice == 4:
           break

main()