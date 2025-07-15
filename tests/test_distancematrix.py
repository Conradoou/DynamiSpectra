import os
from dynamispectra.DistanceMatrix import distance_matrix_analysis

def test_distance_matrix_analysis(tmp_path):
    # Path to test .xpm file
    base_path = os.path.join(os.path.dirname(__file__), "data", "Distance matrix")
    test_file = os.path.join(base_path, "Inter-residue distance matrix.xpm")

    # Output path for saving the plot (without extension)
    output_path = tmp_path / "distance_matrix_plot"

    # Plot configuration
    plot_config = {
        'xlabel': 'Residue Index',
        'ylabel': 'Residue Index',
        'label_fontsize': 12,
        'title': 'Protein Distance Matrix',
        'title_fontsize': 14,
        'colorbar_label': 'Distance (nm)',
        'max_distance': 1.5,
        'cmap': 'jet'
    }

    # Run analysis
    matrix = distance_matrix_analysis(
        xpm_file_path=test_file,
        output_path=str(output_path),
        plot=True,
        config=plot_config
    )

    # Assertions to check output
    assert matrix is not None, "Matrix was not loaded"
    assert matrix.shape[0] > 0 and matrix.shape[1] > 0, "Matrix is empty"
    assert (tmp_path / "distance_matrix_plot.png").exists(), "PNG plot was not generated"
    assert (tmp_path / "distance_matrix_plot.tiff").exists(), "TIFF plot was not generated"
