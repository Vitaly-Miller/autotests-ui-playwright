"""
Обработка Validation Errors
"""
from pydantic import BaseModel, Field, ValidationError

#==================================================== Schema ===========================================================
class UserSchema(BaseModel):
    id: str | int = Field(gt=10, description='ID must be greater than 10')    # (> 10)  greater than     (gt)
    books: str | int = Field(ge=10)                                           # (≥ 10)  greater or equal (ge)
    age: str | int = Field(lt=10)                                             # (< 10)  less than        (lt)
    score: str | int = Field(le=10)                                           # (≤ 10)  less or equal    (le)

#--------------------------------------------------- ✅Valid dict -----------------------------------------------------
user_dict = {
    'id': 11,
    'books': 10,
    'age': 9,
    'score': 10
}

valid_user = UserSchema(**user_dict)  # ** - распаковка dict

print(valid_user)                     # id=11 books=10 age=9 score=10

#--------------------------------------------------- ✅Valid model -----------------------------------------------------
valid_user_model = UserSchema(
    id=11,
    books=10,
    age=9,
    score=10
)

print(valid_user_model)               # id=11 books=10 age=9 score=10



#----------------------------------------------- ❌Invalid model/dict --------------------------------------------------
try:
    invalid_user = UserSchema(
        id=11,
        books=10,
        age=10,                 # 👈Передаем ❌ошибочный аргумент
        score=10
    )
except ValidationError as e:     # Перехват ошибки типа ValidationError и сохранения описания в переменную <e>
    print('❌ ERROR:', e)        # ❌ ERROR: 1 validation error for UserSchema
                                 # age
                                 #  Input should be less than 10 [type=less_than, input_value=10, input_type=int]
                                 #    For further information visit https://errors.pydantic.dev/2.13/v/less_than

    # Подробный вывод исключения
    print(e.errors())            # [{'type': 'less_than', 'loc': ('age',), 'msg': 'Input should be less than 10', 'input': 10, 'ctx': {'lt': 10}, 'url': 'https://errors.pydantic.dev/2.13/v/less_than'}]

#-----------------------------------------------------------------------------------------------------------------------
