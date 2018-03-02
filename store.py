import itertools, models


class MemberStore:
    members = []
    posts = []
    last_id = 1
    def __init__(self):
        pass

    def add(self, member):
        member.member_id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self,member_id):
        self.member_id = member_id
        return MemberStore.members[self.member_id - 1]

    def entity_exists(self, member):
        self.member = member
        for i in MemberStore.members:
            if i.name == self.member:
                return "The member {} is exists".format(self.member)
            else:
                return "The member {} is not exist".format(self.member)

    def delete(self, member_id):
        self.member_id = member_id
        del MemberStore.members[self.member_id - 1]
        return "The member {} has been deleted".format(self.member)

    
class PostStore:

    def __init__(self):
        pass

    def add(self, post):
        MemberStore.posts.append(post)

    def get_all(self):
        return MemberStore.posts
