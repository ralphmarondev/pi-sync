#!/bin/bash

cd api
source .venv/Scripts/activate
echo "Starting Django REST Framework application..."
python manage.py runserver &
DJANGO_PID=$!

cd ../raspberrypi/app
echo "Starting Tkinter application..."
python main.py &
TKINTER_PID=$!

wait $DJANGO_PID $TKINTER_PID
