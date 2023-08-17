# Utilisez une image de base Python officielle
FROM python:3.10

# Définissez les variables d'environnement pour Python en mode non-tamponné
ENV PYTHONUNBUFFERED 1

# Créez un répertoire pour le projet dans le conteneur
RUN mkdir /app

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le Pipfile et Pipfile.lock dans le conteneur
COPY Pipfile Pipfile.lock /app/

# Installez les dépendances système requises par certaines bibliothèques Python
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Installez pipenv et les dépendances du projet
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copiez le contenu de votre projet dans le conteneur
COPY . /app/

# Exposez le port sur lequel l'application fonctionne
EXPOSE 8000

# Définissez la commande à exécuter lorsque le conteneur démarre
CMD ["pipenv", "run", "python", "income_expense/manage.py", "runserver", "0.0.0.0:8000"]
