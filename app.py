import secrets

from flask import Flask, render_template, flash, jsonify, request
from .database import db_session
from .forms import FeatureRequestForm
from .database.models import FeatureRequest, Client, ProductArea

from typing import List

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Boilerplate that's needed for SQLAlchemy to manage db sessions
# noinspection PyUnusedLocal
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def resort_feature_requests(new_priority: int, client_id: int) -> int:
    client_feature_requests: List[FeatureRequest] = FeatureRequest.query.filter(
        FeatureRequest.client_id == client_id).order_by(FeatureRequest.client_priority).all()

    if len(client_feature_requests) == 0:
        return 1

    if new_priority > client_feature_requests[-1].client_priority:
        return client_feature_requests[-1].client_priority + 1
    else:
        for feature_request in client_feature_requests:
            if feature_request.client_priority >= new_priority:
                feature_request.client_priority += 1

    db_session.bulk_save_objects(client_feature_requests)
    db_session.commit()
    return new_priority


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeatureRequestForm()
    form.client.choices = [(client.id, client.name) for client in Client.query.all()]
    form.product_area.choices = [(product_area.id, product_area.name)
                                 for product_area in ProductArea.query.all()]

    if form.validate_on_submit():
        new_feature_request = FeatureRequest(
            title=form.title.data,
            description=form.description.data,
            client_id=form.client.data,
            client_priority=resort_feature_requests(form.client_priority.data, form.client.data),
            target_date=form.target_date.data,
            product_area_id=form.product_area.data,
        )
        db_session.add(new_feature_request)
        db_session.commit()
        flash("We are thankful for your feedback!")

    return render_template("index.html", form=form)


@app.route('/list', methods=['GET'])
def list_feature_requests():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    feature_requests: List[FeatureRequest] = FeatureRequest.query.order_by(FeatureRequest.client_priority).limit(limit).offset(offset).all()
    return jsonify({
        "count": FeatureRequest.query.count(),
        "data": [fr.to_camel_case_dict() for fr in feature_requests]
    })


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
