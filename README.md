# Alcolizer Hook Compose

This script reads the required API response and then composes the message for Azure Service Bus

## config

environment variables needed to run the script

| environment var name | value
|----------------------| ------
|ALCOLIZER_API_HOST|`uri` the base url for the connecting to the API host (_example http://127.0.0.1:8080_)
|ALCOLIZER_API_KEY|`str` A private shared key between the API server and this script
|AZURE_SERVICE_BUS_CONNECTION_STRING|`str` The connection string from Azure for the service bus account
|AZURE_SERVICE_BUS_QUEUE|`str` The name of the azure service bus queue

## dev setup

setup the virtual environment using pipenv, run this command in the directory with this file in it. (be sure you have the following environ set `PIPENV_VENV_IN_PROJECT=true`)

    pipenv install --dev

open the folder with this file in it, with VS Code. (only works if you have installed the shell command for VS Code)

    code .

## updating requirements.txt

to update requirements.txt use the following command in the directory with this file.

    pipenv lock -r > requirements.txt

## installing for production

install the requirements for this code with

    pip install -U -r requirements.txt
