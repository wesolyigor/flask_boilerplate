from flask import Blueprint, render_template, request, flash, url_for
from flask_login import login_required
from sqlalchemy import desc
from werkzeug.utils import redirect

from app import db
from app.forms.article_forms import ArticleForm
from app.models.article_model import Article

bp_admin = Blueprint('admin', __name__, url_prefix='/cleaver-admin')


@bp_admin.route('/')
@login_required
def admin():
    return render_template('admin.html')


@bp_admin.route('/articles', methods=['GET', 'POST'])
@login_required
def admin_articles():
    all_articles = Article.query.order_by(desc(Article.created)).limit(50)
    form = ArticleForm()

    if form.validate_on_submit():
        article = Article(title=form.title.data, lead=form.lead.data, text=form.text.data, author=form.author.data)

        db.session.add(article)
        db.session.commit()

        flash(f'Article added!')
        return redirect(url_for('admin.admin_articles'))
    return render_template('admin_articles.html', articles=all_articles, form=form)


@bp_admin.route('/delete_article/<int:article_id>', methods=['GET'])
@login_required
def delete_article(article_id):
    article = Article.query.filter_by(id=article_id).first_or_404()
    if request.method == 'GET':
        db.session.delete(article)
        db.session.commit()
        flash(f'Deleted {article.title}', 'warning')
        return redirect(url_for('admin.admin_articles'))
    flash(f"There's no article with this {article_id}", 'danger')
    return redirect(url_for('admin.admin_articles'))


@bp_admin.route('/edit_article/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):

    article = Article.query.filter_by(id=article_id).first_or_404()
    form = ArticleForm(obj=article)
    form.submit.label.text = "Edit article"

    if form.validate_on_submit():
        form.populate_obj(article)
        db.session.commit()
        flash(f'{article.title} changed', 'success')
        return redirect(url_for('admin.admin_articles'))
    return render_template('edit_article.html', form=form)

