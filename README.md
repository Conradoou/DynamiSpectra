Overview
=========

[![PyPI Package latest release](https://img.shields.io/pypi/v/dynamispectra.svg)](https://pypi.org/project/dynamispectra)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/dynamispectra.svg)](https://pypi.org/project/dynamispectra)
[![Supported versions](https://img.shields.io/pypi/pyversions/dynamispectra.svg)](https://pypi.org/project/dynamispectra)
[![Supported implementations](https://img.shields.io/pypi/implementation/dynamispectra.svg)](https://pypi.org/project/dynamispectra)
[![Commits since latest release](https://img.shields.io/github/commits-since/conradoou/dynamispectra/v1.0.0.svg)](https://github.com/conradoou/dynamispectra/compare/v1.0.0...main)


DynamiSpectra: from molecular dynamics simulations to comprehensive data analysis
----------------------------------------------------------------------------------

*DynamiSpectra* is an advanced Python package designed for analyzing molecular dynamics simulation data. Built to process and interpret results primarily from `GROMACS <https://www.gromacs.org/>` structure, *DynamiSpectra* provides a streamlined and efficient workflow for researchers in the field of molecular dynamics. By leveraging the power of Python, this package enables users to perform complex analyses, visualize molecular behaviors, and gain valuable insights from simulation outputs. Whether you're studying protein folding, ligand interactions, or other molecular phenomena, *DynamiSpectra* empowers you to dive deep into your data and uncover meaningful patterns. 

It provides powerful tools to calculate and visualize a wide range of molecular properties, including Hydrogen bonds, Root Mean Square Deviation (RMSD), Root Mean Square Fluctuation (RMSF), Solvent Accessible Surface Area (SASA), Radius of Gyration (Rg), Molecular Orientation, Secondary Structure Analysis, Binding Energy, Protein-Ligand Contacts, System Density, Temperature and Pressure, Distance Matrix, Hydrophobic Contacts, Ligand Dihedral Angles, Protein Rotamers, Phi and Psi Angles, and Salt Bridges. These features enable researchers to gain deep insights into the dynamics of molecular systems, study conformational changes, and investigate interactions between molecules with greater precision.

Installation
------------

::

    pip install DynamiSpectra

You can also install the in-development version with::

    pip install https://github.com/Conradoou/DynamiSpectra/archive/main.zip

Note: *DynamiSpectra* uses the package SciPy, which requires a fortran compiler to be installed to build its source,which can be tricky on some systems. An alternative to this is to use Anaconda environment. *DynamiSpectra* can then be more easily installed within this environment, using the command line or preferred method. Installing *DynamiSpectra* may take some time on certain systems. If you observe the command line halting, please be patient, as the installation process may require seconds to minutes to complete.

Documentation
-------------

https://github.com/Conradoou/DynamiSpectra/blob/6b8200eae1baf6dd75d88af79e047353c8ffdc8d/Documentation.pdf
https://conradoou.github.io/DynamiSpectra/

Authors
-------

Iverson Conrado Bezerra
Orcid: 0000-0003-0524-8913

Register
--------

DynamiSpectra is registered with the Brazilian National Institute of Industrial Property (INPI) under the code BR 51 2025 002221-2.

Demo
----

In the repository, specifically in DynamiSpectra/datas, there are several folders for each analysis with the corresponding GROMACS output data for testing.
