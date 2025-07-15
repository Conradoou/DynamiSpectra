import os
from glob import glob
from dynamispectra.Density import density_analysis

def test_density_analysis_runs(tmp_path):
    # Path to the test data directories
    base_path = os.path.join(os.path.dirname(__file__), "data", "Density")
    
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
    output_dir = tmp_path / "density_output"

    # Configuration for the time-resolved density plot
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Density (kg/m³)',
        'label_fontsize': 12,
        'figsize': (8, 6)
    }

    # Configuration for the density KDE distribution plot
    distribution_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.4,
        'xlabel': 'Density (kg/m³)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 5)
    }

    # Run the analysis, passando os arquivos como argumentos posicionais
    density_analysis(
        str(output_dir),
        *simulation_file_groups,
        density_config=density_config,
        distribution_config=distribution_config
    )

    # Assert that the expected output plots were generated
    assert (output_dir / "density_plot.png").exists(), "Density time series plot was not generated"
    assert (output_dir / "density_distribution.png").exists(), "Density KDE distribution plot was not generated"
