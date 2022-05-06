from flask import session
from settings import *
import json
from sqlalchemy import delete, insert
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    prix = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'description': self.description,
                'name': self.name, 'prix': self.prix}

    def add_article(_name, _description, _prix):
        new_article = Article(name=_name, description=_description, prix=_prix)
        db.session.add(new_article)
        db.session.flush()
        db.session.refresh(new_article)
        db.session.commit()
        return new_article.json()

    def get_all_article():
        return [Article.json(article) for article in Article.query.all()]

    def get_article(_id):
        try:
            article = Article.json(Article.query.filter_by(id=_id).first())
            return article
        except:
            return None

    def update_article(_id, _name, _description, _prix):
        article_to_update = Article.query.filter_by(id=_id).first()
        article_to_update.name = _name
        article_to_update.description = _description
        article_to_update.prix = _prix
        db.session.commit()
        updated_article = Article.get_article(_id)
        return updated_article

    def delete_article(_id):
        a = Article.query.filter_by(id=_id).delete()

        db.session.commit()
