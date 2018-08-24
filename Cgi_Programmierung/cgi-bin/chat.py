#!/C:\\Users\\Fahri\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe

HTTP_SCHABLONE = '''Content-Type: text/html

<html><head><title>Python Chat</title></head>
    <body>
        <h1>Python Chat</h1>
        {} <hr>
        <form action="http://localhost/cgi-bin/chat.py" method="POST">
            <input type="hidden" name="username" value="{}">
            Ich sage: <input type="text" name="message" size="40" maxlenght="50">
            <input type="Submit" value="OK">
        </form>
    </body>
</html>'''

PATH = 'Chat/dialog.txt'

import cgi, cgitb
cgitb.enable()

class Dialog:
    def __init__(self, file):
        self.file = file        
        try:
            f = open(file, 'r')
            self.text = f.readlines()
            f.close()
        except:
            self.text = []
            f = open(file, 'w')
            f.close()

    def update(self, name, message):
        """This function adds a new message into the Dialog"""
        if len(self.text) > 10:
            self.text = self.text[-10:]
        newLine = name + ': ' + message + '<br>'
        self.text.append(newLine)
        f = open(self.file, 'w')
        for l in self.text:
            f.write(l)
        f.close()

    def __str__(self):
        # Dialog will be shown as HTML
        dialog = ''
        for l in self.text:
            dialog += l
        return dialog

class Chatroom:
    def __init__(self):
        self.form = cgi.FieldStorage()
        self.dialog = Dialog(PATH)
        self.message = self.form.getvalue('message')
        self.username = self.form.getvalue('username')
        if self.message:
            self.dialog.update(self.username, self.message)

    def __str__(self):
        return HTTP_SCHABLONE.format(self.dialog, self.username)

print(Chatroom())