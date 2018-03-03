class Member:
    def __init__(self, name, age, member_id=0):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.posts = []

    def __str__(self):
        return "ID:%s\nName:%s\nAge:%d" % (self.member_id, self.name, self.age)


class Post:
    def __init__(self, title, content, member_id=0):
        self.post_id = 0
        self.title = title
        self.content = content
        self.member_id = member_id

    def __str__(self):
        return "Title: %s , content: %s" % (self.title, self.content)
