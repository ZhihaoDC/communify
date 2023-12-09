from src import db

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    instance = db.session.merge(instance)
    commit_changes()
    return instance.serialized

def delete_by_id(model, user_id, id):
    deleted_id = model.query.filter_by(user_id=user_id, experiment_id=id).delete()
    commit_changes()
    return deleted_id

def commit_changes():
    db.session.commit()