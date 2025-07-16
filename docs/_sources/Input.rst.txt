Input
=====

*DynamiSpectra* provides a variety of data analysis tools for GROMACS output files:


Root Mean Square Deviation
---------------------------------

*DynamiSpectra* requires GROMACS output files with the `.xvg` extension for RMSD analysis. These files must contain the time series of atomic deviations during the simulation, typically generated using the `gmx rms` tool from GROMACS. The `.xvg` file is expected to have two columns: the first representing simulation time in nanoseconds (ns), and the second containing RMSD values in nanometers (nm). These values correspond to the deviation of the selected atoms or groups of atoms over time, in relation to a reference structure.

To generate this file using GROMACS, the following command can be used:

.. code:: bash

    gmx rms -s Simulation.tpr -f Simulation.xtc -o rmsd.xvg -tu ns

*DynamiSpectra* allows the analysis of one or more simulation groups. Each group can include one or multiple replicate `.xvg` files. The analysis function automatically computes the average and standard deviation across replicates for each group and produces both time-resolved and density plots.

**Code Execution**

The analysis is performed by calling the `rmsd_analysis` function from the RMSD module:

.. code:: python

    from dynamispectra.RMSD import rmsd_analysis

The following example shows how to analyze three simulation groups, each containing three replicates:

.. code:: python

    # Input RMSD files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSD\rmsd_Replicate3.xvg'
    ]

    # Output directory to save plots
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Optional configuration for the RMSD vs time plot
    rmsd_config = {
        # Labels for each group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Line colors for each group
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency of the shaded error area                
        'alpha': 0.2,
        # Size of the figure (width, height)                                                
        'figsize': (9, 6),
        # Label for the x-axis                                          
        'xlabel': 'Simulation Time (ns)',
        # Label for the y-axis                            
        'ylabel': 'RMSD (nm)', 
        # Font size for axis labels                                      
        'label_fontsize': 12                                         
    }

    # Optional configuration for the RMSD density (distribution) plot
    density_config = {
        # Labels for each group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Line colors for each group
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency of the curves               
        'alpha': 0.6,
        # Size of the density plot                                                
        'figsize': (6, 6), 
        # Label for the x-axis                                          
        'xlabel': 'RMSD (nm)', 
        # Label for the y-axis                                     
        'ylabel': 'Kernel Density',
         # Font size for axis labels                                
        'label_fontsize': 12                                        
    }

    # Run the analysis
    rmsd_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        rmsd_config=rmsd_config,
        density_config=density_config
    )

The `rmsd_config` and `density_config` dictionaries allow users to customize the appearance of the plots. All fields are optional, and default values will be applied if no configuration is provided.

Although the function supports multiple groups with replicates, it also works with a single group and a single replicate. For example, calling:

.. code:: python

    rmsd_analysis(output_folder, simulation1_files)

is sufficient to generate RMSD and density plots for just one simulation set. This flexibility allows users to perform both basic and comparative analyses without modifying the source code, regardless of the number of replicates available.


Root Mean Square Fluctuation
-----------------------------------

*DynamiSpectra* requires GROMACS output files with the `.xvg` extension for RMSF analysis. These files must contain the root mean square fluctuation of each residue, typically generated using the `gmx rmsf` tool from GROMACS. The `.xvg` file must contain two columns: the first indicating the residue number, and the second representing the RMSF value (nm) for each residue. These values quantify the flexibility or mobility of each residue along the simulation trajectory.

To generate the required file using GROMACS, the following command can be used:

.. code:: bash

    gmx rmsf -f Simulation.xtc -s Simulation.tpr -o rmsf.xvg -res

*DynamiSpectra* allows analyzing one or more simulation groups, each optionally containing multiple replicate `.xvg` files. The analysis function computes the average and standard deviation across replicates and generates two types of plots: a per-residue fluctuation curve and a density distribution of RMSF values.

**Code Execution**

Import the analysis function:

.. code:: python

    from dynamispectra.RMSF import rmsf_analysis

Example with three simulation groups, each containing three replicates:

.. code:: python

    # Define replicate file paths for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\RMSF\rmsf_Replicate3.xvg'
    ]

    # Output directory to save the plots
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Optional configuration for the per-residue RMSF plot
    rmsf_config = {
        # Labels for each group in the legend
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'], 
        # Line colors for each group 
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency of the shaded error region                
        'alpha': 0.3,   
        # Size of the figure (width, height)                                             
        'figsize': (9, 6), 
        # Label for the x-axis                                          
        'xlabel': 'Residue Number', 
        # Label for the y-axis                                 
        'ylabel': 'RMSF (nm)',
        # Font size for axis labels                                       
        'label_fontsize': 12,
        # X-axis limits (optional)                                       
        'xlim': (1, 42), 
        # Y-axis limits (optional)                                            
        'ylim': (0.1, 0.9),                                         
    }

    # Optional configuration for the RMSF density plot
    density_config = {
        # Labels for KDE curves
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Colors for KDE curves  
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency of the KDE fill               
        'alpha': 0.5,
        # Size of the density figure                                                
        'figsize': (6, 6),
        # X-axis label                                           
        'xlabel': 'RMSF (nm)', 
        # Y-axis label                                      
        'ylabel': 'Density',
        # Font size for axis labels                                         
        'label_fontsize': 12,  
        # X-axis limits (optional)                                      
        'xlim': (0, 1), 
        # Y-axis limits (None = automatic)                                            
        'ylim': None,                                               
    }

    # Run the RMSF analysis
    rmsf_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        rmsf_config=rmsf_config,
        density_config=density_config
    )

You may also analyze a single group with a single replicate by passing only one list of files:

.. code:: python

    rmsf_analysis(output_folder, simulation1_files)

Both configuration dictionaries (`rmsf_config` and `density_config`) are optional. If not provided, the function will generate plots with default layout and colors. This flexibility allows users to customize plots according to their preferences while keeping the function compatible with both simple and advanced use cases.


Radius of Gyration
-----------------------

*DynamiSpectra* requires GROMACS output files with the `.xvg` extension for Radius of Gyration (Rg) analysis. These files should contain the time series of Rg values computed during the simulation, typically generated with the `gmx gyrate` tool. The `.xvg` file must include the simulation time in nanoseconds (ns) in the first column and the total radius of gyration in nanometers (nm) in the second column. Additional columns (typically third to fifth) may include component values along the X, Y, and Z axes, though only the total Rg (second column) is used in this analysis.

To generate a compatible file using GROMACS, the following command can be used:

