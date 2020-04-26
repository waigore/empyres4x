import enum
from empyres.core.tech import *
from empyres.core.util import GameObject

class PlayerTechTypes(enum.Enum):
    ShipSize = 'ShipSize'
    Attack = 'Attack'
    Defense = 'Defense'
    Tactics = 'Tactics'
    Movement = 'Movement'
    Terraform = 'Terraform'
    Exploration = 'Exploration'
    Shipyard = 'Shipyard'

TechMapping = {
    PlayerTechTypes.ShipSize: ShipSizeTechs,
    PlayerTechTypes.Attack: AttackTechs,
    PlayerTechTypes.Defense: DefenseTechs,
    PlayerTechTypes.Tactics: TacticsTechs,
    PlayerTechTypes.Movement: MovementTechs,
    PlayerTechTypes.Terraform: TerraformTechs,
    PlayerTechTypes.Exploration: ExplorationTechs,
    PlayerTechTypes.Shipyard: ShipyardTechs
}

class PlayerTechnology(GameObject):
    def __init__(self, color):
        super().__init__('PlayerTechnology')
        self.color = color
        self.techs = {playerTech: tech.initial() for playerTech, tech in TechMapping.items()}

    def getTech(self, playerTechType):
        return self.techs[playerTechType]

    def techUpgradable(self, playerTechType):
        tech = TechMapping[playerTechType]
        allLevels = tech.ordered()
        currTech = self.techs[playerTechType]

        return allLevels.index(currTech) < len(allLevels) - 1

    def upgradeTech(self, playerTechType):
        if not self.techUpgradable(playerTechType):
            raise ValueError('Player tech {} already at maximum!'.format(playerTechType))

        tech = TechMapping[playerTechType]
        allLevels = tech.ordered()
        currTech = self.techs[playerTechType]

        self.techs[playerTechType] = allLevels[allLevels.index(currTech)+1]

    def snapshot(self):
        return {playerTech: tech for playerTech, tech in self.techs.items()}
