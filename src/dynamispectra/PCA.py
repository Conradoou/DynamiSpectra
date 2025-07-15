"""
===============================================================================
                        Principal Component Analysis (PCA)
===============================================================================

This module is part of the DynamiSpectra project and is designed to perform 
Principal Component Analysis (PCA) on molecular dynamics simulations using 
GROMACS output files. It reads projection data and eigenvalues from `.xvg` 
files and generates the following plot:

 1. Scatter plot of PC1 vs PC2 colored by simulation time

The variance explained by PC1 and PC2 is calculated from the eigenvalues and 
displayed on the axis labels. The output figure is saved in high-resolution 
PNG format.

Author: Iverson Conrado Bezerra
-------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Function to read the PCA projection data from a GROMACS .xvg file
def read_xvg(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            # Skip comments and metadata
            if not line.startswith(("#", "@")):
                values = line.split()
                # Store the first two columns: PC1 and PC2
                data.append([float(values[0]), float(values[1])])
    return np.array(data)

# Function to read eigenvalues from a GROMACS .xvg file
def read_eigenvalues(file_path):
    eigenvalues = []
    with open(file_path, "r") as file:
        for line in file:
            # Skip comments and metadata
            if not line.startswith(("#", "@")):
                # Store only the second column (eigenvalue)
                eigenvalues.append(float(line.split()[1]))
    return np.array(eigenvalues)

# Function to generate and save the PCA scatter plot
def plot_pca(
    pca_data,                   # 2D array with PC1 and PC2 data
    eigenvalues,                # Eigenvalues array to compute explained variance
    output_folder,              # Directory where the plot will be saved
    title="PCA",                # Title of the plot
    figsize=(7, 6),             # Figure size (width, height)
    cmap="viridis",             # Colormap for simulation time
    point_size=30,              # Size of each scatter point
    alpha=0.8,                  # Transparency level of points
    axis_label_fontsize=12,     # Font size for axis labels
    title_fontsize=14,          # Font size for the plot title
    colorbar_label_fontsize=12, # Font size for colorbar label
    colorbar_tick_fontsize=10   # Font size for colorbar tick labels
):
    # Calculate the percentage of variance explained by PC1 and PC2
    total_variance = np.sum(eigenvalues)
    pc1_var = (eigenvalues[0] / total_variance) * 100
    pc2_var = (eigenvalues[1] / total_variance) * 100

    # Create the plot
    plt.figure(figsize=figsize)
    scatter = plt.scatter(
        pca_data[:, 0],             # PC1 values on x-axis
        pca_data[:, 1],             # PC2 values on y-axis
        c=np.linspace(0, 1, len(pca_data)),  # Gradient color based on time
        cmap=cmap,                  # Use selected colormap
        s=point_size,               # Point size
        alpha=alpha,                # Transparency
        edgecolors='k',             # Black edge for better visibility
        linewidths=0.8              # Edge line thickness
    )

    # Add axis labels with variance explained
    plt.xlabel(f"PC1 ({pc1_var:.2f}%)", fontsize=axis_label_fontsize)
    plt.ylabel(f"PC2 ({pc2_var:.2f}%)", fontsize=axis_label_fontsize)

    # Add plot title
    plt.title(title, fontsize=title_fontsize)

    # Add colorbar to show simulation time progression
    cbar = plt.colorbar(scatter)
    cbar.set_label("Simulation time", fontsize=colorbar_label_fontsize)
    cbar.ax.tick_params(labelsize=colorbar_tick_fontsize)

    # Optional grid and layout settings
    plt.grid(False)
    plt.tight_layout()

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Save the plot as a high-resolution PNG image
    plt.savefig(os.path.join(output_folder, 'pca_plot.png'), dpi=300)
    plt.show()

# Main function to perform PCA analysis using GROMACS output
def pca_analysis(
    pca_file_path,               # Path to PCA projection .xvg file
    eigenval_path,               # Path to eigenvalues .xvg file
    output_folder,               # Output directory for the plot
    title="PCA",                 # Title of the plot
    figsize=(7, 6),              # Figure size (width, height)
    cmap="viridis",              # Colormap used for time
    point_size=30,               # Scatter point size
    alpha=0.8,                   # Transparency level
    axis_label_fontsize=12,      # Font size for axis labels
    title_fontsize=14,           # Font size for title
    colorbar_label_fontsize=12,  # Font size for colorbar label
    colorbar_tick_fontsize=10    # Font size for colorbar ticks
):
    # Read PCA projection data from file
    pca_data = read_xvg(pca_file_path)
    # Read eigenvalues from file
    eigenvalues = read_eigenvalues(eigenval_path)
    # Generate and save the PCA plot
    plot_pca(
        pca_data,
        eigenvalues,
        output_folder,
        title,
        figsize,
        cmap,
        point_size,
        alpha,
        axis_label_fontsize,
        title_fontsize,
        colorbar_label_fontsize,
        colorbar_tick_fontsize
    )
