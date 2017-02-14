from gmail import Gmail
import datetime
from bs4 import BeautifulSoup

g = Gmail()
g.login('whiletrumpwastweeting@gmail.com', 'generalassembly1')
g.inbox().mail(unread=True)

content = []
emails = g.inbox().mail(before=datetime.date(2017, 4, 1))
for email in emails:
    content.append(email.body) # can also unread(), delete(), spam(), or star()
    # email.archive()

soup = BeautifulSoup(content[0])
soup.find(name='p').text