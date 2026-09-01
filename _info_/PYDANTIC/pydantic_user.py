from pydantic import BaseModel, ValidationError

#=======================================================================================================================
#------------------------------------------------ Пример валидации объекта ---------------------------------------------
# Схема класса User
class User(BaseModel):
    id: int                                  # int
    username: str
    email: str
    is_active: bool = True

#------------------------------------------
# Dict
user_data = {
    'id': 1,                                 # ✅ - int
    'username': 'John Doe',
    'email': 'john@email.com',
}

# v.1 Распаковка dict через <**>
user = User(**user_data)
print(user)                                   # id=1 username='John Doe' email='john@email.com' is_active=True

# v.2 Распаковка dict через <.model_validate>
user = User.model_validate(user_data)
print(user)                                   # id=1 username='John Doe' email='john@email.com' is_active=True

#------------------------------------------
# Dict (Invalid data)
user_data_invalid_1 = {
    'id': '1',                                # ⚠️ - str - Допускается с "числовыми сроками" (переводит в int)
    'username': 'John Doe',
    'email': 'john@email.com',
}

user = User(**user_data_invalid_1)
print(user)                                   # id=1 username='John Doe' email='john@email.com' is_active=True
#------------------------------------------

# Dict (Invalid data)
user_data_invalid_one = {
    'id': 'one',                              # ❌ - str - НЕ допускается с "классическими сроками"
    'username': 'John Doe',
    'email': 'john@email.com',
}

# user = User(**user_data_invalid_one)
# print(user)                                 # ❌ ValidationError: for User - id should be a valid integer


# Отлов ошибки
try:
    user = User(**user_data_invalid_one)
    print(user)
except ValidationError as e:
    print('❌ ERROR:', e)      # ❌ ERROR: 1 validation error for User
                               # id
                               #   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='one', input_type=str]
                               #     For further information visit https://errors.pydantic.dev/2.13/v/int_parsing
