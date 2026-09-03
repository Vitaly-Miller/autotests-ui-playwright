"""
default_factory + lambda
"""
from pydantic import BaseModel, Field
from faker import Faker

fake = Faker()

#====================================================== default= =======================================================
#--------------------------------------------------- 'static value' ----------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default='ID-123')           # Default value = 'статическое_значение' для ВСЕХ экземпляров

id_1 = Schema()
id_2 = Schema()

print(id_1)     # id='ID-123' ┐
print(id_2)     # id='ID-123' ┘

#-------------------------------------------------- ❌fake.numerify ----------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default=fake.numerify)      # без () -> Объект в памяти

id_1 = Schema()
id_2 = Schema()

print(id_1)     # id=<bound method BaseProvider.numerify of <faker.providers.user_agent.Provider object at 0x108c8dd30>>
print(id_2)     # id=<bound method BaseProvider.numerify of <faker.providers.user_agent.Provider object at 0x108c8dd30>>


#-------------------------------------------------- fake.numerify() ----------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default=fake.numerify())          # () -> ОДНА генерация за сессию для ВСЕХ экземпляров

id_1 = Schema()
id_2 = Schema()

print(id_1)     # id='177' ┐
print(id_2)     # id='177' ┘



#=================================================== default_factory= ==================================================
#---------------------------------------------------- ✅fake.numerify --------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default_factory=fake.numerify)     # НОВАЯ генерация для КАЖДОГО экземпляра

id_1 = Schema()
id_2 = Schema()

print(id_1)      # id='593'
print(id_2)      # id='187'


#------------------------------------------ ✅lambda: fake.numerify (CUSTOMIZE👈) --------------------------------------
class Schema(BaseModel):
    id: str = Field(default_factory=lambda: fake.numerify(text='ID-###'))   # Генерация (с КАСТОМИЗАЦИЕЙ) для КАЖДОГО экземпляра

id_1 = Schema()
id_2 = Schema()

print(id_1)      # id='ID-884'
print(id_2)      # id='ID-571'

#=======================================================================================================================
