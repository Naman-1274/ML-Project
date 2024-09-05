import sys

def error_message_descriptor(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error has occurred in file : [{0}] in line no : [{1}] and the Error is : [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

class Excception_handler(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_descriptor(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
