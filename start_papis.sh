#!/bin/bash
export DISPLAY=:0
export XAUTHORITY=/home/mistpl/.Xauthority

# Give Svfb some time to start up
# sleep 5

/home/mistpl/inderr-receiver/venv/bin/python /home/mistpl/inderr-receiver/main.py >> /home/mistpl/inderr-receiver/papis.log 2>&1
