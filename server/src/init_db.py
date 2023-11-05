# from sqlalchemy import event
# from . import db
# from .models.UserModel import User

# @event.listens_for(User.__table__, 'after_create')
# def init_database():
#     deafult_user = User(username="david19",
#         email="david19@gmail.com", 
#         firstname="david", 
#         lastname="fernandez", 
#         profile_description="data scientist")

#     db.session.add(deafult_user)

#     db.session.commit()
