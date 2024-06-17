#!/bin/bash

cd front && poetry install && cd ..
cd backend && poetry install && cd ..
cd azureml && poetry install && cd ..
pre-commit install

