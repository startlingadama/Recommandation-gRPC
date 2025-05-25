# gRPC Recommender Service

Ce projet implémente un service gRPC simple en Python qui recommande un prix, une durée et un moyen de transport entre deux villes.

## Structure du projet

```text
grpc\_recommender/
├── client.py          # Client gRPC qui interroge le service
├── server.py          # Serveur gRPC avec une implémentation simple
├── service.proto      # Fichier de définition du service gRPC
├── service\_pb2.py     # Fichier généré automatiquement
├── service\_pb2\_grpc.py# Fichier généré automatiquement

```

## Installation

1. **Cloner le projet** (si besoin)  
2. **Créer un environnement virtuel** (optionnel mais recommandé) :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
```

3. **Installer les dépendances** :

   ```bash
   pip install grpcio grpcio-tools
   ```

## Génération des fichiers gRPC

Exécute cette commande pour générer les fichiers Python à partir du `.proto` :

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
```

Cela va générer :

* `service_pb2.py`
* `service_pb2_grpc.py`

##  Lancer le serveur

```bash
python server.py
```

Tu verras :

```
Serveur gRPC démarré sur le port 50051
```

## 📡 Lancer le client

Dans un autre terminal :

```bash
python client.py
```

Résultat attendu :

```
Prix: 150 MAD, Durée: 4h10, Transport: Bus
```

## Technologies utilisées

* Python 3.8+
* gRPC (Google Remote Procedure Call)
* Protocol Buffers (protobuf)

## Utilité

Ce projet peut servir de base à un microservice de recommandation (prix, trajet, etc.) dans un système plus large utilisant :

* des agents LLM
* un orchestrateur (ex: FastAPI, GraphQL)
* un front (React, mobile, etc.)


