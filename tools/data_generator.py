"""
Data Generator
"""
from faker import Faker

#=======================================================================================================================
class Fake:
    """
    Class for generating random test data using the Faker library

    .
    """
    def __init__(self, faker: Faker):
        self.faker = faker

    #------------------------------------------------ User Credentials -------------------------------------------------
    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def last_name(self) -> str:
        return self.faker.last_name()

    def username(self) -> str:
        return self.faker.user_name()

    def email(self, domain: str | None = None) -> str:
        """
        Generate an email with optional @custom-domain.com

        :param: domain: - Custom domain ['custom-domain.com'] Default —> ...@example.com
        :return: email
        """
        unique_id = self.faker.uuid4()[:8]
        domain_part = domain or 'example.com'
        return f'test_{unique_id}@{domain_part}'

    def password(self) -> str:
        return self.faker.password()

    #-------------------------------------------------------- ID -------------------------------------------------------
    def user_id(self) -> str:
        """
        Generate a business-format User-ID

        :return: String in the format: User-1234
        """
        number = self.faker.random_int()
        return f'Test_User_ID-{number}'

    def uuid4(self) -> str:
        """
        Generate a UUID

        :return: String in the format: cad77163-f85d-4b96-b807-27670ffc9c29
        """
        return self.faker.uuid4()

    def random_int(self) -> int:
        """
        Generate a random 4-digit number

        :return: Random number: 1234
        """
        return self.faker.random_int()

    #------------------------------------------------------- Text ------------------------------------------------------
    def sentence(self, nb_words: int = 5):
        """
        Generate a 5-word sentence

        :return: Sentence of 5 words (default)
        """
        return self.faker.sentence(nb_words=nb_words)

    def text(self, max_nb_chars: int = 50) -> str:
        """
        Generate text with the given maximum length

        :param max_nb_chars: Number of characters. Default = 50
        :return: Random sentences
        """
        return self.faker.text(max_nb_chars=max_nb_chars)

    #----------------------------------------------------- Timing ------------------------------------------------------
    def estimated_time(self, minimum: int = 2, maximum: int = 9) -> str:
        """
        Generate estimated time in weeks. Default = [2-9]
        :param minimum: Range start (Default = 2)
        :param maximum: Range end (Default = 9)
        :return: [2-9] weeks
        """
        number = self.faker.random_int(minimum, maximum)
        return f'{number} weeks'

    #----------------------------------------------------- Scores -------------------------------=----------------------
    def max_score(self) -> int:
        """
        Generate a max score in the range [50-100]

        :return: Max score [50-100]
        """
        return self.faker.random_int(50, 100)

    def min_score(self) -> int:
        """
        Generate a min score in the range [1-30]

        :return: Min score [1-30]
        """
        return self.faker.random_int(1, 30)

    #------------------------------------------------------ Files ------------------------------------------------------
    def png_file_name(self) -> str:
        """
        Generate a .png file name for saving the file on the server (Upload)

        :return: String in the format file_1234.png
        """
        number = self.faker.random_int(1000, 9999)
        return f'file_{number}.png'


#================================================ Helper (GLOBAL VARIABLE) =============================================
# Initialize Fake() class instances with different settings
fake = Fake(faker=Faker())                     # en_US - Default
fake_ru = Fake(faker=Faker(locale='ru_RU'))    # ru_RU


#=======================================================================================================================
