#!/bin/bash

cp ext/FLIP.cpp ext/nbvh/ext/flip-cuda/common/FLIP.cpp

cd ext/nbvh

cmake -G Ninja -DCMAKE_CUDA_ARCHITECTURES=89 -B build && {
    cmake --build build --config Release
}