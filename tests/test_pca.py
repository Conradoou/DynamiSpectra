import os
from dynamispectra.PCA import pca_analysis

def test_pca_analysis_runs(tmp_path):
    base_path = os.path.join(os.path.dirname(__file__), "data", "PCA")

    pca_file = os.path.join(base_path, "2dproj.xvg")
    eigenval_file = os.path.join(base_path, "eigenvalues.xvg")

    output_dir = tmp_path / "pca_output"
    os.makedirs(output_dir, exist_ok=True)

    # Run the PCA analysis
    pca_analysis(
        pca_file_path=pca_file,
        eigenval_path=eigenval_file,
        output_folder=str(output_dir),
        title="PCA Analysis",
        figsize=(7, 6),
        cmap="inferno",
        point_size=30,
        alpha=0.8,
        axis_label_fontsize=12,
        title_fontsize=14,
        colorbar_label_fontsize=12,
        colorbar_tick_fontsize=10
    )

    # Assert output file was created
    assert (output_dir / "pca_plot.png").exists(), "PCA plot PNG file was not created"
