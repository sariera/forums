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
        result = None
        all_members = self.get_all()
        for member in all_members:
            if member.member_id == member_id:
                result = member
                break
        return result

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.member_id) is None:
            result = False
        return result

    def delete(self, member_id):
        member = self.get_by_id(member_id)
        MemberStore.members.remove(member)

    def update(self,member):
        result = member
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.member_id == member.member_id:
                all_members[index] = member
                break
        return result

    def get_by_name(self, member_name):
        result = None
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all()
        for post in all_posts:
            for member in all_members:
                if post.member_id == member.member_id:
                    member.posts.append(post)
        yield member


    
class PostStore:

    def __init__(self):
        pass

    def add(self, post):
        MemberStore.posts.append(post)

    def get_all(self):
        return MemberStore.posts

    def get_by_id(self,member_id):
        result =[]
        all_posts = self.get_all()
        for e in all_posts:
            if e.member_id == member_id:
                result.append(e)
        return result

