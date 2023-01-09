import PyPDF2, pyttsx3

path = open('Codigo_Limpo.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()
