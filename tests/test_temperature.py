import os
from glob import glob
from dynamispectra.Temperature import temperature_analysis

def test_temperature_analysis_runs(tmp_path):
    base_path = os.path.join(os.path.dirname(__file__), "data", "Temperature")

    # Lista os diretórios de simulações (e.g., Simulation1, Simulation2, ...)
    simulation_dirs = sorted([
        os.path.join(base_path, d) for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ])

    # Agrupa os arquivos .xvg por simulação
    simulation_file_groups = []
    for sim_dir in simulation_dirs:
        xvg_files = sorted(glob(os.path.join(sim_dir, "*.xvg")))
        if xvg_files:
            simulation_file_groups.append(xvg_files)

    # Pasta de saída temporária
    output_dir = tmp_path / "temperature_output"

    # Configuração do gráfico de temperatura ao longo do tempo
    temp_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.3,
        'xlabel': 'Time (ns)',
        'ylabel': 'Temperature (K)',
        'label_fontsize': 12,
        'figsize': (9, 6)
    }

    # Configuração do gráfico de densidade (KDE)
    density_config = {
        'labels': [f"Simulation {i+1}" for i in range(len(simulation_file_groups))],
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],
        'alpha': 0.4,
        'xlabel': 'Temperature (K)',
        'ylabel': 'Density',
        'label_fontsize': 12,
        'figsize': (6, 6)
    }

    # Executa a análise (corrigido para usar *simulation_file_groups)
    temperature_analysis(
        str(output_dir),
        *simulation_file_groups,
        temp_config=temp_config,
        density_config=density_config
    )

    # Verifica se os gráficos esperados foram gerados
    assert (output_dir / "temperature_plot.png").exists(), "Temperature time series plot was not generated"
    assert (output_dir / "temperature_plot.tiff").exists(), "Temperature time series TIFF was not generated"
    assert (output_dir / "temperature_density.png").exists(), "Temperature density plot was not generated"
    assert (output_dir / "temperature_density.tiff").exists(), "Temperature density TIFF plot was not generated"
