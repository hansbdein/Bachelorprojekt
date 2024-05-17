# Galactic Structure And Dynamics
Notes for Bovy's graduate course on Galactic Structure and Dynamics

## Setting up the necessary python environment

Most of the necessary packages can be installed by doing

```
conda env create -f environment.yml
```

which creates the conda environment ``galdyncourse``. Activate this
environment with
```
source activate galdyncourse
```
[NOT CURRENTLY NECESSARY] Some packages cannot be installed through conda, for those run (after activating the environment)
```
pip install -r requirements.txt
```
Finally, a small set of tools specific to these notes can be installed with
```
python setup.py install
```

## Developing these notes

These notes require my custom version of ``sphinx`` and ``nbsphinx``, which can be found [here](https://github.com/jobovy/sphinx) and [here](https://github.com/jobovy/nbsphinx/tree/always-show-code).

Copying to my web server is currently done with
```
rsync -azv build/html/ uoft:/home/bovy/web/AST1420/notes-2018/
```