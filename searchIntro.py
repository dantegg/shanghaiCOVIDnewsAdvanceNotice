import re
introContent = '今天（3月13日）18:00，举行上海市第121场疫情防控工作新闻发布会，'

matchCase = re.search(r"上海市第\d+场疫情防控工作新闻发布会", introContent)
print(matchCase)
if matchCase is not None:
    print("matchCase", matchCase)
else:
    print("not found")