def distribute_resources(
    region,
    resource,
    quantity,
    resource_inventory,
    resource_distribution,
    affected_regions,
):
    """
    Distribute the specified quantity of a resource to a region.
    """
    if region not in affected_regions:
        return f"Region {region} is not affected."

    if resource not in resource_inventory:
        return f"Resource {resource} is not available."

    if quantity > resource_inventory[resource]:
        return f"Not enough {resource} available."

    # Deduct the distributed quantity from the resource inventory
    resource_inventory[resource] -= quantity

    # Update resource distribution for the region
    if region not in resource_distribution:
        resource_distribution[region] = {}

    # Add the distributed quantity to the region's resource list
    resource_distribution[region][resource] = (
        resource_distribution[region].get(resource, 0) + quantity
    )

    return f"Distributed {quantity} of {resource} to {region}."


def update_region_status(region, new_status, region_status):
    """
    Update the status of a specified region.
    """
    if region in region_status:
        region_status[region] = new_status
        return f"Updated status of {region} to {new_status}."
    else:
        return f"Region {region} does not exist."


# Data
affected_regions = [
    "one_region",
    "two_region",
    "three_region",
    "four_region",
    "five_region",
]
resource_inventory = {
    "Water_bottle": 3000,
    "Instant_ramen": 500,
    "Dry_food": 4000,
    "Medical_supplies": 8000,
    "Mineral_water": 3000,
}
resource_distribution = {}
region_status = {
    "one_region": "Critical",
    "two_region": "Stable",
    "three_region": "Recovered",
    "four_region": "Stable",
    "five_region": "Critical",
}

# Example Usage
selected_region = affected_regions[1]
selected_resource = "Instant_ramen"
desired_quantity = 400

# Distribute resources
distribution_result = distribute_resources(
    selected_region,
    selected_resource,
    desired_quantity,
    resource_inventory,
    resource_distribution,
    affected_regions,
)
print(distribution_result)

# Update region status
region_to_update = "one_region"
new_status = "Stable"
status_update_result = update_region_status(region_to_update, new_status, region_status)
print(status_update_result)
