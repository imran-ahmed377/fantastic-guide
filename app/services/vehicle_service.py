class VehicleService:
    def __init__(self):
        self.vehicles = []  # Initializing an empty list to store vehicles in the system

    def add_vehicle(self, vehicle):
        # Method to add a vehicle to the system by appending it to the vehicles list
        self.vehicles.append(vehicle)

    def get_available_vehicles(self):
        # Method to get a list of available vehicles by filtering the vehicles list for those that are marked as available
        return [v for v in self.vehicles if v._is_available]

    # Method to find a vehicle by its ID by iterating through the vehicles list and returning the matching vehicle, or None if not found
    def find_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v._vehicle_id == vehicle_id:
                return v
        return None
