import  json as j



def load_shop():
    try :
        with open('smart_shop/smart.json') as file :
            product_list =j.load(file)
    except FileNotFoundError:
        product_list = []

    return product_list
def save_product(product_list):
    with open('smart_shop/smart.json','w') as file:
        j.dump(product_list,file)

    return 

