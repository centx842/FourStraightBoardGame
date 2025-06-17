FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    python3 python3-pip python3-venv \
    build-essential python3-dev curl git

RUN pip3 install pyinstaller pygame numpy

WORKDIR /app
COPY . /app

RUN pyinstaller --onefile --noconsole --icon=Resources/game.png --name=tictactoe Resources/TicTacToe_Agent.py
