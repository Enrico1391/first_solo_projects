from pathlib import Path

from weather_data_plotter import WeatherDataPlotter as WDP


# Analize the low temperatures (C°) in Madrid (SP) for the year 2023.


if __name__ == "__main__":
    # Create a plotter instance.
    weather_plotter = WDP(title="Daily Low Temperatures, 2023", title_color="k")

    # Add data for Madrid to the plotter dataset.
    path = Path("weather_data/madrid_weather_2023_C_cm.csv")

    weather_plotter.weather_dataset(
        path=path,
        low=True,
        color="blue",
        label="Madrid",
    )

    # Generate the visualization.
    weather_plotter.plot_visual()
