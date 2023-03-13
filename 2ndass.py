categories = [
    {
        'id' : 1,
        'categoryName' : 'Men Fashion',
    },
    {
        'id' : 2,
        'categoryName' : 'Women Fashion',
    },
]

sub_categories = [
    {
        'id' : 1,
        'subCatName' : 'Women Accessories',
        'category' : categories[0]
    },
    {
        'id' : 2,
        'subCatName' : 'Men Accessories',
        'category' : categories[1]
    }
]

colors = [
    {
        'id' : 1,
        'name' : 'Red'
    },
    {
        'id' : 2,
        'name' : 'Blue'
    },
]


products = [
    {
        'id' : 1,
        'name' : 'Apple',
        'subCategory' : sub_categories[0],
        'availableQTY' : 0,
        'colors' : [
            {
                'colorId' : colors[0],
                'price' : 200,
                'qty' : 20
            },
            {
                'colorId' : colors[1],
                'price' : 150,
                'qty' : 10
            },
        ]
    },
    {
        'id' : 2,
        'name' : 'Apple',
        'subCategory' : sub_categories[0],
        'availableQTY' : 0,
        'colors' : [
            {
                'colorId' : colors[0],
                'price' : 200,
                'qty' : 5
            },
            {
                'colorId' : colors[1],
                'price' : 150,
                'qty' : 3
            },
        ]
    }
]


for pro in products:
    tot = 0
    for color in pro['colors']:
        tot += color['qty']
    pro['availableQTY'] = tot


# print(products)



 
# task =>
    # calculate availableQTY qty from all colors
    # update qty & availableQTY when user buy a product
    # update qty & availableQTY when owner buy a new products

    # NOTE=> use FP ( Functional Programming ) all data stored dynamic

###################################### Add ##############################################  
def add(id,color_id,quant):
    for pro in products:  
        if pro['id'] == id:
            print(pro)  
            for itm in pro['colors']:
                if itm['colorId']['id'] == color_id:
                      itm['qty'] = itm['qty'] + quant   
            pro['availableQTY'] = pro['availableQTY']  + quant 
            print('+'*100) 
            print(pro)  
        
          
add(1,1,15)
add(1,2,3)
###################################### Minus ##############################################  
def minus(id,color_id,quant):
    for pro in products:  
        if pro['id'] == id:
            print(pro)  
            for itm in pro['colors']:
                if itm['colorId']['id'] == color_id:
                      itm['qty'] = itm['qty'] - quant   
            pro['availableQTY'] = pro['availableQTY']  - quant 
            print('-'*100) 
            print(pro)  
        
          
minus(1,1,15)
minus(1,2,3)