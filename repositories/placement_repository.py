class PlacementRepository:
    """
    CampusPilot AI - Placement Repository
    """

    def __init__(self, database):
        self.database = database

    def save_placement(self, placement):
        try:
            return self.database.save_placement(placement)
        except Exception as e:
            raise RuntimeError(f"Failed to save placement: {e}")

    def get_placements(self):
        try:
            return self.database.get_placements()
        except Exception as e:
            raise RuntimeError(f"Failed to fetch placements: {e}")

    def delete_placement(self, placement_id):
        try:
            return self.database.delete_placement(placement_id)
        except Exception as e:
            raise RuntimeError(f"Failed to delete placement: {e}")