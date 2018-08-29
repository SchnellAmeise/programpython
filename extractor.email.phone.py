import re, pyperclip

#phoneExtractor = re.compile(r'(\d\d)?-?(\d\d\d\d\d)-?(\d\d\d\d)')
#emailExtractor = re.compile(r'(\w+\.?\w+@\w+\.\w+.\w+?)')
#
#text = ("This is a simple text to test regex and see if they work email@hotmail.com enrico@gmail.com and telefone numbers 19982916821 or (19)98291-6821 or maybe 19-982916821")
#variable2 = emailExtractor.findall(text)
#variable1 = phoneExtractor.findall(text)
#print(variable2)
#print(variable1)
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile (r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
