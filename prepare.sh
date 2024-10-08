#!/bin/bash

VENV_DIR=.venv


#Virtual env doesnt exist -> install deps
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR" || rm -rf "$VENV_DIR"
  source "$VENV_DIR/bin/activate"
fi


#Virtual env exists -> load
if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
fi

if [ ! -f "$VENV_DIR/installed" ]; then
    pip install numpy scikit-image opencv-python && touch "$VENV_DIR/installed"
fi
