#!/bin/bash

# Run both Python files in the background
echo "Starting fingerprint detection and solenoid control..."

# Start main.py (GUI-based) in the background
python3 main.py &

# Start solenoid.py in the background
python3 solenoid.py &

# Wait for both processes to complete (optional)
wait
