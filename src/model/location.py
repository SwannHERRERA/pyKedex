class Location:
    def __init__(self, name, region_name, areas):
        self.name = name
        self.region_name = region_name
        self.areas = areas

    def __str__(self):
        res = f"""
name: {self.name}
region: {self.region_name}
"""
        res += self.get_areas()
        return res

    def get_areas(self):
        res = "areas: ["
        for area in self.areas:
            res += f"{area} "
        res += "]"
        return res
