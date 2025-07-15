import os
import matplotlib.pyplot as plt
from glob import glob
from dynamispectra.LigandAngle import angle_ligand_analysis

def test_ligand_angle_analysis_runs(tmp_path):
    # Define base path for the ligand angle test data
    base_path = os.path.join(os.path.dirname(__file__), "data", "Ligand angle")

    # List all simulation group subdirectories
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ])

    # Collect all .xvg files from each simulation group folder (replicates)
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    # Define temporary output directory for plots
    output_dir = tmp_path / "ligand_angle_output"
    os.makedirs(output_dir, exist_ok=True)

    # Configurations for plots
    time_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.2,
        'xlabel': 'Time (ns)',
        'ylabel': 'Dihedral angle (°)',
        'label_fontsize': 12,
        'figsize': (8, 5),
        'smooth_window': 20,
    }

    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.4,
        'xlabel': 'Dihedral angle (°)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 5),
    }

    kde2d_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'cmap': 'jet',
        'xlabel': 'Time (ns)',
        'ylabel': 'Dihedral angle (°)',
        'label_fontsize': 12,
        'figsize': (8, 6),
    }

    # Run the ligand dihedral angle analysis
    angle_ligand_analysis(
        str(output_dir),
        *simulation_file_groups,
        time_config=time_config,
        density_config=density_config,
        kde2d_config=kde2d_config
    )

    # Assert output files were created
    assert (output_dir / "angle_over_time.png").exists(), "Angle over time PNG plot was not created"
    assert (output_dir / "angle_over_time.tiff").exists(), "Angle over time TIFF plot was not created"
    assert (output_dir / "angle_density.png").exists(), "Angle density PNG plot was not created"
    assert (output_dir / "angle_density.tiff").exists(), "Angle density TIFF plot was not created"
    
    # Check if all 2D KDE files were created for each simulation group
    for label in kde2d_config['labels']:
        filename = f"{label.replace(' ', '_').lower()}_kde_2d.png"
        assert (output_dir / filename).exists(), f"2D KDE plot {filename} was not created"