.. code:: bash

    gmx gyrate -f Simulation.xtc -s Simulation.tpr -o gyrate.xvg

The analysis supports one or more simulation groups, each potentially composed of multiple replicate `.xvg` files. *DynamiSpectra* calculates average and standard deviation across replicates for each group, and produces both a time-resolved plot and a distribution (KDE) plot of the Rg values.

**Code Execution**

Import the analysis function from the Rg module:

.. code:: python

    from dynamispectra.Rg import rg_analysis

Example using three simulation groups with three replicates each:

.. code:: python

    # Define replicate files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Rg\gyrate_Replicate3.xvg'
    ]

    # Output directory to save the plots
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Configuration for the Rg time series plot
    rg_config = {
        # Legend labels for each simulation group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Line and fill colors  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency for shaded error band                 
        'alpha': 0.2, 
        # Width and height of the figure                                               
        'figsize': (9, 6),  
         # Label for the x-axis                                        
        'xlabel': 'Simulation Time (ns)',
        # Label for the y-axis                           
        'ylabel': 'Rg (nm)',  
        # Font size for axis labels                                       
        'label_fontsize': 12                                      
    }

    # Configuration for the Rg distribution (KDE) plot
    density_config = {
        # Labels matching each simulation group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Fill colors for density curves  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency for KDE fill                 
        'alpha': 0.6,  
        # Width and height of the KDE figure                                              
        'figsize': (6, 6),  
        # Label for the x-axis                                        
        'xlabel': 'Rg (nm)', 
        # Label for the y-axis                                        
        'ylabel': 'Kernel Density', 
        # Font size for axis labels                                 
        'label_fontsize': 12                                       
    }

    # Run the Rg analysis and generate both plots
    rg_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        rg_config=rg_config,
        density_config=density_config
    )

It is also possible to run the analysis using a single group with only one replicate. For example:

.. code:: python

    rg_analysis(output_folder, simulation1_files)

All plot configuration dictionaries are optional. If omitted, the plots will be generated with default visual settings. This design allows users to tailor the visualization for presentations or publications without altering the analysis logic.


Hydrogen Bond Analysis
------------------------------

*DynamiSpectra* requires `.xvg` output files from GROMACS for hydrogen bond analysis. These files are typically generated using the `gmx hbond` tool and must contain the time-resolved data of H-bond interactions observed during molecular dynamics simulations.

The `.xvg` file must have the following structure:

- Column 1: Simulation time in nanoseconds  
- Column 2: Total number of hydrogen bonds detected at each time point  
- Column 3: Number of atom pairs within 0.35 nm (potential H-bond candidates)

These data enable detailed tracking of H-bond dynamics and the compactness or rearrangement of molecular systems throughout the simulation.

To generate the required `.xvg` file using GROMACS:

.. code:: bash

    gmx hbond -s Simulation.tpr -f Simulation.xtc -num hbond.xvg -tu ns

*DynamiSpectra* supports analysis of one or multiple simulation groups, each optionally including several replicate files. It computes the average and standard deviation of H-bond counts across replicates and generates both time-resolved and density plots.

**Code Execution**

Import the H-bond analysis function:

.. code:: python

    from dynamispectra.Hbond import hbond_analysis

Example using three simulation groups:

.. code:: python

    # Define paths to .xvg replicate files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Hbond\hbond_Replicate3.xvg'
    ]

    # Folder where the plots will be saved
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Plot configuration for H-bond over time
    hbond_config = {
        # Legend labels for each simulation
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'], 
        # Line and fill colors for each group 
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency for shaded error area                
        'alpha': 0.2,    
        # Width and height of the time series figure                                            
        'figsize': (9, 6), 
        # Label for the x-axis                                         
        'xlabel': 'Time (ns)', 
        # Label for the y-axis                                      
        'ylabel': 'Number of H-bonds',
        # Font size of axis labels                               
        'label_fontsize': 12                                        
    }

    # Plot configuration for H-bond density (KDE)
    density_config = {
        # KDE labels
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # KDE fill colors  
        'colors': ['#333333', '#6A9EDA', '#49C547'],   
        # Transparency for KDE areas              
        'alpha': 0.6,        
        # Width and height of the KDE figure                                        
        'figsize': (6, 6),            
        # x-axis label                              
        'xlabel': 'Number of H-bonds',
        # y-axis label                               
        'ylabel': 'Kernel Density', 
        # Font size for axis labels                               
        'label_fontsize': 12                                         
    }

    # Run the H-bond analysis
    hbond_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        hbond_config=hbond_config,
        density_config=density_config
    )

You can also run the analysis with a single group and a single replicate:

.. code:: python

    hbond_analysis(output_folder, simulation1_files)

If configuration dictionaries are omitted, *DynamiSpectra* will generate the plots with default settings. These customization options allow full control of the appearance for publications or presentations.


Solvent Accessible Surface Area
--------------------------------------

*DynamiSpectra* requires `.xvg` output files from GROMACS for SASA analysis. These files are typically generated using the `gmx sasa` tool and provide time-resolved measurements of the solvent-accessible surface area of the selected atoms during the simulation.

The `.xvg` file must follow this format:

- Column 1: Simulation time (ps)  
- Column 2: Total SASA (nm²) of the selected group of atoms over time

This information enables detailed evaluation of conformational changes and solvation properties of the system.

To generate the required `.xvg` file using GROMACS:

.. code:: bash

    gmx sasa -s Simulation.tpr -f Simulation.xtc -o sasa.xvg -probe 0.14

*DynamiSpectra* supports multiple simulation groups, each with one or more replicates. The package automatically aligns time series, computes mean and standard deviation, and generates plots for both time evolution and density distribution of SASA.

**Code Execution**

Import the SASA analysis module:

.. code:: python

    from dynamispectra.SASA import sasa_analysis

Example with three groups of simulations, each containing three replicates:

.. code:: python

    # Define paths to .xvg replicate files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\data\SASA\sasa_Replicate3.xvg'
    ]

    # Output folder where the plots will be saved
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Configuration for the SASA time series plot
    sasa_config = {
        # Labels shown in legend
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Colors for curves and shaded area  
        'colors': ['#333333', '#6A9EDA', '#49C547'],  
        # Transparency of std deviation fill               
        'alpha': 0.2,          
        # Size of the time series figure                                     
        'figsize': (9, 6),     
        # Label for x-axis                                     
        'xlabel': 'Simulation Time (ns)',
        # Label for y-axis                            
        'ylabel': 'SASA (nm²)',   
        # Font size for axis labels
        'label_fontsize': 12                                        
    }

    # Configuration for the SASA density distribution plot (KDE)
    density_config = {
        # Legend labels for KDE plot
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Fill colors for KDE areas  
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency for filled areas                
        'alpha': 0.6,   
        # Size of the density plot                                             
        'figsize': (6, 6),      
        # x-axis label                                   
        'xlabel': 'SASA (nm²)', 
        # y-axis label                                     
        'ylabel': 'Kernel Density', 
        # Font size for axis labels                                 
        'label_fontsize': 12                                         
    }

    # Run the analysis for SASA
    sasa_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        sasa_config=sasa_config,
        density_config=density_config
    )

