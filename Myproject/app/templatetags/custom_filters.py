from django import template

register = template.Library()

@register.filter(name='rupee')
def addRupeeSign(value):
    return f'₹ {value}'

@register.filter(name='sale_price')
def getSalePrice(product):
    if (product.Quantity==1):
        return (product.price - (product.price * (product.discount/100)))
    elif(product.Quantity==2):
        return((product.price - (product.price * (product.discount/100)))*2)
    elif(product.Quantity==0.50):
        return((product.price - (product.price * (product.discount/100)))/2)