from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field


class DefaultPhoto(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class MatchedTerm(BaseModel):
    type: str


class ObservationsCount(BaseModel):
    type: str


class Properties(BaseModel):
    default_photo: DefaultPhoto
    matched_term: MatchedTerm
    observations_count: ObservationsCount


class AllOfItem(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties] = None
    type: Optional[str] = None


class AutocompleteTaxon(BaseModel):
    allOf: List[AllOfItem]


class Page(BaseModel):
    type: str


class PerPage(BaseModel):
    type: str


class TotalResults(BaseModel):
    type: str


class Properties1(BaseModel):
    page: Page
    per_page: PerPage
    total_results: TotalResults


class BaseResponse(BaseModel):
    properties: Properties1
    type: str


class Id(BaseModel):
    type: str


class Value(BaseModel):
    type: str


class Properties2(BaseModel):
    id: Id
    value: Value


class Color(BaseModel):
    properties: Properties2
    type: str


class CreatedAt(BaseModel):
    format: str
    type: str


class CreatedAtDetails(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class User(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Properties3(BaseModel):
    created_at: CreatedAt
    created_at_details: CreatedAtDetails
    id: Id
    user: User


class Comment(BaseModel):
    properties: Properties3
    type: str


class Place(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class PlaceId(BaseModel):
    type: str


class Status(BaseModel):
    type: str


class Properties4(BaseModel):
    place: Place
    place_id: PlaceId
    status: Status


class ConservationStatus(BaseModel):
    properties: Properties4
    type: str


class DisplayName(BaseModel):
    type: str


class Name(BaseModel):
    type: str


class Properties5(BaseModel):
    display_name: DisplayName
    id: Id
    name: Name


class CorePlace(BaseModel):
    properties: Properties5
    type: str


class IconicTaxonId(BaseModel):
    type: str


class IconicTaxonName(BaseModel):
    type: str


class IsActive(BaseModel):
    type: str


class PreferredCommonName(BaseModel):
    type: str


class Rank(BaseModel):
    type: str


class RankLevel(BaseModel):
    type: str


class Properties6(BaseModel):
    iconic_taxon_id: IconicTaxonId
    iconic_taxon_name: IconicTaxonName
    id: Id
    is_active: IsActive
    name: Name
    preferred_common_name: PreferredCommonName
    rank: Rank
    rank_level: RankLevel


class CoreTaxon(BaseModel):
    properties: Properties6
    type: str


class Date(BaseModel):
    format: str
    type: str


class Day(BaseModel):
    type: str


class Hour(BaseModel):
    type: str


class Month(BaseModel):
    type: str


class Week(BaseModel):
    type: str


class Year(BaseModel):
    type: str


class Properties7(BaseModel):
    date: Date
    day: Day
    hour: Hour
    month: Month
    week: Week
    year: Year


class DateDetails(BaseModel):
    properties: Properties7
    type: str


class Code(BaseModel):
    type: str


class Message(BaseModel):
    type: str


class Properties8(BaseModel):
    code: Code
    message: Message


class Error(BaseModel):
    properties: Properties8
    type: str


class EstablishmentMeans1(BaseModel):
    type: str


class Properties9(BaseModel):
    establishment_means: EstablishmentMeans1
    place: Place


class EstablishmentMeans(BaseModel):
    properties: Properties9
    type: str


class VotableId(BaseModel):
    type: str


class Properties10(BaseModel):
    created_at: CreatedAt
    id: Id
    user: User
    votable_id: VotableId


class Fave(BaseModel):
    properties: Properties10
    type: str


class Properties11(BaseModel):
    name: Name
    value: Value


class FieldValue(BaseModel):
    properties: Properties11
    type: str


class Body(BaseModel):
    type: str


class Current(BaseModel):
    type: str


class ObservationId(BaseModel):
    type: str


class Taxon(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class UpdatedAt(BaseModel):
    format: str
    type: str


class Properties12(BaseModel):
    body: Body
    created_at: CreatedAt
    current: Current
    id: Id
    observation_id: ObservationId
    taxon: Taxon
    updated_at: UpdatedAt


class Identification(BaseModel):
    properties: Properties12
    type: str


class Items(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Results(BaseModel):
    items: Items
    type: str


class Properties13(BaseModel):
    results: Results


class AllOfItem1(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties13] = None
    required: Optional[List[str]] = None


class IdentificationsResponse(BaseModel):
    allOf: List[AllOfItem1]


class FromUser(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Subject(BaseModel):
    type: str


class Items1(BaseModel):
    type: str


class ThreadFlags(BaseModel):
    description: str
    items: Items1
    type: str


class ThreadId(BaseModel):
    description: str
    type: str


class ThreadMessagesCount(BaseModel):
    description: str
    type: str


class ToUser(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class UserId(BaseModel):
    description: str
    type: str


class Properties14(BaseModel):
    body: Body
    from_user: FromUser
    id: Id
    subject: Subject
    thread_flags: ThreadFlags
    thread_id: ThreadId
    thread_messages_count: ThreadMessagesCount
    to_user: ToUser
    user_id: UserId


class Message1(BaseModel):
    properties: Properties14
    type: str


class Items2(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Results1(BaseModel):
    items: Items2
    type: str


class Properties15(BaseModel):
    results: Results1


class AllOfItem2(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties15] = None
    required: Optional[List[str]] = None


class MessagesResponse(BaseModel):
    allOf: List[AllOfItem2]


class Community(BaseModel):
    items: Items2
    type: str


class Standard(BaseModel):
    items: Items2
    type: str


class Properties17(BaseModel):
    community: Community
    standard: Standard


class Results2(BaseModel):
    properties: Properties17
    type: str


class Properties16(BaseModel):
    results: Results2


class AllOfItem3(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties16] = None
    required: Optional[List[str]] = None


class NearbyPlacesResponse(BaseModel):
    allOf: List[AllOfItem3]


class Properties18(BaseModel):
    body: Body
    created_at: CreatedAt
    created_at_details: CreatedAtDetails
    id: Id
    user: User


class NonOwnerIdentification(BaseModel):
    properties: Properties18
    type: str


class CachedVotesTotal(BaseModel):
    type: str


class Captive(BaseModel):
    type: str


class Comments(BaseModel):
    items: Items2
    type: str


class CommentsCount(BaseModel):
    type: str


class CreatedTimeZone(BaseModel):
    type: str


class Description(BaseModel):
    type: str


class FavesCount(BaseModel):
    type: str


class Geojson(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Geoprivacy(BaseModel):
    type: str


class IdPlease(BaseModel):
    type: str


class IdentificationsCount(BaseModel):
    type: str


class IdentificationsMostAgree(BaseModel):
    type: str


class IdentificationsMostDisagree(BaseModel):
    type: str


class IdentificationsSomeAgree(BaseModel):
    type: str


class LicenseCode(BaseModel):
    type: str


class Location(BaseModel):
    description: str
    type: str


class Mappable(BaseModel):
    type: str


class NonOwnerIds(BaseModel):
    items: Items2
    type: str


class NumIdentificationAgreements(BaseModel):
    type: str


class NumIdentificationDisagreements(BaseModel):
    type: str


class Obscured(BaseModel):
    type: str


class ObservedOn(BaseModel):
    format: str
    type: str


class ObservedOnDetails(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class ObservedOnString(BaseModel):
    type: str


class ObservedTimeZone(BaseModel):
    type: str


class Ofvs(BaseModel):
    items: Items2
    type: str


class OutOfRange(BaseModel):
    type: str


class Photos(BaseModel):
    items: Items2
    type: str


class PlaceGuess(BaseModel):
    type: str


class Items9(BaseModel):
    type: str


class PlaceIds(BaseModel):
    items: Items9
    type: str


class ProjectIds(BaseModel):
    items: Items9
    type: str


class ProjectIdsWithCuratorId(BaseModel):
    items: Items9
    type: str


class ProjectIdsWithoutCuratorId(BaseModel):
    items: Items9
    type: str


class QualityGrade(BaseModel):
    type: str


class ReviewedBy(BaseModel):
    items: Items9
    type: str


class SiteId(BaseModel):
    type: str


class Items14(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Sounds(BaseModel):
    items: Items14
    type: str


class SpeciesGuess(BaseModel):
    type: str


class Items15(BaseModel):
    type: str


class Tags(BaseModel):
    items: Items15
    type: str


class TaxonGeoprivacy(BaseModel):
    type: str


class TimeObservedAt(BaseModel):
    format: str
    type: str


class TimeZoneOffset(BaseModel):
    type: str


class Uri(BaseModel):
    type: str


class Verifiable(BaseModel):
    type: str


class Properties19(BaseModel):
    cached_votes_total: CachedVotesTotal
    captive: Captive
    comments: Comments
    comments_count: CommentsCount
    created_at: CreatedAt
    created_at_details: CreatedAtDetails
    created_time_zone: CreatedTimeZone
    description: Description
    faves_count: FavesCount
    geojson: Geojson
    geoprivacy: Geoprivacy
    id: Id
    id_please: IdPlease
    identifications_count: IdentificationsCount
    identifications_most_agree: IdentificationsMostAgree
    identifications_most_disagree: IdentificationsMostDisagree
    identifications_some_agree: IdentificationsSomeAgree
    license_code: LicenseCode
    location: Location
    mappable: Mappable
    non_owner_ids: NonOwnerIds
    num_identification_agreements: NumIdentificationAgreements
    num_identification_disagreements: NumIdentificationDisagreements
    obscured: Obscured
    observed_on: ObservedOn
    observed_on_details: ObservedOnDetails
    observed_on_string: ObservedOnString
    observed_time_zone: ObservedTimeZone
    ofvs: Ofvs
    out_of_range: OutOfRange
    photos: Photos
    place_guess: PlaceGuess
    place_ids: PlaceIds
    project_ids: ProjectIds
    project_ids_with_curator_id: ProjectIdsWithCuratorId
    project_ids_without_curator_id: ProjectIdsWithoutCuratorId
    quality_grade: QualityGrade
    reviewed_by: ReviewedBy
    site_id: SiteId
    sounds: Sounds
    species_guess: SpeciesGuess
    tags: Tags
    taxon: Taxon
    taxon_geoprivacy: TaxonGeoprivacy
    time_observed_at: TimeObservedAt
    time_zone_offset: TimeZoneOffset
    updated_at: UpdatedAt
    uri: Uri
    user: User
    verifiable: Verifiable


class Observation(BaseModel):
    properties: Properties19
    type: str


class AncestorIds(BaseModel):
    items: Items15
    type: str


class Ancestry(BaseModel):
    type: str


class ConservationStatus1(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Endemic(BaseModel):
    type: str


class EstablishmentMeans2(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Introduced(BaseModel):
    type: str


class Native(BaseModel):
    type: str


class Threatened(BaseModel):
    type: str


class Properties20(BaseModel):
    ancestor_ids: AncestorIds
    ancestry: Ancestry
    conservation_status: ConservationStatus1
    endemic: Endemic
    establishment_means: EstablishmentMeans2
    introduced: Introduced
    native: Native
    threatened: Threatened


class AllOfItem4(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties20] = None
    type: Optional[str] = None


class ObservationTaxon(BaseModel):
    allOf: List[AllOfItem4]


class ObservationCount(BaseModel):
    type: str


class SpeciesCount(BaseModel):
    type: str


class Properties22(BaseModel):
    observation_count: ObservationCount
    species_count: SpeciesCount
    user: User


class Items17(BaseModel):
    properties: Properties22
    type: str


class Results3(BaseModel):
    items: Items17
    type: str


class Properties21(BaseModel):
    results: Results3


class AllOfItem5(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties21] = None
    required: Optional[List[str]] = None


class ObservationsObserversResponse(BaseModel):
    allOf: List[AllOfItem5]


class Items18(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Results4(BaseModel):
    items: Items18
    type: str


class Properties23(BaseModel):
    results: Results4


class AllOfItem6(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties23] = None
    required: Optional[List[str]] = None


class ObservationsResponse(BaseModel):
    allOf: List[AllOfItem6]


class Results5(BaseModel):
    items: Items18
    type: str


class Properties24(BaseModel):
    results: Results5


class AllOfItem7(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties24] = None
    required: Optional[List[str]] = None


class ObservationsShowResponse(BaseModel):
    allOf: List[AllOfItem7]


class Attribution(BaseModel):
    type: str


class Url(BaseModel):
    type: str


class Properties25(BaseModel):
    attribution: Attribution
    id: Id
    license_code: LicenseCode
    url: Url


class Photo(BaseModel):
    properties: Properties25
    type: str


class Results6(BaseModel):
    items: Items18
    type: str


class Properties26(BaseModel):
    results: Results6


class AllOfItem8(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties26] = None
    required: Optional[List[str]] = None


class PlacesResponse(BaseModel):
    allOf: List[AllOfItem8]


class Items21(BaseModel):
    format: str
    type: str


class Coordinates(BaseModel):
    description: str
    items: Items21
    type: str


class Type(BaseModel):
    type: str


class Properties27(BaseModel):
    coordinates: Coordinates
    type: Type


class PointGeoJson(BaseModel):
    properties: Properties27
    type: str


class Items23(BaseModel):
    description: str
    items: Items21
    type: str


class Items22(BaseModel):
    items: Items23
    type: str


class Coordinates1(BaseModel):
    items: Items22
    type: str


class Properties28(BaseModel):
    coordinates: Coordinates1
    type: Type


class PolygonGeoJson(BaseModel):
    properties: Properties28
    type: str


class ControlledAttributeId(BaseModel):
    type: str


class ControlledValueId(BaseModel):
    type: str


class ResourceId(BaseModel):
    type: str


class ResourceType(BaseModel):
    enum: List[str]
    type: str


class Properties30(BaseModel):
    controlled_attribute_id: ControlledAttributeId
    controlled_value_id: ControlledValueId
    resource_id: ResourceId
    resource_type: ResourceType


class Annotation(BaseModel):
    properties: Properties30
    type: str


class Properties29(BaseModel):
    annotation: Annotation


class PostAnnotation(BaseModel):
    properties: Properties29
    type: str


class ParentId(BaseModel):
    type: str


class ParentType(BaseModel):
    enum: List[str]
    type: str


class Properties32(BaseModel):
    body: Body
    parent_id: ParentId
    parent_type: ParentType


class Comment1(BaseModel):
    properties: Properties32
    type: str


class Properties31(BaseModel):
    comment: Comment1


class PostComment(BaseModel):
    properties: Properties31
    type: str


class Flag1(BaseModel):
    enum: List[str]


class FlaggableId(BaseModel):
    type: str


class FlaggableType(BaseModel):
    enum: List[str]
    type: str


class Properties34(BaseModel):
    flag: Flag1
    flaggable_id: FlaggableId
    flaggable_type: FlaggableType


class Flag(BaseModel):
    properties: Properties34
    type: str


class FlagExplanation(BaseModel):
    type: str


class Properties33(BaseModel):
    flag: Flag
    flag_explanation: FlagExplanation


class PostFlag(BaseModel):
    properties: Properties33
    type: str


class TaxonId(BaseModel):
    type: str


class Properties36(BaseModel):
    body: Body
    current: Current
    observation_id: ObservationId
    taxon_id: TaxonId


class Identification1(BaseModel):
    properties: Properties36
    type: str


class Properties35(BaseModel):
    identification: Identification1


class PostIdentification(BaseModel):
    properties: Properties35
    type: str


class Body5(BaseModel):
    description: str
    type: str


class Subject1(BaseModel):
    description: str
    type: str


class ToUserId(BaseModel):
    description: str
    type: str


class Properties38(BaseModel):
    body: Body5
    subject: Subject1
    thread_id: ThreadId
    to_user_id: ToUserId


class Message2(BaseModel):
    properties: Properties38
    type: str


class Properties37(BaseModel):
    message: Message2


class PostMessage(BaseModel):
    properties: Properties37
    type: str


class Properties40(BaseModel):
    description: Description
    species_guess: SpeciesGuess
    taxon_id: TaxonId


class Observation1(BaseModel):
    properties: Properties40
    type: str


class Properties39(BaseModel):
    observation: Observation1


class PostObservation(BaseModel):
    properties: Properties39
    type: str


class ObservationFieldId(BaseModel):
    type: str


class Properties42(BaseModel):
    observation_field_id: ObservationFieldId
    observation_id: ObservationId
    value: Value


class ObservationFieldValue(BaseModel):
    properties: Properties42
    type: str


class Properties41(BaseModel):
    observation_field_value: ObservationFieldValue


class PostObservationFieldValue(BaseModel):
    properties: Properties41
    type: str


class Properties44(BaseModel):
    observation_id: ObservationId


class ObservationPhoto(BaseModel):
    properties: Properties44
    type: str


class Properties43(BaseModel):
    observation_photo: ObservationPhoto


class PostObservationPhoto(BaseModel):
    properties: Properties43
    type: str


class Scope(BaseModel):
    enum: List[str]


class Vote(BaseModel):
    enum: List[str]
    type: str


class Properties45(BaseModel):
    scope: Scope
    vote: Vote


class PostObservationVote(BaseModel):
    properties: Properties45
    type: str


class Commit(BaseModel):
    example: str
    type: str


class Body6(BaseModel):
    type: str


class ParentType1(BaseModel):
    example: str
    type: str


class PreferredFormatting(BaseModel):
    example: str
    type: str


class Title(BaseModel):
    type: str


class UserId1(BaseModel):
    type: str


class Properties47(BaseModel):
    body: Body6
    parent_id: ParentId
    parent_type: ParentType1
    preferred_formatting: PreferredFormatting
    title: Title
    user_id: UserId1


class Post(BaseModel):
    properties: Properties47
    type: str


class Properties46(BaseModel):
    commit: Commit
    post: Post


class PostPost(BaseModel):
    properties: Properties46
    type: str


class Properties48(BaseModel):
    observation_id: ObservationId


class PostProjectAdd(BaseModel):
    properties: Properties48
    type: str


class ProjectId(BaseModel):
    type: str


class Properties49(BaseModel):
    observation_id: ObservationId
    project_id: ProjectId


class PostProjectObservation(BaseModel):
    properties: Properties49
    type: str


class Agree(BaseModel):
    type: str


class Properties50(BaseModel):
    agree: Agree


class PostQuality(BaseModel):
    properties: Properties50
    type: str


class IconDelete(BaseModel):
    default: bool
    description: str
    type: str


class Description2(BaseModel):
    description: str
    type: str


class Email(BaseModel):
    type: str


class Icon(BaseModel):
    description: str
    type: str


class Locale(BaseModel):
    description: str
    type: str


class Login(BaseModel):
    type: str


class Name3(BaseModel):
    description: str
    type: str


class PlaceId1(BaseModel):
    description: str
    type: str


class TimeZone(BaseModel):
    description: str
    type: str


class Properties52(BaseModel):
    description: Description2
    email: Email
    icon: Icon
    locale: Locale
    login: Login
    name: Name3
    place_id: PlaceId1
    time_zone: TimeZone


class User5(BaseModel):
    properties: Properties52
    type: str


class Properties51(BaseModel):
    icon_delete: IconDelete
    user: User5


class PostUser(BaseModel):
    properties: Properties51
    type: str


class PreferredTaxonPageAncestorsShown(BaseModel):
    type: str


class PreferredTaxonPagePlaceId(BaseModel):
    type: str


class PreferredTaxonPageTab(BaseModel):
    type: str


class PrefersHideObsShowAnnotations(BaseModel):
    type: str


class PrefersHideObsShowCopyright(BaseModel):
    type: str


class PrefersHideObsShowIdentifiers(BaseModel):
    type: str


class PrefersHideObsShowObservationFields(BaseModel):
    type: str


class PrefersHideObsShowProjects(BaseModel):
    type: str


class PrefersHideObsShowQualityMetrics(BaseModel):
    type: str


class PrefersHideObsShowTags(BaseModel):
    type: str


class PrefersSkipCoarerIdModal(BaseModel):
    type: str


class Properties53(BaseModel):
    preferred_taxon_page_ancestors_shown: PreferredTaxonPageAncestorsShown
    preferred_taxon_page_place_id: PreferredTaxonPagePlaceId
    preferred_taxon_page_tab: PreferredTaxonPageTab
    prefers_hide_obs_show_annotations: PrefersHideObsShowAnnotations
    prefers_hide_obs_show_copyright: PrefersHideObsShowCopyright
    prefers_hide_obs_show_identifiers: PrefersHideObsShowIdentifiers
    prefers_hide_obs_show_observation_fields: PrefersHideObsShowObservationFields
    prefers_hide_obs_show_projects: PrefersHideObsShowProjects
    prefers_hide_obs_show_quality_metrics: PrefersHideObsShowQualityMetrics
    prefers_hide_obs_show_tags: PrefersHideObsShowTags
    prefers_skip_coarer_id_modal: PrefersSkipCoarerIdModal


class PostUserUpdateSession(BaseModel):
    properties: Properties53
    type: str


class Properties54(BaseModel):
    vote: Vote


class PostVote(BaseModel):
    properties: Properties54
    type: str


class Description3(BaseModel):
    type: str


class Slug(BaseModel):
    type: str


class Properties55(BaseModel):
    description: Description3
    id: Id
    slug: Slug
    title: Title


class Project(BaseModel):
    properties: Properties55
    type: str


class Role(BaseModel):
    enum: List[str]
    type: str


class TaxaCount(BaseModel):
    type: str


class User6(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Properties56(BaseModel):
    created_at: CreatedAt
    id: Id
    observations_count: ObservationsCount
    project_id: ProjectId
    role: Role
    taxa_count: TaxaCount
    updated_at: UpdatedAt
    user: User6


class ProjectMember(BaseModel):
    properties: Properties56
    type: str


class Items25(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Results7(BaseModel):
    items: Items25
    type: str


class Properties57(BaseModel):
    results: Results7


class AllOfItem9(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties57] = None
    required: Optional[List[str]] = None


class ProjectMembersResponse(BaseModel):
    allOf: List[AllOfItem9]


class Results8(BaseModel):
    items: Items25
    type: str


class Properties58(BaseModel):
    results: Results8


class AllOfItem10(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties58] = None
    required: Optional[List[str]] = None


class ProjectsResponse(BaseModel):
    allOf: List[AllOfItem10]


class Resolved(BaseModel):
    type: str


class Properties60(BaseModel):
    resolved: Resolved


class Flag2(BaseModel):
    properties: Properties60
    type: str


class Properties59(BaseModel):
    flag: Flag2


class PutFlag(BaseModel):
    properties: Properties59
    type: str


class Authority(BaseModel):
    description: str
    type: str


class Geoprivacy1(BaseModel):
    description: str
    type: str


class Iucn(BaseModel):
    description: str
    type: str


class SourceId(BaseModel):
    description: str
    type: str


class Status1(BaseModel):
    description: str
    type: str


class StatusName(BaseModel):
    description: str
    type: str


class Properties61(BaseModel):
    authority: Authority
    geoprivacy: Geoprivacy1
    iucn: Iucn
    source_id: SourceId
    status: Status1
    status_name: StatusName


class RawConservationStatus(BaseModel):
    properties: Properties61
    type: str


class Faves(BaseModel):
    items: Items25
    type: str


class Identifications(BaseModel):
    items: Items25
    type: str


class Properties62(BaseModel):
    faves: Faves
    identifications: Identifications


class AllOfItem11(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties62] = None
    type: Optional[str] = None


class ShowObservation(BaseModel):
    allOf: List[AllOfItem11]


class AdminLevel(BaseModel):
    type: str


class Items29(BaseModel):
    type: str


class AncestorPlaceIds(BaseModel):
    items: Items29
    type: str


class BboxArea(BaseModel):
    format: str
    type: str


class GeometryGeojson(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Name4(BaseModel):
    type: str


class PlaceType(BaseModel):
    type: str


class Properties63(BaseModel):
    admin_level: AdminLevel
    ancestor_place_ids: AncestorPlaceIds
    bbox_area: BboxArea
    geometry_geojson: GeometryGeojson
    location: Location
    name: Name4
    place_type: PlaceType


class AllOfItem12(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties63] = None
    type: Optional[str] = None


class ShowPlace(BaseModel):
    allOf: List[AllOfItem12]


class AncestorIds1(BaseModel):
    items: Items29
    type: str


class Items31(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Colors(BaseModel):
    items: Items31
    type: str


class ConservationStatuses(BaseModel):
    items: Items31
    type: str


class PreferredEstablishmentMeans(BaseModel):
    type: str


class Properties64(BaseModel):
    ancestor_ids: AncestorIds1
    colors: Colors
    conservation_status: ConservationStatus1
    conservation_statuses: ConservationStatuses
    default_photo: DefaultPhoto
    establishment_means: EstablishmentMeans2
    observations_count: ObservationsCount
    preferred_establishment_means: PreferredEstablishmentMeans


class AllOfItem13(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties64] = None
    type: Optional[str] = None


class ShowTaxon(BaseModel):
    allOf: List[AllOfItem13]


class Properties65(BaseModel):
    attribution: Attribution
    id: Id
    license_code: LicenseCode


class Sound(BaseModel):
    properties: Properties65
    type: str


class Count(BaseModel):
    type: str


class Properties67(BaseModel):
    count: Count
    taxon: Taxon


class Items33(BaseModel):
    properties: Properties67
    type: str


class Results9(BaseModel):
    items: Items33
    type: str


class Properties66(BaseModel):
    results: Results9


class AllOfItem14(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties66] = None
    required: Optional[List[str]] = None


class SpeciesCountsResponse(BaseModel):
    allOf: List[AllOfItem14]


class Items34(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Results10(BaseModel):
    items: Items34
    type: str


class Properties68(BaseModel):
    results: Results10


class AllOfItem15(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties68] = None
    required: Optional[List[str]] = None


class TaxaAutocompleteResponse(BaseModel):
    allOf: List[AllOfItem15]


class Results11(BaseModel):
    items: Items34
    type: str


class Properties69(BaseModel):
    results: Results11


class AllOfItem16(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties69] = None
    required: Optional[List[str]] = None


class TaxaShowResponse(BaseModel):
    allOf: List[AllOfItem16]


class Properties70(BaseModel):
    place: Place


class AllOfItem17(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties70] = None
    type: Optional[str] = None


class TaxonConservationStatus(BaseModel):
    allOf: List[AllOfItem17]


class MediumUrl(BaseModel):
    type: str


class SquareUrl(BaseModel):
    type: str


class Properties71(BaseModel):
    medium_url: MediumUrl
    square_url: SquareUrl


class AllOfItem18(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties71] = None
    type: Optional[str] = None


class TaxonPhoto(BaseModel):
    allOf: List[AllOfItem18]


class Data(BaseModel):
    type: str


class Items36(BaseModel):
    type: str


class Grid(BaseModel):
    items: Items36
    type: str


class Keys(BaseModel):
    items: Items36
    type: str


class Properties72(BaseModel):
    data: Data
    grid: Grid
    keys: Keys


class UTFGridResponse(BaseModel):
    properties: Properties72


class PrefersCuratorCoordinateAccess(BaseModel):
    type: str


class Properties74(BaseModel):
    observation_id: ObservationId
    prefers_curator_coordinate_access: PrefersCuratorCoordinateAccess
    project_id: ProjectId


class ProjectObservation(BaseModel):
    properties: Properties74
    type: str


class Properties73(BaseModel):
    project_observation: ProjectObservation


class UpdateProjectObservation(BaseModel):
    properties: Properties73
    type: str


class Icon1(BaseModel):
    type: str


class IconContentType(BaseModel):
    type: str


class IconFileName(BaseModel):
    type: str


class IconUrl(BaseModel):
    type: str


class Properties75(BaseModel):
    icon: Icon1
    icon_content_type: IconContentType
    icon_file_name: IconFileName
    icon_url: IconUrl
    id: Id
    login: Login
    name: Name4


class User7(BaseModel):
    properties: Properties75
    type: str


class User8(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Properties77(BaseModel):
    count: Count
    user: User8


class Items38(BaseModel):
    properties: Properties77
    type: str


class Results12(BaseModel):
    items: Items38
    type: str


class Properties76(BaseModel):
    results: Results12


class AllOfItem19(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    properties: Optional[Properties76] = None
    required: Optional[List[str]] = None


class UserCountsResponse(BaseModel):
    allOf: List[AllOfItem19]


class Definitions(BaseModel):
    AutocompleteTaxon: AutocompleteTaxon
    BaseResponse: BaseResponse
    Color: Color
    Comment: Comment
    ConservationStatus: ConservationStatus
    CorePlace: CorePlace
    CoreTaxon: CoreTaxon
    DateDetails: DateDetails
    Error: Error
    EstablishmentMeans: EstablishmentMeans
    Fave: Fave
    FieldValue: FieldValue
    Identification: Identification
    IdentificationsResponse: IdentificationsResponse
    Message: Message1
    MessagesResponse: MessagesResponse
    NearbyPlacesResponse: NearbyPlacesResponse
    NonOwnerIdentification: NonOwnerIdentification
    Observation: Observation
    ObservationTaxon: ObservationTaxon
    ObservationsObserversResponse: ObservationsObserversResponse
    ObservationsResponse: ObservationsResponse
    ObservationsShowResponse: ObservationsShowResponse
    Photo: Photo
    PlacesResponse: PlacesResponse
    PointGeoJson: PointGeoJson
    PolygonGeoJson: PolygonGeoJson
    PostAnnotation: PostAnnotation
    PostComment: PostComment
    PostFlag: PostFlag
    PostIdentification: PostIdentification
    PostMessage: PostMessage
    PostObservation: PostObservation
    PostObservationFieldValue: PostObservationFieldValue
    PostObservationPhoto: PostObservationPhoto
    PostObservationVote: PostObservationVote
    PostPost: PostPost
    PostProjectAdd: PostProjectAdd
    PostProjectObservation: PostProjectObservation
    PostQuality: PostQuality
    PostUser: PostUser
    PostUserUpdateSession: PostUserUpdateSession
    PostVote: PostVote
    Project: Project
    ProjectMember: ProjectMember
    ProjectMembersResponse: ProjectMembersResponse
    ProjectsResponse: ProjectsResponse
    PutFlag: PutFlag
    RawConservationStatus: RawConservationStatus
    ShowObservation: ShowObservation
    ShowPlace: ShowPlace
    ShowTaxon: ShowTaxon
    Sound: Sound
    SpeciesCountsResponse: SpeciesCountsResponse
    TaxaAutocompleteResponse: TaxaAutocompleteResponse
    TaxaShowResponse: TaxaShowResponse
    TaxonConservationStatus: TaxonConservationStatus
    TaxonPhoto: TaxonPhoto
    UTFGridResponse: UTFGridResponse
    UpdateProjectObservation: UpdateProjectObservation
    User: User7
    UserCountsResponse: UserCountsResponse


class Info(BaseModel):
    description: str
    title: str
    version: str


class Acc(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AccAbove(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AccBelow(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AccBelowOrUnknown(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AllNames(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AnnotationPathId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class Items39(BaseModel):
    type: str


class AnnotationUserId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class ApplyProjectRulesFor(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AssociatedPlaceId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class AutocompleteProjectId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class AutocompleteQ(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class AutocompleteQNotRequired(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Captive1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class CreatedAfter(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class CreatedD1(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class CreatedD2(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class CreatedDay(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    maximum: int
    minimum: int
    name: str
    type: str


class CreatedMonth(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    maximum: int
    minimum: int
    name: str
    type: str


class CreatedOn(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class CreatedYear(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class Cs(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Csa(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Csi(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class D1(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class D2(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class DateField(BaseModel):
    default: str
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class Day1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    maximum: int
    minimum: int
    name: str
    type: str


class Endemic1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Featured(BaseModel):
    description: str
    enum: List[bool]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Geo(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Geoprivacy2(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class HasParams(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class HasPosts(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Hrank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IconicTaxa(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Id14(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdAbove(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdBelow(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdPlease1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdentUserId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Identifications1(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Identified(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsCategory(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsCurrent(BaseModel):
    default: bool
    description: str
    enum: List[Union[bool, str]]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsCurrentTaxon(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsD1(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsD2(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsHrank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsIconicTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdsId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsIsChange(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsLrank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservationCreatedD1(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservationCreatedD2(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservationHrank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservationIconicTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdsObservationLrank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservationRank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsObservationTaxonActive(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservationTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdsObservedD1(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsObservedD2(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsOrderBy(BaseModel):
    default: str
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsOwnObservation(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsPlaceId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsQualityGrade(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsRank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsTaxonActive(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class IdsTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdsUserId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdsUserLogin(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class IdsWithoutObservationTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class IdsWithoutTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class Interval(BaseModel):
    default: str
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class Introduced1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Lat(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class License(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Licensed(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ListId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Lng(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Locale1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Lrank(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Mappable1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class MemberId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Month1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    maximum: int
    minimum: int
    name: str
    type: str


class Native1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Nelat(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class NelatRequired(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class Nelng(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class NelngRequired(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class NotId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class NotInProject(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class NotMatchingProjectRulesFor(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Noteworthy(BaseModel):
    description: str
    enum: List[bool]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ObservationAccuracyExperimentId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class ObservationsBy(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ObservedOn1(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class OfvDatatype(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    maximum: int
    minimum: int
    name: str
    type: str


class OnlyId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Order(BaseModel):
    default: str
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class OrderBy(BaseModel):
    default: str
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class OutOfRange1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Page1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ParentId2(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PathId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class PathMetric(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class PathMultiId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    required: bool
    type: str


class PathMultiIdOrSlug(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    required: bool
    type: str


class PathPlaceId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class PathTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class Pcid(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PerPage1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PerPageSpeciesCounts(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PhotoLicense(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class PhotoLicensed(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Photos1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PlaceId2(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Popular(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PostsLogin(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PostsProjectId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class PreferredPlaceId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ProjectId3(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class ProjectType(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ProjectsOrderBy(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ProjectsRadius(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ProjectsSiteId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Q(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class QualityGrade1(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Radius(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Rank1(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class RankLevel1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Reviewed(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class RuleDetails(BaseModel):
    description: str
    enum: List[bool]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class SearchOn(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class SearchQ(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Since(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class SiteId1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class SoundLicense(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Sounds1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Sources(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Swlat(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class SwlatRequired(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class Swlng(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class SwlngRequired(BaseModel):
    description: str
    format: str
    in_: str = Field(..., alias="in")
    name: str
    required: bool
    type: str


class TaxaOrderBy(BaseModel):
    default: str
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    name: str
    type: str


class TaxaTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class TaxonGeoprivacy1(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class TaxonId2(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class TaxonIsActive(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class TaxonName(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class TermId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class TermIdOrUnknown(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class TermValueId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Threatened1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class TileColor(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Ttl(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Type2(BaseModel):
    description: str
    enum: List[str]
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class UnobservedByUserId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class UpdatedSince(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class UserId2(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class UserLogin(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class Verifiable1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Viewed(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class ViewerId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class WithoutTaxonId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class WithoutTermId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class WithoutTermValueId(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    name: str
    type: str


class X(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    minimum: int
    name: str
    required: bool
    type: str


class Y(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    minimum: int
    name: str
    required: bool
    type: str


class Year1(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    items: Items39
    minimum: int
    name: str
    type: str


class Zoom(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    maximum: int
    minimum: int
    name: str
    required: bool
    type: str


class Parameters(BaseModel):
    acc: Acc
    acc_above: AccAbove
    acc_below: AccBelow
    acc_below_or_unknown: AccBelowOrUnknown
    all_names: AllNames
    annotation_path_id: AnnotationPathId
    annotation_user_id: AnnotationUserId
    apply_project_rules_for: ApplyProjectRulesFor
    associated_place_id: AssociatedPlaceId
    autocomplete_project_id: AutocompleteProjectId
    autocomplete_q: AutocompleteQ
    autocomplete_q_not_required: AutocompleteQNotRequired
    captive: Captive1
    created_after: CreatedAfter
    created_d1: CreatedD1
    created_d2: CreatedD2
    created_day: CreatedDay
    created_month: CreatedMonth
    created_on: CreatedOn
    created_year: CreatedYear
    cs: Cs
    csa: Csa
    csi: Csi
    d1: D1
    d2: D2
    date_field: DateField
    day: Day1
    endemic: Endemic1
    featured: Featured
    geo: Geo
    geoprivacy: Geoprivacy2
    has_params: HasParams
    has_posts: HasPosts
    hrank: Hrank
    iconic_taxa: IconicTaxa
    id: Id14
    id_above: IdAbove
    id_below: IdBelow
    id_please: IdPlease1
    ident_user_id: IdentUserId
    identifications: Identifications1
    identified: Identified
    ids_category: IdsCategory
    ids_current: IdsCurrent
    ids_current_taxon: IdsCurrentTaxon
    ids_d1: IdsD1
    ids_d2: IdsD2
    ids_hrank: IdsHrank
    ids_iconic_taxon_id: IdsIconicTaxonId
    ids_id: IdsId
    ids_is_change: IdsIsChange
    ids_lrank: IdsLrank
    ids_observation_created_d1: IdsObservationCreatedD1
    ids_observation_created_d2: IdsObservationCreatedD2
    ids_observation_hrank: IdsObservationHrank
    ids_observation_iconic_taxon_id: IdsObservationIconicTaxonId
    ids_observation_lrank: IdsObservationLrank
    ids_observation_rank: IdsObservationRank
    ids_observation_taxon_active: IdsObservationTaxonActive
    ids_observation_taxon_id: IdsObservationTaxonId
    ids_observed_d1: IdsObservedD1
    ids_observed_d2: IdsObservedD2
    ids_order_by: IdsOrderBy
    ids_own_observation: IdsOwnObservation
    ids_place_id: IdsPlaceId
    ids_quality_grade: IdsQualityGrade
    ids_rank: IdsRank
    ids_taxon_active: IdsTaxonActive
    ids_taxon_id: IdsTaxonId
    ids_user_id: IdsUserId
    ids_user_login: IdsUserLogin
    ids_without_observation_taxon_id: IdsWithoutObservationTaxonId
    ids_without_taxon_id: IdsWithoutTaxonId
    interval: Interval
    introduced: Introduced1
    lat: Lat
    license: License
    licensed: Licensed
    list_id: ListId
    lng: Lng
    locale: Locale1
    lrank: Lrank
    mappable: Mappable1
    member_id: MemberId
    month: Month1
    native: Native1
    nelat: Nelat
    nelat_required: NelatRequired
    nelng: Nelng
    nelng_required: NelngRequired
    not_id: NotId
    not_in_project: NotInProject
    not_matching_project_rules_for: NotMatchingProjectRulesFor
    noteworthy: Noteworthy
    observation_accuracy_experiment_id: ObservationAccuracyExperimentId
    observations_by: ObservationsBy
    observed_on: ObservedOn1
    ofv_datatype: OfvDatatype
    only_id: OnlyId
    order: Order
    order_by: OrderBy
    out_of_range: OutOfRange1
    page: Page1
    parent_id: ParentId2
    path_id: PathId
    path_metric: PathMetric
    path_multi_id: PathMultiId
    path_multi_id_or_slug: PathMultiIdOrSlug
    path_place_id: PathPlaceId
    path_taxon_id: PathTaxonId
    pcid: Pcid
    per_page: PerPage1
    per_page_species_counts: PerPageSpeciesCounts
    photo_license: PhotoLicense
    photo_licensed: PhotoLicensed
    photos: Photos1
    place_id: PlaceId2
    popular: Popular
    posts_login: PostsLogin
    posts_project_id: PostsProjectId
    preferred_place_id: PreferredPlaceId
    project_id: ProjectId3
    project_type: ProjectType
    projects_order_by: ProjectsOrderBy
    projects_radius: ProjectsRadius
    projects_site_id: ProjectsSiteId
    q: Q
    quality_grade: QualityGrade1
    radius: Radius
    rank: Rank1
    rank_level: RankLevel1
    reviewed: Reviewed
    rule_details: RuleDetails
    search_on: SearchOn
    search_q: SearchQ
    since: Since
    site_id: SiteId1
    sound_license: SoundLicense
    sounds: Sounds1
    sources: Sources
    swlat: Swlat
    swlat_required: SwlatRequired
    swlng: Swlng
    swlng_required: SwlngRequired
    taxa_order_by: TaxaOrderBy
    taxa_taxon_id: TaxaTaxonId
    taxon_geoprivacy: TaxonGeoprivacy1
    taxon_id: TaxonId2
    taxon_is_active: TaxonIsActive
    taxon_name: TaxonName
    term_id: TermId
    term_id_or_unknown: TermIdOrUnknown
    term_value_id: TermValueId
    threatened: Threatened1
    tile_color: TileColor
    ttl: Ttl
    type: Type2
    unobserved_by_user_id: UnobservedByUserId
    updated_since: UpdatedSince
    user_id: UserId2
    user_login: UserLogin
    verifiable: Verifiable1
    viewed: Viewed
    viewer_id: ViewerId
    without_taxon_id: WithoutTaxonId
    without_term_id: WithoutTermId
    without_term_value_id: WithoutTermValueId
    x: X
    y: Y
    year: Year1
    zoom: Zoom


class Schema(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Parameter(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema = Field(..., alias="schema")


class Field200(BaseModel):
    description: str


class Responses(BaseModel):
    field_200: Field200 = Field(..., alias="200")


class SecurityItem(BaseModel):
    api_token: List


class Post1(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter]
    responses: Responses
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldAnnotations(BaseModel):
    post: Post1


class Parameter1(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses1(BaseModel):
    field_200: Field200 = Field(..., alias="200")


class Delete(BaseModel):
    description: str
    parameters: List[Parameter1]
    responses: Responses1
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldAnnotationsId(BaseModel):
    delete: Delete


class Field2002(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses2(BaseModel):
    field_200: Field2002 = Field(..., alias="200")
    default: Default


class Get(BaseModel):
    description: str
    parameters: List[Parameter1]
    responses: Responses2
    summary: str
    tags: List[str]


class FieldColoredHeatmapZoomXYGridJson(BaseModel):
    get: Get


class Field2003(BaseModel):
    description: str


class Responses3(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Get1(BaseModel):
    description: str
    parameters: List[Parameter1]
    produces: List[str]
    responses: Responses3
    summary: str
    tags: List[str]


class FieldColoredHeatmapZoomXYPng(BaseModel):
    get: Get1


class Parameter4(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema = Field(..., alias="schema")


class Responses4(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Post2(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter4]
    responses: Responses4
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldComments(BaseModel):
    post: Post2


class Parameter5(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses5(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Delete1(BaseModel):
    description: str
    parameters: List[Parameter5]
    responses: Responses5
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter6(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema] = Field(None, alias="schema")


class Responses6(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Put(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter6]
    responses: Responses6
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldCommentsId(BaseModel):
    delete: Delete1
    put: Put


class Responses7(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Get2(BaseModel):
    description: str
    responses: Responses7
    summary: str
    tags: List[str]


class FieldControlledTerms(BaseModel):
    get: Get2


class Parameter7(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    minimum: int
    name: str
    required: bool
    type: str


class Responses8(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Get3(BaseModel):
    description: str
    parameters: List[Parameter7]
    responses: Responses8
    summary: str
    tags: List[str]


class FieldControlledTermsForTaxon(BaseModel):
    get: Get3


class Parameter8(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema = Field(..., alias="schema")


class Responses9(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Post3(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter8]
    responses: Responses9
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldFlags(BaseModel):
    post: Post3


class Parameter9(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses10(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Delete2(BaseModel):
    description: str
    parameters: List[Parameter9]
    responses: Responses10
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter10(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema] = Field(None, alias="schema")


class Responses11(BaseModel):
    field_200: Field2003 = Field(..., alias="200")


class Put1(BaseModel):
    description: str
    parameters: List[Parameter10]
    responses: Responses11
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldFlagsId(BaseModel):
    delete: Delete2
    put: Put1


class Parameter11(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20012(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default1(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses12(BaseModel):
    field_200: Field20012 = Field(..., alias="200")
    default: Default1


class Get4(BaseModel):
    description: str
    parameters: List[Parameter11]
    responses: Responses12
    summary: str
    tags: List[str]


class FieldGridZoomXYGridJson(BaseModel):
    get: Get4


class Field20013(BaseModel):
    description: str


class Responses13(BaseModel):
    field_200: Field20013 = Field(..., alias="200")


class Get5(BaseModel):
    description: str
    parameters: List[Parameter11]
    produces: List[str]
    responses: Responses13
    summary: str
    tags: List[str]


class FieldGridZoomXYPng(BaseModel):
    get: Get5


class Field20014(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default2(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses14(BaseModel):
    field_200: Field20014 = Field(..., alias="200")
    default: Default2


class Get6(BaseModel):
    description: str
    parameters: List[Parameter11]
    responses: Responses14
    summary: str
    tags: List[str]


class FieldHeatmapZoomXYGridJson(BaseModel):
    get: Get6


class Field20015(BaseModel):
    description: str


class Responses15(BaseModel):
    field_200: Field20015 = Field(..., alias="200")


class Get7(BaseModel):
    description: str
    parameters: List[Parameter11]
    produces: List[str]
    responses: Responses15
    summary: str
    tags: List[str]


class FieldHeatmapZoomXYPng(BaseModel):
    get: Get7


class Responses16(BaseModel):
    field_200: Field20015 = Field(..., alias="200")


class Get8(BaseModel):
    description: str
    parameters: List[Parameter11]
    responses: Responses16
    summary: str
    tags: List[str]


class Parameter16(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema = Field(..., alias="schema")


class Responses17(BaseModel):
    field_200: Field20015 = Field(..., alias="200")


class Post4(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter16]
    responses: Responses17
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldIdentifications(BaseModel):
    get: Get8
    post: Post4


class Parameter17(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses18(BaseModel):
    field_200: Field20015 = Field(..., alias="200")


class Get9(BaseModel):
    description: str
    parameters: List[Parameter17]
    responses: Responses18
    summary: str
    tags: List[str]


class FieldIdentificationsCategories(BaseModel):
    get: Get9


class Field20019(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default3(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses19(BaseModel):
    field_200: Field20019 = Field(..., alias="200")
    default: Default3


class Get10(BaseModel):
    description: str
    parameters: List[Parameter17]
    responses: Responses19
    summary: str
    tags: List[str]


class FieldIdentificationsIdentifiers(BaseModel):
    get: Get10


class Field20020(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default4(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses20(BaseModel):
    field_200: Field20020 = Field(..., alias="200")
    default: Default4


class Get11(BaseModel):
    description: str
    parameters: List[Parameter17]
    responses: Responses20
    summary: str
    tags: List[str]


class FieldIdentificationsObservers(BaseModel):
    get: Get11


class Field20021(BaseModel):
    description: str


class Responses21(BaseModel):
    field_200: Field20021 = Field(..., alias="200")


class Get12(BaseModel):
    description: str
    parameters: List[Parameter17]
    responses: Responses21
    summary: str
    tags: List[str]


class FieldIdentificationsRecentTaxa(BaseModel):
    get: Get12


class Parameter21(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    minimum: Optional[int] = None
    name: Optional[str] = None
    required: Optional[bool] = None
    type: Optional[str] = None


class Responses22(BaseModel):
    field_200: Field20021 = Field(..., alias="200")


class Get13(BaseModel):
    description: str
    parameters: List[Parameter21]
    responses: Responses22
    summary: str
    tags: List[str]


class FieldIdentificationsSimilarSpecies(BaseModel):
    get: Get13


class Parameter22(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    default: Optional[str] = None
    description: Optional[str] = None
    enum: Optional[List[str]] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Field20023(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default5(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses23(BaseModel):
    field_200: Field20023 = Field(..., alias="200")
    default: Default5


class Get14(BaseModel):
    description: str
    parameters: List[Parameter22]
    responses: Responses23
    summary: str
    tags: List[str]


class FieldIdentificationsSpeciesCounts(BaseModel):
    get: Get14


class Parameter23(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20024(BaseModel):
    description: str


class Responses24(BaseModel):
    field_200: Field20024 = Field(..., alias="200")


class Delete3(BaseModel):
    description: str
    parameters: List[Parameter23]
    responses: Responses24
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Responses25(BaseModel):
    field_200: Field20024 = Field(..., alias="200")


class Get15(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter23]
    responses: Responses25
    summary: str
    tags: List[str]


class Parameter25(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema] = Field(None, alias="schema")


class Responses26(BaseModel):
    field_200: Field20024 = Field(..., alias="200")


class Put2(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter25]
    responses: Responses26
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldIdentificationsId(BaseModel):
    delete: Delete3
    get: Get15
    put: Put2


class Parameter26(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    default: Optional[Union[bool, str]] = None
    description: Optional[str] = None
    enum: Optional[List[str]] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Default6(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses27(BaseModel):
    field_200: Field20024 = Field(..., alias="200")
    default: Default6


class Get16(BaseModel):
    description: str
    parameters: List[Parameter26]
    responses: Responses27
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter27(BaseModel):
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema = Field(..., alias="schema")


class Field20028(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Default7(BaseModel):
    description: str
    schema_: Schema = Field(..., alias="schema")


class Responses28(BaseModel):
    field_200: Field20028 = Field(..., alias="200")
    default: Default7


class Post5(BaseModel):
    description: str
    parameters: List[Parameter27]
    responses: Responses28
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldMessages(BaseModel):
    get: Get16
    post: Post5


class Count2(BaseModel):
    description: str
    type: str


class Properties78(BaseModel):
    count: Count2


class Schema23(BaseModel):
    properties: Properties78


class Field20029(BaseModel):
    description: str
    schema_: Schema23 = Field(..., alias="schema")


class Schema24(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Default8(BaseModel):
    description: str
    schema_: Schema24 = Field(..., alias="schema")


class Responses29(BaseModel):
    field_200: Field20029 = Field(..., alias="200")
    default: Default8


class Get17(BaseModel):
    responses: Responses29
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldMessagesUnread(BaseModel):
    get: Get17


class Parameter28(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20030(BaseModel):
    description: str


class Field404(BaseModel):
    description: str


class Default9(BaseModel):
    description: str
    schema_: Schema24 = Field(..., alias="schema")


class Responses30(BaseModel):
    field_200: Field20030 = Field(..., alias="200")
    field_404: Field404 = Field(..., alias="404")
    default: Default9


class Delete4(BaseModel):
    description: str
    parameters: List[Parameter28]
    responses: Responses30
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FlaggableMessageId(BaseModel):
    description: str
    type: str


class ReplyToUser(BaseModel):
    field_ref: str = Field(..., alias="$ref")
    description: str


class Items90(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Results13(BaseModel):
    items: Items90
    type: str


class Properties79(BaseModel):
    flaggable_message_id: FlaggableMessageId
    reply_to_user: ReplyToUser
    results: Results13
    thread_id: ThreadId


class Schema26(BaseModel):
    properties: Properties79


class Field20031(BaseModel):
    description: str
    schema_: Schema26 = Field(..., alias="schema")


class Schema27(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Default10(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses31(BaseModel):
    field_200: Field20031 = Field(..., alias="200")
    default: Default10


class Get18(BaseModel):
    description: str
    parameters: List[Parameter28]
    responses: Responses31
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldMessagesId(BaseModel):
    delete: Delete4
    get: Get18


class Parameter30(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema27 = Field(..., alias="schema")


class Field20032(BaseModel):
    description: str


class Responses32(BaseModel):
    field_200: Field20032 = Field(..., alias="200")


class Post6(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter30]
    responses: Responses32
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationFieldValues(BaseModel):
    post: Post6


class Parameter31(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses33(BaseModel):
    field_200: Field20032 = Field(..., alias="200")


class Delete5(BaseModel):
    description: str
    parameters: List[Parameter31]
    responses: Responses33
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter32(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses34(BaseModel):
    field_200: Field20032 = Field(..., alias="200")


class Put3(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter32]
    responses: Responses34
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationFieldValuesId(BaseModel):
    delete: Delete5
    put: Put3


class Parameter33(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Responses35(BaseModel):
    field_200: Field20032 = Field(..., alias="200")


class Post7(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter33]
    responses: Responses35
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationPhotos(BaseModel):
    post: Post7


class Parameter34(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses36(BaseModel):
    field_200: Field20032 = Field(..., alias="200")


class Delete6(BaseModel):
    description: str
    parameters: List[Parameter34]
    responses: Responses36
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter35(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Responses37(BaseModel):
    field_200: Field20032 = Field(..., alias="200")


class Put4(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter35]
    responses: Responses37
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationPhotosId(BaseModel):
    delete: Delete6
    put: Put4


class Parameter36(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20038(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default11(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses38(BaseModel):
    field_200: Field20038 = Field(..., alias="200")
    default: Default11


class Get19(BaseModel):
    description: str
    parameters: List[Parameter36]
    responses: Responses38
    summary: str
    tags: List[str]


class Parameter37(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema27 = Field(..., alias="schema")


class Field20039(BaseModel):
    description: str


class Responses39(BaseModel):
    field_200: Field20039 = Field(..., alias="200")


class Post8(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter37]
    responses: Responses39
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservations(BaseModel):
    get: Get19
    post: Post8


class Parameter38(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses40(BaseModel):
    field_200: Field20039 = Field(..., alias="200")


class Get20(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses40
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsDeleted(BaseModel):
    get: Get20


class Default12(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses41(BaseModel):
    field_200: Field20039 = Field(..., alias="200")
    default: Default12


class Get21(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses41
    summary: str
    tags: List[str]


class FieldObservationsHistogram(BaseModel):
    get: Get21


class Field20042(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default13(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses42(BaseModel):
    field_200: Field20042 = Field(..., alias="200")
    default: Default13


class Get22(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses42
    summary: str
    tags: List[str]


class FieldObservationsIdentifiers(BaseModel):
    get: Get22


class Field20043(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default14(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses43(BaseModel):
    field_200: Field20043 = Field(..., alias="200")
    default: Default14


class Get23(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses43
    summary: str
    tags: List[str]


class FieldObservationsObservers(BaseModel):
    get: Get23


class Field20044(BaseModel):
    description: str


class Responses44(BaseModel):
    field_200: Field20044 = Field(..., alias="200")


class Get24(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses44
    summary: str
    tags: List[str]


class FieldObservationsPopularFieldValues(BaseModel):
    get: Get24


class Field20045(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default15(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses45(BaseModel):
    field_200: Field20045 = Field(..., alias="200")
    default: Default15


class Get25(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses45
    summary: str
    tags: List[str]


class FieldObservationsSpeciesCounts(BaseModel):
    get: Get25


class Field20046(BaseModel):
    description: str


class Responses46(BaseModel):
    field_200: Field20046 = Field(..., alias="200")


class Get26(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses46
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsUpdates(BaseModel):
    get: Get26


class Responses47(BaseModel):
    field_200: Field20046 = Field(..., alias="200")


class Delete7(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses47
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Field20048(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default16(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses48(BaseModel):
    field_200: Field20048 = Field(..., alias="200")
    default: Default16


class Get27(BaseModel):
    description: str
    parameters: List[Parameter38]
    responses: Responses48
    summary: str
    tags: List[str]


class Parameter47(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Field20049(BaseModel):
    description: str


class Responses49(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Put5(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter47]
    responses: Responses49
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsId(BaseModel):
    delete: Delete7
    get: Get27
    put: Put5


class Parameter48(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses50(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Post9(BaseModel):
    description: str
    parameters: List[Parameter48]
    responses: Responses50
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdFave(BaseModel):
    post: Post9


class Responses51(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Delete8(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter48]
    responses: Responses51
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter50(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses52(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Post10(BaseModel):
    description: str
    parameters: List[Parameter50]
    responses: Responses52
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdQualityMetric(BaseModel):
    delete: Delete8
    post: Post10


class Parameter51(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses53(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Post11(BaseModel):
    description: str
    parameters: List[Parameter51]
    responses: Responses53
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdReview(BaseModel):
    post: Post11


class Responses54(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Get28(BaseModel):
    description: str
    parameters: List[Parameter51]
    responses: Responses54
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdSubscriptions(BaseModel):
    get: Get28


class Responses55(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Get29(BaseModel):
    description: str
    parameters: List[Parameter51]
    responses: Responses55
    summary: str
    tags: List[str]


class FieldObservationsIdTaxonSummary(BaseModel):
    get: Get29


class Responses56(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Delete9(BaseModel):
    description: str
    parameters: List[Parameter51]
    responses: Responses56
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdUnfave(BaseModel):
    delete: Delete9


class Responses57(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Post12(BaseModel):
    description: str
    parameters: List[Parameter51]
    responses: Responses57
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdUnreview(BaseModel):
    post: Post12


class Responses58(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Put6(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter51]
    responses: Responses58
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldObservationsIdViewedUpdates(BaseModel):
    put: Put6


class Parameter57(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    type: str


class Responses59(BaseModel):
    field_200: Field20049 = Field(..., alias="200")


class Post13(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter57]
    responses: Responses59
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldPhotos(BaseModel):
    post: Post13


class Parameter58(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    enum: Optional[List[str]] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Field20060(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default17(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses60(BaseModel):
    field_200: Field20060 = Field(..., alias="200")
    default: Default17


class Get30(BaseModel):
    description: str
    parameters: List[Parameter58]
    responses: Responses60
    summary: str
    tags: List[str]


class FieldPlacesAutocomplete(BaseModel):
    get: Get30


class Parameter59(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Field20061(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default18(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses61(BaseModel):
    field_200: Field20061 = Field(..., alias="200")
    default: Default18


class Get31(BaseModel):
    description: str
    parameters: List[Parameter59]
    responses: Responses61
    summary: str
    tags: List[str]


class FieldPlacesNearby(BaseModel):
    get: Get31


class Items91(BaseModel):
    type: str


class Parameter60(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    enum: Optional[List[int]] = None
    in_: Optional[str] = Field(None, alias="in")
    items: Optional[Items91] = None
    name: Optional[str] = None
    type: Optional[str] = None


class Field20062(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default19(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses62(BaseModel):
    field_200: Field20062 = Field(..., alias="200")
    default: Default19


class Get32(BaseModel):
    description: str
    parameters: List[Parameter60]
    responses: Responses62
    summary: str
    tags: List[str]


class FieldPlacesId(BaseModel):
    get: Get32


class Parameter61(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20063(BaseModel):
    description: str


class Responses63(BaseModel):
    field_200: Field20063 = Field(..., alias="200")


class Get33(BaseModel):
    description: str
    parameters: List[Parameter61]
    produces: List[str]
    responses: Responses63
    summary: str
    tags: List[str]


class FieldPlacesPlaceIdZoomXYPng(BaseModel):
    get: Get33


class Field20064(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default20(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses64(BaseModel):
    field_200: Field20064 = Field(..., alias="200")
    default: Default20


class Get34(BaseModel):
    description: str
    parameters: List[Parameter61]
    responses: Responses64
    summary: str
    tags: List[str]


class FieldPointsZoomXYGridJson(BaseModel):
    get: Get34


class Field20065(BaseModel):
    description: str


class Responses65(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Get35(BaseModel):
    description: str
    parameters: List[Parameter61]
    produces: List[str]
    responses: Responses65
    summary: str
    tags: List[str]


class FieldPointsZoomXYPng(BaseModel):
    get: Get35


class Responses66(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Get36(BaseModel):
    description: str
    parameters: List[Parameter61]
    responses: Responses66
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter65(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses67(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Post14(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter65]
    responses: Responses67
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldPosts(BaseModel):
    get: Get36
    post: Post14


class Parameter66(BaseModel):
    description: Optional[str] = None
    format: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None
    field_ref: Optional[str] = Field(None, alias="$ref")


class Responses68(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Get37(BaseModel):
    description: str
    parameters: List[Parameter66]
    responses: Responses68
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldPostsForUser(BaseModel):
    get: Get37


class Parameter67(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses69(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Delete10(BaseModel):
    description: str
    parameters: List[Parameter67]
    responses: Responses69
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter68(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses70(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Put7(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter68]
    responses: Responses70
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldPostsId(BaseModel):
    delete: Delete10
    put: Put7


class Parameter69(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses71(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Post15(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter69]
    responses: Responses71
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectObservations(BaseModel):
    post: Post15


class Parameter70(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses72(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Delete11(BaseModel):
    description: str
    parameters: List[Parameter70]
    responses: Responses72
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Parameter71(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses73(BaseModel):
    field_200: Field20065 = Field(..., alias="200")


class Put8(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter71]
    responses: Responses73
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectObservationsId(BaseModel):
    delete: Delete11
    put: Put8


class Parameter72(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20074(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default21(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses74(BaseModel):
    field_200: Field20074 = Field(..., alias="200")
    default: Default21


class Get38(BaseModel):
    description: str
    parameters: List[Parameter72]
    responses: Responses74
    summary: str
    tags: List[str]


class FieldProjects(BaseModel):
    get: Get38


class Field20075(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default22(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses75(BaseModel):
    field_200: Field20075 = Field(..., alias="200")
    default: Default22


class Get39(BaseModel):
    description: str
    parameters: List[Parameter72]
    responses: Responses75
    summary: str
    tags: List[str]


class FieldProjectsAutocomplete(BaseModel):
    get: Get39


class Field20076(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default23(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses76(BaseModel):
    field_200: Field20076 = Field(..., alias="200")
    default: Default23


class Get40(BaseModel):
    description: str
    parameters: List[Parameter72]
    responses: Responses76
    summary: str
    tags: List[str]


class FieldProjectsId(BaseModel):
    get: Get40


class Parameter75(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Field20077(BaseModel):
    description: str


class Responses77(BaseModel):
    field_200: Field20077 = Field(..., alias="200")


class Post16(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter75]
    responses: Responses77
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectsIdAdd(BaseModel):
    post: Post16


class Parameter76(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses78(BaseModel):
    field_200: Field20077 = Field(..., alias="200")


class Post17(BaseModel):
    description: str
    parameters: List[Parameter76]
    responses: Responses78
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectsIdJoin(BaseModel):
    post: Post17


class Responses79(BaseModel):
    field_200: Field20077 = Field(..., alias="200")


class Delete12(BaseModel):
    description: str
    parameters: List[Parameter76]
    responses: Responses79
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectsIdLeave(BaseModel):
    delete: Delete12


class Parameter78(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    enum: Optional[List[str]] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Field20080(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default24(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses80(BaseModel):
    field_200: Field20080 = Field(..., alias="200")
    default: Default24


class Get41(BaseModel):
    description: str
    parameters: List[Parameter78]
    responses: Responses80
    summary: str
    tags: List[str]


class FieldProjectsIdMembers(BaseModel):
    get: Get41


class Parameter79(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20081(BaseModel):
    description: str


class Responses81(BaseModel):
    field_200: Field20081 = Field(..., alias="200")


class Get42(BaseModel):
    description: str
    parameters: List[Parameter79]
    responses: Responses81
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectsIdMembership(BaseModel):
    get: Get42


class Parameter80(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses82(BaseModel):
    field_200: Field20081 = Field(..., alias="200")


class Delete13(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter80]
    responses: Responses82
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectsIdRemove(BaseModel):
    delete: Delete13


class Parameter81(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses83(BaseModel):
    field_200: Field20081 = Field(..., alias="200")


class Get43(BaseModel):
    deprecated: bool
    description: str
    parameters: List[Parameter81]
    responses: Responses83
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldProjectsIdSubscriptions(BaseModel):
    get: Get43


class Responses84(BaseModel):
    field_200: Field20081 = Field(..., alias="200")


class Get44(BaseModel):
    description: str
    parameters: List[Parameter81]
    responses: Responses84
    summary: str
    tags: List[str]


class FieldSearch(BaseModel):
    get: Get44


class Responses85(BaseModel):
    field_200: Field20081 = Field(..., alias="200")


class Post18(BaseModel):
    description: str
    parameters: List[Parameter81]
    responses: Responses85
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldSubscriptionsObservationIdSubscribe(BaseModel):
    post: Post18


class Responses86(BaseModel):
    field_200: Field20081 = Field(..., alias="200")


class Post19(BaseModel):
    description: str
    parameters: List[Parameter81]
    responses: Responses86
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldSubscriptionsProjectIdSubscribe(BaseModel):
    post: Post19


class Parameter85(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    type: Optional[str] = None


class Field20087(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default25(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses87(BaseModel):
    field_200: Field20087 = Field(..., alias="200")
    default: Default25


class Get45(BaseModel):
    description: str
    parameters: List[Parameter85]
    responses: Responses87
    summary: str
    tags: List[str]


class FieldTaxa(BaseModel):
    get: Get45


class Field20088(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default26(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses88(BaseModel):
    field_200: Field20088 = Field(..., alias="200")
    default: Default26


class Get46(BaseModel):
    description: str
    parameters: List[Parameter85]
    responses: Responses88
    summary: str
    tags: List[str]


class FieldTaxaAutocomplete(BaseModel):
    get: Get46


class Parameter87(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Field20089(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Default27(BaseModel):
    description: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses89(BaseModel):
    field_200: Field20089 = Field(..., alias="200")
    default: Default27


class Get47(BaseModel):
    description: str
    parameters: List[Parameter87]
    responses: Responses89
    summary: str
    tags: List[str]


class FieldTaxaId(BaseModel):
    get: Get47


class Field20090(BaseModel):
    description: str


class Responses90(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Get48(BaseModel):
    description: str
    parameters: List[Parameter87]
    produces: List[str]
    responses: Responses90
    summary: str
    tags: List[str]


class FieldTaxonPlacesTaxonIdZoomXYPng(BaseModel):
    get: Get48


class Responses91(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Get49(BaseModel):
    description: str
    parameters: List[Parameter87]
    produces: List[str]
    responses: Responses91
    summary: str
    tags: List[str]


class FieldTaxonRangesTaxonIdZoomXYPng(BaseModel):
    get: Get49


class Responses92(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Get50(BaseModel):
    description: str
    parameters: List[Parameter87]
    responses: Responses92
    summary: str
    tags: List[str]


class FieldUsersAutocomplete(BaseModel):
    get: Get50


class Responses93(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Get51(BaseModel):
    description: str
    responses: Responses93
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldUsersMe(BaseModel):
    get: Get51


class Responses94(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Post20(BaseModel):
    consumes: List[str]
    description: str
    responses: Responses94
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldUsersResendConfirmation(BaseModel):
    post: Post20


class Parameter91(BaseModel):
    description: str
    in_: str = Field(..., alias="in")
    name: str
    schema_: Schema27 = Field(..., alias="schema")


class Responses95(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Put9(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter91]
    responses: Responses95
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldUsersUpdateSession(BaseModel):
    put: Put9


class Parameter92(BaseModel):
    field_ref: str = Field(..., alias="$ref")


class Responses96(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Get52(BaseModel):
    description: str
    parameters: List[Parameter92]
    responses: Responses96
    summary: str
    tags: List[str]


class Responses97(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Put10(BaseModel):
    consumes: List[str]
    description: str
    parameters: List[Parameter92]
    responses: Responses97
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldUsersId(BaseModel):
    get: Get52
    put: Put10


class Responses98(BaseModel):
    field_200: Field20090 = Field(..., alias="200")
    field_404: Field404 = Field(..., alias="404")


class Delete14(BaseModel):
    description: str
    parameters: List[Parameter92]
    responses: Responses98
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class Responses99(BaseModel):
    field_200: Field20090 = Field(..., alias="200")
    field_404: Field404 = Field(..., alias="404")


class Post21(BaseModel):
    description: str
    parameters: List[Parameter92]
    responses: Responses99
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldUsersIdMute(BaseModel):
    delete: Delete14
    post: Post21


class Responses100(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Get53(BaseModel):
    description: str
    parameters: List[Parameter92]
    responses: Responses100
    summary: str
    tags: List[str]


class FieldUsersIdProjects(BaseModel):
    get: Get53


class Responses101(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Delete15(BaseModel):
    description: str
    parameters: List[Parameter92]
    responses: Responses101
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldVotesUnvoteAnnotationId(BaseModel):
    delete: Delete15


class Parameter98(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses102(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Delete16(BaseModel):
    description: str
    parameters: List[Parameter98]
    responses: Responses102
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldVotesUnvoteObservationId(BaseModel):
    delete: Delete16


class Parameter99(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses103(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Post22(BaseModel):
    description: str
    parameters: List[Parameter99]
    responses: Responses103
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldVotesVoteAnnotationId(BaseModel):
    post: Post22


class Parameter100(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    in_: Optional[str] = Field(None, alias="in")
    name: Optional[str] = None
    schema_: Optional[Schema27] = Field(None, alias="schema")


class Responses104(BaseModel):
    field_200: Field20090 = Field(..., alias="200")


class Post23(BaseModel):
    description: str
    parameters: List[Parameter100]
    responses: Responses104
    security: List[SecurityItem]
    summary: str
    tags: List[str]


class FieldVotesVoteObservationId(BaseModel):
    post: Post23


class Paths(BaseModel):
    field_annotations: FieldAnnotations = Field(..., alias="/annotations")
    field_annotations__id_: FieldAnnotationsId = Field(..., alias="/annotations/{id}")
    field_colored_heatmap__zoom___x___y__grid_json: FieldColoredHeatmapZoomXYGridJson = Field(
        ..., alias="/colored_heatmap/{zoom}/{x}/{y}.grid.json"
    )
    field_colored_heatmap__zoom___x___y__png: FieldColoredHeatmapZoomXYPng = Field(
        ..., alias="/colored_heatmap/{zoom}/{x}/{y}.png"
    )
    field_comments: FieldComments = Field(..., alias="/comments")
    field_comments__id_: FieldCommentsId = Field(..., alias="/comments/{id}")
    field_controlled_terms: FieldControlledTerms = Field(..., alias="/controlled_terms")
    field_controlled_terms_for_taxon: FieldControlledTermsForTaxon = Field(
        ..., alias="/controlled_terms/for_taxon"
    )
    field_flags: FieldFlags = Field(..., alias="/flags")
    field_flags__id_: FieldFlagsId = Field(..., alias="/flags/{id}")
    field_grid__zoom___x___y__grid_json: FieldGridZoomXYGridJson = Field(
        ..., alias="/grid/{zoom}/{x}/{y}.grid.json"
    )
    field_grid__zoom___x___y__png: FieldGridZoomXYPng = Field(
        ..., alias="/grid/{zoom}/{x}/{y}.png"
    )
    field_heatmap__zoom___x___y__grid_json: FieldHeatmapZoomXYGridJson = Field(
        ..., alias="/heatmap/{zoom}/{x}/{y}.grid.json"
    )
    field_heatmap__zoom___x___y__png: FieldHeatmapZoomXYPng = Field(
        ..., alias="/heatmap/{zoom}/{x}/{y}.png"
    )
    field_identifications: FieldIdentifications = Field(..., alias="/identifications")
    field_identifications_categories: FieldIdentificationsCategories = Field(
        ..., alias="/identifications/categories"
    )
    field_identifications_identifiers: FieldIdentificationsIdentifiers = Field(
        ..., alias="/identifications/identifiers"
    )
    field_identifications_observers: FieldIdentificationsObservers = Field(
        ..., alias="/identifications/observers"
    )
    field_identifications_recent_taxa: FieldIdentificationsRecentTaxa = Field(
        ..., alias="/identifications/recent_taxa"
    )
    field_identifications_similar_species: FieldIdentificationsSimilarSpecies = Field(
        ..., alias="/identifications/similar_species"
    )
    field_identifications_species_counts: FieldIdentificationsSpeciesCounts = Field(
        ..., alias="/identifications/species_counts"
    )
    field_identifications__id_: FieldIdentificationsId = Field(
        ..., alias="/identifications/{id}"
    )
    field_messages: FieldMessages = Field(..., alias="/messages")
    field_messages_unread: FieldMessagesUnread = Field(..., alias="/messages/unread")
    field_messages__id_: FieldMessagesId = Field(..., alias="/messages/{id}")
    field_observation_field_values: FieldObservationFieldValues = Field(
        ..., alias="/observation_field_values"
    )
    field_observation_field_values__id_: FieldObservationFieldValuesId = Field(
        ..., alias="/observation_field_values/{id}"
    )
    field_observation_photos: FieldObservationPhotos = Field(
        ..., alias="/observation_photos"
    )
    field_observation_photos__id_: FieldObservationPhotosId = Field(
        ..., alias="/observation_photos/{id}"
    )
    field_observations: FieldObservations = Field(..., alias="/observations")
    field_observations_deleted: FieldObservationsDeleted = Field(
        ..., alias="/observations/deleted"
    )
    field_observations_histogram: FieldObservationsHistogram = Field(
        ..., alias="/observations/histogram"
    )
    field_observations_identifiers: FieldObservationsIdentifiers = Field(
        ..., alias="/observations/identifiers"
    )
    field_observations_observers: FieldObservationsObservers = Field(
        ..., alias="/observations/observers"
    )
    field_observations_popular_field_values: FieldObservationsPopularFieldValues = (
        Field(..., alias="/observations/popular_field_values")
    )
    field_observations_species_counts: FieldObservationsSpeciesCounts = Field(
        ..., alias="/observations/species_counts"
    )
    field_observations_updates: FieldObservationsUpdates = Field(
        ..., alias="/observations/updates"
    )
    field_observations__id_: FieldObservationsId = Field(
        ..., alias="/observations/{id}"
    )
    field_observations__id__fave: FieldObservationsIdFave = Field(
        ..., alias="/observations/{id}/fave"
    )
    field_observations__id__quality__metric_: FieldObservationsIdQualityMetric = Field(
        ..., alias="/observations/{id}/quality/{metric}"
    )
    field_observations__id__review: FieldObservationsIdReview = Field(
        ..., alias="/observations/{id}/review"
    )
    field_observations__id__subscriptions: FieldObservationsIdSubscriptions = Field(
        ..., alias="/observations/{id}/subscriptions"
    )
    field_observations__id__taxon_summary: FieldObservationsIdTaxonSummary = Field(
        ..., alias="/observations/{id}/taxon_summary"
    )
    field_observations__id__unfave: FieldObservationsIdUnfave = Field(
        ..., alias="/observations/{id}/unfave"
    )
    field_observations__id__unreview: FieldObservationsIdUnreview = Field(
        ..., alias="/observations/{id}/unreview"
    )
    field_observations__id__viewed_updates: FieldObservationsIdViewedUpdates = Field(
        ..., alias="/observations/{id}/viewed_updates"
    )
    field_photos: FieldPhotos = Field(..., alias="/photos")
    field_places_autocomplete: FieldPlacesAutocomplete = Field(
        ..., alias="/places/autocomplete"
    )
    field_places_nearby: FieldPlacesNearby = Field(..., alias="/places/nearby")
    field_places__id_: FieldPlacesId = Field(..., alias="/places/{id}")
    field_places__place_id___zoom___x___y__png: FieldPlacesPlaceIdZoomXYPng = Field(
        ..., alias="/places/{place_id}/{zoom}/{x}/{y}.png"
    )
    field_points__zoom___x___y__grid_json: FieldPointsZoomXYGridJson = Field(
        ..., alias="/points/{zoom}/{x}/{y}.grid.json"
    )
    field_points__zoom___x___y__png: FieldPointsZoomXYPng = Field(
        ..., alias="/points/{zoom}/{x}/{y}.png"
    )
    field_posts: FieldPosts = Field(..., alias="/posts")
    field_posts_for_user: FieldPostsForUser = Field(..., alias="/posts/for_user")
    field_posts__id_: FieldPostsId = Field(..., alias="/posts/{id}")
    field_project_observations: FieldProjectObservations = Field(
        ..., alias="/project_observations"
    )
    field_project_observations__id_: FieldProjectObservationsId = Field(
        ..., alias="/project_observations/{id}"
    )
    field_projects: FieldProjects = Field(..., alias="/projects")
    field_projects_autocomplete: FieldProjectsAutocomplete = Field(
        ..., alias="/projects/autocomplete"
    )
    field_projects__id_: FieldProjectsId = Field(..., alias="/projects/{id}")
    field_projects__id__add: FieldProjectsIdAdd = Field(..., alias="/projects/{id}/add")
    field_projects__id__join: FieldProjectsIdJoin = Field(
        ..., alias="/projects/{id}/join"
    )
    field_projects__id__leave: FieldProjectsIdLeave = Field(
        ..., alias="/projects/{id}/leave"
    )
    field_projects__id__members: FieldProjectsIdMembers = Field(
        ..., alias="/projects/{id}/members"
    )
    field_projects__id__membership: FieldProjectsIdMembership = Field(
        ..., alias="/projects/{id}/membership"
    )
    field_projects__id__remove: FieldProjectsIdRemove = Field(
        ..., alias="/projects/{id}/remove"
    )
    field_projects__id__subscriptions: FieldProjectsIdSubscriptions = Field(
        ..., alias="/projects/{id}/subscriptions"
    )
    field_search: FieldSearch = Field(..., alias="/search")
    field_subscriptions_observation__id__subscribe: FieldSubscriptionsObservationIdSubscribe = Field(
        ..., alias="/subscriptions/observation/{id}/subscribe"
    )
    field_subscriptions_project__id__subscribe: FieldSubscriptionsProjectIdSubscribe = (
        Field(..., alias="/subscriptions/project/{id}/subscribe")
    )
    field_taxa: FieldTaxa = Field(..., alias="/taxa")
    field_taxa_autocomplete: FieldTaxaAutocomplete = Field(
        ..., alias="/taxa/autocomplete"
    )
    field_taxa__id_: FieldTaxaId = Field(..., alias="/taxa/{id}")
    field_taxon_places__taxon_id___zoom___x___y__png: FieldTaxonPlacesTaxonIdZoomXYPng = Field(
        ..., alias="/taxon_places/{taxon_id}/{zoom}/{x}/{y}.png"
    )
    field_taxon_ranges__taxon_id___zoom___x___y__png: FieldTaxonRangesTaxonIdZoomXYPng = Field(
        ..., alias="/taxon_ranges/{taxon_id}/{zoom}/{x}/{y}.png"
    )
    field_users_autocomplete: FieldUsersAutocomplete = Field(
        ..., alias="/users/autocomplete"
    )
    field_users_me: FieldUsersMe = Field(..., alias="/users/me")
    field_users_resend_confirmation: FieldUsersResendConfirmation = Field(
        ..., alias="/users/resend_confirmation"
    )
    field_users_update_session: FieldUsersUpdateSession = Field(
        ..., alias="/users/update_session"
    )
    field_users__id_: FieldUsersId = Field(..., alias="/users/{id}")
    field_users__id__mute: FieldUsersIdMute = Field(..., alias="/users/{id}/mute")
    field_users__id__projects: FieldUsersIdProjects = Field(
        ..., alias="/users/{id}/projects"
    )
    field_votes_unvote_annotation__id_: FieldVotesUnvoteAnnotationId = Field(
        ..., alias="/votes/unvote/annotation/{id}"
    )
    field_votes_unvote_observation__id_: FieldVotesUnvoteObservationId = Field(
        ..., alias="/votes/unvote/observation/{id}"
    )
    field_votes_vote_annotation__id_: FieldVotesVoteAnnotationId = Field(
        ..., alias="/votes/vote/annotation/{id}"
    )
    field_votes_vote_observation__id_: FieldVotesVoteObservationId = Field(
        ..., alias="/votes/vote/observation/{id}"
    )


class ApiToken(BaseModel):
    in_: str = Field(..., alias="in")
    name: str
    type: str


class SecurityDefinitions(BaseModel):
    api_token: ApiToken


class Tag(BaseModel):
    description: str
    name: str


class Model(BaseModel):
    basePath: str
    definitions: Definitions
    info: Info
    parameters: Parameters
    paths: Paths
    produces: List[str]
    schemes: List[str]
    securityDefinitions: SecurityDefinitions
    swagger: str
    tags: List[Tag]
