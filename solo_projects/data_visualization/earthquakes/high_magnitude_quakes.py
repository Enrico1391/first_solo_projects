from quakes_plotter import EartquakesPlotter as EP
from pathlib import Path


# Visualize earthquakes of 4.5+ magnitude for mid-June to mid-July, 2024.


if __name__ == "__main__":
    # Make the instance and visualize the data.
    path = Path("earthquakes_files/4.5_month.geojson")
    reformat_path = Path("earthquakes_files/4.5_month_readable.geojson")

    quakes_plotter = EP(path=path)
    quakes_plotter.plot_quakes(quakes_color="Cividis")