To run the analysis with a single group or a single file, just provide one list:

.. code:: python

    sasa_analysis(output_folder, simulation1_files)

If no configuration dictionaries are provided, default settings will be used. Customize the plots as needed to match the desired presentation style or publication format.


Salt Bridge
-----------

*DynamiSpectra* requires `.xvg` output files from GROMACS for salt bridge analysis between the ligand and the protein, or only protein. These files are typically generated using the `gmx mindist` tool with appropriate index groups and contain time series of minimum distances between charged groups.

The `.xvg` file must follow this format:

- Column 1: Simulation time (ps)  
- Column 2: Minimum salt-bridge distance (nm) between charged groups over time

This data allows monitoring the presence or absence of salt-bridge interactions during the simulation.

To generate the required `.xvg` file using GROMACS:

.. code:: bash

    gmx mindist -f Simulation.xtc -s Simulation.tpr -n index.ndx -od Simulation.xvg -on saltbridge.xvg -group -d 0.4

*DynamiSpectra* supports multiple simulation groups, each with one or more replicates. The package automatically aligns time series, computes mean and standard deviation, and generates plots for both time evolution and density distribution of salt-bridge distances.

**Code Execution**

Import the salt bridge analysis module:

.. code:: python

    from dynamispectra.saltbridge import saltbridge_analysis

Example with three groups of simulations, each containing three replicates:

.. code:: python

    # Define paths to .xvg replicate files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\saltbridge_310k_Replicate3.xvg'
    ]

    # Output folder where the plots will be saved
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Configuration for the salt-bridge time series plot
    saltbridge_config = {
        # Labels shown in legend
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Colors for curves and shaded area  
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency of std deviation fill               
        'alpha': 0.2,      
        # Size of the time series figure                                          
        'figsize': (9, 6),     
        # Label for x-axis                                      
        'xlabel': 'Simulation Time (ns)',     
        # Label for y-axis                       
        'ylabel': 'Salt-Bridge Distance (nm)',  
        # Font size for axis labels                    
        'label_fontsize': 12                                        
    }

    # Configuration for the salt-bridge density distribution plot (KDE)
    density_config = {
        # Legend labels for KDE plot
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Fill colors for KDE areas  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency for filled areas                 
        'alpha': 0.6,   
        # Size of the density plot                                             
        'figsize': (6, 6),            
        # x-axis label                               
        'xlabel': 'Salt-Bridge Distance (nm)',  
        # y-axis label                     
        'ylabel': 'Kernel Density', 
        # Font size for axis labels                                 
        'label_fontsize': 12                                        
    }

    # Run the analysis for salt-bridge distances
    saltbridge_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        saltbridge_config=saltbridge_config,
        density_config=density_config
    )

To run the analysis with a single group or a single file, just provide one list:

.. code:: python

    saltbridge_analysis(output_folder, simulation1_files)

If no configuration dictionaries are provided, default settings will be used. Customize the plots as needed to match your presentation or publication style.


Protein–Ligand Contacts
-----------------------

*DynamiSpectra* requires `.xvg` output files from GROMACS for analyzing the number of atomic contacts between protein and ligand during the simulation. These files are typically generated using the `gmx mindist` or `gmx contact` tool with appropriate index groups for the protein and ligand atoms.

The `.xvg` file must follow this format:

- Column 1: Simulation time (ps)
- Column 2: Number of contacts between the selected groups over time

This information allows monitoring interaction stability, binding dynamics, and fluctuation of protein–ligand contacts across time.

To generate the required `.xvg` file using GROMACS:

.. code:: bash

    gmx mindist -f Simulation.xtc -s Simulation.tpr -n index.ndx -on contacts.xvg -d 0.35

*DynamiSpectra* supports multiple simulation groups, each with one or more replicates. The package automatically aligns time series, computes mean and standard deviation, and generates plots for both time evolution and density distribution of contacts.

**Code Execution**

Import the contact analysis module:

.. code:: python

    from dynamispectra.Contacts import contact_analysis

Example with three groups of simulations, each containing three replicates:

.. code:: python

    # Define paths to .xvg replicate files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\contacts_Replicate3.xvg'
    ]

    # Output folder where the plots will be saved
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Configuration for the contact vs. time plot
    contact_config = {
        # Legend labels
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Curve and fill colors  
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Shaded area transparency                
        'alpha': 0.2,  
        # Figure size (width, height)                                              
        'figsize': (9, 6),   
        # x-axis label                                        
        'xlabel': 'Time (ns)', 
        # y-axis label                                      
        'ylabel': 'Number of Contacts', 
        # Font size for labels                            
        'label_fontsize': 12                                         
    }

    # Configuration for the contact density (KDE) plot
    density_config = {
        # Legend labels for KDE
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # KDE fill colors  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency for density                 
        'alpha': 0.2,       
        # Size of the density plot                                         
        'figsize': (9, 6), 
        # x-axis label                                          
        'xlabel': 'Number of Contacts',
        # y-axis label                              
        'ylabel': 'Kernel Density',
        # Font size for labels                                 
        'label_fontsize': 12                                         
    }

    # Run the contact analysis
    contact_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        contact_config=contact_config,
        density_config=density_config
    )

To run the analysis with a single group or a single file, just provide one list:

.. code:: python

    contact_analysis(output_folder, simulation1_files)

If no configuration dictionaries are provided, default settings will be used. Customize the plots to suit your analysis or publication needs.


Protein–Ligand Minimum Distance
-------------------------------

*DynamiSpectra* requires `.xvg` output files from GROMACS to analyze the minimum distance between protein and ligand atoms during molecular dynamics simulations. These files are typically generated using the `gmx distance` tool with selected atom groups from an index file.

The `.xvg` file must follow this format:

- Column 1: Simulation time (ps)
- Column 2: Minimum distance (nm) between protein and ligand atoms at each time point

This analysis allows the evaluation of binding stability, complex dissociation, and proximity of interaction over time.

To generate the required `.xvg` file using GROMACS:

