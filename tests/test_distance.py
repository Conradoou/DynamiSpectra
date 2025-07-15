import os
from glob import glob
from dynamispectra.Distance import distance_analysis

def test_distance_analysis_runs(tmp_path):
    # Path to the test data directories
    base_path = os.path.join(os.path.dirname(__file__), "data", "Distance")
    
    # List all subdirectories corresponding to each simulation group
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ])

    # Collect .xvg files for each simulation group
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    # Temporary output directory for generated plots
    output_dir = tmp_path / "distance_output"

    # Configuration for the time-resolved distance plot
    distance_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Minimum Distance (nm)',
        'label_fontsize': 12,
        'figsize': (8, 6)
    }

    # Configuration for the KDE distribution plot
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.4,
        'xlabel': 'Minimum Distance (nm)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 5)
    }

    # Run the distance analysis
    distance_analysis(
        str(output_dir),  # output_folder (positional argument)
        *simulation_file_groups,  # unpack list into positional arguments
        distance_config=distance_config,
        density_config=density_config
    )

    # Assert that the expected output plots were generated
    assert (output_dir / "distance_plot.png").exists(), "Distance time series plot was not generated"
    assert (output_dir / "distance_density.png").exists(), "Distance KDE distribution plot was not generated"
