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
    pip install numpy scikit-image lpips opencv-python flip-evaluator pyexr && 
    pip install -r ext/neural_sdf/infra/requirements.txt &&
    touch "$VENV_DIR/installed"


    patch ext/nbvh/ext/flip-cuda/common/FLIP.cpp ext/FLIP.cpp.patch

fi
