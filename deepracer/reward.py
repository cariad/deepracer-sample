from typing import Any, Dict


def reward_function(params: Dict[str, Any]):

    if float(params["distance_from_center"]) <= float(params["track_width"]) * 0.6:
        return 2.0

    elif bool(params["all_wheels_on_track"]):
        return 0.2

    else:
        return 1e-3
