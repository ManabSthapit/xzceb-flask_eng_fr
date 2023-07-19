"""This module functions as a translation device"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """This function does english to french translation"""

    frenchtext = MyMemoryTranslator(source='en-GB', target='french').translate(englishtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """This function does french to english translation"""

    englishtext = MyMemoryTranslator(source='french', target='en-GB').translate(frenchtext)
    return englishtext
