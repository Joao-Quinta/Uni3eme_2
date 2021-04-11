#!/usr/bin/env bash

# Get CIFAR10
if [ "$(uname)" == "Darwin" ]; then
    # Mac OS X platform
    curl -O http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz        
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # GNU/Linux platform
    wget http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
fi
tar -xzvf cifar-10-python.tar.gz
rm cifar-10-python.tar.gz 
