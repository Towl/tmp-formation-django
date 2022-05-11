# Django & Django Rest Framework

Toujours se référer aux documentations officielles:

* [Django](https://docs.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)


## Initialisation de l'environment

```python
python -m venv <venv-name>
source <venv-name>/bin/activate
pip install -U pip
pip install -r src/requirements.txt -r src/requirements-dev.txt
```

## Initialisation d'un projet Django

```python
django-admin startproject <myproject> src
```

### Composition d'un projet Django

```bash
src/
./*.Dockerfile          # Les dockerfiles pour générer les environnements Openshift
./requirements.txt      # Requirement de prod
./requirements-dev.txt  # Requirement additionnel pour le dev
./manage.py             # Point d'entrée Django
./<myproject>/          # Project Django
  ./asgi.py             # Point d'entrée config server Asynchrone
  ./__init__.py         # Un project django est un package python donc __init__.py obligatoire, même vide
  ./settings.py         # Configuration du projet
  ./urls.py             # Liste des urls et mapping avec les apps
  ./wsgi.py             # Point d'entrée config server Syncrhone
  ./<myfirstapp>/       # Une application spécifique au projet
  ./<mysecondapp>/      # Une application spécifique au projet
  ./templates/          # Template spécifique au projet (potentiellement surcharge)
```

### Gestion configuration multi-environment

Le fichier `settings.py` peut-être décomposé à volonté.
Il est recommandé d'utilisé des fichiers différent pour chaque environment.

Le fichier utilisé par Django est difini par l'env `DJANGO_SETTINGS_MODULE` (cf. [manage.py](./src/manage.py)).

Par exemple, on peut créer un fichier `settings_local.py`:

```python
from .settings_common import *

ALLOWED_HOSTS = ["localhost"]
DEBUG = True
...
```

De la même façon un fichier pour la prod `settings_prod.py`:

```python
from .settings_common import *

DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
...
```

### Configuration Django

Confère la [documentation](https://docs.djangoproject.com/en/4.0/topics/settings/) et la [référence](https://docs.djangoproject.com/en/4.0/ref/settings/)

Voici les plus importantes:

* `DEBUG`: C'est un booléan permettant d'activer / désactiver le mode debug de Django. Ce mode fourni énormément d'information en cas d'exception. **A ne surtout pas laisser actif en PROD**.
* `ALLOWED_HOSTS`: Cette variable contient la liste des domaines authorisés à accéder à l'application (http header Host). Si un domaine n'est pas dans liste, Django retournera une erreur systématiquement.
* `SECRET_KEY`: Cette variable est une chaîne de caractère aléatoire utilisé pour l'encryption. Il est recommandé d'avoir une valeur différente pour chaque environnement. **Attention a ne jamais changer cette valeur par la suite**.
* `INSTALLED_APPS`: La liste des applications chargés par le projet. Concrètement le projet Django importera le fichier apps.py de toutes les applications listées ici, dans l'ordre indiqué. **L'ordre est important !** Par ailleurs une application peut être utilisée comme package uniquement. Dans ce cas, elle n'a pas besoin d'être dans la liste.
* `LOGGING`: Cette variable permet de définir le format et le niveau des logs. Pour plus d'info [la doc](https://docs.djangoproject.com/en/4.0/topics/logging/#configuring-logging)

Il est important de noter que chaque application peut venir avec son lot de configurations qu'il faudra ajouter aux settings.

## Initialisation d'une application Django

```bash
src/myproject/
django-admin startapp <myapp>
```

### Composition d'une application Django

```bash
src/myproject/myapp/
./__init__.py     # Une application django est un package python donc __init__.py obligatoire, même vide
./apps.py         # Point d'entrée de l'application. C'est le fichier qui est chargé par Django si l'application est dans les INSTALLED_APPS
./models.py       # Peut être nommé différement, contient les models
./admin.py        # Peut être nommé différement, Contient les models admin
./tests.py        # Contient les tests, en réalité tous les fichiers tests*.py sont utilisés pour les tests
./views.py        # Peut être nommé différement, Contient les vues
./migrations/     # Dossier contenant toutes les migrations de l'application
  ./__init__.py   # Les migrations sont des packages python donc __init__.py obligatoire, même vide
```

Vous pouvez créer autant de fichier que vous le souhaitez. La seule recommandation est de maintenir une cohérence entre le nom du fichier et son contenu.


## CLI Django

Le point d'entrée pour toutes les commandes Django est `manage.py`.

```bash
python src/manage.py
```

### Initialisation/mise à jour de la DB

```bash
python src/manage.py makemigrations
python src/manage.py migrate
```

### Vérifier l'intégrité du projet

```bash
python src/manage.py check
```

### Django Shell

```bash
python src/manage.py shell
```

### Lancement du server de dèveloppement

```bash
python src/manage.py runserver
```

### Accéder à la DB via Django

```bash
python src/manage dbshell
```

# [Next](./doc/README.md)
