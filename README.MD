# Flask

Budowa na przykładzie _flask_boilerplate_

-----

*_jeżeli nie uruchamiamy pliku flaska z run.sh lub pycharma to trzeba stworzyć zmienną środowiskową w terminalu na development z production_

    export FLASK_ENV=development

### to start flask_boilerplate:

    mkdir _namedirection_
    git checkout _actualbranch_
    git clone git@github.com:wesolyigor/flask_boilerplate.git .
    rm -rf .git
    
    ./run.sh

alternatywnie każdy plik flaska odpalamy za pomocą 
`flask run`

## Konstrukcja aplikacji we flasku:

Podstawowa budowa aplikacji flask to realizacja wzorca MVC

Model - Views - Templates




## Rejestracja Blueprint

`views:`

bp_article = Blueprint('articles', __name__, url_prefix='/articles')
@bp_article.route('/')

`__init__.py`

from app.views.article_views import bp_article
app.register_blueprint(bp_article)

Jeżeli podajemy jako parametr do root int, to zawsze w pierwszej kolejności wypisujemy go

`@bp_article.route('/<int:article_id>')
`

### login_required - wymaganie logowania 

# Formularze (FORMS)

from flask_wtf import FlaskForm

## walidacja w formularzu - przykład
    
    validators=[DataRequired(), Length(1, 120), Email()]

## wybrane walidatory:

    DataRequired() - wymagane wypełnienie

    Length(1, 120) / Length(min=10, message="Minimum 160 znaków") - długość

    Regexp('^[A-Za-z0-9_]{3,}$',message='Usernames consist of numbers, letters and underscore.')

    Email()

    Optional() - zezwala, żeby pole nie było wypełniane i przerywa walidację w tym miejscu

    InputRequired() - (do sprawdzenia); informuje o konieczności wypełnienia przed wypełnieniem

    IPAddress() - ip
    URL() - url

    EqualTo('confirm', message='Passwords must match') - porównuje 2 pola, np. potwierdź hasło
    
## Rodzaje pól fields

    BooleanField(false_values=None)
    FormField() - formularz w formularzu
          _przykład_  

        class TelephoneForm(Form):
            country_code = IntegerField('Country Code', [validators.required()])
            area_code    = IntegerField('Area Code/Exchange', [validators.required()])
            number       = StringField('Number')
        
        class ContactForm(Form):
            first_name   = StringField()
            last_name    = StringField()
            mobile_phone = FormField(TelephoneForm)
            office_phone = FormField(TelephoneForm)

        
    FieldList  - uporządkowana lista
    StringField
    SubmitField

## Walidacja czy mail był już użyty do rejestracji:

    @staticmethod
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address')


validatory muszą się w ten sposób nazywać validate_nazwapola(inaczej nie będą działąć)
self jest dlatego, że te medoty są wykorzystywane też jako metody obiektu

#Model

Tworzenie:
  
    class NameModel(db.Model)

    opcjonalnie dodajemy (UserMixin) w przypadku tworzenia usera





## Parametry do query:

- filter_by()
  
      CLassName.query.filter_by(username=username_field.data)

- first_or_404()
  
      user = User.query.filter_by(username=current_user.username).first_or_404()
  
- get_or_404()


## funkcja sprawdzająca zaszyfrowane hasło względem hasła

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

## zabezpieczanie haseł we Flasku z użyciem generate_password_hash

jeżeli pobieramy samo hasło pojawi się błąd AttribiuteError

    @property
    def password(self):
        raise AttributeError('password: write-only field')

w przypadku pobrania i przypisania wartości przypisujemy wywołanie funkcji generate_password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

## metoda statyczna zwracająca użytkownika po jego nazwie

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()


# Templates



## _base.html:

Składa sie:

head

body

footer

script 




## blocki:

content 

aside

mainnav

nav

## Tworzenie z Macros

{% macro render_field(field) %}
{% endmacro %}


## Korzystanie z Macros

{% from "_form_macros.html" import render_field %}

## Dziedziczenie templatek 

    {% extends '_base_admin.html' %}

Możemy użyć tylko tych bloków, które podaliśmy w templatce bazowej 

Jeżeli użyjemy blocków w templatce dziecka to ją przeciążymy, nawet jeśli będą puste.


Jeżeli nie chcemy przeciążyć tylko użyć polimorfizmu to używamy `{{ super() }}`

## Przekazywanie templatek wewnatrz bloków

{% include '_form.html' %}

## tworzenie unikalnych wartości set, ustaw tę nazwę i przypisz wartość

    {% set modal_id='articleModalForm' %}
    {% set btn_id='addForm' %}
    {% set form_title='Add Article' %}

  btn_id np. to id przekazywane w parametrze id button
    
    id="{{ btn_id }}"



## modals - wyskakujące okienka, w których może znaleźć się treść do wypełnienia

tworzymy je w oddzielnym pliku _modal, a następnie możemy przekazać dalej za pomocą parametru modal_id

## {{ super() }}

użycie polimorfizmu i nadpisanie zawartości




###############33

return redirect(request.args.get('next') or url_for("main.home"))

args = skąd przychodzi ten request, ten zapis pozwala wrócić na stronę na której było 