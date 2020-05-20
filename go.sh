#!/bin/bash

date

python3 make_init_vel_field.py
mpiexec -np 4 fds dol.fds

date
