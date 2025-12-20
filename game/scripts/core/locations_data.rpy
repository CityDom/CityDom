
# Centralized location registry (non-breaking).
# This mirrors existing button mappings into a read-only LOCATIONS dict
# so you can gradually adopt data-driven UI with zero changes to current names.

init 1 python:
    from collections import defaultdict

    LOCATIONS = {}          # key = lowercased location name, value = dict
    _LOC_BUTTONS = defaultdict(list)        # visible buttons
    _LOC_INVISIBLE = defaultdict(list)      # invisible hotspot buttons
    _LOC_RETURN = {}                         # return paths

    def _safe_get(name):
        try:
            return globals()[name]
        except KeyError:
            try:
                return getattr(store, name)
            except Exception:
                return None

    def _mirror_existing():
        # Pull data from existing mappings if present
        door_map = _safe_get("door_button_mappings")
        inv_map  = _safe_get("invisible_door_button_mappings")
        ret_map  = _safe_get("returnLocation_mappings")

        if isinstance(door_map, dict):
            for loc, buttons in door_map.items():
                _LOC_BUTTONS[str(loc).strip().lower()].extend(buttons)

        if isinstance(inv_map, dict):
            for loc, buttons in inv_map.items():
                _LOC_INVISIBLE[str(loc).strip().lower()].extend(buttons)

        if isinstance(ret_map, dict):
            for k, v in ret_map.items():
                _LOC_RETURN[str(k).strip().lower()] = v

        # Build LOCATIONS
        keys = set(_LOC_BUTTONS.keys()) | set(_LOC_INVISIBLE.keys())
        for k in keys:
            LOCATIONS[k] = {
                "name": k,
                "buttons": tuple(_LOC_BUTTONS.get(k, ())),
                "invisible_buttons": tuple(_LOC_INVISIBLE.get(k, ())),
                "return_to": _LOC_RETURN.get(k, None),
            }

    _mirror_existing()

    def get_location(name):
        return LOCATIONS.get(str(name).strip().lower())

    def get_buttons(name, invisible=False):
        loc = get_location(name)
        if not loc:
            return ()
        return loc["invisible_buttons"] if invisible else loc["buttons"]