.. code:: bash

    gmx mindist -f Simulation.xtc -s Simulation.tpr -n index.ndx -od mindist.xvg -d 0.35

*DynamiSpectra* supports multiple simulation groups, each with one or more replicates. The tool aligns all time series, computes mean and standard deviation, and generates plots showing time evolution and the distribution of distances.

**Code Execution**

Import the distance analysis module:

.. code:: python

    from dynamispectra.Distance import distance_analysis

Example with three simulation groups, each containing three replicates:

.. code:: python

    # Define paths to .xvg replicate files for each simulation group
    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate3.xvg'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate3.xvg'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate1.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate2.xvg',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\distance_Replicate3.xvg'
    ]

    # Output folder for saving plots and results
    output_folder = r'C:\Users\Conrado\Documents\Test'

    # Configuration for the distance time series plot
    distance_config = {
        # Legend labels for each simulation group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Line colors for the plots  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency of shaded area (std deviation)                  
        'alpha': 0.2,
        # Width and height of the time series plot                                                 
        'figsize': (9, 6),
        # X-axis label                                            
        'xlabel': 'Simulation Time (ns)',
        # Y-axis label                             
        'ylabel': 'Minimum Distance (nm)', 
        # Font size for axis labels                                      
        'label_fontsize': 12    
    }

    # Configuration for the distance density distribution (KDE) plot
    density_config = {
        # Legend labels for KDE
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Fill colors for each simulation group  
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Transparency of KDE fill                
        'alpha': 0.6,     
        # Width and height of the KDE plot                                            
        'figsize': (6, 6),     
        # X-axis label                                       
        'xlabel': 'Minimum Distance (nm)',
        # Y-axis label                          
        'ylabel': 'Kernel Density', 
        # Font size for labels                                  
        'label_fontsize': 12                                          
    }

    # Run the analysis for minimum distance
    distance_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        distance_config=distance_config,
        density_config=density_config
    )

To run the analysis with a single group or a single file, just provide one list:

.. code:: python

    distance_analysis(output_folder, simulation1_files)

If no configuration dictionaries are provided, default plot settings will be applied. You can tailor the plot appearance for presentations or publications by adjusting the dictionary values.


Protein-Ligand Hydrophobic Contacts
-----------------------------------

*DynamiSpectra* supports the analysis of hydrophobic contacts between ligand and protein from `.xvg` files. These files typically represent the number of hydrophobic contacts over time, generated using custom GROMACS selections involving hydrophobic atoms.

The `.xvg` file must follow this format:

- Column 1: Simulation time (ps)  
- Column 2: Number of hydrophobic contacts between ligand and protein

This analysis helps to evaluate the contribution of nonpolar interactions to the stability and binding of protein–ligand complexes.

To generate `.xvg` files, you can use GROMACS with `gmx select` or other post-processing tools with appropriate selections:

.. code:: bash

    gmx select -f Simulation.xtc -s Simulation.tpr -n index.ndx -select 'group "LIG" and within 0.6 of group "Protein"' -os hydrophobic_contacts.xvg

**Code Execution**

Import the analysis function:

.. code:: python

    from dynamispectra.Hydrophobic_contacts import hydrophobic_analysis

Example with three simulation groups, each with three replicate files:

.. code:: python

    simulation1_files = [
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts_Rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts_Rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts_Rep3.xvg'
    ]

    simulation2_files = [
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts2_Rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts2_Rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts2_Rep3.xvg'
    ]

    simulation3_files = [
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts3_Rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts3_Rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\hydrophobic_contacts3_Rep3.xvg'
    ]

    output_folder = r'C:\Users\Conrado\Documents\Test'

    contact_config = {
        # Legend labels for each simulation group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Colors for curves and shaded area  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency of std deviation fill                 
        'alpha': 0.2,            
        # Figure size for time series                                    
        'figsize': (9, 6),         
        # X-axis label                              
        'xlabel': 'Time (ns)', 
        # Y-axis label                                    
        'ylabel': 'Number of Hydrophobic Contacts',                  
        # Font size for axis labels
        'label_fontsize': 12                                        
    }

    density_config = {
        # Labels for KDE curves
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Fill colors for KDE  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency of fill                 
        'alpha': 0.2,
        # Size of the KDE plot                                                
        'figsize': (6, 6),
        # X-axis label                                           
        'xlabel': 'Number of Hydrophobic Contacts',
        # Y-axis label                 
        'ylabel': 'Kernel Density',
        # Font size for axis labels                                  
        'label_fontsize': 12                                        
    }

    hydrophobic_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        contact_config=contact_config,
        density_config=density_config
    )

To run the analysis with only one group or a single file, simply provide one list:

.. code:: python

    hydrophobic_analysis(output_folder, simulation1_files)

If the configuration dictionaries are not provided, default plotting settings will be used.


Inter-residue Distance Matrix
-----------------------------

*DynamiSpectra* supports the visualization of inter-residue distance matrices using `.xpm` files generated by GROMACS. These matrices represent the average distances between residue pairs throughout a trajectory and are useful for identifying compact or flexible regions within a protein.

The `.xpm` file can be generated using the following GROMACS command:

.. code:: bash

    gmx mdmat -f Simulation.xtc -s Simulation.tpr -mean Simulation.xpm -no Simulation.xvg

This analysis is typically used for all-against-all residue contact distances in a protein structure.

**Code Execution**

Import the distance matrix analysis module:

.. code:: python

    from dynamispectra.DistanceMatrix import distance_matrix_analysis

Example for one `.xpm` file corresponding to a single simulation or replicate:

.. code:: python

    xpm_file_path = r'C:\Users\Conrado\Documents\Test\mdmat.xpm'

    output_path = r'C:\Users\Conrado\Documents\Test\distance_matrix'

    config = {
        # Label for the X-axis
        'xlabel': 'Residues',
        # Label for the Y-axis                    
        'ylabel': 'Residues',
        # Font size for axis labels                    
        'label_fontsize': 12,
        # Title of the matrix plot                    
        'title': 'Distance Matrix - Replica 1',
        # Font size for the plot title  
        'title_fontsize': 12,
        # Label for the color scale                    
        'colorbar_label': 'Distance (nm)',
        # Maximum distance value (cmap upper limit)       
        'max_distance': 2.0,
        # Colormap (e.g., 'jet', 'viridis', 'plasma')                     
        'cmap': 'jet'                            
    }

    distance_matrix_analysis(
        xpm_file_path,
        output_path,
        plot=True,
        config=config
    )

