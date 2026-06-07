#!/bin/bash
redis-server --daemonize yes --loglevel warning
sleep 1
python3 main.py
