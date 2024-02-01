from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Verify(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return '<Text %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        text_content = request.form['content']
        new_text = Verify(content=text_content)

        try:
            db.session.add(new_text)
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue adding new text...'
    else:
        texts = Verify.query.order_by(Verify.id).all()
        return render_template('home.html', texts=texts)




