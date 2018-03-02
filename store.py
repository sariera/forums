import itertools, models


class MemberStore:
    members = []
    posts = []
    last_id = 1
    def __init__(self):
        pass

    def add(self, member):
        self.members.append(member)
    last_id += 1

    def get_all(self):
        return MemberStore.members

    
class PostStore:

    def __init__(self):
        pass

    def add(self, post):
        MemberStore.posts.append(post)

    def get_all(self):
        return MemberStore.posts
