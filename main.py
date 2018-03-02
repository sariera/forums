import models
import store

member1 = models.Member("Ahmad", 27)
member2 = models.Member("Ali", 30)
member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)
print member_store.get_all()
post1 = models.Post("Topic 1", "Contents of Topic 1", 1)
post2 = models.Post("Topic 2", "Contents of Topic 2", 1)
post3 = models.Post("Topic 3", "Contents of Topic 3", 2)
post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print post_store.get_all()

