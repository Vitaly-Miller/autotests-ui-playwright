"""
Input file (upload) element
"""
import allure
from elements.base_element import BaseElement

#=======================================================================================================================
class InputFile(BaseElement):
    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Upload]
    def upload(self, file: str):
        """
        ▶ Upload file

        :param file: File name
        """
        with allure.step(f'▶ Upload "{file}" via {self.name}'):
            self.locator.set_input_files(self.FILES/file)


#=======================================================================================================================
