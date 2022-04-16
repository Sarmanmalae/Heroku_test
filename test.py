db_sess = db_session.create_session()
b_ = None
for u in db_sess.query(Users).filter(Users.id == id):
    b_ = [int(i) for i in u.basket.split(', ')]
b = [db_sess.query(Meals).filter(Meals.id == i).first().name for i in b_]
bask = {}
for i in b:
    if i not in bask:
        bask[i] = b.count(i)
print(bask)