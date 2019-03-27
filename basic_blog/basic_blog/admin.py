from flask import redirect, request
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, url_for_security

from app import db
from auth import app
from models import Post, Tag


class AdminMixin:
    """Примесь для представлений админки.

    Должен быть ПЕРВЫМ классом в цепочке наследования.
    """

    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for_security('login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class AdminHomeView(AdminMixin, AdminIndexView):
    pass


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super().on_model_change(form, model, is_created)


class AdminPostView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']


class AdminTagView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


admin = Admin(
    app,
    name='FlaskApp',
    url='/',
    template_mode='bootstrap3',
    index_view=AdminHomeView(name='Home')
)
admin.add_view(AdminPostView(Post, db.session))
admin.add_view(AdminTagView(Tag, db.session))
