from models import Member, Post
from store import MemberStore, PostStore

member1 = Member(0, "Ali", 30)
member2 = Member(1, "Rawan", 27)

post1 = Post("Topic 1", "This is the First Topic")
post2 = Post("Topic 2", "This is the Second Topic")
post3 = Post("Topic 3", "This is the Third Topic")

member_store = MemberStore()
member_store.add(member1)
member_store.add(member2)
member_store.add(member2)
print member_store.get_all()

post_store = PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print post_store.get_all()

print member_store.get_by_id(1)
member_store.delete(1)
print member_store.get_all()

print member_store.entity_exists('Ali')
print member_store.entity_exists("Ahmad")
