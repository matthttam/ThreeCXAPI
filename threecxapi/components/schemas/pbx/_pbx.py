from decimal import Decimal
from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import Field
from threecxapi.components.schema import Schema
from threecxapi.components.schemas import BaseCollectionPaginationCountResponse
from threecxapi.components.schemas.pbx.enums import *


class AbandonedChatsStatistics(Schema):
    ChatId: int = Field(default=None)
    DateOfRequest: str = Field(default=None)
    ParticipantEmail: str = Field(default=None)
    ParticipantMessage: str = Field(default=None)
    ParticipantName: Optional[str] = Field(default=None)
    ParticipantNumber: str = Field(default=None)
    QueueDisplayName: Optional[str] = Field(default=None)
    QueueNo: str = Field(default=None)
    ReasonForAbandoned: Optional[str] = Field(default=None)
    ReasonForDealtWith: Optional[str] = Field(default=None)
    Source: str = Field(default=None)


class AbandonedQueueCalls(Schema):
    CallerId: Optional[str] = Field(default=None)
    CallHistoryId: Optional[str] = Field(default=None)
    CallTime: Optional[str] = Field(default=None)
    CallTimeForCsv: Optional[str] = Field(default=None)
    ExtensionDisplayName: Optional[str] = Field(default=None)
    ExtensionDn: Optional[str] = Field(default=None)
    IsLoggedIn: Optional[bool] = Field(default=None)
    PollingAttempts: Optional[int] = Field(default=None)
    QueueDisplayName: Optional[str] = Field(default=None)
    QueueDn: str = Field(default=None)
    WaitTime: Optional[str] = Field(default=None)


class ActiveCall(Schema):
    Callee: Optional[str] = Field(default=None)
    Caller: Optional[str] = Field(default=None)
    EstablishedAt: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    LastChangeStatus: Optional[str] = Field(default=None)
    ServerNow: Optional[str] = Field(default=None)
    Status: Optional[str] = Field(default=None)


class ActivityLogEvent(Schema):
    Index: int = Field(default=None)
    Message: Optional[str] = Field(default=None)
    TimeStamp: Optional[str] = Field(default=None)


class AgentLoginHistory(Schema):
    Agent: str = Field(default=None)
    AgentNo: str = Field(default=None)
    Day: Optional[str] = Field(default=None)
    LoggedInDayInterval: Optional[str] = Field(default=None)
    loggedInDt: Optional[str] = Field(default=None)
    LoggedInInterval: Optional[str] = Field(default=None)
    LoggedInTotalInterval: Optional[str] = Field(default=None)
    LoggedOutDt: Optional[str] = Field(default=None)
    QueueNo: str = Field(default=None)
    TalkingDayInterval: Optional[str] = Field(default=None)
    TalkingInterval: Optional[str] = Field(default=None)
    TalkingTotalInterval: Optional[str] = Field(default=None)


class AgentsInQueueStatistics(Schema):
    AnsweredCount: Optional[int] = Field(default=None)
    AnsweredPercent: Optional[int] = Field(default=None)
    AnsweredPerHourCount: Optional[int] = Field(default=None)
    AvgRingTime: Optional[str] = Field(default=None)
    AvgTalkTime: Optional[str] = Field(default=None)
    Dn: str = Field(default=None)
    DnDisplayName: Optional[str] = Field(default=None)
    LoggedInTime: Optional[str] = Field(default=None)
    LostCount: Optional[int] = Field(default=None)
    queue: Optional[str] = Field(default=None, alias="Queue")
    QueueDisplayName: Optional[str] = Field(default=None)
    RingTime: Optional[str] = Field(default=None)
    TalkTime: Optional[str] = Field(default=None)


class AntiHackingSettings(Schema):
    HackAuthRequests: Optional[int] = Field(default=None)
    HackBarrierAmber: Optional[int] = Field(default=None)
    HackBarrierGreen: Optional[int] = Field(default=None)
    HackBarrierRed: Optional[int] = Field(default=None)
    HackBlacklistDuration: Optional[int] = Field(default=None)
    HackChallengeRequests: Optional[int] = Field(default=None)
    MaxRequestPerPeriod: Optional[int] = Field(default=None)
    SecurityDefenseProgram: Optional[bool] = Field(default=None)
    ThrottlePeriodLength: Optional[int] = Field(default=None)


class ArchiveSubsystem(Schema):
    Archiving: Optional[bool] = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    Folder: Optional[str] = Field(default=None)
    ScheduleDays: Optional[int] = Field(default=None)


class AuditLog(Schema):
    Action: Optional[int] = Field(default=None)
    Id: int = Field(default=None)
    Ip: Optional[str] = Field(default=None)
    NewData: Optional[str] = Field(default=None)
    ObjectName: Optional[str] = Field(default=None)
    ObjectType: Optional[int] = Field(default=None)
    PrevData: Optional[str] = Field(default=None)
    Source: Optional[int] = Field(default=None)
    Timestamp: Optional[str] = Field(default=None)
    UserName: Optional[str] = Field(default=None)


class AutoSchedulerSettings(Schema):
    Enabled: Optional[bool] = Field(default=None)
    ProfileAvailable: Optional[str] = Field(default=None)
    ProfileAway: Optional[str] = Field(default=None)
    ProfileDND: Optional[str] = Field(default=None)


class BackupExtras(Schema):
    Footprint: Optional[int] = Field(default=None)
    IsEncrypted: Optional[bool] = Field(default=None)
    Version: str = Field(default=None)


class BackupFailoverSettings(Schema):
    Condition: FailoverCondition = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    Interval: Optional[int] = Field(default=None)
    Mode: FailoverMode = Field(default=None)
    PostStartScript: Optional[str] = Field(default=None)
    PreStartScript: Optional[str] = Field(default=None)
    RemoteServer: Optional[str] = Field(default=None)
    TestSIPServer: Optional[bool] = Field(default=None)
    TestTunnel: Optional[bool] = Field(default=None)
    TestWebServer: Optional[bool] = Field(default=None)


class BackupSchedule(Schema):
    Day: DayOfWeek = Field(default=None)
    RepeatHours: Optional[int] = Field(default=None)
    schedule_type: ScheduleType = Field(default=None, alias="ScheduleType")
    Time: Optional[str] = Field(default=None)


class Backups(Schema):
    CreationTime: Optional[str] = Field(default=None)
    DownloadLink: str = Field(default=None)
    FileName: str = Field(default=None)
    Size: Optional[int] = Field(default=None)


class BaseCollectionPaginationCountResponse(Schema):
    count: Optional[int] = Field(default=None, alias="@odata.count")


class AbandonedChatsStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[AbandonedChatsStatistics]] = Field(default=None)


class AbandonedQueueCallsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[AbandonedQueueCalls]] = Field(default=None)


class ActiveCallCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ActiveCall]] = Field(default=None)


class ActivityLogEventCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ActivityLogEvent]] = Field(default=None)


class AgentLoginHistoryCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[AgentLoginHistory]] = Field(default=None)


class AgentsInQueueStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[AgentsInQueueStatistics]] = Field(default=None)


class AuditLogCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[AuditLog]] = Field(default=None)


class BackupsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Backups]] = Field(default=None)


class BlackListNumber(Schema):
    CallerId: str = Field(default=None)
    Description: Optional[str] = Field(default=None)
    Id: str = Field(default=None)


class BlackListNumberCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[BlackListNumber]] = Field(default=None)


class BlocklistAddr(Schema):
    added_by: AddedBy = Field(default=None, alias="AddedBy")
    block_type: BlockType = Field(default=None, alias="BlockType")
    Description: Optional[str] = Field(default=None)
    ExpiresAt: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    IPAddrMask: Optional[str] = Field(default=None)


class BlocklistAddrCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[BlocklistAddr]] = Field(default=None)


class BreachesSla(Schema):
    CallerId: str = Field(default=None)
    CallTime: str = Field(default=None)
    queue: str = Field(default=None, alias="Queue")
    QueueDnNumber: Optional[str] = Field(default=None)
    WaitingTime: Optional[str] = Field(default=None)


class BreachesSlaCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[BreachesSla]] = Field(default=None)


class CDRSettingsField(Schema):
    Length: Optional[int] = Field(default=None)
    Name: Optional[str] = Field(default=None)


class CDRSettings(Schema):
    Enabled: Optional[bool] = Field(default=None)
    EnabledFields: Optional[list[CDRSettingsField]] = Field(default=None)
    LogSize: Optional[int] = Field(default=None)
    LogType: TypeOfCDRLog = Field(default=None)
    PossibleFields: Optional[list[Optional[str]]] = Field(default=None)
    RemoveCommaDelimiters: Optional[bool] = Field(default=None)
    SocketIpAddress: Optional[str] = Field(default=None)
    SocketPort: Optional[int] = Field(default=None)


class CDRSettingsFieldCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CDRSettingsField]] = Field(default=None)


class CIDFormatting(Schema):
    ReplacePattern: Optional[str] = Field(default=None)
    SourcePattern: Optional[str] = Field(default=None)


class CIDFormattingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CIDFormatting]] = Field(default=None)


class CallCostByExtensionGroup(Schema):
    BillingCost: Optional[int] = Field(default=None)
    CallType: Optional[str] = Field(default=None)
    DstDn: Optional[str] = Field(default=None)
    DstDnClass: Optional[int] = Field(default=None)
    GroupName: Optional[str] = Field(default=None)
    IsAnswered: Optional[bool] = Field(default=None)
    RingingDur: Optional[str] = Field(default=None)
    SegId: str = Field(default=None)
    SrcDisplayName: Optional[str] = Field(default=None)
    SrcDn: Optional[str] = Field(default=None)
    StartTime: Optional[str] = Field(default=None)
    TalkingDur: Optional[str] = Field(default=None)


class CallCostByExtensionGroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallCostByExtensionGroup]] = Field(default=None)


class CallCostSettings(Schema):
    CountryName: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    Invalid: Optional[bool] = Field(default=None)
    Prefix: Optional[str] = Field(default=None)
    Rate: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    ReadOnly: Optional[bool] = Field(default=None)


class CallCostSettingsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallCostSettings]] = Field(default=None)


class CallDistribution(Schema):
    DateTimeInterval: str = Field(default=None)
    IncomingCount: int = Field(default=None)
    OutgoingCount: int = Field(default=None)


class CallDistributionCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallDistribution]] = Field(default=None)


class CallFlowScript(Schema):
    Description: Optional[str] = Field(default=None)
    Help: Optional[str] = Field(default=None)
    Id: str = Field(default=None)
    Versions: Optional[list[Optional[str]]] = Field(default=None)


class CallFlowScriptCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallFlowScript]] = Field(default=None)


class CallHistoryView(Schema):
    CallAnswered: Optional[bool] = Field(default=None)
    CallTime: str = Field(default=None)
    DstCallerNumber: Optional[str] = Field(default=None)
    DstDisplayName: Optional[str] = Field(default=None)
    DstDn: Optional[str] = Field(default=None)
    DstDnType: int = Field(default=None)
    DstExtendedDisplayName: Optional[str] = Field(default=None)
    DstExternal: bool = Field(default=None)
    DstId: int = Field(default=None)
    DstInternal: bool = Field(default=None)
    DstParticipantId: int = Field(default=None)
    DstRecId: Optional[int] = Field(default=None)
    SegmentActionId: int = Field(default=None)
    SegmentEndTime: str = Field(default=None)
    SegmentId: int = Field(default=None)
    SegmentStartTime: str = Field(default=None)
    SegmentType: int = Field(default=None)
    SrcCallerNumber: Optional[str] = Field(default=None)
    SrcDisplayName: Optional[str] = Field(default=None)
    SrcDn: Optional[str] = Field(default=None)
    SrcDnType: int = Field(default=None)
    SrcExtendedDisplayName: Optional[str] = Field(default=None)
    SrcExternal: bool = Field(default=None)
    SrcId: int = Field(default=None)
    SrcInternal: bool = Field(default=None)
    SrcParticipantId: int = Field(default=None)
    SrcRecId: Optional[int] = Field(default=None)


class CallHistoryViewCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallHistoryView]] = Field(default=None)


class CallLogData(Schema):
    ActionDnCallerId: Optional[str] = Field(default=None)
    ActionDnDisplayName: Optional[str] = Field(default=None)
    actionDnDn: Optional[str] = Field(default=None)
    ActionDnType: Optional[int] = Field(default=None)
    ActionType: Optional[int] = Field(default=None)
    Answered: Optional[bool] = Field(default=None)
    CallCost: Optional[int] = Field(default=None)
    CallHistoryId: Optional[str] = Field(default=None)
    CallId: int = Field(default=None)
    CallType: Optional[str] = Field(default=None)
    CdrId: str = Field(default=None)
    DestinationCallerId: Optional[str] = Field(default=None)
    DestinationDisplayName: Optional[str] = Field(default=None)
    DestinationDn: Optional[str] = Field(default=None)
    destination_type: Optional[int] = Field(default=None, alias="DestinationType")
    Direction: Optional[str] = Field(default=None)
    DstRecId: Optional[int] = Field(default=None)
    Indent: Optional[int] = Field(default=None)
    MainCallHistoryId: Optional[str] = Field(default=None)
    quality_report: Optional[bool] = Field(default=None, alias="QualityReport")
    Reason: Optional[str] = Field(default=None)
    RecordingUrl: Optional[str] = Field(default=None)
    RingingDuration: Optional[str] = Field(default=None)
    SegmentId: Optional[int] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)
    SourceCallerId: Optional[str] = Field(default=None)
    SourceDisplayName: Optional[str] = Field(default=None)
    SourceDn: Optional[str] = Field(default=None)
    SourceType: Optional[int] = Field(default=None)
    SrcRecId: Optional[int] = Field(default=None)
    StartTime: Optional[str] = Field(default=None)
    Status: Optional[str] = Field(default=None)
    SubrowDescNumber: Optional[int] = Field(default=None)
    Summary: Optional[str] = Field(default=None)
    TalkingDuration: Optional[str] = Field(default=None)
    Transcription: Optional[str] = Field(default=None)


class CallLogDataCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallLogData]] = Field(default=None)


class CallParkingSettings(Schema):
    AutoPickupEnabled: Optional[bool] = Field(default=None)
    AutoPickupForwardDN: Optional[str] = Field(default=None)
    AutoPickupForwardExternalNumber: Optional[str] = Field(default=None)
    AutoPickupForwardType: TypeOfAutoPickupForward = Field(default=None)
    AutoPickupTimeout: Optional[int] = Field(default=None)
    MaximumParkedCalls: Optional[int] = Field(default=None)
    MusicOnHold: Optional[str] = Field(default=None)


class CallParticipant(Schema):
    CallId: int = Field(default=None)
    DeviceId: str = Field(default=None)
    DirectControl: bool = Field(default=None)
    DN: str = Field(default=None)
    Id: int = Field(default=None)
    LegId: int = Field(default=None)
    PartyCallerId: str = Field(default=None)
    PartyCallerName: str = Field(default=None)
    PartyDn: str = Field(default=None)
    PartyDnType: str = Field(default=None)
    Status: str = Field(default=None)


class CallControlResultResponse(Schema):
    FinalStatus: str = Field(default=None)
    Reason: str = Field(default=None)
    ReasonText: str = Field(default=None)
    Result: CallParticipant = Field(default=None)
    VttId: Optional[str] = Field(default=None)


class CallTypeInfo(Schema):
    DigitsLength: Optional[str] = Field(default=None)
    Prefix: Optional[str] = Field(default=None)


class CallTypesSettings(Schema):
    International: CallTypeInfo = Field(default=None)
    Local: CallTypeInfo = Field(default=None)
    Mobile: CallTypeInfo = Field(default=None)
    National: CallTypeInfo = Field(default=None)


class CategoryUpdate(Schema):
    Category: Optional[str] = Field(default=None)
    Count: int = Field(default=None)


class CategoryUpdateCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CategoryUpdate]] = Field(default=None)


class ChatHistoryView(Schema):
    ChatName: Optional[str] = Field(default=None)
    ConversationId: int = Field(default=None)
    FromName: Optional[str] = Field(default=None)
    FromNo: Optional[str] = Field(default=None)
    IsExternal: bool = Field(default=None)
    Message: Optional[str] = Field(default=None)
    ParticipantEmail: Optional[str] = Field(default=None)
    ParticipantIp: Optional[str] = Field(default=None)
    ParticipantPhone: Optional[str] = Field(default=None)
    ParticipantsGroupsArray: Optional[list[Optional[str]]] = Field(default=None)
    ProviderName: Optional[str] = Field(default=None)
    ProviderType: ChatType = Field(default=None)
    QueueNumber: Optional[str] = Field(default=None)
    Source: Optional[str] = Field(default=None)
    TimeSent: str = Field(default=None)


class ChatHistoryViewCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ChatHistoryView]] = Field(default=None)


class ChatLinkNameValidation(Schema):
    FriendlyName: str = Field(default=None)
    Pair: str = Field(default=None)


class ChatLogSettings(Schema):
    AutoClearMonths: Optional[int] = Field(default=None)
    AutoCloseDays: Optional[int] = Field(default=None)
    RemoteStorageEnabled: Optional[bool] = Field(default=None)


