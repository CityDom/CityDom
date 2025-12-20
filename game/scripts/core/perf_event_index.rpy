init -2 python:
    # Lightweight events indexer to avoid full scans each loop.
    from collections import defaultdict

    class _EventIndex(object):
        def __init__(self):
            self.by_loc = defaultdict(list)
            self.built = False

        def _extract(self, ev):
            try:
                start = getattr(ev, "start_hour", getattr(ev, "Start", getattr(ev, "start", None)))
                end   = getattr(ev, "end_hour",   getattr(ev, "End",   getattr(ev, "end",   None)))
                day   = getattr(ev, "day", getattr(ev, "Day", None))
                loc   = getattr(ev, "location", getattr(ev, "Location", None))
                block = getattr(ev, "block", getattr(ev, "BlockToCall", None))
                active= getattr(ev, "is_active", getattr(ev, "Active", getattr(ev, "active", True)))
            except Exception:
                start=end=day=loc=block=active=None

            if start is None:
                try:
                    start, end, day, loc, block, active = ev[0], ev[1], ev[2], ev[3], ev[4], ev[5]
                except Exception:
                    return None
            return (start, end, day, str(loc).strip().lower() if loc is not None else "", block, bool(active))

        def build(self):
            if self.built:
                return
            try:
                evs = EVENTS
            except Exception:
                return
            for _k, ev in evs.items():
                row = self._extract(ev)
                if not row:
                    continue
                start, end, day, loc, block, active = row
                if block and loc:
                    self.by_loc[loc].append((int(start), int(end), int(day) if day is not None else -1, str(block), bool(active)))
            for loc in self.by_loc:
                self.by_loc[loc].sort(key=lambda x: (x[0], x[1]))
            self.built = True

        def get(self, loc, hour, day):
            self.build()
            key = str(loc).strip().lower()
            result = []
            items = self.by_loc.get(key, ())
            for start, end, evday, block, active in items:
                if not active:
                    continue
                # Match hour range
                if not (start <= int(hour) <= int(end)):
                    continue
                # Match day rules (replicates date_check behavior)
                if evday == -1:
                    # Weekday-only
                    if not (1 <= int(day) <= 5):
                        continue
                elif evday == -2:
                    # Weekend-only
                    if not (int(day) == 0 or int(day) == 6):
                        continue
                elif evday == -3:
                    # Any day
                    pass
                else:
                    # Specific calendar day
                    if int(day) != evday:
                        continue
                result.append(block)
            return result

    _event_index = _EventIndex()

    def find_events_for_context(loc, hour, day):
        return _event_index.get(loc, hour, day)

    def rebuild_events_index():
        global _event_index
        _event_index = _EventIndex()
        _event_index.build()
