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
