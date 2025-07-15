import os
from glob import glob
from dynamispectra.RMSF import rmsf_analysis  # ajuste o import conforme sua estrutura

def test_rmsf_analysis_runs(tmp_path):
    # Base directory containing RMSF simulation subfolders
    base_path = os.path.join(os.path.dirname(__file__), "data", "RMSF")

    # Find all simulation directories (simulation 1, 2, 3...)
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d)) and d.lower().startswith("simulation")
    ])

    # Collect .xvg files from each simulation directory
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    # Temporary output directory for generated plots
    output_dir = tmp_path / "rmsf_output"

    # Configuration for RMSF profile plot
    rmsf_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#54b36a'],
        'alpha': 0.3,
        'xlabel': 'Residue',
        'ylabel': 'RMSF (nm)',
        'label_fontsize': 12,
        'figsize': (8, 6),
        'xlim': (1, 42)
    }

    # Configuration for RMSF density KDE plot
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#54b36a'],
        'alpha': 0.4,
        'xlabel': 'RMSF (nm)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    # Run the RMSF analysis function
    rmsf_analysis(
        str(output_dir),  # output_folder como primeiro argumento posicional
        *simulation_file_groups,
        rmsf_config=rmsf_config,
        density_config=density_config
    )

    # Assert that the expected plots have been generated
    assert (output_dir / "rmsf_plot.png").exists(), "RMSF profile plot was not generated"
    assert (output_dir / "rmsf_plot.tiff").exists(), "RMSF profile TIFF plot was not generated"
    assert (output_dir / "density_plot.png").exists(), "RMSF density plot was not generated"
    assert (output_dir / "density_plot.tiff").exists(), "RMSF density TIFF plot was not generated"
