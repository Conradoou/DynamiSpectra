import os
from glob import glob
from dynamispectra.Hydrophobic_contacts import hydrophobic_analysis

def test_hydrophobic_analysis_runs(tmp_path):
    # Path to the test data directory
    base_path = os.path.join(os.path.dirname(__file__), "data", "Hydrophobic contacts")

    # List all subdirectories representing simulation groups (Simulation 1, 2, 3...)
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
    output_dir = tmp_path / "hydrophobic_output"

    # Configuration for the contact time series plot
    contact_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Hydrophobic Contacts',
        'label_fontsize': 12,
        'figsize': (8, 6)
    }

    # Configuration for the KDE density plot
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.5,
        'xlabel': 'Number of Contacts',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    # Run the hydrophobic contacts analysis
    hydrophobic_analysis(
        str(output_dir),
        *simulation_file_groups,
        contact_config=contact_config,
        density_config=density_config
    )

    # Check if output plots were generated successfully
    assert (output_dir / "hydrophobic_contacts_plot.png").exists(), "Hydrophobic contacts line plot was not generated"
    assert (output_dir / "hydrophobic_contacts_density.png").exists(), "Hydrophobic contacts density plot was not generated"
