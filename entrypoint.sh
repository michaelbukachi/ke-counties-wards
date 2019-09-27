#!/usr/bin/env bash

export PYTHONUNBUFFERED=0

gunicorn -c settings.py wsgi:app