The resulting plot will be saved as `.png` and `.tiff` using the specified `output_path` as prefix. The matrix is rendered as a color-coded heatmap where the color intensity reflects inter-residue distances.

To use default plotting parameters, omit the `config` argument:

.. code:: python

    distance_matrix_analysis(xpm_file_path, output_path)


Phi and Psi Angles
------------------

*DynamiSpectra* analyzes backbone dihedral angles φ (phi) and ψ (psi) from .xvg files generated by GROMACS. These files contain Ramachandran angle distributions used to assess protein conformational states over time. The analysis produces individual plots for each simulation replica as well as a combined plot representing the circular average of all replicas.

The `.xvg` files can be generated with the following GROMACS command:

.. code:: bash

    gmx rama -s Simulation.tpr -f Simulation.xtc -o rama.xvg

This analysis creates kernel density estimation (KDE) heatmaps of φ-ψ angle distributions, helping identify favored secondary structure conformations.

**Code Execution**

Import the phi-psi analysis module:

.. code:: python

    from dynamispectra.PhiPsi import phipsi_analysis

Example input files:

.. code:: python

    simulation1_files = [
        r'E:\Conrado\PNU\Dynamics\rama_rep1.xvg',
        r'E:\Conrado\PNU\Dynamics\rama_rep2.xvg',
        r'E:\Conrado\PNU\Dynamics\rama_rep3.xvg'
    ]

    output_folder = r'C:\Users\Conrado\Documents\Test'

    phipsi_config = {
        # Colormap for KDE heatmaps
        'cmap': 'jet',
        # KDE grid resolution                    
        'grid_size': 100,
        # Heatmap opacity                 
        'alpha': 1, 
        # Size of each subplot (width, height)                      
        'figsize_subplot': (6, 5),
        # Overall figure size (currently unused)        
        'figsize_overall': (6, 6),
        # Font size for axis labels and colorbar       
        'label_fontsize': 12,
        # Custom names for each simulation group             
        'group_names': ['Control Group']
    }

    phipsi_analysis(
        output_folder,
        simulation1_files,
        phipsi_config=phipsi_config,
        residue_name="ALA-30"
    )

The resulting KDE plots display favored φ and ψ angle regions per group, facilitating comparison of backbone conformational sampling.

To analyze all residues without filtering, omit the `residue_name` parameter or set it to `None`:

.. code:: python

    phipsi_analysis(
        output_folder,
        simulation1_files,
        phipsi_config=phipsi_config
    )


Rotamers (Dihedral χ1 and χ2 Angles)
------------------------------------

*DynamiSpectra* supports detailed analysis of side-chain rotamer states through the dihedral angles χ1 and χ2 extracted from .xvg files generated by GROMACS. This analysis helps characterize conformational changes and rotamer preferences during molecular dynamics simulations. Circular mean statistics are used to average χ1 and χ2 angles across replicates, properly accounting for their periodic nature. This module generates three types of plots to visualize rotamer distributions.

- **KDE**: Kernel Density Estimation (2D KDE heatmap) showing the probability density of χ1 and χ2 angles combined.  
- **Dotplot**: Scatter plot filtered by the selected time window.  
- **Histogram (Hist)**: Distribution plots of χ1 and χ2 angles separately, showing frequency density.

You can extract χ1 and χ2 dihedral angles with GROMACS using commands like:

.. code:: bash

    gmx chi -s Simulation.tpr -f Simulation.xtc -n index.ndx -o chi1.xvg -type dihedral
    gmx chi -s Simulation.tpr -f Simulation.xtc -n index.ndx -o chi2.xvg -type dihedral

These visualizations provide a comprehensive view of side-chain conformations during the simulation.

**Note:** The atom groups defining the χ1 and χ2 dihedral angles must be correctly specified in the GROMACS index file (`.ndx`) prior to angle calculation.

**Code Execution**

Import the rotamer analysis function from *DynamiSpectra*:

.. code:: python

    from dynamispectra.Rotamers import dihedral_kde_and_dotplot

Example input files for χ1 and χ2 angles:

.. code:: python

    chi1_files = [
        r'E:\Conrado\PNU\Dynamics\rotamers_chi1_chi2\chi1_time_Rep1.xvg',
        r'E:\Conrado\PNU\Dynamics\rotamers_chi1_chi2\chi1_time_Rep2.xvg',
        r'E:\Conrado\PNU\Dynamics\rotamers_chi1_chi2\chi1_time_Rep3.xvg'
    ]

    chi2_files = [
        r'E:\Conrado\PNU\Dynamics\rotamers_chi1_chi2\chi2_time_Rep1.xvg',
        r'E:\Conrado\PNU\Dynamics\rotamers_chi1_chi2\chi2_time_Rep2.xvg',
        r'E:\Conrado\PNU\Dynamics\rotamers_chi1_chi2\chi2_time_Rep3.xvg'
    ]

    output_folder = r'C:\Users\Conrado\Documents\Test'

Specify the time window (in picoseconds) to filter the angle data analyzed:

.. code:: python

    time_window = (35000, 40000)  # Analyze frames between a time chosen

Run the analysis and generate KDE maps, dotplots, and histograms with customized titles, labels, colors, and output filename:

.. code:: python

    dihedral_kde_and_dotplot(
        output_folder,
        chi1_files,
        chi2_files,
        config={
            'kde_title': 'Rotamers of Leu34 at 35–40 ns',
            'dot_title': 'Rotamers of Leu34 at 35–40 ns',
            'hist_title': 'Rotamer Distributions of Leu34 at 35–40 ns',
            # X-axis label for histograms
            'hist_xlabel': 'Angles (°)',
            # Y-axis label for histograms                        
            'hist_ylabel': 'Density',   
            # Histogram legend labels                        
            'hist_legend_labels': [r'$\mathit{\chi_1}$', r'$\mathit{\chi_2}$'], 
            # Output filename
            'save_name': 'rotamers_plot.png',
            # Colormap for KDE heatmaps                   
            'cmap': 'Oranges', 
            # Dot color in dotplot                                 
            'dot_color': 'brown', 
            # Label for KDE colorbar                              
            'colorbar_label': 'Estimated Density',
            # Histogram color for χ1              
            'chi1_color': 'brown',
            # Histogram color for χ2                              
            'chi2_color': 'orange'                              
        },
        time_window=time_window
    )

The output will include combined KDE, dotplot, and histogram figures illustrating the rotamer distributions for the selected residue and time window.

To change the analyzed residue or time window, modify the input files and `time_window` parameter accordingly.


Ligand Density
--------------

