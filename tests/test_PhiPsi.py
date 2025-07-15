import os
import matplotlib

from dynamispectra.PhiPsi import phipsi_analysis

def test_phipsi_analysis_runs(tmp_path):
    base_path = os.path.join(os.path.dirname(__file__), "data", "PhiPsi")

    # List all .xvg files in the folder as one simulation group (3 replicas)
    simulation_files = sorted([os.path.join(base_path, f) for f in os.listdir(base_path) if f.endswith('.xvg')])

    output_dir = tmp_path / "phipsi_output"
    os.makedirs(output_dir, exist_ok=True)

    phipsi_analysis(
        str(output_dir),
        *[simulation_files],  # single group with 3 replicas unpacked as positional argument
        phipsi_config={
            'group_names': ['Simulation 1'],
            'grid_size': 100,
            'cmap': 'jet',
            'alpha': 1,
            'figsize_subplot': (6, 5),
            'label_fontsize': 12,
        },
        residue_name=None  # or specify residue name like 'GLY'
    )

    # Check if output files for combined and individual plots exist
    combined_png = os.path.join(output_dir, "phipsi_kde_subplots_all.png")
    combined_tiff = os.path.join(output_dir, "phipsi_kde_subplots_all.tiff")

    assert os.path.exists(combined_png), "Combined PhiPsi KDE PNG plot not created."
    assert os.path.exists(combined_tiff), "Combined PhiPsi KDE TIFF plot not created."

    # Individual plots for replicas (e.g. Simulation_1_Replica_1.png)
    for i in range(len(simulation_files)):
        ind_png = os.path.join(output_dir, f"phipsi_kde_Simulation_1_Replica_{i+1}.png")
        ind_tiff = os.path.join(output_dir, f"phipsi_kde_Simulation_1_Replica_{i+1}.tiff")
        assert os.path.exists(ind_png), f"Replica {i+1} PNG plot not created."
        assert os.path.exists(ind_tiff), f"Replica {i+1} TIFF plot not created."
