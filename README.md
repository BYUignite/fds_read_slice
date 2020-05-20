### D. Lignell May 20, 2020.

Case is a box with a square plume with wind on a slope. 
The slope is modeled through the gravity vector.
Case is setup for four MPI processes (four meshes).

**Files:**
* case.fds:               input file
* go.sh:                  driver script: run this!
* make_init_vel_field.py: creates the initial velocity profile files; called by go.sh
* get_var_slice.py:       get a slice of a var for ALL meshes; reads case.fds, uses slread.py; plots if run as main.
* slread.py:              from fds/Utilities; bug fix + added skipping; called by get_var_slice.py
* plot_slice.ipynb:       plotting routine; calls get_var_slice.py

Use Python3.

Developed, run, and tested on a mac 10.15.2
