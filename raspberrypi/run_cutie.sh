#!/bin/bash
#
# MIT License
# 
# Copyright (c) 2025 Ralph Maron Eda
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# 💜 Hello there :))
echo -e "\n\033[1;35m✨ Created with love by Ralph Maron Eda 💜\033[0m"
sleep 3

x-terminal-emulator -e bash -c "sudo python3 solenoid.py; exec bash" &
x-terminal-emulator -e bash -c "source .venv/bin/activate && python lcd_main.py; exec bash" &
x-terminal-emulator -e bash -c "source .venv/bin/activate && python fingerprint.py; exec bash" &

# 📝 Instructions:
# Navigate to the folder containing run_cutie.sh first:
# cd ~/pi-sync/raspberrypi/
# Then make it executable once:
# chmod +x run_cutie.sh
# And run it:
# ./run_cutie.sh
