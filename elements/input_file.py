"""
Input file (upload) element
"""
import allure
from config import Dir
from elements.base_element import BaseElement

#=======================================================================================================================
class InputFile(BaseElement):
    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Upload]
    def upload(self, file: str):
        """
        ▶ Upload file

        :param file: File name (Ex.: 'image.jpg')
        """
        step = f'▶ Upload "{file}" via {self.name}'
        with allure.step(step):
            self.logger.info(step)
            self.locator.set_input_files(Dir.FILES/file)

#=======================================================================================================================
