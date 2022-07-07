from src import db
from src.services import experiment_thumbnail_service


def get_all(model):
    data = model.query.all()
    return data


def get_all_by_user_id(model, user_id):
    data = model.query.filter_by(user_id=user_id).all()
    return [result.serialized for result in data]


def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()


# def delete_instance(model, id):
#     model.query.filter_by(id=id).delete()
#     commit_changes()


# def edit_instance(model, id, **kwargs):
#     instance = model.query.filter_by(id=id).all()[0]
#     for attr, new_value in kwargs.items():
#         setattr(instance, attr, new_value)
#     commit_changes()


def commit_changes():
    db.session.commit()