class ChatMessagesHistoryView(Schema):
    ConversationId: int = Field(default=None)
    IsExternal: bool = Field(default=None)
    Message: Optional[str] = Field(default=None)
    MessageId: int = Field(default=None)
    ParticipantsGroupsArray: Optional[list[Optional[str]]] = Field(default=None)
    QueueNumber: Optional[str] = Field(default=None)
    Recipients: Optional[str] = Field(default=None)
    SenderParticipantEmail: Optional[str] = Field(default=None)
    SenderParticipantIp: Optional[str] = Field(default=None)
    SenderParticipantName: Optional[str] = Field(default=None)
    SenderParticipantNo: Optional[str] = Field(default=None)
    SenderParticipantPbx: Optional[str] = Field(default=None)
    SenderParticipantPhone: Optional[str] = Field(default=None)
    TimeSent: str = Field(default=None)


class ChatMessagesHistoryViewCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ChatMessagesHistoryView]] = Field(default=None)


class Choice(Schema):
    Key: str = Field(default=None)
    Value: str = Field(default=None)


class ChoiceCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Choice]] = Field(default=None)


class Codec(Schema):
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    RfcName: Optional[str] = Field(default=None)


class CodecCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Codec]] = Field(default=None)


class CodecsSettings(Schema):
    ExternalCodecList: Optional[list[Optional[str]]] = Field(default=None)
    LocalCodecList: Optional[list[Optional[str]]] = Field(default=None)


class ConcealedDataFile(Schema):
    Concealed: Optional[bool] = Field(default=None)
    Contents: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)


class ConcealedPassword(Schema):
    Concealed: Optional[bool] = Field(default=None)
    Value: Optional[str] = Field(default=None)


class BackupContents(Schema):
    CallHistory: Optional[bool] = Field(default=None)
    DisableBackupCompression: Optional[bool] = Field(default=None)
    EncryptBackup: Optional[bool] = Field(default=None)
    EncryptBackupPassword: ConcealedPassword = Field(default=None)
    FQDN: Optional[bool] = Field(default=None)
    license: Optional[bool] = Field(default=None, alias="License")
    PhoneProvisioning: Optional[bool] = Field(default=None)
    Prompts: Optional[bool] = Field(default=None)
    Recordings: Optional[bool] = Field(default=None)
    VoiceMails: Optional[bool] = Field(default=None)


class BackupSettings(Schema):
    Contents: BackupContents = Field(default=None)
    Rotation: Optional[int] = Field(default=None)
    schedule: BackupSchedule = Field(default=None, alias="Schedule")
    ScheduleEnabled: Optional[bool] = Field(default=None)


class ConferenceSettings(Schema):
    AutoCallParticipants: Optional[bool] = Field(default=None)
    EnableLocalMCU: Optional[bool] = Field(default=None)
    EnablePin: Optional[bool] = Field(default=None)
    Extension: Optional[str] = Field(default=None)
    ExternalNumbers: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    LogoPath: Optional[str] = Field(default=None)
    MusicOnHold: Optional[str] = Field(default=None)
    PinNumber: Optional[str] = Field(default=None)
    Zone: Optional[str] = Field(default=None)


class ConsoleRestrictions(Schema):
    AccessRestricted: Optional[bool] = Field(default=None)
    Id: str = Field(default=None)
    IpWhitelist: Optional[list[Optional[str]]] = Field(default=None)
    MyIpAddress: Optional[str] = Field(default=None)


class Contact(Schema):
    Business: Optional[str] = Field(default=None)
    Business2: Optional[str] = Field(default=None)
    BusinessFax: Optional[str] = Field(default=None)
    CompanyName: Optional[str] = Field(default=None)
    contact_type: Optional[str] = Field(default=None, alias="ContactType")
    Department: Optional[str] = Field(default=None)
    Email: Optional[str] = Field(default=None)
    FirstName: Optional[str] = Field(default=None)
    Home: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    LastName: Optional[str] = Field(default=None)
    Mobile2: Optional[str] = Field(default=None)
    Other: Optional[str] = Field(default=None)
    Pager: Optional[str] = Field(default=None)
    PhoneNumber: Optional[str] = Field(default=None)
    Tag: Optional[str] = Field(default=None)
    Title: Optional[str] = Field(default=None)


class ContactCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Contact]] = Field(default=None)


class ContactsDirSearchSettings(Schema):
    ExchangeCalendarProfileSwitching: Optional[bool] = Field(default=None)
    ExchangeEmailAddresses: Optional[list[Optional[str]]] = Field(default=None)
    ExchangeFolders: Optional[list[Optional[str]]] = Field(default=None)
    ExchangePassword: ConcealedPassword = Field(default=None)
    ExchangeServerUrl: Optional[str] = Field(default=None)
    ExchangeUser: Optional[str] = Field(default=None)


class Country(Schema):
    Continent: Optional[str] = Field(default=None)
    CountryCode: Optional[str] = Field(default=None)
    country_codes: Optional[list[Optional[str]]] = Field(default=None, alias="CountryCodes")
    DownloadUrl: Optional[str] = Field(default=None)
    ErpCode: Optional[str] = Field(default=None)
    ExitCode: Optional[str] = Field(default=None)
    Name: str = Field(default=None)
    ParentErpCode: Optional[str] = Field(default=None)
    StunServer: Optional[str] = Field(default=None)
    VoicemailNo: Optional[str] = Field(default=None)
    WebMeetingZone: Optional[str] = Field(default=None)


class CountryCodes(Schema):
    country_codes: Optional[list[Optional[str]]] = Field(default=None, alias="CountryCodes")


class CountryCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Country]] = Field(default=None)


class CreateBackup(Schema):
    Contents: BackupContents = Field(default=None)
    Name: str = Field(default=None)


class CreateTicket(Schema):
    CanCreateTicket: Optional[bool] = Field(default=None)
    create_ticket_status: CreateTicketStatus = Field(default=None, alias="CreateTicketStatus")
    FixUrl: Optional[str] = Field(default=None)


class CrmAuthentication(Schema):
    Type: AuthenticationType = Field(default=None)
    Values: Optional[list[Optional[str]]] = Field(default=None)


class CrmChoice(Schema):
    Key: str = Field(default=None)
    Value: Optional[str] = Field(default=None)


class CrmChoiceCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CrmChoice]] = Field(default=None)


class CrmContact(Schema):
    CompanyName: Optional[str] = Field(default=None)
    ContactRawData: Optional[str] = Field(default=None)
    contact_type: ContactType = Field(default=None, alias="ContactType")
    ContactUrl: Optional[str] = Field(default=None)
    Department: Optional[str] = Field(default=None)
    Email: Optional[str] = Field(default=None)
    FaxBusiness: Optional[str] = Field(default=None)
    FirstName: Optional[str] = Field(default=None)
    LastName: Optional[str] = Field(default=None)
    Pager: Optional[str] = Field(default=None)
    PhoneBusiness: Optional[str] = Field(default=None)
    PhoneBusiness2: Optional[str] = Field(default=None)
    PhoneHome: Optional[str] = Field(default=None)
    PhoneMobile: Optional[str] = Field(default=None)
    PhoneMobile2: Optional[str] = Field(default=None)
    PhoneOther: Optional[str] = Field(default=None)
    PhotoUrl: Optional[str] = Field(default=None)
    Title: Optional[str] = Field(default=None)


class CrmContactCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CrmContact]] = Field(default=None)


class CrmParameter(Schema):
    Default: Optional[str] = Field(default=None)
    Editor: EditorType = Field(default=None)
    ListValues: Optional[list[Optional[str]]] = Field(default=None)
    ListValuesText: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Parent: Optional[str] = Field(default=None)
    RequestUrl: Optional[str] = Field(default=None)
    RequestUrlParameters: Optional[str] = Field(default=None)
    ResponseScenario: Optional[str] = Field(default=None)
    Title: Optional[str] = Field(default=None)
    Type: ParameterType = Field(default=None)
    Validation: Optional[str] = Field(default=None)


class CrmParameterCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CrmParameter]] = Field(default=None)


class CrmSelectableValue(Schema):
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)


class CrmIntegration(Schema):
    country: Optional[str] = Field(default=None, alias="Country")
    EnabledForDidCalls: Optional[bool] = Field(default=None)
    EnabledForExternalCalls: Optional[bool] = Field(default=None)
    Id: str = Field(default=None)
    Name: str = Field(default=None)
    phonebook_priority_options: PhonebookPriorityOptions = Field(default=None, alias="PhonebookPriorityOptions")
    PhonebookSynchronization: Optional[bool] = Field(default=None)
    PossibleValues: Optional[list[CrmSelectableValue]] = Field(default=None)
    VariableChoices: Optional[list[CrmChoice]] = Field(default=None)


class CrmSelectableValueCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CrmSelectableValue]] = Field(default=None)


class CrmTemplate(Schema):
    authentication: CrmAuthentication = Field(default=None, alias="Authentication")
    Name: str = Field(default=None)
    Parameters: Optional[list[CrmParameter]] = Field(default=None)


class CrmTemplateCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CrmTemplate]] = Field(default=None)


class CrmTemplateSource(Schema):
    Value: Optional[str] = Field(default=None)


class CrmTestResult(Schema):
    IsError: Optional[bool] = Field(default=None)
    Log: Optional[str] = Field(default=None)
    Message: Optional[str] = Field(default=None)
    SearchResult: Optional[list[CrmContact]] = Field(default=None)


class CustomPrompt(Schema):
    CanBeDeleted: bool = Field(default=None)
    DisplayName: str = Field(default=None)
    FileLink: str = Field(default=None)
    Filename: str = Field(default=None)
    prompt_type: PromptType = Field(default=None, alias="PromptType")


class CustomPromptCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CustomPrompt]] = Field(default=None)


class CustomQueueRingtone(Schema):
    queue: Optional[str] = Field(default=None, alias="Queue")
    Ringtone: Optional[str] = Field(default=None)


class CustomQueueRingtoneCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CustomQueueRingtone]] = Field(default=None)


class DNProperty(Schema):
    Description: Optional[str] = Field(default=None)
    Id: Optional[int] = Field(default=None)
    Name: str = Field(default=None)
    Value: str = Field(default=None)


class DNPropertyCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[DNProperty]] = Field(default=None)


class DNRange(Schema):
    From: Optional[str] = Field(default=None)
    To: Optional[str] = Field(default=None)


class DNRangeCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[DNRange]] = Field(default=None)


class Destination(Schema):
    External: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    Tags: Optional[list[UserTag]] = Field(default=None)
    To: DestinationType = Field(default=None)
    Type: PeerType = Field(default=None)


class AvailableRouting(Schema):
    BusyAllCalls: Optional[bool] = Field(default=None)
    BusyExternal: Destination = Field(default=None)
    BusyInternal: Destination = Field(default=None)
    NoAnswerAllCalls: Optional[bool] = Field(default=None)
    NoAnswerExternal: Destination = Field(default=None)
    NoAnswerInternal: Destination = Field(default=None)
    NotRegisteredAllCalls: Optional[bool] = Field(default=None)
    NotRegisteredExternal: Destination = Field(default=None)
    NotRegisteredInternal: Destination = Field(default=None)


class AwayRouting(Schema):
    AllHoursExternal: Optional[bool] = Field(default=None)
    AllHoursInternal: Optional[bool] = Field(default=None)
    External: Destination = Field(default=None)
    Internal: Destination = Field(default=None)


class DetailedQueueStatistics(Schema):
    AnsweredCount: Optional[int] = Field(default=None)
    AvgRingTime: Optional[str] = Field(default=None)
    AvgTalkTime: Optional[str] = Field(default=None)
    CallbacksCount: Optional[int] = Field(default=None)
    CallsCount: Optional[int] = Field(default=None)
    QueueDn: Optional[str] = Field(default=None)
    QueueDnNumber: str = Field(default=None)
    RingTime: Optional[str] = Field(default=None)
    TalkTime: Optional[str] = Field(default=None)


class DetailedQueueStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[DetailedQueueStatistics]] = Field(default=None)


class DeviceInfo(Schema):
    Assigned: Optional[bool] = Field(default=None)
    AssignedUser: Optional[str] = Field(default=None)
    DetectedAt: Optional[str] = Field(default=None)
    FirmwareVersion: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    InterfaceLink: Optional[str] = Field(default=None)
    MAC: Optional[str] = Field(default=None)
    Model: Optional[str] = Field(default=None)
    NetworkAddress: Optional[str] = Field(default=None)
    NetworkPath: Optional[str] = Field(default=None)
    Parameters: Optional[str] = Field(default=None)
    SbcName: Optional[str] = Field(default=None)
    TemplateName: Optional[str] = Field(default=None)
    UserAgent: Optional[str] = Field(default=None)
    Vendor: Optional[str] = Field(default=None)
    ViaSBC: Optional[bool] = Field(default=None)


class DeviceInfoCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[DeviceInfo]] = Field(default=None)


class DeviceLine(Schema):
    Key: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: str = Field(default=None)


class DeviceLineCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[DeviceLine]] = Field(default=None)


class DialCodeSettings(Schema):
    DialCodeBillingCode: Optional[str] = Field(default=None)
    DialCodeHideCallerID: Optional[str] = Field(default=None)
    DialCodeHotdesking: Optional[str] = Field(default=None)
    DialCodeHotelAccess: Optional[str] = Field(default=None)
    DialCodeIntercom: Optional[str] = Field(default=None)
    DialCodeLoggedInQueue: Optional[str] = Field(default=None)
    DialCodeLoggedOutQueue: Optional[str] = Field(default=None)
    DialCodeOutOffice: Optional[str] = Field(default=None)
    DialCodePark: Optional[str] = Field(default=None)
    DialCodePickup: Optional[str] = Field(default=None)
    DialCodeProfileStatus: Optional[str] = Field(default=None)
    DialCodeUnpark: Optional[str] = Field(default=None)
    DialCodeVMail: Optional[str] = Field(default=None)


class DirectoryParameters(Schema):
    Filesystem: FileSystemType = Field(default=None)
    Json: Optional[str] = Field(default=None)
    Path: Optional[str] = Field(default=None)


class E164Settings(Schema):
    AreaCode: Optional[str] = Field(default=None)
    CountryCode: Optional[str] = Field(default=None)
    CountryName: Optional[str] = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    InternationalCode: Optional[str] = Field(default=None)
    NationalCode: Optional[str] = Field(default=None)
    Prefix: Optional[str] = Field(default=None)
    RemoveAreaCode: Optional[bool] = Field(default=None)
    RemoveCountryCode: Optional[bool] = Field(default=None)


class EmailTemplate(Schema):
    Body: str = Field(default=None)
    From: Optional[str] = Field(default=None)
    IsConference: Optional[bool] = Field(default=None)
    IsDefault: Optional[bool] = Field(default=None)
    Lang: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Subject: Optional[str] = Field(default=None)
    TemplatePath: str = Field(default=None)


class EmailTemplateCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[EmailTemplate]] = Field(default=None)


class EmergencyGeoLocation(Schema):
    FriendlyName: str = Field(default=None)
    Id: str = Field(default=None)


class EmergencyGeoLocationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[EmergencyGeoLocation]] = Field(default=None)


class EmergencyGeoTrunkLocation(Schema):
    Id: str = Field(default=None)
    Location: EmergencyGeoLocation = Field(default=None)
    ProviderUri: str = Field(default=None)
    TrunkDn: Optional[str] = Field(default=None)


class EmergencyGeoTrunkLocationCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[EmergencyGeoTrunkLocation]] = Field(default=None)


class EntityRestrictions(Schema):
    Allowed: Optional[int] = Field(default=None)
    Unlimited: Optional[bool] = Field(default=None)
    Used: Optional[int] = Field(default=None)


class EventLog(Schema):
    EventId: Optional[int] = Field(default=None)
    group: Optional[str] = Field(default=None, alias="Group")
    GroupName: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    Message: Optional[str] = Field(default=None)
    Params: Optional[list[Optional[str]]] = Field(default=None)
    Source: Optional[str] = Field(default=None)
    TimeGenerated: Optional[str] = Field(default=None)
    Type: EventLogType = Field(default=None)


class EventLogCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[EventLog]] = Field(default=None)


class ExtensionFilter(Schema):
    CallIds: Optional[list[Optional[str]]] = Field(default=None)
    Number: Optional[str] = Field(default=None)


class ActivityLogsFilter(Schema):
    Extensions: Optional[list[ExtensionFilter]] = Field(default=None)


class ExtensionFilterCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ExtensionFilter]] = Field(default=None)


class ExtensionStatistics(Schema):
    DisplayName: Optional[str] = Field(default=None)
    Dn: str = Field(default=None)
    InboundAnsweredCount: Optional[int] = Field(default=None)
    InboundAnsweredTalkingDur: Optional[str] = Field(default=None)
    InboundUnansweredCount: Optional[int] = Field(default=None)
    OutboundAnsweredCount: Optional[int] = Field(default=None)
    OutboundAnsweredTalkingDur: Optional[str] = Field(default=None)
    OutboundUnansweredCount: Optional[int] = Field(default=None)


class ExtensionStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ExtensionStatistics]] = Field(default=None)


