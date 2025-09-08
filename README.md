# Legal Translator REST API

A simple FastAPI REST API that serves the English → Serbian legal document translator model.
This service exposes endpoints for translation so the model can be integrated into other applications.

Port forwarded with ngrok to test but currently only defined so it can run localy 

It is designed in mind to integrate my trained pytorch model with the flutter front. Currently as is in the code, its just fetching
a trained huggingface translation model

# Features

REST API built with FastAPI.

Endpoint for translating English text into Serbian legal language.

Ready for integration with frontend apps or other services.

# API Endpoints
🔹 Translate Text

POST /translate

Request Body:

{
  "text": "This agreement shall remain in force until terminated by either party."
}


Response:

{
  "translation": "Ovaj ugovor ostaje na snazi sve dok ga ne raskine jedna od strana."
}

# Roadmap

Not yet deployed with docker

Currently not running from a server, only local


# Important Notes
The src file is only for reference, everything is done in colab notebooks using their gps from the cloud.
TODO: organize the notebook better.
