import json

def main():
    form = open('form.json', 'w')
    print('Ketik untuk mengisi data')
    print('Name:')
    inputname = input()
    print('Email:')
    inputemail = input()

    jsonfile = {
    "name": inputname,
    "email": inputemail
    }

    jsonobject = json.dumps(jsonfile)

    form.write(jsonobject)
    form.close()

    print('Data sudah terinput')