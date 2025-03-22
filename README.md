# Monimate : Budget Tracker

## Description

Le **Budget Tracker** est une application web construite avec **Python** et **Flask**. Elle permet aux utilisateurs de suivre et gérer leurs finances personnelles, d'ajouter des dépenses, de visualiser leurs soldes, et de catégoriser leurs transactions pour mieux comprendre leurs habitudes de dépenses.

L'application permet de se connecter, de créer des catégories de dépenses, et d'ajouter des transactions avec des informations détaillées. Elle est conçue pour être simple et intuitive, avec une interface légère et réactive.

## Fonctionnalités

- Authentification des utilisateurs
- Suivi des transactions (dépenses et revenus)
- Catégorisation des dépenses
- Affichage des soldes et des graphiques de dépenses
- Interaction avec une base de données PostgreSQL pour la gestion des informations

## Technologies

- **Backend**: Flask (Python)
- **Base de données**: PostgreSQL
- **CI/CD**: GitLab CI
- **Gestion des dépendances**: Poetry

## Pipeline CI/CD

Le pipeline CI/CD utilisé dans ce projet est configuré sur **GitLab CI** et comprend les étapes suivantes :

### Stages

1. **Build** : Construction de l'image Docker et push dans le registre GitLab.
2. **Setup-back** : Installation des dépendances Python via Poetry.
3. **Test** : Exécution des tests unitaires et vérification du code via des outils comme `autopep8`, `flake8`, `black`, `isort`, `mypy`, `pylint`, et `bandit`.
4. **Deploy** : Déploiement de l'application sur l'environnement de production.

### Pipeline détaillé

Voici les étapes définies dans le pipeline GitLab CI :

#### Build Job

- **Stage**: build
- **Image**: `docker`
- **Services**: `docker:dind` (Docker-in-Docker)
- **Actions**:
  - **Authentification avec le registre Docker** : Utilise les variables d'environnement GitLab pour se connecter au registre Docker.
  - **Construction de l'image Docker** : Crée une image Docker de l'application.
  - **Push de l'image dans le registre GitLab** : Pousse l'image construite vers le registre GitLab pour une utilisation ultérieure dans d'autres jobs.

#### Setup-back Job

- **Stage**: setup-back
- **Actions**:
  - **Installation des dépendances Python via Poetry** : Poetry est utilisé pour installer les dépendances du projet à partir du fichier `pyproject.toml`. Cela permet de gérer les environnements virtuels et les paquets Python de manière cohérente.

#### pycs (Code Quality Check)

- **Stage**: test
- **Actions**:
  - **Installation et exécution des outils de formatage de code et de linting** :
    - **autopep8** : Outil de formatage de code qui modifie le code Python pour respecter la convention PEP 8.
    - **flake8** : Linter qui analyse le code pour détecter des erreurs potentielles, des problèmes de style et des incohérences.
    - **black** : Outil de formatage de code "opinionated", qui reformate le code selon des règles de style strictes.
    - **isort** : Outil qui trie les importations dans les fichiers Python pour améliorer la lisibilité et le respect des conventions.

#### pystan (Static Analysis)

- **Stage**: test
- **Actions**:
  - **Exécution de l'analyse statique du code** :
    - **mypy** : Outil de vérification des types statiques dans le code Python, permettant de détecter les erreurs de type avant l'exécution.
    - **pylint** : Linter qui analyse le code pour en évaluer la qualité en termes de style, de sécurité et d'optimisation.
    - **bandit** : Outil de sécurité qui analyse le code pour détecter des vulnérabilités potentielles, comme l'utilisation de fonctions ou de pratiques dangereuses.

#### Test

- **Stage**: test
- **Services**: `postgres:latest`
- **Actions**:
  - **Exécution des tests unitaires avec pytest** : `pytest` est utilisé pour exécuter les tests unitaires du projet. Il aide à s'assurer que l'application fonctionne comme prévu et à détecter les bugs.

#### Deploy

- **Stage**: deploy
- **Actions**:
  - **Déploiement de l'application sur l'environnement de production** : Cette étape est responsable du déploiement de l'application une fois que toutes les étapes précédentes (build, tests, etc.) ont été validées.

## Installation

### Prérequis

- Python 13+
- Docker (optionnel, pour exécuter l'application via un conteneur)
- PostgreSQL (pour la gestion des données)

### Cloner le projet

```bash
git clone https://gitlab.com/dlsptm/monimate-back.git
cd monimate-back
