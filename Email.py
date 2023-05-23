class Email:
    def __init__(self, sender, reciever, content):
        self.sender, self.reciever, self.content = sender, reciever, content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}"

emails = []
line = input()
while line != "Stop":
    tokens = line.split(" ")
    sender = tokens[0]
    reciever = tokens[1]
    content = tokens[2]
    email = Email(sender, reciever, content)
    emails.append(email)
    line = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))
for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
    
