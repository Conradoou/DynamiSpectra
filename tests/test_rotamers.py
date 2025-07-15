import os
from glob import glob
from dynamispectra.Rotamers import dihedral_kde_and_dotplot

def test_rotamer_analysis_runs(tmp_path):
    # Base directories for Chi1 and Chi2 angle data
    base_path_chi1 = os.path.join(os.path.dirname(__file__), "data", "Rotamers", "X1 (chi1)")
    base_path_chi2 = os.path.join(os.path.dirname(__file__), "data", "Rotamers", "X2 (chi2)")

    # Collect all .xvg files for Chi1 and Chi2
    chi1_files = sorted(glob(os.path.join(base_path_chi1, "*.xvg")))
    chi2_files = sorted(glob(os.path.join(base_path_chi2, "*.xvg")))

    # Check that files are found
    assert len(chi1_files) > 0, "No Chi1 .xvg files found"
    assert len(chi2_files) > 0, "No Chi2 .xvg files found"

    # Output directory for plots
    output_dir = tmp_path / "rotamers_output"

    # Configuration for plotting
    config = {
        'figsize': (18, 5),
        'kde_title': 'Chi1 vs Chi2 KDE Plot',
        'dot_title': 'Chi1 vs Chi2 Dotplot',
        'hist_title': 'Distribution of Chi1 and Chi2',
        'save_name': 'test_kde_dotplot_chi1_vs_chi2.png',
        'cmap': 'Oranges',
        'levels': 100,
        'bins': 50
    }

    # Define time window (ps) for filtering the input angle data
    time_window = (35000, 40000)

    # Run the rotamer analysis plotting function with time window
    dihedral_kde_and_dotplot(
        output_folder=str(output_dir),
        chi1_files=chi1_files,
        chi2_files=chi2_files,
        config=config,
        time_window=time_window
    )

    # Assert that the plot file was created
    assert (output_dir / config['save_name']).exists(), "Rotamer KDE and dotplot figure was not generated"
