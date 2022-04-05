from pysimgame import plotting

plotting.Plot(
    "Original View",
    plotting.PlotLine("", "nonrenewable_resources", y_lims=[0, 1e9]),
    attributes=[
        "food_per_capita",
        "population",
        "persistent_pollution",
        "industrial_output_per_capita",
    ],
)
