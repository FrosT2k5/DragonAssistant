#!/bin/bash

# Colors
RED="\033[1;31m" # For errors / warnings
GREEN="\033[1;32m" # For info
NC="\033[0m" # reset color

# Install some packages
if [[ -e "/usr/bin/apt-get" ]]; then
    echo -e "${GREEN}Installing Some requirements${NC}"
    sudo apt-get install python3 python3-pip curl wget python3-pyaudio espeak -y
else
   echo -e "${RED}Looks like you aren't using a debian based distro, please install python, pip, python3-pyaudio and espeak with your distro's package manager${NC}"
fi
pip3 install -r requirements.txt