class ExtensionsStatisticsByRingGroups(Schema):
    ExtensionAnsweredCount: Optional[int] = Field(default=None)
    ExtensionDisplayName: Optional[str] = Field(default=None)
    ExtensionDn: str = Field(default=None)
    RingGroupDisplayName: Optional[str] = Field(default=None)
    RingGroupDn: str = Field(default=None)
    RingGroupReceivedCount: Optional[int] = Field(default=None)
    RingGroupUnansweredCount: Optional[int] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)
    SortOrder: Optional[int] = Field(default=None)


class ExtensionsStatisticsByRingGroupsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ExtensionsStatisticsByRingGroups]] = Field(default=None)


class ExternalAccount(Schema):
    Email: str = Field(default=None)
    Id: str = Field(default=None)
    Name: str = Field(default=None)


class ExternalAccountCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ExternalAccount]] = Field(default=None)


class ExternalAccountsPage(Schema):
    NextPageToken: Optional[str] = Field(default=None)
    Users: Optional[list[ExternalAccount]] = Field(default=None)


class FailoverScriptFile(Schema):
    Filename: str = Field(default=None)


class FaxServerSettings(Schema):
    AuthId: Optional[str] = Field(default=None)
    AuthPassword: ConcealedPassword = Field(default=None)
    AutoCleanup: Optional[bool] = Field(default=None)
    Email: Optional[str] = Field(default=None)
    FaxServerId: Optional[int] = Field(default=None)
    G711ToT38Fallback: Optional[bool] = Field(default=None)
    MaxAge: Optional[int] = Field(default=None)
    Number: str = Field(default=None)
    RemoteStorageEnabled: Optional[bool] = Field(default=None)


class FirewallState(Schema):
    Html: Optional[str] = Field(default=None)
    Id: str = Field(default=None)
    Running: Optional[bool] = Field(default=None)
    Stopping: Optional[bool] = Field(default=None)


class Firmware(Schema):
    Filename: Optional[str] = Field(default=None)
    Id: str = Field(default=None)
    Model: Optional[str] = Field(default=None)
    Vendor: Optional[str] = Field(default=None)
    Version: Optional[str] = Field(default=None)


class FirmwareCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Firmware]] = Field(default=None)


class FirmwareState(Schema):
    Count: Optional[int] = Field(default=None)
    FileNames: Optional[list[Optional[str]]] = Field(default=None)
    Id: Optional[str] = Field(default=None)
    TotalSize: Optional[int] = Field(default=None)


class FirstAvailableNumber(Schema):
    Number: Optional[str] = Field(default=None)


class ForwardingProfile(Schema):
    AcceptMultipleCalls: Optional[bool] = Field(default=None)
    AvailableRoute: AvailableRouting = Field(default=None)
    AwayRoute: AwayRouting = Field(default=None)
    BlockPushCalls: Optional[bool] = Field(default=None)
    CustomMessage: Optional[str] = Field(default=None)
    CustomName: Optional[str] = Field(default=None)
    DisableRingGroupCalls: Optional[bool] = Field(default=None)
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    NoAnswerTimeout: Optional[int] = Field(default=None)
    OfficeHoursAutoQueueLogOut: Optional[bool] = Field(default=None)
    RingMyMobile: Optional[bool] = Field(default=None)


class ForwardingProfileCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ForwardingProfile]] = Field(default=None)


class FxsModel(Schema):
    CanBeSBC: Optional[bool] = Field(default=None)
    DisplayName: str = Field(default=None)
    UserAgent: str = Field(default=None)


class FxsModelCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[FxsModel]] = Field(default=None)


class FxsProvisioning(Schema):
    LocalAudioPortEnd: Optional[int] = Field(default=None)
    LocalAudioPortStart: Optional[int] = Field(default=None)
    LocalInterface: Optional[str] = Field(default=None)
    LocalSipPort: Optional[int] = Field(default=None)
    Method: ProvType = Field(default=None)
    ProvLink: Optional[str] = Field(default=None)
    RemoteFQDN: Optional[str] = Field(default=None)
    RemotePort: Optional[int] = Field(default=None)
    SbcName: Optional[str] = Field(default=None)


class FxsVariableChoice(Schema):
    DisplayName: str = Field(default=None)
    Name: str = Field(default=None)


class FxsVariable(Schema):
    Choices: Optional[list[FxsVariableChoice]] = Field(default=None)
    Name: str = Field(default=None)
    Title: str = Field(default=None)
    ValidationType: Optional[str] = Field(default=None)


class FxsTemplate(Schema):
    AllowedNetConfigs: Optional[list[Optional[str]]] = Field(default=None)
    AllowSSLProvisioning: Optional[bool] = Field(default=None)
    Brand: str = Field(default=None)
    Content: Optional[str] = Field(default=None)
    device_type: DeviceType = Field(default=None, alias="DeviceType")
    Id: str = Field(default=None)
    IsCustom: bool = Field(default=None)
    Languages: Optional[list[Optional[str]]] = Field(default=None)
    Models: Optional[list[FxsModel]] = Field(default=None)
    NumberOfExtensions: int = Field(default=None)
    RpsEnabled: Optional[bool] = Field(default=None)
    template_type: TemplateType = Field(default=None, alias="TemplateType")
    TimeZones: Optional[list[Optional[str]]] = Field(default=None)
    URL: str = Field(default=None)
    Variables: Optional[list[FxsVariable]] = Field(default=None)


class FxsTemplateCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[FxsTemplate]] = Field(default=None)


class FxsVariableChoiceCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[FxsVariableChoice]] = Field(default=None)


class FxsVariableCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[FxsVariable]] = Field(default=None)


class GarbageCollect(Schema):
    Blocking: Optional[bool] = Field(default=None)
    Compacting: Optional[bool] = Field(default=None)
    Generation: Optional[int] = Field(default=None)
    Mode: GCCollectionMode = Field(default=None)


class GatewayParameter(Schema):
    CanHaveDID: Optional[bool] = Field(default=None)
    Description: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    InboundPossibleValues: Optional[list[Optional[str]]] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    OutboundPossibleValues: Optional[list[Optional[str]]] = Field(default=None)
    SourceIDPossibleValues: Optional[list[Optional[str]]] = Field(default=None)


class GatewayParameterBinding(Schema):
    Custom: Optional[str] = Field(default=None)
    ParamId: int = Field(default=None)
    ValueId: int = Field(default=None)


class Gateway(Schema):
    Codecs: Optional[list[Optional[str]]] = Field(default=None)
    DeliverAudio: Optional[bool] = Field(default=None)
    DestNumberInRemotePartyIDCalled: Optional[bool] = Field(default=None)
    DestNumberInRequestLineURI: Optional[bool] = Field(default=None)
    DestNumberInTo: Optional[bool] = Field(default=None)
    Host: Optional[str] = Field(default=None)
    Id: Optional[int] = Field(default=None)
    InboundParams: Optional[list[GatewayParameterBinding]] = Field(default=None)
    Internal: Optional[bool] = Field(default=None)
    IPInRegistrationContact: IPInRegistrationContactType = Field(default=None)
    Lines: Optional[int] = Field(default=None)
    MatchingStrategy: MatchingStrategyType = Field(default=None)
    Name: Optional[str] = Field(default=None)
    OutboundCallerID: Optional[str] = Field(default=None)
    OutboundParams: Optional[list[GatewayParameterBinding]] = Field(default=None)
    Port: Optional[int] = Field(default=None)
    ProxyHost: Optional[str] = Field(default=None)
    ProxyPort: Optional[int] = Field(default=None)
    RequireRegistrationFor: RequireRegistrationForType = Field(default=None)
    SourceIdentification: Optional[list[GatewayParameterBinding]] = Field(default=None)
    SpecifiedIPForRegistrationContact: Optional[str] = Field(default=None)
    SRTPMode: SRTPModeType = Field(default=None)
    SupportReinvite: Optional[bool] = Field(default=None)
    SupportReplaces: Optional[bool] = Field(default=None)
    TemplateFilename: Optional[str] = Field(default=None)
    TimeBetweenReg: Optional[int] = Field(default=None)
    Type: GatewayType = Field(default=None)
    UseIPInContact: Optional[bool] = Field(default=None)
    VariableChoices: Optional[list[Choice]] = Field(default=None)


class GatewayParameterBindingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[GatewayParameterBinding]] = Field(default=None)


class GatewayParameterCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[GatewayParameter]] = Field(default=None)


class GatewayParameterValue(Schema):
    Description: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)


class GatewayParameterValueCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[GatewayParameterValue]] = Field(default=None)


class GeneralLiveChatSettings(Schema):
    AllowSoundNotifications: Optional[bool] = Field(default=None)
    authentication: Authentication = Field(default=None, alias="Authentication")
    DisableOfflineMessages: Optional[bool] = Field(default=None)
    EnableGA: Optional[bool] = Field(default=None)
    EnableOnMobile: Optional[bool] = Field(default=None)
    GdprEnabled: Optional[bool] = Field(default=None)
    greeting: LiveChatGreeting = Field(default=None, alias="Greeting")


class GeneralSettingsForApps(Schema):
    AllowChangePassword: Optional[bool] = Field(default=None)
    auto_scheduler_settings: AutoSchedulerSettings = Field(default=None, alias="AutoSchedulerSettings")
    avatar_style: AvatarStyle = Field(default=None, alias="AvatarStyle")
    BrandLogoImage: Optional[str] = Field(default=None)
    BrandMainImage: Optional[str] = Field(default=None)
    BrandUrl: Optional[str] = Field(default=None)
    EnableChat: Optional[bool] = Field(default=None)
    HideAbandonedQueueCalls: Optional[bool] = Field(default=None)
    HideCRMContacts: Optional[bool] = Field(default=None)
    HideInteractionHistory: Optional[bool] = Field(default=None)
    HideSystemExtensions: Optional[bool] = Field(default=None)
    NameOfCustomAvailableStatus: Optional[str] = Field(default=None)
    NameOfCustomOutOfOfficeStatus: Optional[str] = Field(default=None)


class GeneralSettingsForPbx(Schema):
    AllowFwdToExternal: Optional[bool] = Field(default=None)
    BusyMonitor: Optional[bool] = Field(default=None)
    BusyMonitorTimeout: Optional[int] = Field(default=None)
    DisableOutboundCallsOutOfficeHours: Optional[bool] = Field(default=None)
    EnableVMenuOutboundCalls: Optional[bool] = Field(default=None)
    HDAutoLogoutEnabled: Optional[bool] = Field(default=None)
    HDAutoLogoutTime: Optional[str] = Field(default=None)
    LimitCallPickup: Optional[bool] = Field(default=None)
    OperatorExtension: Optional[str] = Field(default=None)
    PlayBusy: Optional[bool] = Field(default=None)
    ScheduledReportGenerationTime: Optional[str] = Field(default=None)


class GoogleUserSync(Schema):
    IsEnabled: Optional[bool] = Field(default=None)
    IsSyncDepartments: Optional[bool] = Field(default=None)
    IsSyncPersonalContacts: Optional[bool] = Field(default=None)
    IsSyncPhoto: Optional[bool] = Field(default=None)
    SelectedUsers: Optional[list[Optional[str]]] = Field(default=None)
    StartingExtensionNumber: Optional[str] = Field(default=None)
    SyncType: IntegrationSyncType = Field(default=None)
    UseCalendarEventsAsPresence: Optional[bool] = Field(default=None)


class GoogleSettings(Schema):
    ClientId: Optional[str] = Field(default=None)
    ClientSecret: ConcealedPassword = Field(default=None)
    Id: str = Field(default=None)
    IsExtensionSignInEnabled: Optional[bool] = Field(default=None)
    ProjectId: Optional[str] = Field(default=None)
    ProvisionUrl: Optional[str] = Field(default=None)
    ReCaptchaEnabled: Optional[bool] = Field(default=None)
    UserSync: GoogleUserSync = Field(default=None)


class Greeting(Schema):
    DisplayName: Optional[str] = Field(default=None)
    Filename: Optional[str] = Field(default=None)
    Type: ProfileType = Field(default=None)


class GreetingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Greeting]] = Field(default=None)


class GreetingFile(Schema):
    DisplayName: Optional[str] = Field(default=None)
    Filename: str = Field(default=None)


class GroupProps(Schema):
    DectMaxCount: Optional[int] = Field(default=None)
    Fqdn: Optional[str] = Field(default=None)
    LiveChatMaxCount: Optional[int] = Field(default=None)
    OutboundRulesMaxCount: Optional[int] = Field(default=None)
    PersonalContactsMaxCount: Optional[int] = Field(default=None)
    PromptsMaxCount: Optional[int] = Field(default=None)
    ResellerId: Optional[str] = Field(default=None)
    ResellerName: Optional[str] = Field(default=None)
    SbcMaxCount: Optional[int] = Field(default=None)
    startup_license: StartupLicense = Field(default=None, alias="StartupLicense")
    StartupOwnerEmail: Optional[str] = Field(default=None)
    SubcriptionExpireDate: Optional[str] = Field(default=None)
    Subscription: Optional[str] = Field(default=None)
    SubscriptionType: Optional[str] = Field(default=None)
    SystemNumberFrom: Optional[str] = Field(default=None)
    SystemNumberTo: Optional[str] = Field(default=None)
    TrunkNumberFrom: Optional[str] = Field(default=None)
    TrunkNumberTo: Optional[str] = Field(default=None)
    TrunksMaxCount: Optional[int] = Field(default=None)
    UserNumberFrom: Optional[str] = Field(default=None)
    UserNumberTo: Optional[str] = Field(default=None)


class Holiday(Schema):
    Day: int = Field(default=None)
    DayEnd: int = Field(default=None)
    HolidayPrompt: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    IsRecurrent: Optional[bool] = Field(default=None)
    Month: int = Field(default=None)
    MonthEnd: int = Field(default=None)
    Name: str = Field(default=None)
    TimeOfEndDate: str = Field(default=None)
    TimeOfStartDate: str = Field(default=None)
    Year: int = Field(default=None)
    YearEnd: int = Field(default=None)


class HolidayCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Holiday]] = Field(default=None)


class HotelServices(Schema):
    Enabled: Optional[bool] = Field(default=None)
    HotelGroups: Optional[list[Optional[str]]] = Field(default=None)
    IntegrationType: PmsIntegrationType = Field(default=None)
    IpAddress: Optional[str] = Field(default=None)
    NoAnswerDestination: Destination = Field(default=None)
    NoAnswerTimeout: Optional[int] = Field(default=None)
    Port: Optional[int] = Field(default=None)


class IActionResult(Schema):
    pass


class InboundCall(Schema):
    CallDuration: str = Field(default=None)
    CallHistoryId: Optional[str] = Field(default=None)
    CdrId: str = Field(default=None)
    DestinationCallerId: Optional[str] = Field(default=None)
    DestinationDisplayName: Optional[str] = Field(default=None)
    DestinationDn: Optional[str] = Field(default=None)
    Did: Optional[str] = Field(default=None)
    quality_report: Optional[bool] = Field(default=None, alias="QualityReport")
    RecordingId: Optional[int] = Field(default=None)
    RecordingUrl: Optional[str] = Field(default=None)
    RingingDuration: str = Field(default=None)
    RuleName: Optional[str] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)
    SourceCallerId: Optional[str] = Field(default=None)
    SourceDisplayName: Optional[str] = Field(default=None)
    SourceDn: Optional[str] = Field(default=None)
    StartTime: str = Field(default=None)
    Status: Optional[str] = Field(default=None)
    Summary: Optional[str] = Field(default=None)
    TalkingDuration: str = Field(default=None)
    Transcription: Optional[str] = Field(default=None)
    TrunkName: Optional[str] = Field(default=None)
    TrunkNumber: Optional[str] = Field(default=None)


class InboundCallCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[InboundCall]] = Field(default=None)


class InboundRuleReport(Schema):
    DID: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    InOfficeRouting: Destination = Field(default=None)
    OutOfficeRouting: Destination = Field(default=None)
    RuleName: Optional[str] = Field(default=None)
    trunk: Optional[str] = Field(default=None, alias="Trunk")


class InboundRuleReportCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[InboundRuleReport]] = Field(default=None)


class InstallUpdates(Schema):
    Entries: Optional[list[str]] = Field(default=None)
    Key: str = Field(default=None)


class KeyValuePair_2OfString_OnBoardConnectedParticipant(Schema):
    pass


class KeyValuePair_2OfString_OnBoardConnectedParticipantCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[KeyValuePair_2OfString_OnBoardConnectedParticipant]] = Field(default=None)


class LanguageItem(Schema):
    Code: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)


class LastCdrAndChatMessageTimestamp(Schema):
    LastCdrStartedAt: str = Field(default=None)
    LastChatMessageTimeSent: str = Field(default=None)


class LastCdrAndChatMessageTimestampCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[LastCdrAndChatMessageTimestamp]] = Field(default=None)


class License(Schema):
    CountryCode: Optional[str] = Field(default=None)
    IsMaintainceExpired: Optional[bool] = Field(default=None)
    ProductCode: Optional[str] = Field(default=None)


