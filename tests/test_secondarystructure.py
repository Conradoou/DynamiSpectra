import os
from glob import glob
from dynamispectra.SecondaryStructure import ss_analysis

def test_ss_analysis_runs(tmp_path):
    # Path to the directories with test data
    base_path = os.path.join(os.path.dirname(__file__), "data", "Secondary Structure Probability")

    # List all subdirectories representing each simulation group
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ])

    # For each simulation group, collect all .dat files
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        dat_files = sorted(glob(os.path.join(sim_dir, "*.dat")))
        if dat_files:
            simulation_file_groups.append(dat_files)

    # Temporary folder to save generated plots
    output_dir = tmp_path / "secondary_structure_output"

    # Configuration for plotting
    plot_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.7,
        'axis_label_size': 12,
        'y_axis_label': 'Probability (%)',
        'figsize': (8, 6)
    }

    # Run the secondary structure analysis function (corrigido)
    ss_analysis(
        str(output_dir),
        *simulation_file_groups,
        plot_config=plot_config
    )

    # Verify that the boxplot was generated
    assert (output_dir / "secondary_structure_boxplot.png").exists(), "Secondary structure boxplot was not generated"
    assert (output_dir / "secondary_structure_boxplot.tiff").exists(), "Secondary structure boxplot TIFF was not generated"
