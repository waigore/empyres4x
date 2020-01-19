import enum
import logging
import random
from .marker import *
from .region import (
    HomeRegionYellow,
    HomeRegionGreen,
    HomeRegionRed,
    HomeRegionBlue,
    TheDeepSpace,
    MapRegionTypes
)
from empyres.core.player import PlayerColors

logger = logging.getLogger(__name__)

class SystemMarkerDistributions(enum.Enum):
    Sparse = 'Sparse'
    Normal = 'Normal'
    Abundant = 'Abundant'

DistributionNumbers = {
    SystemMarkerTypes.Planet: {
        SystemMarkerDistributions.Normal: 4
    },
    SystemMarkerTypes.Nebulae: {
        SystemMarkerDistributions.Normal: 6
    },
    SystemMarkerTypes.Asteroids: {
        SystemMarkerDistributions.Normal: 4
    },
    SystemMarkerTypes.BlackHole: {
        SystemMarkerDistributions.Normal: 2
    },
    SystemMarkerTypes.Danger: {
        SystemMarkerDistributions.Normal: 2
    },
    SystemMarkerTypes.Supernova: {
        SystemMarkerDistributions.Normal: 3
    },
    SystemMarkerTypes.LostInSpace: {
        SystemMarkerDistributions.Normal: 3
    },
    SystemMarkerTypes.Minerals: {
        SystemMarkerDistributions.Normal: 6
    },
    SystemMarkerTypes.SpaceWreck: {
        SystemMarkerDistributions.Normal: 6
    },
}

class SystemMarkerGenRegions(enum.Enum):
    HomeRegionOnly = 'HomeRegionOnly'
    DeepSpaceOnly = 'DeepSpaceOnly'
    Anywhere = 'Anywhere'

PossibleRegions = {
    SystemMarkerTypes.Planet: SystemMarkerGenRegions.HomeRegionOnly,
    SystemMarkerTypes.Nebulae: SystemMarkerGenRegions.Anywhere,
    SystemMarkerTypes.Asteroids: SystemMarkerGenRegions.Anywhere,
    SystemMarkerTypes.BlackHole: SystemMarkerGenRegions.DeepSpaceOnly,
    SystemMarkerTypes.Danger: SystemMarkerGenRegions.DeepSpaceOnly,
    SystemMarkerTypes.Supernova: SystemMarkerGenRegions.Anywhere,
    SystemMarkerTypes.LostInSpace: SystemMarkerGenRegions.DeepSpaceOnly,
    SystemMarkerTypes.Minerals: SystemMarkerGenRegions.Anywhere,
    SystemMarkerTypes.SpaceWreck: SystemMarkerGenRegions.Anywhere,
}

def FertilePlanetMarker():
    return PlanetMarker(PlanetTypes.Fertile)

def RandomMineralsMarker():
    return MineralsMarker(random.choice(list(MineralAmounts)))


SystemMarkerCreatorsByType = {
    SystemMarkerTypes.Planet: FertilePlanetMarker,
    SystemMarkerTypes.Nebulae: NebulaeMarker,
    SystemMarkerTypes.Asteroids: AsteroidsMarker,
    SystemMarkerTypes.BlackHole: BlackHoleMarker,
    SystemMarkerTypes.Danger: DangerMarker,
    SystemMarkerTypes.Supernova: SupernovaMarker,
    SystemMarkerTypes.LostInSpace: LostInSpaceMarker,
    SystemMarkerTypes.Minerals: RandomMineralsMarker,
    SystemMarkerTypes.SpaceWreck: SpaceWreckMarker
}

class SystemMarkerGenProfile(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.planets = kwargs.setdefault('planets', SystemMarkerDistributions.Normal)
        self.features = kwargs.setdefault('features', SystemMarkerDistributions.Normal)
        self.dangers = kwargs.setdefault('dangers', SystemMarkerDistributions.Normal)
        self.resources = kwargs.setdefault('resources', SystemMarkerDistributions.Normal)
        self.fuzzy = kwargs.setdefault('fuzzy', False)

    def getMarkerCount(self, markerType):
        if markerType in [
                SystemMarkerTypes.Nebulae,
                SystemMarkerTypes.Asteroids,
                SystemMarkerTypes.BlackHole,
                SystemMarkerTypes.Supernova]:
            distrib = self.features
        elif markerType in [SystemMarkerTypes.Danger, SystemMarkerTypes.LostInSpace]:
            distrib = self.dangers
        elif markerType in [SystemMarkerTypes.Minerals, SystemMarkerTypes.SpaceWreck]:
            distrib = self.resources
        elif markerType in [SystemMarkerTypes.Planet]:
            distrib = self.planets
        else:
            raise ValueError('Invalid markerType = {}!'.format(markerType))
        return DistributionNumbers[markerType][distrib]

StandardProfile = SystemMarkerGenProfile('Normal')

class SystemMarkerGen(object):
    def __init__(self, map, genProfile = None, **kwargs):
        self.map = map
        self.genProfile = StandardProfile if genProfile is None else genProfile
        self.seed = kwargs.setdefault('seed', None)

    def populateMarkerBucket(self, bucket, marker, num):
        bucket.extend([marker] * num)

    def populateMarkerBuckets(self, buckets, marker, num):
        i = num
        while i > 0:
            random.choice(buckets).append(marker)
            i -= 1

    def assignMarkersToRegion(self, markers, map, region):
        aPointList = list(region.aPoints)
        random.shuffle(aPointList)

        for marker, aPoint in zip(markers, aPointList):
            hex = map.getHexAt(aPoint)
            hex.systemMarker = SystemMarkerCreatorsByType[marker]()

    def populateMap(self):
        if self.seed:
            logger.info('Generator seed: {}'.format(self.seed))
            random.seed(self.seed)
        markerBuckets = {
            PlayerColors.Yellow: [],
            PlayerColors.Green: [],
            PlayerColors.Red: [],
            PlayerColors.Blue: []
        }
        deepSpaceBucket = []
        sortedMarkerBuckets = [markerBuckets[key] for key in PlayerColors.ordered()]
        allBuckets = sortedMarkerBuckets + [deepSpaceBucket]

        for markerType in SystemMarkerTypes:
            possibleRegion = PossibleRegions[markerType] if markerType in PossibleRegions else None
            if possibleRegion is None:
                continue

            number = self.genProfile.getMarkerCount(markerType)

            if possibleRegion == SystemMarkerGenRegions.HomeRegionOnly:
                for markerBucket in sortedMarkerBuckets:
                    self.populateMarkerBucket(markerBucket, markerType, number)
            elif possibleRegion == SystemMarkerGenRegions.DeepSpaceOnly:
                self.populateMarkerBucket(deepSpaceBucket, markerType, number)
            else:
                self.populateMarkerBuckets(allBuckets, markerType, number)

        self.assignMarkersToRegion(
                    markerBuckets[PlayerColors.Yellow],
                    self.map,
                    self.map.getHomeRegion(PlayerColors.Yellow))
        self.assignMarkersToRegion(
                    markerBuckets[PlayerColors.Green],
                    self.map,
                    self.map.getHomeRegion(PlayerColors.Green))
        self.assignMarkersToRegion(
                    markerBuckets[PlayerColors.Blue],
                    self.map,
                    self.map.getHomeRegion(PlayerColors.Blue))
        self.assignMarkersToRegion(
                    markerBuckets[PlayerColors.Red],
                    self.map,
                    self.map.getHomeRegion(PlayerColors.Red))
        self.assignMarkersToRegion(
                    deepSpaceBucket,
                    self.map,
                    self.map.getDeepSpace())
