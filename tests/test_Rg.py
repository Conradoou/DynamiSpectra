import os
from glob import glob
from dynamispectra.Rg import rg_analysis

def test_rg_analysis_runs(tmp_path):
    base_path = os.path.join(os.path.dirname(__file__), "data", "Rg")

    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d)) and d.lower().startswith("simulation")
    ])

    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    output_dir = tmp_path / "rg_output"

    rg_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Radius of Gyration (nm)',
        'label_fontsize': 12,
        'figsize': (7, 6)
    }

    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#333333', '#6A9EDA', '#49C547'],
        'alpha': 0.4,
        'xlabel': 'Radius of Gyration (nm)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    rg_analysis(
        str(output_dir),
        *simulation_file_groups,
        rg_config=rg_config,
        density_config=density_config
    )

    assert (output_dir / "rg_plot.png").exists(), "Rg time series plot was not generated"
    assert (output_dir / "rg_plot.tiff").exists(), "Rg time series TIFF plot was not generated"
    assert (output_dir / "rg_density.png").exists(), "Rg density plot was not generated"
    assert (output_dir / "rg_density.tiff").exists(), "Rg density TIFF plot was not generated"