*DynamiSpectra* enables visualization of ligand density maps using `.xpm` files generated by GROMACS. These maps represent the spatial occupancy of ligand atoms around the target molecule during the simulation, helping identify preferred binding regions or solvent-exposed areas.

The `.xpm` file can be generated with a GROMACS command such as:

.. code:: bash

    gmx densmap -f Simulation.xtc -s Simulation.tpr -n index.ndx -o ligand_density.xpm

This analysis provides a 2D heatmap of ligand occupancy, with colors representing the frequency of ligand presence in specific spatial bins.

**Code Execution**

Import the ligand density analysis module:

.. code:: python

    from dynamispectra.ligand_density import ligand_density_analysis

Example usage for one `.xpm` file and specifying output plot parameters:

.. code:: python

    xpm_file_path = r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\Ligand_Density\ligand_density.xpm'

    output_path = r'C:\Users\Conrado\Documents\Test'

    ligand_density_analysis(
        # Input .xpm file path
        xpm_file_path,
        # Output path prefix (no extension added)             
        output_path=output_path,
        # Show plot interactively   
        plot=True,
        # Colormap for heatmap visualization                 
        cmap='inferno',   
        # X-axis label         
        xlabel='Z-axis (nm)', 
        # Y-axis label     
        ylabel='X-axis (nm)', 
        # Plot title     
        title='Ligand Density around Target',
        # Colorbar label  
        colorbar_label='Occupancy',
         # Figure size in inches (width, height)            
        figsize=(7, 6),  
        # Font size for axis labels and colorbar          
        label_fontsize=12          
    )

The resulting plots are saved in `.png` and `.tiff` formats at the specified output location.

To use default plotting parameters, call the function with just the `.xpm` file and output path:

.. code:: python

    ligand_density_analysis(xpm_file_path, output_path)


Ligand Dihedral Angle Analysis
------------------------------

*DynamiSpectra* provides analysis and visualization of ligand dihedral angles over time, allowing insight into conformational changes and flexibility of ligand torsions during molecular dynamics simulations.

Input data consist of `.xvg` files containing dihedral angle values measured at each simulation frame for multiple replicas across different simulation groups.

.. code:: bash

    gmx gangle -f Simulation.xtc -n Simulation.ndx -g1 dihedral -group1 diedro_1 -oall diedro_ligand.xvg

**Note:** To extract ligand dihedral angles using GROMACS, the specific atoms defining each dihedral must be pre-defined in the index (`.ndx`) file.

**Code Execution**

Import the ligand angle analysis function:

.. code:: python

    from dynamispectra.LigandAngle import angle_ligand_analysis

Example with three simulation groups, each containing three replicate `.xvg` files:

.. code:: python

    simulation1_files = [
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep1_angle1.xvg',
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep2_angle1.xvg',
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep3_angle1.xvg',
    ]

    simulation2_files = [
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep1_angle1.xvg',
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep2_angle1.xvg',
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep3_angle1.xvg',
    ]

    simulation3_files = [
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep1_angle1.xvg',
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep2_angle1.xvg',
        r'E:\Project\MD\LigandDihedral\ligand_dihedral_Rep3_angle1.xvg',
    ]


    output_folder = r'C:\Users\Bioinformatics\Documents\LigandAngleResults'

    time_config = {
    # Legend labels
    'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'], 
    # Line colors   
    'colors': ['#333333', '#6A9EDA', '#49C547'],
    # Shaded area transparency (±SD)                    
    'alpha': 0.2,  
    # Figure size (width, height)                                                 
    'figsize': (9, 6),   
    # X-axis label                                           
    'xlabel': 'Time (ns)', 
    # Y-axis label                                         
    'ylabel': 'Dihedral angle (°)',  
    # Font size for axis labels                               
    'label_fontsize': 12,   
    # Smoothing window (optional)                                        
    'smooth_window': 20,
    # Y-axis range                                            
    'ylim': (110, 127)                                              
    }

    density_config = {
    # Legend labels
    'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
    # Fill colors    
    'colors': ['#333333', '#6A9EDA', '#49C547'],
    # Transparency for KDE                    
    'alpha': 0.6,    
    # Figure size                                               
    'figsize': (6, 6),
    # X-axis label                                              
    'xlabel': 'Dihedral angle (°)', 
    # Y-axis label                                
    'ylabel': 'Density',  
    # Font size for axis labels                                          
    'label_fontsize': 12                                            
    }

    kde2d_config = {
    # Legend labels
    'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
    # Marker/line colors    
    'colors': ['#333333', '#6A9EDA', '#49C547'],  
    # Figure size                  
    'figsize': (8, 6),
    # X-axis label                                             
    'xlabel': 'Time (ns)', 
    # Y-axis label                                         
    'ylabel': 'Dihedral angle (°)',
    # Font size for axis labels                                 
    'label_fontsize': 12, 
    # Colormap for 2D KDE heatmap                                          
    'cmap': 'Oranges'                                               
    }


    angle_ligand_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        time_config=time_config,
        density_config=density_config,
        kde2d_config=kde2d_config
    )

This will produce plots of dihedral angles over time with mean ± standard deviation shading, KDE density distributions, and 2D KDE heatmaps showing angle vs. simulation time, all saved to the specified output folder.

To run the analysis with a single group or a single file, just provide one list:

.. code:: python

    angle_ligand_analysis(output_folder, simulation1_files)

If no configuration dictionaries are provided, default plot settings will be applied. You can tailor the plot appearance for presentations or publications by adjusting the dictionary values.


Principal Component Analysis (PCA)
----------------------------------

*DynamiSpectra* provides tools to visualize and interpret the results of principal component analysis (PCA) applied to molecular dynamics trajectories. This analysis allows the identification of dominant motions and conformational changes by projecting atomic displacements onto principal components.

The input files consist of:

- A `.xvg` file containing the projection of atomic displacements onto PC1 and PC2 (typically generated using `gmx covar` and `gmx anaeig`)
- A `.xvg` file containing the eigenvalues for each principal component (typically `eigenval.xvg` from `gmx anaeig`)

**Code Execution**

Import the PCA analysis function:

.. code:: python

    from dynamispectra.PCA import pca_analysis

Define input files, output folder and run the analysis:

