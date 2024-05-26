import os
import sys


def error_msg_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in script name [{0}] line num [{1}] error [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )    
    return error_message


class Usvisaexception(Exception):
    def __init__(self, error_message, error_detail):

        super().__init__(error_message)
        self.error_message = error_msg_detail(
            error_message, error_detail = error_detail
        )

    def __str__(self) -> str:
        return self.error_message