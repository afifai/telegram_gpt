import os
from chatgpt3 import ChatGPT3

gpt = ChatGPT3(os.getenv("OPENAPI_TOKEN"),
                suffix=None,
                temperature=0)

def tanya_asisten(teks, konteks=False):
    if konteks:
        konteks = f'''{konteks}\n
        T: {teks}
        J:'''
    else:
        konteks = teks

    return gpt.ngobrol(konteks)