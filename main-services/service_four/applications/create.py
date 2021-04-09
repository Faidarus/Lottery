from app import db, Lottery

db.drop_all()
db.create_all()

name = Lottery(name = 'Fatima Aidarus')

db.session.add(name)
db.session.commit()