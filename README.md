## FDS Python Reader for Slice File

### D. Lignell May 20, 2020.

Case is a box with a square plume with wind on a slope. 
The slope is modeled through the gravity vector.
Case is setup for four MPI processes (four meshes).
There is also a case2 that uses 256 MPI processes (256 meshes) and multiple planes.

The purpose of this case and code is the get_var_slice.py script that reads the
slice files across multiple meshes and outputs a single variable at all (or fewer) output times.
The QUANTITIES allowed should be fairly generic, but this was not extensively tested.
The meshes are assumed to be set up in a Cartesian layout in a right rectangular prism.
No accounting is made for overlapping, refined, or stretched meshes.

**Files:**
* case.fds:               input file
* go.sh:                  driver script: run this!
* make_init_vel_field.py: creates the initial velocity profile files; called by go.sh
* get_var_slice.py:       get a slice of a var for ALL meshes; reads case.fds, uses slread.py; plots if run as main.
* slread.py:              from fds/Utilities; bug fix + added skipping; called by get_var_slice.py
* plot_slice.ipynb:       plotting routine; calls get_var_slice.py

Use Python3.

Developed, run, and tested on a mac 10.15.2
