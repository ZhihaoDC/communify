from src import db

def save_experiment_thumbnail(model, **kwargs):
    instance = model(**kwargs)

    db.session.add(instance)
    commit_changes()


def get_by_experiment_id(model, experiment_id):
    data = model.query.filter_by(experiment_id=experiment_id).first()
    return data.serialized


def commit_changes():
    db.session.commit()