init python:
    _STAT_REWARD_SUFFIX = {
        "love": "_love",
        "corruption": "_Corruption",
        "obedience": "_Obedience",
    }

    def _normalize_stat_key(key):
        if not key:
            return None
        key = str(key).strip().lower()
        if key in _STAT_REWARD_SUFFIX:
            return key
        return None

    def format_stat_rewards(changes, color="#808080"):
        if not isinstance(changes, dict):
            return []
        lines = []
        for display_name, stats in changes.items():
            if not isinstance(stats, dict):
                continue
            for stat_key, delta in stats.items():
                stat_key = _normalize_stat_key(stat_key)
                if stat_key is None:
                    continue
                delta = int(delta)
                if delta == 0:
                    continue
                sign = "+" if delta > 0 else "-"
                amount = abs(delta)
                lines.append(
                    f"{{color={color}}}**{display_name} {stat_key} {sign} {amount}**{{/color}}"
                )
        return lines

    def apply_stat_rewards(changes):
        if not isinstance(changes, dict):
            return
        touched = set()
        for display_name, stats in changes.items():
            if not isinstance(stats, dict):
                continue
            for stat_key, delta in stats.items():
                stat_key = _normalize_stat_key(stat_key)
                if stat_key is None:
                    continue
                delta = int(delta)
                if delta == 0:
                    continue
                var_name = display_name + _STAT_REWARD_SUFFIX[stat_key]
                renpy.store.__dict__[var_name] = renpy.store.__dict__.get(var_name, 0) + delta
                touched.add(display_name)
        update_fn = renpy.store.__dict__.get("check_and_update_character_stats")
        if update_fn:
            for name in touched:
                update_fn(name)

    def show_stat_rewards(lines):
        for line in lines:
            renpy.say(None, line)

label stat_reward(changes, return_to="ReturnToLocation", dissolve_time=0.5, color="#808080"):
    scene BlackScreen
    if dissolve_time is not None:
        with Dissolve(dissolve_time)
    $ _stat_reward_lines = format_stat_rewards(changes, color=color)
    $ show_stat_rewards(_stat_reward_lines)
    $ apply_stat_rewards(changes)
    if return_to:
        $ renpy.call(return_to)
    return
