import sys

def error_message(error, detail):

    _, _, exc_tb = detail.exc_info()

    return f"""

Error:

{error}

Line Number:

{exc_tb.tb_lineno}

"""