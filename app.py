import secrets

from flask import Flask, render_template, flash
from .database import db_session
from .forms import FeatureRequestForm
from .database.models import FeatureRequest, Client, ProductArea

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Boilerplate that's needed for SQLAlchemy to manage db sessions
# noinspection PyUnusedLocal
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


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
            client_priority=form.client_priority.data,
            target_date=form.target_date.data,
            product_area_id=form.product_area.data,
        )
        db_session.add(new_feature_request)
        db_session.commit()
        flash("We are thankful for your feedback!")

    print(form.errors)

    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
