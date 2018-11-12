import secrets

from flask import Flask, render_template, flash
from .database import db_session
from .forms import FeatureRequestForm
from .database.models import FeatureRequest

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)


# Boilerplate that's needed for SQLAlchemy to manage db sessions
# noinspection PyUnusedLocal
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET', 'POST'])
def index():
    print(FeatureRequest.query.all())
    form = FeatureRequestForm()
    if form.validate_on_submit():
        new_feature_request = FeatureRequest(title=form.title.data, description=form.description.data)
        db_session.add(new_feature_request)
        db_session.commit()
        flash("We are thankful for your feedback!")

    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
