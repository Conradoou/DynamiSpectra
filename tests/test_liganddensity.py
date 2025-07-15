import os
from dynamispectra.ligand_density import ligand_density_analysis

def test_ligand_density_analysis_runs(tmp_path):
    # Define base path to the ligand density data folder
    base_path = os.path.join(os.path.dirname(__file__), "data", "Ligand Density")

    # Path to the test .xpm file
    xpm_file = os.path.join(base_path, "densmap.xpm")

    # Temporary output directory for plots
    output_dir = tmp_path / "ligand_density_output"
    os.makedirs(output_dir, exist_ok=True)

    # Run ligand density analysis and plot
    matrix = ligand_density_analysis(
        xpm_file_path=xpm_file,
        output_path=str(output_dir / "ligand_density_map"),
        plot=True,
        cmap='inferno',
        xlabel='X (nm)',
        ylabel='Y (nm)',
        title='Ligand Density Map',
        colorbar_label='Relative Density',
        figsize=(6, 5),
        label_fontsize=12
    )

    # Check if output files were created successfully
    assert (output_dir / "ligand_density_map.png").exists(), "Ligand density PNG plot was not created"
    assert (output_dir / "ligand_density_map.tiff").exists(), "Ligand density TIFF plot was not created"

    # Check if the returned matrix is a numpy array
    import numpy as np
    assert isinstance(matrix, np.ndarray), "Returned density matrix is not a numpy array"
