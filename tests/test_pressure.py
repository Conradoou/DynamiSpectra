import os
from glob import glob
from dynamispectra.Pressure import pressure_analysis

def test_pressure_analysis_runs(tmp_path):
    # Path to the Simulation1 folder inside Pressure
    base_path = os.path.join(os.path.dirname(__file__), "data", "Pressure", "Simulation 1")

    # Collect all .xvg files from this folder
    simulation_files = sorted(glob(os.path.join(base_path, "*.xvg")))

    if not simulation_files:
        print("No simulation data found for pressure analysis. Test skipped.")
        return

    output_dir = tmp_path / "pressure_output"

    # Configuration for pressure time series plot
    pressure_config = {
        'labels': ['Simulation 1'],
        'colors': ['#333333'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Pressure (bar)',
        'label_fontsize': 12,
        'figsize': (9, 6),
        'ylim': [800, -800]
    }

    # Configuration for pressure density KDE plot
    density_config = {
        'labels': ['Simulation 1'],
        'colors': ['#333333'],
        'alpha': 0.4,
        'xlabel': 'Pressure (bar)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    # Run the pressure analysis with the single group of 3 replicas
    pressure_analysis(
        str(output_dir),
        *[simulation_files],  # Unpack as a single simulation group
        pressure_config=pressure_config,
        density_config=density_config
    )

    # Check if the output files were generated
    assert (output_dir / "pressure_plot.png").exists(), "Pressure time series plot was not generated"
    assert (output_dir / "pressure_plot.tiff").exists(), "Pressure time series TIFF plot was not generated"
    assert (output_dir / "pressure_density.png").exists(), "Pressure density plot was not generated"
    assert (output_dir / "pressure_density.tiff").exists(), "Pressure density TIFF plot was not generated"
