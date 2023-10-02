from datetime import datetime
from typing import Optional
from .team import Team


class MatchSettings:
    def __init__(
        self,
        useVeto: bool = None,
        useVetoSide: bool = None,
        useBestOfX: bool = None,
        mapVetoId: Optional[str] = None,
        numberOfMaps: int = None,
        isVetoCompleted: bool = None,
        isTwitchStreamingEnabled: bool = None,
        twitchStreamingUrl: Optional[str] = None,
        enableForfeitTimer: bool = None,
        timeToReadyUpBeforeForfeitInSeconds: int = None,
        scoreConfigId: Optional[str] = None,
    ) -> None:
        self.use_veto: bool = useVeto
        self.use_veto_side: bool = useVetoSide
        self.use_best_of_x: bool = useBestOfX
        self.map_veto_id: Optional[str] = mapVetoId
        self.number_of_maps: int = numberOfMaps
        self.is_veto_completed: bool = isVetoCompleted
        self.is_twitch_streaming_enabled: bool = isTwitchStreamingEnabled
        self.twitch_streaming_url: Optional[str] = twitchStreamingUrl
        self.enable_forfeit_timer: bool = enableForfeitTimer
        self.time_to_ready_up_before_forfeit_in_seconds: int = (
            timeToReadyUpBeforeForfeitInSeconds
        )
        self.score_config_id: Optional[str] = scoreConfigId


class GameSettings:
    def __init__(
        self,
        locationId: str = None,
        useAutoForfeit: bool = None,
        forfeitTimeoutInSeconds: int = None,
        customConfigFile: Optional[str] = None,
        version: int = None,
        plugins: list = None,
        insecureServer: bool = None,
    ) -> None:
        self.location_id: str = locationId
        self.use_auto_forfeit: bool = useAutoForfeit
        self.forfeit_timeout_in_seconds: int = forfeitTimeoutInSeconds
        self.custom_config_file: Optional[str] = customConfigFile
        self.version: int = version
        self.plugins: list = plugins
        self.insecure_server: bool = insecureServer


class CompetitionStatus:
    def __init__(self, status: int = 0) -> None:
        self.statuses = {
            0: "None",
            2: "Created",
            16: "Started",
            32: "Completed",
            64: "Stopped",
        }
        self.status: int = status

    def __str__(self) -> str:
        return self.statuses.get(self.status, "Unknown")

    def __repr__(self) -> str:
        return self.statuses.get(self.status, "Unknown")


class MatchStatus:
    def __init__(self, status: int = 0) -> None:
        self.statuses = {
            0: "Not started",
            10: "Starting",
            20: "Started",
            25: "Postgame",
            27: "Paused",
            28: "Failed",
            30: "Finished",
        }
        self.status: int = status

    def __str__(self) -> str:
        return self.statuses.get(self.status, "Unknown")

    def __repr__(self) -> str:
        return self.statuses.get(self.status, "Unknown")


class MatchGameServer:
    def __init__(
        self,
        serverId: str = None,
        host: str = None,
        port: int = None,
        usedAt: Optional[datetime] = None,
    ) -> None:
        self.server_id: str = serverId
        self.host: str = host
        self.port: int = port
        self.used_at: Optional[datetime] = usedAt


class MatchConnectionInfo:
    def __init__(
        self,
        host: str = None,
        port: int = None,
        paused: bool = None,
        status: int = None,
        readyAt: datetime = None,
        location: str = None,
        password: str = None,
        serverId: str = None,
        launchUrl: str = None,
        failedReason: str = None,
        launchGotvUrl: str = None,
        shutdownDelay: int = None,
        usedGameServers: list[dict] = [{}],
        connectionString: str = None,
        gotvConnectionString: str = None,
    ) -> None:
        self.host: str = host
        self.port: int = port
        self.paused: bool = paused
        self.status: int = status
        self.ready_at: Optional[datetime] = readyAt
        self.location: str = location
        self.password: str = password
        self.server_id: str = serverId
        self.launch_url: str = launchUrl
        self.failed_reason: Optional[str] = failedReason
        self.launch_gotv_url: str = launchGotvUrl
        self.shutdown_delay: Optional[int] = shutdownDelay
        self.used_game_servers: list[MatchGameServer] = [
            MatchGameServer(**server) for server in usedGameServers
        ]
        self.connection_string: str = connectionString
        self.gotv_connection_string: str = gotvConnectionString


