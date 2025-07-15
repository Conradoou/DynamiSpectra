import os
from dynamispectra.FractionSS import fractions_ss_analysis

def test_fraction_ss_analysis_runs(tmp_path):
    # Define the base path to the test data
    base_path = os.path.join(os.path.dirname(__file__), "data", "Secondary Structure Fractions")
    
    # Define the path to the secondary structure file
    ss_file = os.path.join(base_path, "ss_fraction.dat")

    # Define the temporary output directory
    output_dir = tmp_path / "fraction_ss_output"

    # Define plot configuration
    plot_config = {
        'title': 'Secondary Structure Fractions',
        'xlabel': 'Frames',
        'ylabel': 'Fraction of Residues',
        'figsize': (8, 6),
        'fontsize': 12,
        'ylim': (0, 1.0),
        'xlim': (0, 5000)
    }

    # Run the analysis
    fractions_ss_analysis(
        file_path=ss_file,
        output_folder=str(output_dir),
        plot_config=plot_config
    )

    # Check if the output files were created
    assert (output_dir / "secondary_structure_fractions.png").exists(), "PNG plot was not generated"
    assert (output_dir / "secondary_structure_fractions.tiff").exists(), "TIFF plot was not generated"
    assert (output_dir / "secondary_structure_fractions.xlsx").exists(), "Excel file was not generated"