class LicenseStatus(Schema):
    Activated: Optional[bool] = Field(default=None)
    ActiveModules: Optional[list[Optional[str]]] = Field(default=None)
    AdminEMail: Optional[str] = Field(default=None)
    CompanyName: Optional[str] = Field(default=None)
    ContactName: Optional[str] = Field(default=None)
    CountryCode: Optional[str] = Field(default=None)
    CountryName: Optional[str] = Field(default=None)
    EMail: Optional[str] = Field(default=None)
    ExpirationDate: Optional[str] = Field(default=None)
    LicenseActive: Optional[bool] = Field(default=None)
    LicenseKey: str = Field(default=None)
    MaintenanceExpiresAt: Optional[str] = Field(default=None)
    MaxSimCalls: Optional[int] = Field(default=None)
    ProductCode: Optional[str] = Field(default=None)
    ResellerName: Optional[str] = Field(default=None)
    SimMeetingParticipants: Optional[int] = Field(default=None)
    Support: Optional[bool] = Field(default=None)
    Telephone: Optional[str] = Field(default=None)
    Version: Optional[str] = Field(default=None)


class LinkMyGroupPartnerRequestBody(Schema):
    resellerId: str = Field(default=None)


class LiveChatAdvancedSettings(Schema):
    CallTitle: Optional[str] = Field(default=None)
    CommunicationOptions: LiveChatCommunication = Field(default=None)
    EnableDirectCall: Optional[bool] = Field(default=None)
    IgnoreQueueOwnership: Optional[bool] = Field(default=None)


class LiveChatBox(Schema):
    button_icon_type: ButtonIconType = Field(default=None, alias="ButtonIconType")
    ButtonIconUrl: Optional[str] = Field(default=None)
    ChatDelay: Optional[int] = Field(default=None)
    Height: Optional[str] = Field(default=None)
    live_chat_language: LiveChatLanguage = Field(default=None, alias="LiveChatLanguage")
    live_message_userinfo_format: LiveMessageUserinfoFormat = Field(default=None, alias="LiveMessageUserinfoFormat")
    MessageDateformat: LiveChatMessageDateformat = Field(default=None)
    MinimizedStyle: LiveChatMinimizedStyle = Field(default=None)
    OperatorIcon: Optional[str] = Field(default=None)
    OperatorName: Optional[str] = Field(default=None)
    ShowOperatorActualName: Optional[bool] = Field(default=None)
    WindowIcon: Optional[str] = Field(default=None)


class LiveChatStyling(Schema):
    Animation: AnimationStyle = Field(default=None)
    Minimized: Optional[bool] = Field(default=None)
    Style: Optional[str] = Field(default=None)
    UseRubik: Optional[bool] = Field(default=None)


class LocationSettings(Schema):
    file_system_type: FileSystemType = Field(default=None, alias="FileSystemType")
    FtpPassword: ConcealedPassword = Field(default=None)
    FtpPath: Optional[str] = Field(default=None)
    FtpUser: Optional[str] = Field(default=None)
    FtpValidateCertificate: Optional[bool] = Field(default=None)
    GbJson: ConcealedDataFile = Field(default=None)
    GbPath: Optional[str] = Field(default=None)
    LocalPath: Optional[str] = Field(default=None)
    NsDomain: Optional[str] = Field(default=None)
    NsPassword: ConcealedPassword = Field(default=None)
    NsPath: Optional[str] = Field(default=None)
    NsUser: Optional[str] = Field(default=None)
    SftpPassword: ConcealedPassword = Field(default=None)
    SftpPath: Optional[str] = Field(default=None)
    SftpPrivateKey: ConcealedDataFile = Field(default=None)
    SftpUser: Optional[str] = Field(default=None)
    SharePointPath: Optional[str] = Field(default=None)


class BackupRepositorySettings(Schema):
    Location: LocationSettings = Field(default=None)


class LogEntry(Schema):
    Text: str = Field(default=None)
    TimeStamp: str = Field(default=None)


class LogEntryCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[LogEntry]] = Field(default=None)


class LoggingSettings(Schema):
    KeepLogs: Optional[bool] = Field(default=None)
    KeepLogsDays: Optional[int] = Field(default=None)
    LoggingLevel: Optional[int] = Field(default=None)


class M365ToPbxBinding(Schema):
    From: SynchronizedM365Profile = Field(default=None)
    To: SynchronizedPbxProfile = Field(default=None)


class M365ToPbxBindingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[M365ToPbxBinding]] = Field(default=None)


class MCURequestStatus(Schema):
    ErrorMessage: Optional[str] = Field(default=None)
    McuId: Optional[str] = Field(default=None)
    Operation: McuOperation = Field(default=None)
    RequestExpiration: Optional[str] = Field(default=None)
    State: McuReqState = Field(default=None)


class MakeCallUserRecordGreetingRequestBody(Schema):
    dn: str = Field(default=None)
    filename: str = Field(default=None)


class MeetingParams(Schema):
    bitrate_data: int = Field(default=None)
    bitrate_video: int = Field(default=None)
    canchangemedia: Optional[int] = Field(default=None)
    clicktocall: Optional[int] = Field(default=None)
    forcemoderator: Optional[int] = Field(default=None)
    hideparticipants: Optional[int] = Field(default=None)
    mcu: str = Field(default=None)
    meetingduration: int = Field(default=None)
    meetingtitle: str = Field(default=None)
    moderateparticipants: Optional[int] = Field(default=None)
    needorganizer: Optional[int] = Field(default=None)
    note: str = Field(default=None)
    org_properties: Optional[str] = Field(default=None)
    part_properties: Optional[str] = Field(default=None)
    privaterooms: Optional[int] = Field(default=None)
    quickmeeting: int = Field(default=None)


class Microsoft365Status(Schema):
    ApplicationId: Optional[str] = Field(default=None)
    ExceptionMessage: Optional[str] = Field(default=None)
    ProvisionUrl: Optional[str] = Field(default=None)


class Microsoft365SubscriptionTestResult(Schema):
    ExceptionMessage: Optional[str] = Field(default=None)
    Fqdn: Optional[str] = Field(default=None)
    IsSubscriptionAvailable: Optional[bool] = Field(default=None)


class Microsoft365TeamsIntegration(Schema):
    AreaCode: Optional[str] = Field(default=None)
    DialPlanCode: Optional[str] = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    Id: int = Field(default=None)
    IsDynamicIP: Optional[bool] = Field(default=None)
    IsNativeFQDN: Optional[bool] = Field(default=None)
    SbcCertificate: ConcealedDataFile = Field(default=None)
    SbcCertificateExpirationDate: Optional[str] = Field(default=None)
    SbcFQDN: Optional[str] = Field(default=None)
    SbcPrivateKey: ConcealedDataFile = Field(default=None)
    SecureSipEnabled: Optional[bool] = Field(default=None)
    SipDomain: Optional[str] = Field(default=None)
    TlsPortForNativeFQDN: Optional[int] = Field(default=None)
    TlsPortForNonNativeFQDN: Optional[int] = Field(default=None)


class MonitoringState(Schema):
    DN: str = Field(default=None)
    Expiration: int = Field(default=None)


class MusicOnHoldSettings(Schema):
    Id: int = Field(default=None)
    MusicOnHold: Optional[str] = Field(default=None)
    MusicOnHold1: Optional[str] = Field(default=None)
    MusicOnHold2: Optional[str] = Field(default=None)
    MusicOnHold3: Optional[str] = Field(default=None)
    MusicOnHold4: Optional[str] = Field(default=None)
    MusicOnHold5: Optional[str] = Field(default=None)
    MusicOnHold6: Optional[str] = Field(default=None)
    MusicOnHold7: Optional[str] = Field(default=None)
    MusicOnHold8: Optional[str] = Field(default=None)
    MusicOnHold9: Optional[str] = Field(default=None)
    MusicOnHoldRandomize: Optional[bool] = Field(default=None)
    MusicOnHoldRandomizePerCall: Optional[bool] = Field(default=None)


class NetworkInterface(Schema):
    Id: str = Field(default=None)


class NetworkInterfaceCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[NetworkInterface]] = Field(default=None)


class NetworkSettings(Schema):
    AllowSourceAsOutbound: Optional[bool] = Field(default=None)
    DirectSIPAllowExternal: Optional[bool] = Field(default=None)
    DirectSIPLocalDomain: Optional[str] = Field(default=None)
    FirewallKeepAlive: Optional[bool] = Field(default=None)
    FirewallKeepAliveInterval: Optional[int] = Field(default=None)
    Id: str = Field(default=None)
    IpV6BindingEnabled: Optional[bool] = Field(default=None)
    PbxPublicFQDN: Optional[str] = Field(default=None)
    PublicInterface: Optional[str] = Field(default=None)
    PublicStaticIP: Optional[str] = Field(default=None)
    SipPort: Optional[int] = Field(default=None)
    StunDisabled: Optional[bool] = Field(default=None)
    StunPrimaryHost: Optional[str] = Field(default=None)
    StunPrimaryPort: Optional[int] = Field(default=None)
    StunQuery: Optional[int] = Field(default=None)
    StunSecondaryHost: Optional[str] = Field(default=None)
    StunSecondaryPort: Optional[int] = Field(default=None)
    StunThirdHost: Optional[str] = Field(default=None)
    StunThirdPort: Optional[int] = Field(default=None)
    TunnelPort: Optional[int] = Field(default=None)


class NotificationSettings(Schema):
    CanEditEmailAddresses: Optional[bool] = Field(default=None)
    CanEditMailServerType: Optional[bool] = Field(default=None)
    EmailAddresses: Optional[str] = Field(default=None)
    FakeId: str = Field(default=None)
    MailAddress: Optional[str] = Field(default=None)
    MailPassword: ConcealedPassword = Field(default=None)
    MailServer: Optional[str] = Field(default=None)
    mail_server_type: MailServerType = Field(default=None, alias="MailServerType")
    MailSslEnabled: Optional[bool] = Field(default=None)
    MailUser: Optional[str] = Field(default=None)
    NotifyCallDenied: Optional[bool] = Field(default=None)
    NotifyEmergencyNumberDialed: Optional[bool] = Field(default=None)
    NotifyExtensionAdded: Optional[bool] = Field(default=None)
    NotifyIPBlocked: Optional[bool] = Field(default=None)
    NotifyLicenseLimit: Optional[bool] = Field(default=None)
    NotifyNetworkError: Optional[bool] = Field(default=None)
    NotifyRequestAntiHacked: Optional[bool] = Field(default=None)
    NotifyServiceStopped: Optional[bool] = Field(default=None)
    NotifyStorageLimit: Optional[bool] = Field(default=None)
    NotifySTUNError: Optional[bool] = Field(default=None)
    NotifySuccessScheduledBackups: Optional[bool] = Field(default=None)
    NotifySystemOwners: Optional[bool] = Field(default=None)
    NotifyTrunkError: Optional[bool] = Field(default=None)
    NotifyTrunkFailover: Optional[bool] = Field(default=None)
    NotifyTrunkStatusChanged: Optional[bool] = Field(default=None)
    NotifyUpdatesAvailable: Optional[bool] = Field(default=None)
    NotifyWhenRecordingsQuotaReached: Optional[bool] = Field(default=None)
    NotifyWhenVoicemailQuotaReached: Optional[bool] = Field(default=None)
    RecordingsQuotaPercentage: Optional[int] = Field(default=None)
    VoicemailQuotaPercentage: Optional[int] = Field(default=None)


class ErrorDetails(Schema):
    code: str = Field(...)
    message: str = Field(...)
    target: Optional[str] = Field(default=None)


class InnerError(Schema):
    pass


class MainError(Schema):
    code: str = Field(...)
    details: Optional[list[ErrorDetails]] = Field(default=None)
    innerError: InnerError = Field(default=None)
    message: str = Field(...)
    target: Optional[str] = Field(default=None)


class ODataError(Schema):
    error: MainError = Field(...)


class OauthState(Schema):
    CodeChallenge: Optional[str] = Field(default=None)
    State: Optional[str] = Field(default=None)


class OauthStateParam(Schema):
    PKCECodeVerifier: Optional[str] = Field(default=None)
    RedirectUri: str = Field(default=None)
    variable: str = Field(default=None, alias="Variable")


class OnBoardMcuDataDetail(Schema):
    Active: bool = Field(default=None)
    Cloud: bool = Field(default=None)
    Enabled: bool = Field(default=None)
    Guid: str = Field(default=None)
    Host: str = Field(default=None)
    Ip: str = Field(default=None)
    Port: int = Field(default=None)
    Version: str = Field(default=None)


class OnBoardMcuData(Schema):
    Attempts: int = Field(default=None)
    AttendeeCount: int = Field(default=None)
    ClockSkew: int = Field(default=None)
    Connected: bool = Field(default=None)
    Cpu: int = Field(default=None)
    Delay: int = Field(default=None)
    Fqdn: str = Field(default=None)
    FreeDiskSpace: int = Field(default=None)
    Mcu: OnBoardMcuDataDetail = Field(default=None)
    MeetingCount: int = Field(default=None)
    Memory: int = Field(default=None)
    NetIn: int = Field(default=None)
    NetOut: int = Field(default=None)
    RestartTime: str = Field(default=None)
    StartTime: str = Field(default=None)
    Ts: str = Field(default=None)
    UpdateInterval: int = Field(default=None)


class OnBoardMcuRow(Schema):
    Active: bool = Field(default=None)
    BandCap: int = Field(default=None)
    CityName: str = Field(default=None)
    Cloud: bool = Field(default=None)
    country: str = Field(default=None, alias="Country")
    CountryName: str = Field(default=None)
    Enabled: bool = Field(default=None)
    Guid: str = Field(default=None)
    Host: str = Field(default=None)
    InstallScript: str = Field(default=None)
    Ip: str = Field(default=None)
    Latitude: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    Longitude: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    ManualGeo: bool = Field(default=None)
    PartsCap: int = Field(default=None)
    Port: int = Field(default=None)
    Secret: str = Field(default=None)
    ServerOS: OnBoardMcuServerOS = Field(default=None)
    ServerStatus: int = Field(default=None)
    TsActivated: str = Field(default=None)
    TsCreated: str = Field(default=None)
    Version: str = Field(default=None)
    Zone: str = Field(default=None)


class OutboundCall(Schema):
    Answered: bool = Field(default=None)
    CallCost: Optional[int] = Field(default=None)
    CallDuration: str = Field(default=None)
    CallHistoryId: Optional[str] = Field(default=None)
    CdrId: str = Field(default=None)
    DestinationCalleeId: Optional[str] = Field(default=None)
    DestinationDisplayName: Optional[str] = Field(default=None)
    DestinationDn: Optional[str] = Field(default=None)
    quality_report: Optional[bool] = Field(default=None, alias="QualityReport")
    RecordingId: Optional[int] = Field(default=None)
    RecordingUrl: Optional[str] = Field(default=None)
    RingingDuration: str = Field(default=None)
    RuleName: Optional[str] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)
    SourceCallerId: Optional[str] = Field(default=None)
    SourceDisplayName: Optional[str] = Field(default=None)
    SourceDn: Optional[str] = Field(default=None)
    StartTime: str = Field(default=None)
    Status: Optional[str] = Field(default=None)
    Summary: Optional[str] = Field(default=None)
    TalkingDuration: str = Field(default=None)
    Transcription: Optional[str] = Field(default=None)
    TrunkName: Optional[str] = Field(default=None)
    TrunkNumber: Optional[str] = Field(default=None)


class OutboundCallCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[OutboundCall]] = Field(default=None)


class OutboundRoute(Schema):
    Append: Optional[str] = Field(default=None)
    CallerID: Optional[str] = Field(default=None)
    Prepend: Optional[str] = Field(default=None)
    StripDigits: Optional[int] = Field(default=None)
    TrunkId: Optional[int] = Field(default=None)
    TrunkName: Optional[str] = Field(default=None)


class OutboundRouteCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[OutboundRoute]] = Field(default=None)


class OutboundRule(Schema):
    DNRanges: Optional[list[DNRange]] = Field(default=None)
    EmergencyRule: Optional[bool] = Field(default=None)
    GroupIds: Optional[list[int]] = Field(default=None)
    GroupNames: Optional[list[Optional[str]]] = Field(default=None)
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    NumberLengthRanges: Optional[str] = Field(default=None)
    Prefix: Optional[str] = Field(default=None)
    Priority: Optional[int] = Field(default=None)
    Routes: Optional[list[OutboundRoute]] = Field(default=None)


class OutboundRuleCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[OutboundRule]] = Field(default=None)


class Parameter(Schema):
    Description: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Value: Optional[str] = Field(default=None)


class ParameterCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Parameter]] = Field(default=None)


class ParticipantDetails(Schema):
    email: str = Field(default=None)
    key: str = Field(default=None)
    moderator: Optional[int] = Field(default=None)
    name: str = Field(default=None)
    pbx_extension: Optional[str] = Field(default=None)


class MeetingObj(Schema):
    documentlist: Optional[str] = Field(default=None)
    friendlyname: Optional[str] = Field(default=None)
    logo: str = Field(default=None)
    meetingid: str = Field(default=None)
    meetingprofile: Optional[str] = Field(default=None)
    openlink: str = Field(default=None)
    organizer: ParticipantDetails = Field(default=None)
    params: MeetingParams = Field(default=None)
    participants: Optional[list[ParticipantDetails]] = Field(default=None)
    theme: str = Field(default=None)


