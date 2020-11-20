import cgi, cgitb
import pickle
from http.cookies import SimpleCookie
import os

cgitb.enable()

PATH = 'Umfrage/result.txt'
HTTP_FORM = '''Content-Type: text/html

<html>
    <head><title>Online-Abstimmung</title></head>
    <body>
        <h1>Online-Abstimmung</h1>
        <h2>{}</h2>
        Hier ist das aktuelle Abstimmungsergebnis:<br>
        Frage: Sind Studiengeb&uuml;hren an Unis sinnvoll?<br><br>
        <b>Ja:</b> {} Stimmen<br>
        <b>Nein:</b> {} Stimmen
    </body>
</html>'''

class Vote:
    def __init__(self, vote, count):
        self.vote = vote
        self.result = []
        try:
            f = open(PATH, 'rb')
            self.result = pickle.load(f)
            f.close()
            if count:
                f = open(PATH, 'wb')
                if self.vote == 'yes':
                    self.result[0] = int(self.result[0]) + 1
                    pickle.dump(self.result, f)
                elif self.vote == 'no':
                    self.result[1] = int(self.result[1]) + 1
                    pickle.dump(self.result, f)
                f.close()
        except FileNotFoundError:
            if self.vote == 'yes':
                self.result.append('1')
                self.result.append('0')
                f = open(PATH, 'wb')
                pickle.dump(self.result, f)
                f.close()
            elif self.vote == 'no':
                self.result.append('0')
                self.result.append('1')
                f = open(PATH, 'wb')
                pickle.dump(self.result, f)
                f.close()
        f = open(PATH, 'wb')
        pickle.dump(self.result, f)
        f.close()

    def getYesVotes(self):
        return self.result[0]
    
    def getNoVotes(self):
        return self.result[1]


class Survey:
    def __init__(self):
        self.form = cgi.FieldStorage()
        self.reply = ''
        self.resultVoting = self.form.getvalue('vote')

        if self.__hasVoted():
            self.reply = 'Du hast schon abgestimmt!'
            self.vote = Vote(self.resultVoting, False)
        else:
            self.reply = 'Vielen Dank f&uuml;r Ihr Voting!'            
            self.vote = Vote(self.resultVoting, True)

    def __hasVoted(self):
        self.cookie = SimpleCookie()
        try:
            self.cookie.load(os.environ['HTTP_COOKIE'])
            if self.cookie['voted'] == 'True':
                return True
        except:
            self.cookie['voted'] = True
            return False

    def __str__(self):
        return HTTP_FORM.format(self.reply, self.vote.getYesVotes(), self.vote.getNoVotes())

print(Survey())