from railway import RailNetwork, Station


brighton = Station("Brighton", "BTN", 50.9, -0.1, "SE", False)
king_cross = Station("King's Cross", "KGX", 51.5, -0.1, "SE", True)
edinburgh_park = Station("Edinburgh Park", "EDP", 55.9, -3.2, "SC", False)

list_of_stations = [brighton,king_cross,edinburgh_park]

rail_network = RailNetwork(list_of_stations)

print(f"List of stations passed in: {list_of_stations}")
print(f"Stations in the network: {list(rail_network.stations.values())}")
print(f"Keys of rail_network.stations(): {list(rail_network.stations.keys())}")

