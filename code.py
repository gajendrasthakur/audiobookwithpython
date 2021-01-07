'''
Collected by :- GAJENDRA SINGH THAKUR
http://gajendrasingh.tech/
Source :- Google
'''
from PyPDF2 import pdf
import pyttsx3,PyPDF2
pdfReader=PyPDF2.PdfFileReader(open('whowillcrywhenyoudie.pdf','rb'))
speaker=pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text=pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
    speaker.stop()