class OnBoardMeeting(Schema):
    McuFqdn: str = Field(default=None)
    Meeting: MeetingObj = Field(default=None)
    MeetingId: str = Field(default=None)
    Parts: Optional[list[KeyValuePair_2OfString_OnBoardConnectedParticipant]] = Field(default=None)
    Profile: str = Field(default=None)
    Recorded: bool = Field(default=None)
    Sessionid: str = Field(default=None)
    Start: str = Field(default=None)


class ParticipantDetailsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ParticipantDetails]] = Field(default=None)


class PbxToM365Binding(Schema):
    From: SynchronizedPbxProfile = Field(default=None)
    To: SynchronizedM365Profile = Field(default=None)


class PbxToM365BindingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PbxToM365Binding]] = Field(default=None)


class PeerGroup(Schema):
    GroupID: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    RoleName: Optional[str] = Field(default=None)


class Peer(Schema):
    Hidden: Optional[bool] = Field(default=None)
    Id: int = Field(default=None)
    MemberOf: Optional[list[PeerGroup]] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    Tags: Optional[list[UserTag]] = Field(default=None)
    Type: PeerType = Field(default=None)


class EmergencyNotificationsSettings(Schema):
    ChatRecipients: ChatRecipientsType = Field(default=None)
    EmergencyDNPrompt: Peer = Field(default=None)
    EmergencyPlayPrompt: Optional[str] = Field(default=None)
    SpecifiedList: Optional[str] = Field(default=None)


class PeerCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Peer]] = Field(default=None)


class PeerGroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PeerGroup]] = Field(default=None)


class Period(Schema):
    day_of_week: DayOfWeek = Field(default=None, alias="DayOfWeek")
    Start: Optional[str] = Field(default=None)
    Stop: Optional[str] = Field(default=None)


class PeriodCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Period]] = Field(default=None)


class PhoneBookSettings(Schema):
    PhoneBookAddQueueName: TypeOfPhoneBookAddQueueName = Field(default=None)
    PhoneBookDisplay: TypeOfPhoneBookDisplay = Field(default=None)
    ResolvingLength: Optional[int] = Field(default=None)
    ResolvingType: TypeOfPhoneBookResolving = Field(default=None)


class PhoneDeviceVlanInfo(Schema):
    Configurable: Optional[bool] = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    Priority: Optional[int] = Field(default=None)
    PriorityConfigurable: Optional[bool] = Field(default=None)
    PriorityMax: Optional[int] = Field(default=None)
    PriorityMin: Optional[int] = Field(default=None)
    Type: PhoneDeviceVlanType = Field(default=None)
    VlanId: Optional[int] = Field(default=None)
    VlanIdMax: Optional[int] = Field(default=None)
    VlanIdMin: Optional[int] = Field(default=None)


class PhoneDeviceVlanInfoCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PhoneDeviceVlanInfo]] = Field(default=None)


class PhoneLldpInfo(Schema):
    Configurable: Optional[bool] = Field(default=None)
    Value: Optional[bool] = Field(default=None)


class PhoneLogo(Schema):
    DisplayName: Optional[str] = Field(default=None)
    Filename: str = Field(default=None)


class PhoneLogoCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PhoneLogo]] = Field(default=None)


class PhoneModel(Schema):
    AddAllowed: Optional[bool] = Field(default=None)
    CanBeSBC: Optional[bool] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    URL: Optional[str] = Field(default=None)
    UserAgent: Optional[str] = Field(default=None)


class PhoneModelCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PhoneModel]] = Field(default=None)


class PhoneRegistrar(Schema):
    Capabilities: Optional[int] = Field(default=None)
    FirmwareAvailable: Optional[str] = Field(default=None)
    FirmwareVersion: Optional[str] = Field(default=None)
    InterfaceLink: Optional[str] = Field(default=None)
    IpAddress: Optional[str] = Field(default=None)
    MAC: Optional[str] = Field(default=None)
    Model: Optional[str] = Field(default=None)
    UserAgent: Optional[str] = Field(default=None)
    Vendor: Optional[str] = Field(default=None)


class PhoneSettings(Schema):
    AllowCustomQueueRingtones: Optional[bool] = Field(default=None)
    Backlight: Optional[str] = Field(default=None)
    Codecs: Optional[list[Optional[str]]] = Field(default=None)
    CustomLogo: Optional[str] = Field(default=None)
    CustomQueueRingtones: Optional[list[CustomQueueRingtone]] = Field(default=None)
    DateFormat: Optional[str] = Field(default=None)
    firmware: Optional[str] = Field(default=None, alias="Firmware")
    FirmwareLang: Optional[str] = Field(default=None)
    IsLogoCustomizable: Optional[bool] = Field(default=None)
    IsSBC: Optional[bool] = Field(default=None)
    LlDpInfo: PhoneLldpInfo = Field(default=None)
    LocalRTPPortEnd: Optional[int] = Field(default=None)
    LocalRTPPortStart: Optional[int] = Field(default=None)
    LocalSipPort: Optional[int] = Field(default=None)
    LogoDescription: Optional[str] = Field(default=None)
    LogoFileExtensionAllowed: Optional[list[Optional[str]]] = Field(default=None)
    OwnBlfs: Optional[bool] = Field(default=None)
    PhoneLanguage: Optional[str] = Field(default=None)
    PowerLed: Optional[str] = Field(default=None)
    ProvisionExtendedData: Optional[str] = Field(default=None)
    ProvisionType: ProvType = Field(default=None)
    QueueRingTone: Optional[str] = Field(default=None)
    RemoteSpmHost: Optional[str] = Field(default=None)
    RemoteSpmPort: Optional[int] = Field(default=None)
    RingTone: Optional[str] = Field(default=None)
    SbcName: Optional[str] = Field(default=None)
    ScreenSaver: Optional[str] = Field(default=None)
    Secret: Optional[str] = Field(default=None)
    Srtp: Optional[str] = Field(default=None)
    TimeFormat: Optional[str] = Field(default=None)
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")
    VlanInfos: Optional[list[PhoneDeviceVlanInfo]] = Field(default=None)
    XferType: XferTypeEnum = Field(default=None)


class Phone(Schema):
    Id: int = Field(default=None)
    Interface: Optional[str] = Field(default=None)
    MacAddress: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    ProvisioningLinkExt: Optional[str] = Field(default=None)
    ProvisioningLinkLocal: Optional[str] = Field(default=None)
    Settings: PhoneSettings = Field(default=None)
    TemplateName: Optional[str] = Field(default=None)


class PhoneCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Phone]] = Field(default=None)


class PhoneTemplate(Schema):
    AddAllowed: Optional[bool] = Field(default=None)
    AllowedNetConfigs: Optional[list[Optional[str]]] = Field(default=None)
    AllowSSLProvisioning: Optional[bool] = Field(default=None)
    BacklightTimeouts: Optional[list[Optional[str]]] = Field(default=None)
    Codecs: Optional[list[Optional[str]]] = Field(default=None)
    Content: Optional[str] = Field(default=None)
    DateFormats: Optional[list[Optional[str]]] = Field(default=None)
    DefaultQueueRingTone: Optional[str] = Field(default=None)
    HotdeskingAllowed: Optional[bool] = Field(default=None)
    Id: str = Field(default=None)
    IsCustom: Optional[bool] = Field(default=None)
    Languages: Optional[list[Optional[str]]] = Field(default=None)
    MaxQueueCustomRingtones: Optional[int] = Field(default=None)
    Models: Optional[list[PhoneModel]] = Field(default=None)
    PowerLedSettings: Optional[list[Optional[str]]] = Field(default=None)
    QueueRingTones: Optional[list[Optional[str]]] = Field(default=None)
    RingTones: Optional[list[Optional[str]]] = Field(default=None)
    RpsEnabled: Optional[bool] = Field(default=None)
    ScreenSaverTimeouts: Optional[list[Optional[str]]] = Field(default=None)
    template_type: TemplateType = Field(default=None, alias="TemplateType")
    TimeFormats: Optional[list[Optional[str]]] = Field(default=None)
    TimeZones: Optional[list[Optional[str]]] = Field(default=None)
    URL: Optional[str] = Field(default=None)
    XferTypeEnabled: Optional[bool] = Field(default=None)


class PhoneTemplateCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PhoneTemplate]] = Field(default=None)


class PhonesSettings(Schema):
    AllowMultiQueueRingtones: Optional[bool] = Field(default=None)
    AutoCleanupFirmware: Optional[bool] = Field(default=None)
    CustomDNDProfile: Optional[str] = Field(default=None)
    FanvilUpdateInterval: Optional[int] = Field(default=None)
    GrandstreamUpdateInterval: Optional[int] = Field(default=None)
    PhoneAllowMultiFirmwares: Optional[bool] = Field(default=None)
    SnomUpdateInterval: Optional[int] = Field(default=None)
    UseProvisioningSecret: Optional[bool] = Field(default=None)
    UseRpcForLocalPhones: Optional[bool] = Field(default=None)
    YealinkUpdateInterval: Optional[int] = Field(default=None)


class Playlist(Schema):
    AutoGain: Optional[bool] = Field(default=None)
    Files: Optional[list[Optional[str]]] = Field(default=None)
    MaxVolumePercent: Optional[int] = Field(default=None)
    Name: str = Field(default=None)
    PromptName: Optional[str] = Field(default=None)
    RepositoryPath: Optional[str] = Field(default=None)
    Shuffle: Optional[bool] = Field(default=None)


class PlaylistCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Playlist]] = Field(default=None)


class Prompt(Schema):
    Filename: Optional[str] = Field(default=None)
    Id: str = Field(default=None)
    Transcription: Optional[str] = Field(default=None)


class PromptCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Prompt]] = Field(default=None)


class PromptSet(Schema):
    CultureCode: Optional[str] = Field(default=None)
    Description: Optional[str] = Field(default=None)
    Folder: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    LanguageCode: Optional[str] = Field(default=None)
    Prompts: Optional[list[Prompt]] = Field(default=None)
    PromptSetName: Optional[str] = Field(default=None)
    prompt_set_type: PromptSetType = Field(default=None, alias="PromptSetType")
    UseAlternateNumberPronunciation: Optional[bool] = Field(default=None)
    Version: Optional[str] = Field(default=None)


class PromptSetCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[PromptSet]] = Field(default=None)


class Property(Schema):
    Description: Optional[str] = Field(default=None)
    Name: str = Field(default=None)
    Value: str = Field(default=None)


class PropertyCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Property]] = Field(default=None)


class PurgeSettings(Schema):
    All: bool = Field(default=None)
    Start: Optional[str] = Field(default=None)
    Stop: Optional[str] = Field(default=None)


class QualityParty(Schema):
    AddressStr: Optional[str] = Field(default=None)
    Burst: Optional[int] = Field(default=None)
    codec: Optional[str] = Field(default=None, alias="Codec")
    Duration: Optional[int] = Field(default=None)
    GlobalPort: Optional[int] = Field(default=None)
    Inbound: Optional[bool] = Field(default=None)
    LocalPort: Optional[int] = Field(default=None)
    Location: Optional[str] = Field(default=None)
    MOSFromPBX: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    MOSToPBX: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    Number: Optional[str] = Field(default=None)
    RTT: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    RxJitter: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    RxLost: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    RxPackets: Optional[int] = Field(default=None)
    TunAddressStr: Optional[str] = Field(default=None)
    TxBursts: Optional[int] = Field(default=None)
    TxJitter: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    TxLost: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    TxPackets: Optional[int] = Field(default=None)
    UserAgent: Optional[str] = Field(default=None)


class QualityReport(Schema):
    MOS: Optional[float] | Optional[str] | ReferenceNumeric = Field(default=None)
    OverallScore: Optional[int] = Field(default=None)
    Party1: QualityParty = Field(default=None)
    Party2: QualityParty = Field(default=None)
    Reason: Optional[str] = Field(default=None)
    Summary: Optional[int] = Field(default=None)
    Transcoding: Optional[bool] = Field(default=None)


class QueueAgent(Schema):
    Id: Optional[int] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: str = Field(default=None)
    SkillGroup: Optional[str] = Field(default=None)


class QueueAgentCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueAgent]] = Field(default=None)


class QueueAgentsChatStatistics(Schema):
    AnsweredCount: Optional[int] = Field(default=None)
    DealtWithCount: Optional[int] = Field(default=None)
    Dn: str = Field(default=None)
    DnDisplayName: Optional[str] = Field(default=None)
    queue: str = Field(default=None, alias="Queue")
    QueueDisplayName: Optional[str] = Field(default=None)
    SortOrder: Optional[int] = Field(default=None)


class QueueAgentsChatStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueAgentsChatStatistics]] = Field(default=None)


class QueueAgentsChatStatisticsTotals(Schema):
    AnsweredCount: Optional[int] = Field(default=None)
    DealtWithCount: Optional[int] = Field(default=None)
    queue: str = Field(default=None, alias="Queue")
    QueueDisplayName: Optional[str] = Field(default=None)


class QueueAgentsChatStatisticsTotalsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueAgentsChatStatisticsTotals]] = Field(default=None)


class QueueAnsweredCallsByWaitTime(Schema):
    AnsweredTime: str = Field(default=None)
    CallTime: str = Field(default=None)
    destination: str = Field(default=None, alias="Destination")
    Dn: str = Field(default=None)
    DnNumber: Optional[str] = Field(default=None)
    RingTime: Optional[str] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)
    Source: str = Field(default=None)


class QueueAnsweredCallsByWaitTimeCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueAnsweredCallsByWaitTime]] = Field(default=None)


class QueueCallbacks(Schema):
    CallbacksCount: Optional[int] = Field(default=None)
    Dn: Optional[str] = Field(default=None)
    FailCallbacksCount: Optional[int] = Field(default=None)
    QueueDnNumber: str = Field(default=None)
    ReceivedCount: Optional[int] = Field(default=None)


class QueueCallbacksCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueCallbacks]] = Field(default=None)


class QueueChatPerformance(Schema):
    AbandonedCount: Optional[int] = Field(default=None)
    AnsweredCount: Optional[int] = Field(default=None)
    IncomingCount: Optional[int] = Field(default=None)
    QuantityAgents: Optional[int] = Field(default=None)
    queue: str = Field(default=None, alias="Queue")
    QueueDisplayName: Optional[str] = Field(default=None)


class QueueChatPerformanceCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueChatPerformance]] = Field(default=None)


class QueueFailedCallbacks(Schema):
    CallbackNo: str = Field(default=None)
    CallTime: str = Field(default=None)
    Dn: str = Field(default=None)
    QueueDnNumber: Optional[str] = Field(default=None)
    RingTime: Optional[str] = Field(default=None)


class QueueFailedCallbacksCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueFailedCallbacks]] = Field(default=None)


class QueueManager(Schema):
    Id: Optional[int] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: str = Field(default=None)


class QueueManagerCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueueManager]] = Field(default=None)


class QueuePerformanceOverview(Schema):
    ExtensionAnsweredCount: Optional[int] = Field(default=None)
    ExtensionDisplayName: Optional[str] = Field(default=None)
    ExtensionDn: str = Field(default=None)
    ExtensionDroppedCount: Optional[int] = Field(default=None)
    QueueAnsweredCount: Optional[int] = Field(default=None)
    QueueDisplayName: str = Field(default=None)
    QueueDn: Optional[str] = Field(default=None)
    QueueReceivedCount: Optional[int] = Field(default=None)
    SortOrder: Optional[int] = Field(default=None)
    TalkTime: Optional[str] = Field(default=None)


class QueuePerformanceOverviewCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueuePerformanceOverview]] = Field(default=None)


class QueuePerformanceTotals(Schema):
    ExtensionAnsweredCount: Optional[int] = Field(default=None)
    ExtensionDroppedCount: Optional[int] = Field(default=None)
    QueueDisplayName: Optional[str] = Field(default=None)
    QueueDn: str = Field(default=None)
    QueueReceivedCount: Optional[int] = Field(default=None)


class QueuePerformanceTotalsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[QueuePerformanceTotals]] = Field(default=None)


class ReceptionistForward(Schema):
    CustomData: Optional[str] = Field(default=None)
    ForwardDN: Optional[str] = Field(default=None)
    ForwardType: IVRForwardType = Field(default=None)
    Id: int = Field(default=None)
    Input: Optional[str] = Field(default=None)
    peer_type: PeerType = Field(default=None, alias="PeerType")


class ReceptionistForwardCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ReceptionistForward]] = Field(default=None)


class Recording(Schema):
    ArchivedUrl: Optional[str] = Field(default=None)
    CallType: RecordingCallType = Field(default=None)
    EndTime: Optional[str] = Field(default=None)
    FromCallerNumber: Optional[str] = Field(default=None)
    FromCrmContact: Optional[str] = Field(default=None)
    FromDidNumber: Optional[str] = Field(default=None)
    FromDisplayName: Optional[str] = Field(default=None)
    FromDn: Optional[str] = Field(default=None)
    FromDnType: Optional[int] = Field(default=None)
    FromIdParticipant: Optional[int] = Field(default=None)
    Id: int = Field(default=None)
    IsArchived: Optional[bool] = Field(default=None)
    RecordingUrl: Optional[str] = Field(default=None)
    RefParticipantId: Optional[int] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)
    StartTime: Optional[str] = Field(default=None)
    Summary: Optional[str] = Field(default=None)
    ToCallerNumber: Optional[str] = Field(default=None)
    ToCrmContact: Optional[str] = Field(default=None)
    ToDidNumber: Optional[str] = Field(default=None)
    ToDisplayName: Optional[str] = Field(default=None)
    ToDn: Optional[str] = Field(default=None)
    ToDnType: Optional[int] = Field(default=None)
    ToIdParticipant: Optional[int] = Field(default=None)
    Transcription: Optional[str] = Field(default=None)


class RecordingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Recording]] = Field(default=None)


class RecordingRepositorySettings(Schema):
    AutoDeleteRecordingDays: Optional[int] = Field(default=None)
    AutoDeleteRecordingEnabled: Optional[bool] = Field(default=None)
    IsRecordingArchiveEnabled: Optional[bool] = Field(default=None)
    RecordingDiskSpace: Optional[int] = Field(default=None)
    RecordingPath: Optional[str] = Field(default=None)
    RecordingsQuota: Optional[int] = Field(default=None)
    RecordingUsedSpace: Optional[int] = Field(default=None)


class ReferenceCreate(Schema):
    id: str = Field(default=None, alias="@odata.id")


class ReferenceUpdate(Schema):
    id: str = Field(default=None, alias="@odata.id")
    type: Optional[str] = Field(default=None, alias="@odata.type")


class RefreshToken(Schema):
    Created: str = Field(default=None)
    CreatedByIp: str = Field(default=None)
    CreatedByUserAgent: str = Field(default=None)
    DisplayName: Optional[str] = Field(default=None)
    Expires: str = Field(default=None)
    Id: int = Field(default=None)
    login_type: LoginType = Field(default=None, alias="LoginType")
    ReasonRevoked: RevokeReason = Field(default=None)
    Revoked: Optional[str] = Field(default=None)
    RevokedByIp: Optional[str] = Field(default=None)
    SlidingExpiration: bool = Field(default=None)
    Token: str = Field(default=None)
    Used: str = Field(default=None)
    UsedByIp: str = Field(default=None)
    UsedByUserAgent: str = Field(default=None)
    Username: str = Field(default=None)


class RefreshTokenCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[RefreshToken]] = Field(default=None)


class RegenerateOptions(Schema):
    ConfigurationLink: bool = Field(default=None)
    DeskphonePassword: bool = Field(default=None)
    RpsKey: bool = Field(default=None)
    SendWelcomeEmail: bool = Field(default=None)
    SipAuth: bool = Field(default=None)
    VoicemailPIN: bool = Field(default=None)
    WebclientPassword: bool = Field(default=None)


class RegenerateRequestBody(Schema):
    opts: RegenerateOptions = Field(default=None)


class RegistrarFxs(Schema):
    InterfaceLink: str = Field(default=None)
    MacAddress: str = Field(default=None)


class RegistrarFxsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[RegistrarFxs]] = Field(default=None)


class RemoteArchivingSettings(Schema):
    backups: ArchiveSubsystem = Field(default=None, alias="Backups")
    Chats: ArchiveSubsystem = Field(default=None)
    Faxes: ArchiveSubsystem = Field(default=None)
    Id: int = Field(default=None)
    Location: LocationSettings = Field(default=None)
    Recordings: ArchiveSubsystem = Field(default=None)
    Voicemails: ArchiveSubsystem = Field(default=None)


class RemotePostgreConfig(Schema):
    authenticate_mode: AuthenticateMode = Field(default=None, alias="AuthenticateMode")
    CACertificate: ConcealedDataFile = Field(default=None)
    ClientCertificate: ConcealedDataFile = Field(default=None)
    Database: Optional[str] = Field(default=None)
    Host: Optional[str] = Field(default=None)
    Password: ConcealedPassword = Field(default=None)
    Port: Optional[int] = Field(default=None)
    server_trust_mode: ServerTrustMode = Field(default=None, alias="ServerTrustMode")
    Username: Optional[str] = Field(default=None)


class DataConnectorSettings(Schema):
    IsBigQueryEnabled: Optional[bool] = Field(default=None)
    offload_destination: OffloadDestination = Field(default=None, alias="OffloadDestination")
    PurgeAfterSync: Optional[bool] = Field(default=None)
    remote_postgre_config: RemotePostgreConfig = Field(default=None, alias="RemotePostgreConfig")
    schedule: BackupSchedule = Field(default=None, alias="Schedule")


class ReplaceMyGroupLicenseKeyRequestBody(Schema):
    licenseKey: str = Field(default=None)


class ReportExtensionStatisticsByGroup(Schema):
    DisplayName: Optional[str] = Field(default=None)
    Dn: str = Field(default=None)
    InboundAnsweredCount: Optional[int] = Field(default=None)
    InboundAnsweredTalkingDur: Optional[str] = Field(default=None)
    InboundUnansweredCount: Optional[int] = Field(default=None)
    OutboundAnsweredCount: Optional[int] = Field(default=None)
    OutboundAnsweredTalkingDur: Optional[str] = Field(default=None)
    OutboundUnansweredCount: Optional[int] = Field(default=None)
    SentimentScore: Optional[int] = Field(default=None)


class ReportExtensionStatisticsByGroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ReportExtensionStatisticsByGroup]] = Field(default=None)


class RequestHelp(Schema):
    GrantPeriodDays: Optional[int] = Field(default=None)
    IssueDescription: str = Field(default=None)
    Name: str = Field(default=None)
    PhoneNumber: Optional[str] = Field(default=None)
    ReplyEmail: str = Field(default=None)


class ResellerInfo(Schema):
    Id: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)


class ResetQueueStatisticsSchedule(Schema):
    Day: DayOfWeek = Field(default=None)
    Frequency: ResetQueueStatisticsFrequency = Field(default=None)
    Time: Optional[str] = Field(default=None)


class RestoreSettings(Schema):
    EncryptBackup: Optional[bool] = Field(default=None)
    EncryptBackupPassword: ConcealedPassword = Field(default=None)
    schedule: BackupSchedule = Field(default=None, alias="Schedule")
    ScheduleEnabled: Optional[bool] = Field(default=None)


class Restrictions(Schema):
    Dects: EntityRestrictions = Field(default=None)
    LiveChats: EntityRestrictions = Field(default=None)
    MaxPrompts: Optional[int] = Field(default=None)
    Sbcs: EntityRestrictions = Field(default=None)
    System: EntityRestrictions = Field(default=None)
    Trunks: EntityRestrictions = Field(default=None)
    Users: EntityRestrictions = Field(default=None)


class RetreivePeersRequest(Schema):
    DnNumbers: Optional[list[Optional[str]]] = Field(default=None)
    IsReportPeers: bool = Field(default=None)


class Rights(Schema):
    AllowIVR: Optional[bool] = Field(default=None)
    AllowParking: Optional[bool] = Field(default=None)
    AllowToChangePresence: Optional[bool] = Field(default=None)
    AllowToManageCompanyBook: Optional[bool] = Field(default=None)
    AssignClearOperations: Optional[bool] = Field(default=None)
    CanBargeIn: Optional[bool] = Field(default=None)
    CanIntercom: Optional[bool] = Field(default=None)
    CanSeeGroupCalls: Optional[bool] = Field(default=None)
    CanSeeGroupMembers: Optional[bool] = Field(default=None)
    CanSeeGroupRecordings: Optional[bool] = Field(default=None)
    Invalid: Optional[bool] = Field(default=None)
    PerformOperations: Optional[bool] = Field(default=None)
    RoleName: str = Field(default=None)
    ShowMyCalls: Optional[bool] = Field(default=None)
    ShowMyPresence: Optional[bool] = Field(default=None)
    ShowMyPresenceOutside: Optional[bool] = Field(default=None)


class RightsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Rights]] = Field(default=None)


class RingGroupMember(Schema):
    Id: int = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)


class RingGroupMemberCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[RingGroupMember]] = Field(default=None)


class RingGroupStatistics(Schema):
    RingGroupAnsweredCount: Optional[int] = Field(default=None)
    RingGroupDisplayName: Optional[str] = Field(default=None)
    RingGroupDn: str = Field(default=None)
    RingGroupReceivedCount: Optional[int] = Field(default=None)
    RingGroupSentimentScore: Optional[int] = Field(default=None)


class RingGroupStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[RingGroupStatistics]] = Field(default=None)


class Route(Schema):
    IsPromptEnabled: Optional[bool] = Field(default=None)
    prompt: Optional[str] = Field(default=None, alias="Prompt")
    route: Destination = Field(default=None, alias="Route")


class Sbc(Schema):
    DisplayName: str = Field(default=None)
    group: Optional[str] = Field(default=None, alias="Group")
    HasConnection: Optional[bool] = Field(default=None)
    LocalIPv4: Optional[str] = Field(default=None)
    Name: str = Field(default=None)
    Password: str = Field(default=None)
    PhoneMAC: Optional[str] = Field(default=None)
    PhoneUserId: Optional[int] = Field(default=None)
    ProvisionLink: Optional[str] = Field(default=None)
    PublicIP: Optional[str] = Field(default=None)
    Version: Optional[str] = Field(default=None)


class SbcCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Sbc]] = Field(default=None)


class Schedule(Schema):
    IgnoreHolidays: Optional[bool] = Field(default=None)
    Periods: Optional[list[Period]] = Field(default=None)
    Type: RuleHoursType = Field(default=None)


class ExtensionRule(Schema):
    CallerId: Optional[str] = Field(default=None)
    destination: Destination = Field(default=None, alias="Destination")
    Hours: Schedule = Field(default=None)
    Id: int = Field(default=None)


class ExtensionRuleCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ExtensionRule]] = Field(default=None)


class InboundRule(Schema):
    AlterDestinationDuringHolidays: Optional[bool] = Field(default=None)
    AlterDestinationDuringOutOfOfficeHours: Optional[bool] = Field(default=None)
    CallType: RuleCallTypeType = Field(default=None)
    Condition: RuleConditionType = Field(default=None)
    CustomData: Optional[str] = Field(default=None)
    Data: Optional[str] = Field(default=None)
    HolidaysDestination: Destination = Field(default=None)
    Hours: Schedule = Field(default=None)
    Id: int = Field(default=None)
    OfficeHoursDestination: Destination = Field(default=None)
    OutOfOfficeHoursDestination: Destination = Field(default=None)
    RuleName: Optional[str] = Field(default=None)
    TrunkDN: Peer = Field(default=None)


class DidNumber(Schema):
    Number: str = Field(default=None)
    RoutingRule: InboundRule = Field(default=None)
    TemplateFileName: Optional[str] = Field(default=None)
    TrunkId: int = Field(default=None)


class DidNumberCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[DidNumber]] = Field(default=None)


class InboundRuleCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[InboundRule]] = Field(default=None)


class OfficeHours(Schema):
    BreakTime: Schedule = Field(default=None)
    Hours: Schedule = Field(default=None)
    OfficeHolidays: Optional[list[Holiday]] = Field(default=None)
    SystemLanguage: Optional[str] = Field(default=None)
    TimeZoneId: Optional[str] = Field(default=None)


class ScheduledReport(Schema):
    DN: str = Field(default=None)
    EmailAddresses: str = Field(default=None)
    FilterDescription: str = Field(default=None)
    Id: int = Field(default=None)
    Name: str = Field(default=None)
    ReportLink: str = Field(default=None)
    ReportParams: str = Field(default=None)
    ReportType: ScheduledReportType = Field(default=None)
    schedule_type: ReportScheduleType = Field(default=None, alias="ScheduleType")


class ScheduledReportCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ScheduledReport]] = Field(default=None)


class SecureSipSettings(Schema):
    Certificate: ConcealedDataFile = Field(default=None)
    PrivateKey: ConcealedDataFile = Field(default=None)


class ServiceInfo(Schema):
    CpuUsage: Optional[int] = Field(default=None)
    DisplayName: Optional[str] = Field(default=None)
    HandleCount: Optional[int] = Field(default=None)
    MemoryUsed: Optional[int] = Field(default=None)
    Name: str = Field(default=None)
    RestartEnabled: Optional[bool] = Field(default=None)
    StartStopEnabled: Optional[bool] = Field(default=None)
    Status: ServiceStatus = Field(default=None)
    ThreadCount: Optional[int] = Field(default=None)


class ServiceInfoCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ServiceInfo]] = Field(default=None)


class SetMonitorStatusRequestBody(Schema):
    days: int = Field(default=None)


class SetRoute(Schema):
    DID: str = Field(default=None)
    DisplayName: Optional[str] = Field(default=None)
    TrunkId: int = Field(default=None)


class SetRouteCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[SetRoute]] = Field(default=None)


class SetRouteRequest(Schema):
    Id: int = Field(default=None)
    Routes: Optional[list[SetRoute]] = Field(default=None)


class SipDevice(Schema):
    DN: Peer = Field(default=None)
    Id: int = Field(default=None)
    PhoneWebPassword: Optional[str] = Field(default=None)
    ProvLink: Optional[str] = Field(default=None)
    Registrar: PhoneRegistrar = Field(default=None)


class SipDeviceCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[SipDevice]] = Field(default=None)


class StatisticSla(Schema):
    BadSlaCallsCount: Optional[int] = Field(default=None)
    Dn: Optional[str] = Field(default=None)
    QueueDnNumber: str = Field(default=None)
    ReceivedCount: Optional[int] = Field(default=None)


class StatisticSlaCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[StatisticSla]] = Field(default=None)


class StatusSyncConfiguration(Schema):
    M365ToPbxBindings: Optional[list[M365ToPbxBinding]] = Field(default=None)
    PBXToM365Bindings: Optional[list[PbxToM365Binding]] = Field(default=None)
    PBXToM365Busy: Optional[bool] = Field(default=None)


class ADUsersSyncConfiguration(Schema):
    EnableSSO: Optional[bool] = Field(default=None)
    IsEnabled: Optional[bool] = Field(default=None)
    IsSyncDepartments: Optional[bool] = Field(default=None)
    IsSyncDetails: Optional[bool] = Field(default=None)
    IsSyncOfficePhone: Optional[bool] = Field(default=None)
    IsSyncPhoto: Optional[bool] = Field(default=None)
    SelectedUsers: Optional[list[Optional[str]]] = Field(default=None)
    SetTeamsPresence: Optional[bool] = Field(default=None)
    StartingExtensionNumber: str = Field(default=None)
    status_sync_configuration: StatusSyncConfiguration = Field(default=None, alias="StatusSyncConfiguration")
    SyncEvents: Optional[bool] = Field(default=None)
    SyncGuestUsers: Optional[bool] = Field(default=None)
    SyncPersonalContacts: Optional[bool] = Field(default=None)
    SyncType: IntegrationSyncType = Field(default=None)


class StringCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[str]] = Field(default=None)


class SystemDatabaseInformation(Schema):
    CallsUsedSpace: Optional[int] = Field(default=None)
    ChatFilesCount: Optional[int] = Field(default=None)
    ChatsUsedSpace: Optional[int] = Field(default=None)
    EventLogUsedSpace: Optional[int] = Field(default=None)
    Id: Optional[int] = Field(default=None)


class SystemDirectory(Schema):
    Dirs: Optional[list[Optional[str]]] = Field(default=None)
    Path: Optional[str] = Field(default=None)


class SystemExtensionStatus(Schema):
    IsRegistered: Optional[bool] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    Type: Optional[str] = Field(default=None)


class SystemHealthStatus(Schema):
    CustomTemplatesCount: Optional[int] = Field(default=None)
    Firewall: Optional[bool] = Field(default=None)
    Id: Optional[int] = Field(default=None)
    Phones: Optional[bool] = Field(default=None)
    Trunks: Optional[bool] = Field(default=None)
    UnsupportedFirmwaresCount: Optional[int] = Field(default=None)


class SystemParameters(Schema):
    Custom1Name: Optional[str] = Field(default=None)
    Custom2Name: Optional[str] = Field(default=None)
    EmRuleCreationAllowed: Optional[bool] = Field(default=None)
    ENL: Optional[int] = Field(default=None)
    FirstExternalPort: Optional[int] = Field(default=None)
    FQDN: Optional[str] = Field(default=None)
    GlobalACPRMSET: Optional[str] = Field(default=None)
    GlobalLanguage: Optional[str] = Field(default=None)
    HttpPort: Optional[int] = Field(default=None)
    HttpsPort: Optional[int] = Field(default=None)
    IpV6: Optional[str] = Field(default=None)
    Is3CXFQDN: Optional[bool] = Field(default=None)
    IsChatLogEnabled: Optional[bool] = Field(default=None)
    IsHosted: Optional[bool] = Field(default=None)
    IsHosted3CX: Optional[bool] = Field(default=None)
    IsMulticompanyMode: Optional[bool] = Field(default=None)
    IsRemoteBackup: Optional[bool] = Field(default=None)
    IsStaticIp: Optional[bool] = Field(default=None)
    IsTranscriptionEnabled: Optional[bool] = Field(default=None)
    license: License = Field(default=None, alias="License")
    MaxDIDPerTrunk: Optional[int] = Field(default=None)
    PbxExternalHost: Optional[str] = Field(default=None)
    RpsEnabled: Optional[bool] = Field(default=None)
    SipPort: Optional[int] = Field(default=None)
    SipsPort: Optional[int] = Field(default=None)
    StaticIp: Optional[str] = Field(default=None)
    StunIp: Optional[str] = Field(default=None)
    TunnnelPort: Optional[int] = Field(default=None)
    Version: Optional[str] = Field(default=None)
    WebrtcLastPort: Optional[int] = Field(default=None)


