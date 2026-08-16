"""
File input (upload) element
(⚠️Page factory)
"""
from elements_.base_element_ import BaseElement

#=======================================================================================================================
class FileInput(BaseElement):

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Upload]
    def set_input_file(self, file: str, **kwargs):
        """
        ▶ Upload file

        :param file: File name
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)          # инициализация локатора
        locator.set_input_files(self.FILES/file)      # Playwright action


#=======================================================================================================================