.. code:: python

    pca_file_path = r'C:\Users\Conrado\Desktop\DynamiSpectra\data\PCA\pca_projection.xvg'
    eigenval_path = r'C:\Users\Conrado\Desktop\DynamiSpectra\data\PCA\eigenval.xvg'
    output_folder = r'C:\Users\Conrado\Documents\Test'

    pca_analysis(
    # Path to PCA projection file
    pca_file_path,
    # Path to eigenvalue file       
    eigenval_path,
    # Output folder to save the plot       
    output_folder,
    # Title of the plot       
    title='', 
    # Size of the figure (width, height) 
    figsize=(8, 7), 
    # Colormap used for time coloring     
    cmap='inferno',
    # Size of the scatter points      
    point_size=50,  
    # Font size for X and Y axis labels     
    axis_label_fontsize=15,
    # Font size for the title            
    title_fontsize=16,    
    # Font size for the colorbar label             
    colorbar_label_fontsize=13,  
    # Font size for the colorbar ticks      
    colorbar_tick_fontsize=10          
    )

This will generate a PCA scatter plot where each point represents a frame projected in the PC1–PC2 space, colored according to simulation time. The fraction of variance explained by PC1 and PC2 is automatically extracted from the eigenvalue file and included in the axis labels. You can modify the colormap, point size, and transparency as needed for presentation or publication purposes.

To use default settings, omit the optional keyword arguments.


Secondary Structure Probability
-------------------------------

*DynamiSpectra* provides tools for the analysis and comparison of secondary structure content across different simulation groups. The analysis is based on `.dat` files containing the fraction of time each residue spent in different secondary structure elements (e.g., helix, sheet, coil) throughout the trajectory.

These `.dat` files are typically generated by external tools such as **dssp** in GROMACS or `gmx dssp`, followed by post-processing to calculate structure probabilities per residue.

**Code Execution**

Import the secondary structure analysis function:

.. code:: python

    from dynamispectra.SecondaryStructure import ss_analysis

Define input files for each simulation group (each group consists of replicate `.dat` files), and run the analysis:

.. code:: python

    simulation1_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation1_rep1.dat',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation1_rep2.dat',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation1_rep3.dat'
    ]

    simulation2_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation2_rep1.dat',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation2_rep2.dat',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation2_rep3.dat'
    ]

    simulation3_files = [
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation3_rep1.dat',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation3_rep2.dat',
        r'C:\Users\Conrado\Desktop\DynamiSpectra\simulation3_rep3.dat'
    ]

    output_folder = r'C:\Users\Conrado\Documents\Test'

    plot_config = {
        # Names of the groups
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Colors for each group
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Transparency of the lines or shaded area
        'alpha': 0.6,
        # Font size for axis labels
        'axis_label_size': 12,
        # Label for the Y-axis
        'y_axis_label': 'Secondary Structure Probability (%)',
        # Figure size (width, height)
        'figsize': (9, 7)
    }

    ss_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        plot_config=plot_config
    )

This will produce a plot showing the average secondary structure probability across residues, with shaded regions representing the standard deviation among replicates for each simulation group. If no plot configuration is provided, default styles will be applied.


Secondary Structure Fractions
-----------------------------

*DynamiSpectra* allows visualization of the time evolution of global secondary structure content during molecular dynamics simulations. This analysis provides insights into the overall structural dynamics by quantifying the fraction of residues adopting each secondary structure type (helix, sheet, coil) per frame.

The input `.dat` file must contain secondary structure assignments per frame, usually obtained using `gmx dssp` followed by conversion to per-frame structural fractions.

**Code Execution**

Import the analysis function:

.. code:: python

    from dynamispectra.FractionSS import fractions_ss_analysis

Specify the input file, output folder and optional plot configuration:

.. code:: python

    file_path = r'C:\Users\Conrado\Desktop\DynamiSpectra\datas\SecondaryStructure\simulation1.dat'
    output_folder = r'C:\Users\Conrado\Documents\Test'

    plot_config = {
        # Plot title
        'title': 'Secondary Structure Fractions Over Time',
        # Label for x-axis     
        'xlabel': 'Simulation Frames',
        # Label for y-axis                          
        'ylabel': 'Residue Fraction',
        # Size of the figure                           
        'figsize': (9, 6),
        # Font size for labels                                      
        'fontsize': 12,  
        # X-axis range (optional)                                       
        'xlim': (0, 10000),
        # Y-axis range (optional)                                    
        'ylim': (0, 0.85)                                      
    }

Run the analysis and export the plot and Excel summary:

.. code:: python

    fractions_ss_analysis(file_path, output_folder, plot_config=plot_config)

This function will produce:

- A time series plot showing the evolution of helix, sheet, and coil content over time.
- An Excel file (`SecondaryStructure_Fractions.xlsx`) containing both raw and average values of each structure type.

If no configuration is provided, the plot will be generated using default settings.


Pressure Analysis
-----------------

*DynamiSpectra* enables visualization of system pressure throughout molecular dynamics simulations. Pressure analysis helps assess system equilibration, barostat performance, and simulation stability over time. This module accepts `.xvg` output files generated by GROMACS using the built-in pressure calculation options during simulation.

To generate the required `.xvg` file for temperature using GROMACS, run:

.. code:: bash

    gmx energy -f Simulation.edr -o pressure.xvg

Input data consists of `.xvg` files output by GROMACS temperature calculations.

**Code Execution**

Import the pressure analysis function:

.. code:: python

    from dynamispectra.Pressure import pressure_analysis

Define the input files for each simulation group:

.. code:: python

    simulation1_files = [
        r'E:\Conrado\PNU\Dynamics\pressure_sim1_rep1.xvg',
        r'E:\Conrado\PNU\Dynamics\pressure_sim1_rep2.xvg',
        r'E:\Conrado\PNU\Dynamics\pressure_sim1_rep3.xvg',
    ]

    simulation2_files = [
        r'E:\Conrado\PNU\Dynamics\pressure_sim2_rep1.xvg',
        r'E:\Conrado\PNU\Dynamics\pressure_sim2_rep2.xvg',
        r'E:\Conrado\PNU\Dynamics\pressure_sim2_rep3.xvg',
    ]

    simulation3_files = [
        r'E:\Conrado\PNU\Dynamics\pressure_sim3_rep1.xvg',
        r'E:\Conrado\PNU\Dynamics\pressure_sim3_rep2.xvg',
        r'E:\Conrado\PNU\Dynamics\pressure_sim3_rep3.xvg',
    ]

Specify the output folder and run the analysis:

