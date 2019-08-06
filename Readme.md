# Basic flask CRUD

## Run

* run with `python -m flask run`
* browse to http://localhost:5000

## Debug

* Vscode start `Python: Flask`

## Docker

1. Build `docker build . -t flask_crud`
2. Start `docker run -p 5000:5000 -it --rm flask_crud:latest /bin/bash`

    * Either `flask@2bb89248f688:~/app/web$ python run`
    * Or `flask@2bb89248f688:~/app/web$ python -m flask run --host 0.0.0.0`
