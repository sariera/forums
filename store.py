class MemberStore:
    members = []
    print members

    def add(self, member):
        for m in self.members:
            if m == member.name:
                print 'Member {} Already Exists'.format(member.name)
                return
        self.members.append(member.member_id)
        self.members.append(member.name)
        self.members.append(member.age)

    def get_all(self):
        return self.members

    def get_by_id(self, member_id):
        self.member_id = self.members.index(member_id)
        return self.members[self.member_id], self.members[self.member_id + 1], self.members[self.member_id + 2]

    def delete(self, member_id):
        self.member_id = member_id
        try:
            del self.members[self.members.index(self.member_id):self.members.index(self.member_id)+3]
        except ValueError:
            print "Member Not Found"

    def entity_exists(self, member):
        self.member_name = member
        return self.member_name in self.members

class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post.title)
        self.posts.append(post.content)

    def get_all(self):
        return self.posts
        
        
