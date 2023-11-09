import matplotlib.pyplot as plt


def fare_price(distance, different_regions, hubs_in_dest_region):
    fp = 1+distance*2.71828^(-distance/100)*(1+different_regions*hubs_in_dest_region/10)
    return fp

class Station:
    def __init__(self, name, crs_code, lat, lon, region, hub):
        self.name = name
        self.crs_code = crs_code
        self.lat = lat
        self.lon = lon
        self.region = region
        self.hub = hub
        self.checkValid()
    def checkValid(self):
        if self.name is None or not isinstance(self.name, str):
            raise ValueError("Station name is empty or not a string")
        if self.crs_code is None or not isinstance(self.crs_code, str):
            raise ValueError("Station crs_code is empty or not a string")
        if self.lat is None or not isinstance(self.lat, float):
            raise ValueError("Station lat is empty or not a float")
        if self.lon is None or not isinstance(self.lon, float):
            raise ValueError("Station lon is empty or not a float")
        if self.region is None or not isinstance(self.region, str):
            raise ValueError("Station region is empty or not a string")
        if self.hub is None or not isinstance(self.hub, bool):
            raise ValueError("Station hub is empty or not a boolean")
        if self.lat < -90 or self.lat > 90:
            raise ValueError("Station lat is not within range")
        if self.lon < -180 or self.lon > 180:
            raise ValueError("Station lon is not within range")
        if len(self.crs_code) != 3:
            raise ValueError("Station crs_code is not 3 characters long")
    def distance_to(self):
        raise NotImplementedError


class RailNetwork:
    def __init__(self, stations):
        self.checkStations(stations)
        self.stations = {station.crs_code: station for station in stations}



    def checkStations(self,stations):
        for i in stations:
            for j in stations:
                if i.crs_code == j.crs_code and i != j:
                    raise ValueError("Two stations have the same CRS code")


    def regions(self):
        raise NotImplementedError

    def n_stations(self):
        raise NotImplementedError

    def hub_stations(self, region):
        raise NotImplementedError

    def closest_hub(self, s):
        raise NotImplementedError

    def journey_planner(self, start, dest):
        raise NotImplementedError

    def journey_fare(self, start, dest, summary):
        raise NotImplementedError

    def plot_fares_to(self, crs_code, save, ADDITIONAL_ARGUMENTS):
        raise NotImplementedError

    def plot_network(self, marker_size: int = 5) -> None:
        """
        A function to plot the rail network, for visualisation purposes.
        You can optionally pass a marker size (in pixels) for the plot to use.

        The method will produce a matplotlib figure showing the locations of the stations in the network, and
        attempt to use matplotlib.pyplot.show to display the figure.

        This function will not execute successfully until you have created the regions() function.
        You are NOT required to write tests nor documentation for this function.
        """
        fig, ax = plt.subplots(figsize=(5, 10))
        ax.set_xlabel("Longitude (degrees)")
        ax.set_ylabel("Latitude (degrees)")
        ax.set_title("Railway Network")

        COLOURS = ["b", "r", "g", "c", "m", "y", "k"]
        MARKERS = [".", "o", "x", "*", "+"]

        for i, r in enumerate(self.regions):
            lats = [s.lat for s in self.stations.values() if s.region == r]
            lons = [s.lon for s in self.stations.values() if s.region == r]

            colour = COLOURS[i % len(COLOURS)]
            marker = MARKERS[i % len(MARKERS)]
            ax.scatter(lons, lats, s=marker_size, c=colour, marker=marker, label=r)

        ax.legend()
        plt.tight_layout()
        plt.show()
        return

    def plot_journey(self, start: str, dest: str) -> None:
        """
        Plot the journey between the start and end stations, on top of the rail network map.
        The start and dest inputs should the strings corresponding to the CRS codes of the
        starting and destination stations, respectively.

        The method will overlay the route that your journey_planner method has found on the
        locations of the stations in your network, and draw lines to indicate the route.

        This function will not successfully execute until you have written the journey_planner method.
        You are NOT required to write tests nor documentation for this function.
        """
        # Plot railway network in the background
        network_lats = [s.lat for s in self.stations.values()]
        network_lons = [s.lon for s in self.stations.values()]

        fig, ax = plt.subplots(figsize=(5, 10))
        ax.scatter(network_lons, network_lats, s=1, c="blue", marker="x")
        ax.set_xlabel("Longitude (degrees)")
        ax.set_ylabel("Latitude (degrees)")

        # Compute the journey
        journey = self.journey_planner(start, dest)
        plot_title = f"Journey from {journey[0].name} to {journey[-1].name}"
        ax.set_title(f"Journey from {journey[0].name} to {journey[-1].name}")

        # Draw over the network with the journey
        journey_lats = [s.lat for s in journey]
        journey_lons = [s.lon for s in journey]
        ax.plot(journey_lons, journey_lats, "ro-", markersize=2)

        plt.show()
        return

