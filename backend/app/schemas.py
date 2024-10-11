
from pydantic import BaseModel
from typing import List, Optional

class GroupBase(BaseModel):
    name: str
    number: int

    class Config:
        orm_mode = True

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    elements: List['Element'] = []

class PeriodBase(BaseModel):
    number: int

    class Config:
        orm_mode = True

class PeriodCreate(PeriodBase):
    pass

class Period(PeriodBase):
    id: int
    elements: List['Element'] = []

class ElectronConfigurationBase(BaseModel):
    configuration: str
    energy: float
    wavefunction: Optional[str] = None  # Serialized wavefunction or file path

    class Config:
        orm_mode = True

class ElectronConfigurationCreate(ElectronConfigurationBase):
    pass

class ElectronConfiguration(ElectronConfigurationBase):
    id: int
    element_id: int

class EquationBase(BaseModel):
    name: str
    description: Optional[str] = None
    expression: str

    class Config:
        orm_mode = True

class EquationCreate(EquationBase):
    pass

class Equation(EquationBase):
    id: int
    elements: List['Element'] = []
    light_waves: List['LightWave'] = []

class NeutronBase(BaseModel):
    mass: float
    spin: float
    isotope: str

    class Config:
        orm_mode = True

class NeutronCreate(NeutronBase):
    pass

class Neutron(NeutronBase):
    id: int
    element_id: int

class PositronBase(BaseModel):
    mass: float
    charge: float

    class Config:
        orm_mode = True

class PositronCreate(PositronBase):
    pass

class Positron(PositronBase):
    id: int
    element_id: int

class LightWaveBase(BaseModel):
    frequency: float
    wavelength: float
    amplitude: float

    class Config:
        orm_mode = True

class LightWaveCreate(LightWaveBase):
    pass

class LightWave(LightWaveBase):
    id: int
    equations: List['Equation'] = []

class ElementBase(BaseModel):
    name: str
    symbol: str
    atomic_number: int
    electron_configuration: str
    Z_eff: float
    group_id: Optional[int] = None
    period_id: Optional[int] = None

    class Config:
        orm_mode = True

class ElementCreate(ElementBase):
    pass

class Element(ElementBase):
    id: int
    group: Optional[Group] = None
    period: Optional[Period] = None
    equations: List[Equation] = []
    neutrons: List[Neutron] = []
    positrons: List[Positron] = []
