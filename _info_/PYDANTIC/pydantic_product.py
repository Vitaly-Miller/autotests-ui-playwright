from pydantic import BaseModel, Field

#=======================================================================================================================
# Схема Маркета
class Market(BaseModel):
    id: int
    name: str

# Схема Product
class Product(BaseModel):
    name: str
    price: float = Field(gt=0, description='Price must be greater than 0')     # ... > 0
    tag: list[str] = []
    market: Market


#---------------------------------
# v.1 Dict
product_dict = {
    'name': 'Orange',
    'price': 10.99,
    'tag': ['Fresh', 'Sale'],
    'market': {
        'id': 12345,
        'name': 'Walmart'
    }
}

product_1 = Product(**product_dict)
print(product_1)              # name='Orange' price=10.99 tag=['Fresh', 'Sale'] market=Market(id=12345, name='Walmart')


# v.2 Object (Model)
product_1 = Product(
    name='Orange',
    price=10.99,
    tag=['Fresh', 'Sale'],
    market=Market(id=12345, name='Walmart')
)
print(product_1)              # name='Orange' price=10.99 tag=['Fresh', 'Sale'] market=Market(id=12345, name='Walmart')

#=======================================================================================================================
