## Commandes à retenir pendant le développement 
| Étape | Opération | Commande / Fichier | Description |
|---|---|---|---|
| 1 | Créer le dossier du projet | `mkdir MonProjet` | Créer le répertoire du projet |
| 2 | Initialiser uv | `uv init --bare` | Initialiser le projet Python sans dossier `src` |
| 3 | Créer l'environnement virtuel | `uv venv` | Créer l'environnement `.venv` |
| 4 | Installer Django 5.2 | `uv add "django==5.2.*"` | Installer Django 5.2 |
| 5 | Vérifier la version | `uv run python -m django --version` | Vérifier la version installée |
| 6 | Créer le projet Django | `uv run django-admin startproject config .` | Créer la configuration Django à la racine |
| 7 | Créer une application | `uv run python manage.py startapp nom_app` | Créer une application Django |
| 8 | Enregistrer l'application | `config/settings.py` | Ajouter l'application dans `INSTALLED_APPS` |
| 9 | Développer les modèles | `nom_app/models.py` | Définir les classes et les relations entre les modèles |
| 10 | Générer les migrations | `uv run python manage.py makemigrations` | Générer les fichiers de migration |
| 11 | Appliquer les migrations | `uv run python manage.py migrate` | Créer ou mettre à jour les tables de la base de données |
| 12 | Configurer l'administration | `nom_app/admin.py` | Enregistrer les modèles dans l'interface d'administration |
| 13 | Créer un administrateur | `uv run python manage.py createsuperuser` | Créer un compte administrateur |
| 14 | Développer les vues | `nom_app/views.py` | Développer la logique métier et les traitements |
| 15 | Configurer les URL | `nom_app/urls.py` et `config/urls.py` | Définir les routes de l'application |
| 16 | Lancer le serveur | `uv run python manage.py runserver` | Démarrer le serveur de développement |
| 17 | Tester l'application | Navigateur web | Vérifier le fonctionnement de l'application |



**Important :** Chaque fois que les modèles sont créés ou modifiés, exécuter les deux commandes suivantes :

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

Documentation officielle : https://docs.djangoproject.com/en/5.2/
