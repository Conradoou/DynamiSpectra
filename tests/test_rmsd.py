import os
from glob import glob
from dynamispectra.RMSD import rmsd_analysis  # ajuste o caminho conforme necessário

def test_rmsd_analysis_runs(tmp_path):
    # Base path to RMSD simulation data folders
    base_path = os.path.join(os.path.dirname(__file__), "data", "RMSD")

    # List all simulation directories (e.g., simulation 1, simulation 2, simulation 3)
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d)) and d.lower().startswith("simulation")
    ])

    # Collect all .xvg files for each simulation group
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    # Temporary directory to save generated plots
    output_dir = tmp_path / "rmsd_output"

    # Configuration for RMSD time series plot
    rmsd_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.3,
        'xlabel': 'Time (ps)',
        'ylabel': 'RMSD (nm)',
        'label_fontsize': 12,
        'figsize': (8, 6)
    }

    # Configuration for RMSD density KDE plot
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.4,
        'xlabel': 'RMSD (nm)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    # Run RMSD analysis function
    rmsd_analysis(
        str(output_dir),  # output_folder como primeiro argumento posicional
        *simulation_file_groups,
        rmsd_config=rmsd_config,
        density_config=density_config
    )

    # Verify that the plots were generated
    assert (output_dir / "rmsd_plot.png").exists(), "RMSD time series plot was not generated"
    assert (output_dir / "rmsd_plot.tiff").exists(), "RMSD time series TIFF plot was not generated"
    assert (output_dir / "density_plot.png").exists(), "RMSD density plot was not generated"
    assert (output_dir / "density_plot.tiff").exists(), "RMSD density TIFF plot was not generated"
