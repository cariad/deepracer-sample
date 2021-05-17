from typing import Any, Dict


def reward_function(params: Dict[str, Any]):

    if not bool(params["all_wheels_on_track"]):
        return 1e-3

    return float(params["track_width"]) - float(params["distance_from_center"]) * 2
