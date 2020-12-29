from flask import Blueprint, render_template
from sqlalchemy import desc

from app.models.article_model import Article

bp_article = Blueprint('articles', __name__, url_prefix='/articles')


@bp_article.route('/')
def articles():
    all_articles = Article.query.order_by(desc(Article.created)).limit(100)

    return render_template('articles.html', articles=all_articles)


@bp_article.route('/<int:article_id>')
def article(article_id):
    one_article = Article.query.filter_by(id=article_id).first_or_404()
    return render_template('article.html', article=one_article)

