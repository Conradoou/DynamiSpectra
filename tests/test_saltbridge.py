import os
from glob import glob
from dynamispectra.saltbridge import saltbridge_analysis

def test_saltbridge_analysis_runs(tmp_path):
    # Path to the directories with test data
    base_path = os.path.join(os.path.dirname(__file__), "data", "saltbridge")
    
    # List all subdirectories representing each simulation group
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ])

    # For each simulation group, collect all .xvg files
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    # Temporary folder to save generated plots
    output_dir = tmp_path / "saltbridge_output"

    # Configuration for the line plot
    saltbridge_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Salt-Bridge Distance (nm)',
        'label_fontsize': 12,
        'figsize': (8, 6)
    }

    # Configuration for the density plot
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.4,
        'xlabel': 'Salt-Bridge Distance (nm)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 5)
    }

    # Run the saltbridge analysis function
    saltbridge_analysis(
        str(output_dir),  # output_folder as positional argument
        *simulation_file_groups,
        saltbridge_config=saltbridge_config,
        density_config=density_config
    )

    # Verify that the plots were generated
    assert (output_dir / "saltbridge_plot.png").exists(), "Saltbridge plot was not generated"
    assert (output_dir / "saltbridge_density.png").exists(), "Density plot was not generated"
