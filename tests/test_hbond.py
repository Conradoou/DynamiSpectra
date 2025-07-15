import os
from glob import glob
from dynamispectra.Hbond import hbond_analysis

def test_hbond_analysis_runs(tmp_path):
    # Path to the test data directories
    base_path = os.path.join(os.path.dirname(__file__), "data", "Hbond")

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

    # Output directory
    output_dir = tmp_path / "hbond_output"

    # Plot config for time-resolved hydrogen bond graph
    hbond_config = {
        'labels': [f'Simulation {i+1}' for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Number of H-bonds',
        'label_fontsize': 12,
        'figsize': (9, 6)
    }

    # Plot config for density plot
    density_config = {
        'labels': [f'Simulation {i+1}' for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.6,
        'xlabel': 'Number of H-bonds',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    # Run analysis
    hbond_analysis(
        str(output_dir),
        *simulation_file_groups,
        hbond_config=hbond_config,
        density_config=density_config
    )

    # Assert that the output files were created
    assert (output_dir / "hbond_plot.png").exists(), "Hbond time series plot was not generated"
    assert (output_dir / "hbond_density.png").exists(), "Hbond density plot was not generated"