class SystemStatus(Schema):
    Activated: Optional[bool] = Field(default=None)
    AutoUpdateEnabled: Optional[bool] = Field(default=None)
    AvailableLocalIps: Optional[str] = Field(default=None)
    BackupScheduled: Optional[bool] = Field(default=None)
    CallsActive: Optional[int] = Field(default=None)
    ChatUsedSpace: Optional[int] = Field(default=None)
    CurrentLocalIp: Optional[str] = Field(default=None)
    DBMaintenanceInProgress: Optional[bool] = Field(default=None)
    DiskUsage: Optional[int] = Field(default=None)
    ExpirationDate: Optional[str] = Field(default=None)
    ExtensionsRegistered: Optional[int] = Field(default=None)
    ExtensionsTotal: Optional[int] = Field(default=None)
    FQDN: Optional[str] = Field(default=None)
    FreeDiskSpace: Optional[int] = Field(default=None)
    HasNotRunningServices: Optional[bool] = Field(default=None)
    HasUnregisteredSystemExtensions: Optional[bool] = Field(default=None)
    Id: int = Field(default=None)
    Ip: Optional[str] = Field(default=None)
    IpV4: Optional[str] = Field(default=None)
    IpV6: Optional[str] = Field(default=None)
    IsAuditLogEnabled: Optional[bool] = Field(default=None)
    IsChatLogEnabled: Optional[bool] = Field(default=None)
    IsRecordingArchiveEnabled: Optional[bool] = Field(default=None)
    LastBackupDateTime: Optional[str] = Field(default=None)
    LastCheckForUpdates: Optional[str] = Field(default=None)
    LastSuccessfulUpdate: Optional[str] = Field(default=None)
    LicenseActive: Optional[bool] = Field(default=None)
    LicenseKey: Optional[str] = Field(default=None)
    LocalIpValid: Optional[bool] = Field(default=None)
    LogUsedSpace: Optional[int] = Field(default=None)
    MaintenanceExpiresAt: Optional[str] = Field(default=None)
    MaxSimCalls: Optional[int] = Field(default=None)
    OS: XOperatingSystemType = Field(default=None)
    OutboundRules: Optional[int] = Field(default=None)
    ProductCode: Optional[str] = Field(default=None)
    RecordingQuota: Optional[int] = Field(default=None)
    RecordingQuotaReached: Optional[bool] = Field(default=None)
    RecordingStopped: Optional[bool] = Field(default=None)
    RecordingUsedSpace: Optional[int] = Field(default=None)
    RemoteConfigurationRequired: Optional[bool] = Field(default=None)
    RemoteStorageEnabled: Optional[bool] = Field(default=None)
    ResellerName: Optional[str] = Field(default=None)
    Support: Optional[bool] = Field(default=None)
    TotalDiskSpace: Optional[int] = Field(default=None)
    TrunksRegistered: Optional[int] = Field(default=None)
    TrunksTotal: Optional[int] = Field(default=None)
    Version: Optional[str] = Field(default=None)
    VoicemailQuotaReached: Optional[bool] = Field(default=None)
    VoicemailStopped: Optional[bool] = Field(default=None)


class TeamQueueGeneralStatistics(Schema):
    AgentsInQueueCount: Optional[int] = Field(default=None)
    AnsweredCount: Optional[int] = Field(default=None)
    AvgTalkTime: Optional[str] = Field(default=None)
    Dn: Optional[str] = Field(default=None)
    QueueDnNumber: str = Field(default=None)
    ReceivedCount: Optional[int] = Field(default=None)
    TotalTalkTime: Optional[str] = Field(default=None)


class TeamQueueGeneralStatisticsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[TeamQueueGeneralStatistics]] = Field(default=None)


class TestCallLog(Schema):
    Entries: Optional[list[LogEntry]] = Field(default=None)


class TestResult(Schema):
    Error: Optional[str] = Field(default=None)
    Parameters: Optional[list[Optional[str]]] = Field(default=None)
    Success: Optional[bool] = Field(default=None)


class TimeReportData(Schema):
    XValue: str = Field(default=None)
    YValue1: Optional[int] = Field(default=None)
    YValue2: Optional[int] = Field(default=None)


class TimeReportDataCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[TimeReportData]] = Field(default=None)


class TimeZone(Schema):
    IanaName: str = Field(default=None)
    Id: str = Field(default=None)
    Name: str = Field(default=None)
    WindowsName: str = Field(default=None)


class Defs(Schema):
    Codecs: Optional[list[Codec]] = Field(default=None)
    GatewayParameters: Optional[list[GatewayParameter]] = Field(default=None)
    GatewayParameterValues: Optional[list[GatewayParameterValue]] = Field(default=None)
    Id: int = Field(default=None)
    TimeZones: Optional[list[TimeZone]] = Field(default=None)


class TimeZoneCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[TimeZone]] = Field(default=None)


class TrunkMessaging(Schema):
    Enabled: Optional[bool] = Field(default=None)
    NumberLength: Optional[int] = Field(default=None)
    NumberLengthEnabled: Optional[bool] = Field(default=None)
    Provider: Optional[str] = Field(default=None)
    Webhook: Optional[str] = Field(default=None)


class TrunkVariable(Schema):
    DefaultValue: Optional[str] = Field(default=None)
    MaxLength: Optional[int] = Field(default=None)
    MinLength: Optional[int] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Option: Optional[str] = Field(default=None)
    OptionType: TrunkVariableType = Field(default=None)
    Pattern: Optional[str] = Field(default=None)
    prompt: Optional[str] = Field(default=None, alias="Prompt")
    Required: Optional[bool] = Field(default=None)
    Title: Optional[str] = Field(default=None)
    Validation: Optional[str] = Field(default=None)


class TrunkMessagingTemplate(Schema):
    MessagingVariables: Optional[list[TrunkVariable]] = Field(default=None)
    optional: Optional[bool] = Field(default=None, alias="Optional")
    Outbound: Optional[bool] = Field(default=None)
    Provider: Optional[str] = Field(default=None)
    Type: Optional[str] = Field(default=None)


class TrunkTemplate(Schema):
    AddAllowed: Optional[bool] = Field(default=None)
    Content: Optional[str] = Field(default=None)
    Countries: Optional[list[Optional[str]]] = Field(default=None)
    DefaultProxyPort: Optional[int] = Field(default=None)
    DefaultRegistrarPort: Optional[int] = Field(default=None)
    Description: Optional[str] = Field(default=None)
    Editors: Optional[list[TrunkEditorType]] = Field(default=None)
    Id: str = Field(default=None)
    MessagingTemplate: TrunkMessagingTemplate = Field(default=None)
    Name: str = Field(default=None)
    Tags: Optional[list[Optional[str]]] = Field(default=None)
    template_type: TemplateType = Field(default=None, alias="TemplateType")
    Url: Optional[str] = Field(default=None)


class TrunkTemplateCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[TrunkTemplate]] = Field(default=None)


class TrunkVariableCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[TrunkVariable]] = Field(default=None)


class TwilioPhoneNumber(Schema):
    FriendlyName: Optional[str] = Field(default=None)
    IsInTrunk: Optional[bool] = Field(default=None)
    IsMessagingEnabled: Optional[bool] = Field(default=None)
    PhoneNumber: Optional[str] = Field(default=None)
    Sid: str = Field(default=None)


class AutoProvisionTrunk(Schema):
    AvailableNumbers: Optional[list[TwilioPhoneNumber]] = Field(default=None)


class TwilioPhoneNumberCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[TwilioPhoneNumber]] = Field(default=None)


class UpdateItem(Schema):
    Category: str = Field(default=None)
    Description: str = Field(default=None)
    DescriptionLink: str = Field(default=None)
    Guid: Optional[str] = Field(default=None)
    Ignore: Optional[bool] = Field(default=None)
    Image: str = Field(default=None)
    LocalVersion: str = Field(default=None)
    Name: str = Field(default=None)
    OutOfDate: Optional[bool] = Field(default=None)
    ServerVersion: str = Field(default=None)
    update_type: UpdateType = Field(default=None, alias="UpdateType")


class UpdateItemCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[UpdateItem]] = Field(default=None)


class UpdateList(Schema):
    Entries: Optional[list[UpdateItem]] = Field(default=None)
    IsMaintananceExpired: Optional[bool] = Field(default=None)
    Key: Optional[str] = Field(default=None)
    LastSuccessfulUpdate: Optional[str] = Field(default=None)


class UpdateSettings(Schema):
    AutoUpdateEnabled: Optional[bool] = Field(default=None)
    schedule: BackupSchedule = Field(default=None, alias="Schedule")


class UpdatesStats(Schema):
    PerPage: Optional[list[CategoryUpdate]] = Field(default=None)
    TcxUpdate: Optional[list[CategoryUpdate]] = Field(default=None)


class UserActivity(Schema):
    AnsweredCount: int = Field(default=None)
    DateTimeInterval: str = Field(default=None)
    UnansweredCount: int = Field(default=None)


class UserActivityCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[UserActivity]] = Field(default=None)


class UserDeleteError(Schema):
    Error: Optional[str] = Field(default=None)
    ExtensionNumber: Optional[str] = Field(default=None)


class UserGroup(Schema):
    CanDelete: Optional[bool] = Field(default=None)
    GroupId: Optional[int] = Field(default=None)
    GroupRights: Rights = Field(default=None)
    Id: Optional[int] = Field(default=None)
    MemberName: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    rights: Rights = Field(default=None, alias="Rights")
    Tags: Optional[list[UserTag]] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    Type: PeerType = Field(default=None)


class CreateTrunk(Schema):
    AccountSid: Optional[str] = Field(default=None)
    ApiKey: Optional[str] = Field(default=None)
    DefaultRule: InboundRule = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    PhoneNumbers: Optional[list[TwilioPhoneNumber]] = Field(default=None)
    Type: TrunkType = Field(default=None)


class Fax(Schema):
    AuthID: Optional[str] = Field(default=None)
    AuthPassword: Optional[str] = Field(default=None)
    FaxServer: Optional[bool] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    Id: int = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OutboundCallerId: Optional[str] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)


class FaxCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Fax]] = Field(default=None)


class Group(Schema):
    AllowCallService: Optional[bool] = Field(default=None)
    AnswerAfter: Optional[int] = Field(default=None)
    BreakRoute: Route = Field(default=None)
    BreakTime: Schedule = Field(default=None)
    CallHandlingMode: Optional[list[CallHandlingFlags]] = Field(default=None)
    CallUsEnableChat: Optional[bool] = Field(default=None)
    CallUsEnablePhone: Optional[bool] = Field(default=None)
    CallUsEnableVideo: Optional[bool] = Field(default=None)
    CallUsRequirement: Authentication = Field(default=None)
    ClickToCallId: Optional[str] = Field(default=None)
    CurrentGroupHours: GroupHoursMode = Field(default=None)
    CustomOperator: Destination = Field(default=None)
    custom_prompt: Optional[str] = Field(default=None, alias="CustomPrompt")
    DisableCustomPrompt: Optional[bool] = Field(default=None)
    GloballyVisible: Optional[bool] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    HasMembers: Optional[bool] = Field(default=None)
    HolidaysRoute: Route = Field(default=None)
    Hours: Schedule = Field(default=None)
    Id: int = Field(default=None)
    IsDefault: Optional[bool] = Field(default=None)
    Language: Optional[str] = Field(default=None)
    LastLoginTime: Optional[str] = Field(default=None)
    Members: Optional[list[UserGroup]] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OfficeHolidays: Optional[list[Holiday]] = Field(default=None)
    OfficeRoute: Route = Field(default=None)
    OutOfOfficeRoute: Route = Field(default=None)
    OverrideExpiresAt: Optional[str] = Field(default=None)
    OverrideHolidays: Optional[bool] = Field(default=None)
    prompt_set: Optional[str] = Field(default=None, alias="PromptSet")
    Props: GroupProps = Field(default=None)
    rights: Optional[list[Rights]] = Field(default=None, alias="Rights")
    TimeZoneId: Optional[str] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)


class GroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Group]] = Field(default=None)


class MultiEditUserData(Schema):
    AllowLanOnly: Optional[bool] = Field(default=None)
    AllowOwnRecordings: Optional[bool] = Field(default=None)
    Blfs: Optional[str] = Field(default=None)
    CallScreening: Optional[bool] = Field(default=None)
    CanMoveForwardingExceptions: Optional[bool] = Field(default=None)
    DisplayNumbers: Optional[str] = Field(default=None)
    EmergencyAdditionalInfo: Optional[str] = Field(default=None)
    EmergencyLocationId: Optional[str] = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    EnableHotdesking: Optional[bool] = Field(default=None)
    ForwardingExceptions: Optional[list[ExtensionRule]] = Field(default=None)
    ForwardingProfiles: Optional[list[ForwardingProfile]] = Field(default=None)
    GoogleCalendarEnabled: Optional[bool] = Field(default=None)
    GoogleContactsEnabled: Optional[bool] = Field(default=None)
    GoogleSignInEnabled: Optional[bool] = Field(default=None)
    Greetings: Optional[list[Greeting]] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    HideInPhonebook: Optional[bool] = Field(default=None)
    Internal: Optional[bool] = Field(default=None)
    Mobile: Optional[str] = Field(default=None)
    MS365CalendarEnabled: Optional[bool] = Field(default=None)
    MS365ContactsEnabled: Optional[bool] = Field(default=None)
    MS365SignInEnabled: Optional[bool] = Field(default=None)
    MS365TeamsEnabled: Optional[bool] = Field(default=None)
    MyPhoneAllowDeleteRecordings: Optional[bool] = Field(default=None)
    MyPhoneHideForwardings: Optional[bool] = Field(default=None)
    MyPhoneShowRecordings: Optional[bool] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    PbxDeliversAudio: Optional[bool] = Field(default=None)
    PinProtected: Optional[bool] = Field(default=None)
    PinProtectTimeout: Optional[int] = Field(default=None)
    prompt_set: Optional[str] = Field(default=None, alias="PromptSet")
    RecordCalls: Optional[bool] = Field(default=None)
    RecordEmailNotify: Optional[bool] = Field(default=None)
    RecordExternalCallsOnly: Optional[bool] = Field(default=None)
    SendEmailMissedCalls: Optional[bool] = Field(default=None)
    SRTPMode: SRTPModeType = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    VMDisablePinAuth: Optional[bool] = Field(default=None)
    VMEmailOptions: VMEmailOptionsType = Field(default=None)
    VMEnabled: Optional[bool] = Field(default=None)
    VMPlayCallerID: Optional[bool] = Field(default=None)
    VMPlayMsgDateTime: VMPlayMsgDateTimeType = Field(default=None)


class Parking(Schema):
    Groups: Optional[list[UserGroup]] = Field(default=None)
    Id: int = Field(default=None)
    Number: Optional[str] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)


class ParkingCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Parking]] = Field(default=None)


class Queue(Schema):
    AgentAvailabilityMode: Optional[bool] = Field(default=None)
    Agents: Optional[list[QueueAgent]] = Field(default=None)
    AnnouncementInterval: Optional[int] = Field(default=None)
    AnnounceQueuePosition: Optional[bool] = Field(default=None)
    BreakRoute: Route = Field(default=None)
    CallbackEnableTime: Optional[int] = Field(default=None)
    CallbackPrefix: Optional[str] = Field(default=None)
    CallUsEnableChat: Optional[bool] = Field(default=None)
    CallUsEnablePhone: Optional[bool] = Field(default=None)
    CallUsEnableVideo: Optional[bool] = Field(default=None)
    CallUsRequirement: Authentication = Field(default=None)
    ClickToCallId: Optional[str] = Field(default=None)
    EnableIntro: Optional[bool] = Field(default=None)
    ForwardNoAnswer: Destination = Field(default=None)
    greeting_file: Optional[str] = Field(default=None, alias="GreetingFile")
    Groups: Optional[list[UserGroup]] = Field(default=None)
    HolidaysRoute: Route = Field(default=None)
    Id: int = Field(default=None)
    IntroFile: Optional[str] = Field(default=None)
    IsRegistered: Optional[bool] = Field(default=None)
    Managers: Optional[list[QueueManager]] = Field(default=None)
    MasterTimeout: Optional[int] = Field(default=None)
    MaxCallersInQueue: Optional[int] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    NotifyCodes: Optional[list[QueueNotifyCode]] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OnHoldFile: Optional[str] = Field(default=None)
    OutOfOfficeRoute: Route = Field(default=None)
    PlayFullPrompt: Optional[bool] = Field(default=None)
    PollingStrategy: PollingStrategyType = Field(default=None)
    PriorityQueue: Optional[bool] = Field(default=None)
    prompt_set: Optional[str] = Field(default=None, alias="PromptSet")
    recording: QueueRecording = Field(default=None, alias="Recording")
    reset_queue_statistics_schedule: ResetQueueStatisticsSchedule = Field(default=None, alias="ResetQueueStatisticsSchedule")
    ResetStatisticsScheduleEnabled: Optional[bool] = Field(default=None)
    RingTimeout: Optional[int] = Field(default=None)
    SLATime: Optional[int] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    type_of_chat_ownership_type: TypeOfChatOwnershipType = Field(default=None, alias="TypeOfChatOwnershipType")
    WrapUpTime: Optional[int] = Field(default=None)


class QueueCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Queue]] = Field(default=None)


class Receptionist(Schema):
    BreakRoute: Route = Field(default=None)
    Forwards: Optional[list[ReceptionistForward]] = Field(default=None)
    ForwardSmsTo: Optional[str] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    HolidaysRoute: Route = Field(default=None)
    Id: int = Field(default=None)
    InvalidKeyForwardDN: Optional[str] = Field(default=None)
    IsRegistered: Optional[bool] = Field(default=None)
    ivr_type: IVRType = Field(default=None, alias="IVRType")
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OutOfOfficeRoute: Route = Field(default=None)
    PromptFilename: Optional[str] = Field(default=None)
    prompt_set: Optional[str] = Field(default=None, alias="PromptSet")
    Timeout: Optional[int] = Field(default=None)
    TimeoutForwardDN: Optional[str] = Field(default=None)
    TimeoutForwardPeerType: PeerType = Field(default=None)
    TimeoutForwardType: IVRForwardType = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    UseMSExchange: Optional[bool] = Field(default=None)


class ReceptionistCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Receptionist]] = Field(default=None)


class RingGroup(Schema):
    BreakRoute: Route = Field(default=None)
    CallUsEnableChat: Optional[bool] = Field(default=None)
    CallUsEnablePhone: Optional[bool] = Field(default=None)
    CallUsEnableVideo: Optional[bool] = Field(default=None)
    CallUsRequirement: Authentication = Field(default=None)
    ClickToCallId: Optional[str] = Field(default=None)
    ForwardNoAnswer: Destination = Field(default=None)
    greeting_file: Optional[str] = Field(default=None, alias="GreetingFile")
    Groups: Optional[list[UserGroup]] = Field(default=None)
    HolidaysRoute: Route = Field(default=None)
    Id: int = Field(default=None)
    IsRegistered: Optional[bool] = Field(default=None)
    Members: Optional[list[RingGroupMember]] = Field(default=None)
    MulticastAddress: Optional[str] = Field(default=None)
    MulticastCodec: Optional[str] = Field(default=None)
    MulticastPacketTime: Optional[int] = Field(default=None)
    MulticastPort: Optional[int] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OutOfOfficeRoute: Route = Field(default=None)
    RingStrategy: StrategyType = Field(default=None)
    RingTime: Optional[int] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)


class RingGroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[RingGroup]] = Field(default=None)


class ServicePrincipal(Schema):
    CallControlEnabled: Optional[bool] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    Id: int = Field(default=None)
    LastUsed: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    Peers: Optional[list[Peer]] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    XAPIEnabled: Optional[bool] = Field(default=None)


class ServicePrincipalCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[ServicePrincipal]] = Field(default=None)


class User(Schema):
    AccessPassword: Optional[str] = Field(default=None)
    AllowLanOnly: Optional[bool] = Field(default=None)
    AllowOwnRecordings: Optional[bool] = Field(default=None)
    AuthID: Optional[str] = Field(default=None)
    AuthPassword: Optional[str] = Field(default=None)
    Blfs: Optional[str] = Field(default=None)
    BreakTime: Schedule = Field(default=None)
    CallScreening: Optional[bool] = Field(default=None)
    CallUsEnableChat: Optional[bool] = Field(default=None)
    CallUsEnablePhone: Optional[bool] = Field(default=None)
    CallUsEnableVideo: Optional[bool] = Field(default=None)
    CallUsRequirement: Authentication = Field(default=None)
    ClickToCallId: Optional[str] = Field(default=None)
    ContactImage: Optional[str] = Field(default=None)
    CurrentProfileName: Optional[str] = Field(default=None)
    DeskphonePassword: Optional[str] = Field(default=None)
    DisplayName: Optional[str] = Field(default=None)
    EmailAddress: Optional[str] = Field(default=None)
    EmergencyAdditionalInfo: Optional[str] = Field(default=None)
    EmergencyLocationId: Optional[str] = Field(default=None)
    Enable2FA: Optional[bool] = Field(default=None)
    Enabled: Optional[bool] = Field(default=None)
    EnableHotdesking: Optional[bool] = Field(default=None)
    FirstName: Optional[str] = Field(default=None)
    ForwardingExceptions: Optional[list[ExtensionRule]] = Field(default=None)
    ForwardingProfiles: Optional[list[ForwardingProfile]] = Field(default=None)
    GoogleCalendarEnabled: Optional[bool] = Field(default=None)
    GoogleContactsEnabled: Optional[bool] = Field(default=None)
    GoogleSignInEnabled: Optional[bool] = Field(default=None)
    Greetings: Optional[list[Greeting]] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    HideInPhonebook: Optional[bool] = Field(default=None)
    HotdeskingAssignment: Optional[str] = Field(default=None)
    Hours: Schedule = Field(default=None)
    Id: int = Field(default=None)
    Internal: Optional[bool] = Field(default=None)
    IsRegistered: Optional[bool] = Field(default=None)
    Language: Optional[str] = Field(default=None)
    LastName: Optional[str] = Field(default=None)
    Mobile: Optional[str] = Field(default=None)
    MS365CalendarEnabled: Optional[bool] = Field(default=None)
    MS365ContactsEnabled: Optional[bool] = Field(default=None)
    MS365SignInEnabled: Optional[bool] = Field(default=None)
    MS365TeamsEnabled: Optional[bool] = Field(default=None)
    MyPhoneAllowDeleteRecordings: Optional[bool] = Field(default=None)
    MyPhoneHideForwardings: Optional[bool] = Field(default=None)
    MyPhonePush: Optional[bool] = Field(default=None)
    MyPhoneShowRecordings: Optional[bool] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OfficeHoursProps: Optional[list[OfficeHoursBits]] = Field(default=None)
    OutboundCallerID: Optional[str] = Field(default=None)
    PbxDeliversAudio: Optional[bool] = Field(default=None)
    Phones: Optional[list[Phone]] = Field(default=None)
    PinProtected: Optional[bool] = Field(default=None)
    PinProtectTimeout: Optional[int] = Field(default=None)
    PrimaryGroupId: Optional[int] = Field(default=None)
    prompt_set: Optional[str] = Field(default=None, alias="PromptSet")
    QueueStatus: QueueStatusType = Field(default=None)
    RecordCalls: Optional[bool] = Field(default=None)
    RecordEmailNotify: Optional[bool] = Field(default=None)
    RecordExternalCallsOnly: Optional[bool] = Field(default=None)
    Require2FA: Optional[bool] = Field(default=None)
    SendEmailMissedCalls: Optional[bool] = Field(default=None)
    SIPID: Optional[str] = Field(default=None)
    SRTPMode: SRTPModeType = Field(default=None)
    Tags: Optional[list[UserTag]] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    VMDisablePinAuth: Optional[bool] = Field(default=None)
    VMEmailOptions: VMEmailOptionsType = Field(default=None)
    VMEnabled: Optional[bool] = Field(default=None)
    VMPIN: Optional[str] = Field(default=None)
    VMPlayCallerID: Optional[bool] = Field(default=None)
    VMPlayMsgDateTime: VMPlayMsgDateTimeType = Field(default=None)
    WebMeetingApproveParticipants: Optional[bool] = Field(default=None)
    WebMeetingFriendlyName: Optional[str] = Field(default=None)


class UserCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[User]] = Field(default=None)


class UserGroupCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[UserGroup]] = Field(default=None)


class UsersRequestOptions(Schema):
    Count: int = Field(default=None)
    NextPageToken: Optional[str] = Field(default=None)
    Search: Optional[str] = Field(default=None)
    type_of_user: TypeOfUser = Field(default=None, alias="TypeOfUser")


class UsersSyncConfiguration(Schema):
    IsEnabled: Optional[bool] = Field(default=None)
    SelectedUsers: Optional[list[Optional[str]]] = Field(default=None)
    SyncType: IntegrationSyncType = Field(default=None)


class Microsoft365Integration(Schema):
    AdUsers: ADUsersSyncConfiguration = Field(default=None)
    ApplicationId: str = Field(default=None)
    Id: int = Field(default=None)
    SharedMailboxesSync: UsersSyncConfiguration = Field(default=None)
    TenantId: str = Field(default=None)


class Variable(Schema):
    Name: str = Field(default=None)
    Value: str = Field(default=None)


class Fxs(Schema):
    Brand: Optional[str] = Field(default=None)
    Codecs: Optional[list[Optional[str]]] = Field(default=None)
    FxsLineCount: Optional[int] = Field(default=None)
    FxsLines: Optional[list[DeviceLine]] = Field(default=None)
    group: Optional[str] = Field(default=None, alias="Group")
    Language: Optional[str] = Field(default=None)
    MacAddress: str = Field(default=None)
    Model: Optional[str] = Field(default=None)
    ModelName: Optional[str] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Password: Optional[str] = Field(default=None)
    Provisioning: FxsProvisioning = Field(default=None)
    Registered: RegistrarFxs = Field(default=None)
    Secret: Optional[str] = Field(default=None)
    Template: FxsTemplate = Field(default=None)
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")
    Variables: Optional[list[Variable]] = Field(default=None)


class FxsCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Fxs]] = Field(default=None)


class Trunk(Schema):
    AuthID: Optional[str] = Field(default=None)
    AuthPassword: ConcealedPassword = Field(default=None)
    Certificate: Optional[str] = Field(default=None)
    CertificateName: Optional[str] = Field(default=None)
    ConfigurationIssue: Optional[str] = Field(default=None)
    DidNumbers: Optional[list[Optional[str]]] = Field(default=None)
    Direction: DirectionType = Field(default=None)
    DisableVideo: Optional[bool] = Field(default=None)
    DiversionHeader: Optional[bool] = Field(default=None)
    E164CountryCode: Optional[str] = Field(default=None)
    E164ProcessIncomingNumber: Optional[bool] = Field(default=None)
    EmergencyGeoLocations: Optional[list[EmergencyGeoTrunkLocation]] = Field(default=None)
    EnableInboundCalls: Optional[bool] = Field(default=None)
    EnableOutboundCalls: Optional[bool] = Field(default=None)
    ExternalNumber: Optional[str] = Field(default=None)
    gateway: Gateway = Field(default=None, alias="Gateway")
    Groups: Optional[list[UserGroup]] = Field(default=None)
    Id: int = Field(default=None)
    InCIDFormatting: Optional[list[CIDFormatting]] = Field(default=None)
    IPRestriction: TypeOfIPDestriction = Field(default=None)
    IsOnline: Optional[bool] = Field(default=None)
    Messaging: TrunkMessaging = Field(default=None)
    Number: Optional[str] = Field(default=None)
    OutboundCallerID: Optional[str] = Field(default=None)
    OutCIDFormatting: Optional[list[CIDFormatting]] = Field(default=None)
    PublicInfoGroups: Optional[list[Optional[str]]] = Field(default=None)
    PublicIPinSIP: Optional[str] = Field(default=None)
    PublishInfo: Optional[bool] = Field(default=None)
    ReceiveExtensions: Optional[list[Peer]] = Field(default=None)
    ReceiveInfo: Optional[bool] = Field(default=None)
    RemoteMyPhoneUriHost: Optional[str] = Field(default=None)
    RemotePBXPreffix: Optional[str] = Field(default=None)
    RoutingRules: Optional[list[InboundRule]] = Field(default=None)
    SecondaryRegistrar: Optional[str] = Field(default=None)
    SeparateAuthId: Optional[str] = Field(default=None)
    SimultaneousCalls: Optional[int] = Field(default=None)
    Tags: Optional[list[UserTag]] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    TransportRestriction: TypeOfTransportRestriction = Field(default=None)
    TrunkRegTimes: Optional[list[Variable]] = Field(default=None)
    TunnelEnabled: Optional[bool] = Field(default=None)
    TunnelRemoteAddr: Optional[str] = Field(default=None)
    TunnelRemotePort: Optional[int] = Field(default=None)
    UseSeparateAuthId: Optional[bool] = Field(default=None)


class CallFlowApp(Schema):
    CompilationLastSuccess: Optional[str] = Field(default=None)
    CompilationResult: Optional[str] = Field(default=None)
    CompilationSucceeded: Optional[bool] = Field(default=None)
    Groups: Optional[list[UserGroup]] = Field(default=None)
    Id: int = Field(default=None)
    InvalidScript: Optional[bool] = Field(default=None)
    IsRegistered: Optional[bool] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Number: Optional[str] = Field(default=None)
    RejectedCode: Optional[str] = Field(default=None)
    RoutingType: CfaRoutingType = Field(default=None)
    ScriptCode: Optional[str] = Field(default=None)
    TranscriptionMode: TranscriptionType = Field(default=None)
    trunk: Trunk = Field(default=None, alias="Trunk")


class CallFlowAppCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[CallFlowApp]] = Field(default=None)


class TrunkCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Trunk]] = Field(default=None)


class VariableCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Variable]] = Field(default=None)


class VersionUpdateType(Schema):
    Type: UpdateType = Field(default=None)


class VoicemailSettings(Schema):
    AutoDeleteDays: Optional[int] = Field(default=None)
    AutoDeleteEnabled: Optional[bool] = Field(default=None)
    Extension: Optional[str] = Field(default=None)
    Id: int = Field(default=None)
    MinDuration: Optional[int] = Field(default=None)
    OperatorEnabled: Optional[bool] = Field(default=None)
    Quota: Optional[int] = Field(default=None)
    RemoteStorageEnabled: Optional[bool] = Field(default=None)
    SendEmailQuotaEnabled: Optional[bool] = Field(default=None)
    SendEmailQuotaPercentage: Optional[int] = Field(default=None)
    transcribe_engine: TranscribeEngine = Field(default=None, alias="TranscribeEngine")
    TranscribeLanguage: Optional[str] = Field(default=None)
    TranscribeRegion: Optional[str] = Field(default=None)
    TranscribeSecretKey: ConcealedPassword = Field(default=None)
    UsedSpace: Optional[int] = Field(default=None)


class VoipProvider(Schema):
    Countries: Optional[list[Optional[str]]] = Field(default=None)
    Id: str = Field(default=None)
    Name: str = Field(default=None)
    Type: TemplateType = Field(default=None)


class WebsiteLinksTranslations(Schema):
    AuthenticationMessage: Optional[str] = Field(default=None)
    EndingMessage: Optional[str] = Field(default=None)
    FirstResponseMessage: Optional[str] = Field(default=None)
    GdprMessage: Optional[str] = Field(default=None)
    GreetingMessage: Optional[str] = Field(default=None)
    GreetingOfflineMessage: Optional[str] = Field(default=None)
    InviteMessage: Optional[str] = Field(default=None)
    OfflineEmailMessage: Optional[str] = Field(default=None)
    OfflineFinishMessage: Optional[str] = Field(default=None)
    OfflineFormInvalidEmail: Optional[str] = Field(default=None)
    OfflineFormInvalidName: Optional[str] = Field(default=None)
    OfflineFormMaximumCharactersReached: Optional[str] = Field(default=None)
    OfflineNameMessage: Optional[str] = Field(default=None)
    StartChatButtonText: Optional[str] = Field(default=None)
    UnavailableMessage: Optional[str] = Field(default=None)
    WindowTitle: Optional[str] = Field(default=None)


class Weblink(Schema):
    Advanced: LiveChatAdvancedSettings = Field(default=None)
    CallsEnabled: Optional[bool] = Field(default=None)
    ChatBox: LiveChatBox = Field(default=None)
    ChatEnabled: Optional[bool] = Field(default=None)
    DefaultRecord: Optional[bool] = Field(default=None)
    DN: Peer = Field(default=None)
    EnableReCaptcha: Optional[bool] = Field(default=None)
    General: GeneralLiveChatSettings = Field(default=None)
    group: Optional[str] = Field(default=None, alias="Group")
    Hidden: Optional[bool] = Field(default=None)
    Id: Optional[int] = Field(default=None)
    Link: str = Field(default=None)
    MeetingEnabled: Optional[bool] = Field(default=None)
    Name: Optional[str] = Field(default=None)
    Styling: LiveChatStyling = Field(default=None)
    Translations: WebsiteLinksTranslations = Field(default=None)
    Website: Optional[list[Optional[str]]] = Field(default=None)


class WeblinkCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[list[Weblink]] = Field(default=None)


class XLicenseParams(Schema):
    CompanyName: Optional[str] = Field(default=None)
    ContactName: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None, alias="Country")
    Email: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None, alias="Phone")


class XOutboundRulePurge(Schema):
    Ids: Optional[list[int]] = Field(default=None)


class XServiceManageOptions(Schema):
    ServiceNames: Optional[list[Optional[str]]] = Field(default=None)