class Match:
    """
    Class holding all information about a match

    """

    def __init__(
        self,
        competitionStatus: int,
        competitionFormat: int,
        competitionName: str,
        parentLeagueId: str,
        parentLeagueName: str,
        parentLeagueGroupId: str,
        parentLeagueSortOrder: Optional[str],
        teams: list[dict],
        series: list,
        startId: Optional[str],
        competitionId: str,
        roundIndex: int,
        matchIndex: int,
        name: str,
        game: int,
        gameId: str,
        status: int,
        statusChangedAt: Optional[datetime],
        settings: dict,
        matchType: int,
        type: int,
        format: int,
        enteredPostgameAt: Optional[datetime],
        completedAt: Optional[datetime],
        failedReason: Optional[str],
        pauseReason: Optional[str],
        pausedBy: Optional[str],
        pausedAt: Optional[datetime],
        markForDeletion: bool,
        isMatchReschedulingEnabled: bool,
        lastPossibleMatchRescheduleDate: Optional[datetime],
        matchScheduleProposals: list,
        startingAt: Optional[datetime],
        startedAt: Optional[datetime],
        createdBy: str,
        teamScores: list,
        connectionInfo: dict,
        gameSettings: dict,
        hasValidTeams: bool,
        playerIds: list,
        teamIds: list,
        hasForfeited: bool,
        hasDisqualified: bool,
        forfeitedOrDisqualified: bool,
        id: str,
        createdAt: datetime,
    ) -> None:
        self.competition_status: CompetitionStatus = CompetitionStatus(
            competitionStatus
        )
        self.compettion_format: int = competitionFormat
        self.competition_name: str = competitionName
        self.parent_league_id: str = parentLeagueId
        self.parent_league_name: str = parentLeagueName
        self.parent_league_group_id: str = parentLeagueGroupId
        self.parent_league_sort_order: Optional[str] = parentLeagueSortOrder
        self.teams = [Team(**team["team"]) for team in teams]
        self.series: list = series
        self.start_id: Optional[str] = startId
        self.competition_id: str = competitionId
        self.round_index: int = roundIndex
        self.match_index: int = matchIndex
        self.name: str = name
        self.game: int = game
        self.game_id: str = gameId
        self.status: MatchStatus = MatchStatus(status)
        self.status_changed_at: Optional[datetime] = statusChangedAt
        self.settings: MatchSettings = MatchSettings(**settings)
        self.match_type: int = matchType
        self.type: int = type
        self.format: int = format
        self.entered_postgame_at: Optional[datetime] = enteredPostgameAt
        self.completed_at: Optional[datetime] = completedAt
        self.failed_reason: Optional[str] = failedReason
        self.pause_reason: Optional[str] = pauseReason
        self.paused_by: Optional[str] = pausedBy
        self.paused_at: Optional[datetime] = pausedAt
        self.mark_for_deletion: bool = markForDeletion
        self.is_match_rescheduled: bool = isMatchReschedulingEnabled
        self.last_possible_match_reschedule_date: Optional[
            datetime
        ] = lastPossibleMatchRescheduleDate
        self.match_schedule_proposals: list = matchScheduleProposals
        self.starting_at: Optional[datetime] = startingAt
        self.started_at: Optional[datetime] = startedAt
        self.created_by: str = createdBy
        self.team_scores: list = teamScores
        self.connection_info: Optional[MatchConnectionInfo] = MatchConnectionInfo(
            **connectionInfo["fields"]
        )
        self.game_settings: GameSettings = GameSettings(**gameSettings)
        self.has_valid_teams: bool = hasValidTeams
        self.player_ids: list = playerIds
        self.team_ids: list = teamIds
        self.has_forfeited: bool = hasForfeited
        self.has_disqualified: bool = hasDisqualified
        self.forfeited_or_disqualified: bool = forfeitedOrDisqualified
        self.id: str = id
        self.created_at: datetime = createdAt

    def __str__(self) -> str:
        return f"{self.name}"

    def get_teams(self) -> list[Team]:
        return self.teams

    def get_date_and_time(self) -> datetime:
        return self.starting_at

    def get_game_settings(self) -> GameSettings:
        return self.game_settings

    def get_connection_info(self) -> Optional[MatchConnectionInfo]:
        return self.connection_info

    def get_match_settings(self) -> MatchSettings:
        return self.settings

    def get_match_status(self) -> MatchStatus:
        return self.status

    def get_competition_status(self) -> CompetitionStatus:
        return self.competition_status
