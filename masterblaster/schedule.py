from operator import attrgetter


class Schedule:
    """
    Class holding all information about scheduled competitions for a team

    :param matches: List of matches

    :ivar matches: List of matches
    """

    def __init__(self, matches: list[dict]) -> None:
        from .match import Match

        self.matches: list = [Match(**match) for match in matches]

    def __iter__(self):
        return iter(self.matches)

    def get_next_match(self):
        return min(self.matches, key=attrgetter("starting_at"))
