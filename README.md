# Crysalis-CIFOD
Jupyter notebook processing Rigaku Crysalis ".cif_od" files.
Can be used for single crystal data obtained at conventional and high pressure experiments.

Files are uploaded into the notebook using an upload button. The code displays information
regarding lattice parameters, volume for constrained and unconstraned unit cell, orientation matrix.

In addition the code uses [plotly](https://plotly.com "Plotly") in order to display orientation of the unit cell with respect to the instrument cartesian coordinates.

Installation of plotly within Jupiter-Notebook or JupyterLab is described [separately](https://plotly.com/python/getting-started/ "Plotly documentation").

Snapshots of the output:
![Stats output](https://github.com/lorcat/Crysalis-CIFOD/blob/main/app/images/example_stats.png)
![3D view output](https://github.com/lorcat/Crysalis-CIFOD/blob/main/app/images/example_unitcell.png)