.. code:: python

    output_folder = r'C:\Users\Conrado\Documents\Test'

    pressure_config = {
        # Legend labels
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Line colors for each group  
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        # Figure size (width, height)                 
        'figsize': (10, 6),  
        # Std deviation fill transparency                                        
        'alpha': 0.3,   
        # X-axis label                                             
        'xlabel': 'Time (ns)',   
        # Y-axis label                                   
        'ylabel': 'Pressure (bar)',
        # Font size for axis and legend                                  
        'label_fontsize': 14,                                       
        # Y-axis range
        'ylim': (-900, 900)                                          
    }

    density_config = {
        # Legend labels
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Fill colors for KDE plots  
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Figure size (width, height)                
        'figsize': (6, 6),       
        # Fill transparency                                   
        'alpha': 0.5,     
        # X-axis label                                           
        'xlabel': 'Pressure (bar)', 
        # Y-axis label                                 
        'ylabel': 'Density', 
        # Font size for labels                                       
        'label_fontsize': 14,  
        # Minimum x-value for KDE plot                                      
        'x_min': -900,
        # Maximum x-value for KDE plot                                               
        'x_max': 900                                                 
    }

    pressure_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        pressure_config=pressure_config,
        density_config=density_config
    )

This will generate a time series plot showing the pressure profile with mean ± standard deviation for each group, and a KDE plot of pressure distributions.


Temperature Analysis
--------------------

*DynamiSpectra* allows analysis and visualization of system temperature during molecular dynamics simulations. Temperature profiles help monitor system equilibration and thermal stability.

To generate the required `.xvg` file for temperature using GROMACS, run:

.. code:: bash

    gmx energy -f Simulation.edr -o temperature.xvg

Input data consists of `.xvg` files output by GROMACS temperature calculations.

**Code Execution**

Import the temperature analysis function:

.. code:: python

    from dynamispectra.Temperature import temperature_analysis

Define the input `.xvg` files for each simulation group (each group with multiple replicates):

.. code:: python

    simulation1_files = [
        r'E:\Conrado\PNU\Dinamica\temperature_rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\temperature_rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\temperature_rep3.xvg'
    ]

    simulation2_files = [
        r'E:\Conrado\PNU\Dinamica\temperature_rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\temperature_rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\temperature_rep3.xvg'
    ]

    simulation3_files = [
        r'E:\Conrado\PNU\Dinamica\temperature_rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\temperature_rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\temperature_rep3.xvg'
    ]

Specify the output folder to save the plots and run the analysis:

.. code:: python

    output_folder = r'C:\Users\Conrado\Documents\Test'

    temp_config = {
        # Legend labels
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Line colors for each group 
        'colors': ['#6A9EDA', '#e04f4f', "#bca140"],
        # Transparency for std deviation shading                
        'alpha': 0.3,          
        # Figure size (width, height)                                     
        'figsize': (9, 6),                                          
        # X-axis label
        'xlabel': 'Time (ns)',                                      
        # Y-axis label
        'ylabel': 'Temperature (K)',                                
        # Font size for axis labels
        'label_fontsize': 12                                        
    }

    density_config = {
        # Legend labels
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'], 
        # Fill colors for KDE plots
        'colors': ['#6A9EDA', '#e04f4f', '#bca140'],    
        # Transparency for KDE fill            
        'alpha': 0.6,        
        # Figure size (width, height)                                       
        'figsize': (6, 6),     
        # X-axis label                                     
        'xlabel': 'Temperature (K)',  
        # Y-axis label                              
        'ylabel': 'Density',       
        # Font size for axis labels                                 
        'label_fontsize': 12                                       
    }

    temperature_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        temp_config=temp_config,
        density_config=density_config
    )

This will generate time series plots showing temperature fluctuations with mean ± standard deviation and KDE plots representing the temperature distribution for each simulation group.

To analyze a single simulation group, provide a single list of files. If the configuration dictionaries are omitted, default plotting parameters will be applied.


Density Analysis
----------------

*DynamiSpectra* allows analysis and visualization of system density throughout molecular dynamics simulations. This provides insight into system stability, phase transitions, and equilibration.

This module processes `.xvg` files typically generated by GROMACS during simulation or via energy analysis tools.

To obtain density data from GROMACS, you can use the following command after your simulation:

.. code:: bash

    gmx energy -f Simulation.edr -o density.xvg

Select the density property when prompted.

**Code Execution**

Import the density analysis function:

.. code:: python

    from dynamispectra.Density import density_analysis

Define the input files for each simulation group:

.. code:: python

    simulation1_files = [
        r'E:\Conrado\PNU\Dinamica\simulation1\density_rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\simulation1\density_rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\simulation1\density_rep3.xvg',
    ]

    simulation2_files = [
        r'E:\Conrado\PNU\Dinamica\simulation2\density_rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\simulation2\density_rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\simulation2\density_rep3.xvg',
    ]

    simulation3_files = [
        r'E:\Conrado\PNU\Dinamica\simulation3\density_rep1.xvg',
        r'E:\Conrado\PNU\Dinamica\simulation3\density_rep2.xvg',
        r'E:\Conrado\PNU\Dinamica\simulation3\density_rep3.xvg',
    ]

Specify the output folder and run the analysis:

.. code:: python

    output_folder = r'C:\Users\Conrado\Documents\Test'

    density_config = {
        # Legend labels for each simulation group
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'], 
        # Colors for each line and shaded area
        'colors': ['#333333', '#6A9EDA', '#49C547'],                
        # Figure size (width, height)
        'figsize': (10, 6),                                         
        # Transparency of shaded std deviation area
        'alpha': 0.3,                                               
        # X-axis label
        'xlabel': 'Time (ns)',                                      
        # Y-axis label
        'ylabel': 'Density (kg/m³)',                                
        # Font size for axis labels
        'label_fontsize': 14,                                       
        # Y-axis limits for better visualization
        'ylim': (950, 1010)                                         
    }

    distribution_config = {
        # Legend labels for KDE plots
        'labels': ['Simulation 1', 'Simulation 2', 'Simulation 3'],
        # Colors for KDE fills 
        'colors': ['#333333', '#6A9EDA', '#49C547'], 
        # Figure size               
        'figsize': (6, 6),   
        # Transparency for KDE fills                                       
        'alpha': 0.5,           
        # X-axis label                                   
        'xlabel': 'Density (kg/m³)',   
        # Y-axis label                             
        'ylabel': 'Density',    
        # Font size for axis labels                                    
        'label_fontsize': 14,    
        # Minimum x value for KDE plot range                                   
        'x_min': 950,                  
        # Maximum x value for KDE plot range                            
        'x_max': 1010                                               
    }

    density_analysis(
        output_folder,
        simulation1_files,
        simulation2_files,
        simulation3_files,
        density_config=density_config,
        distribution_config=distribution_config
    )

This will generate plots of density over time with mean ± standard deviation shading, plus KDE density distribution plots, all saved to the specified output folder.
