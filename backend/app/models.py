
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Association Table for Many-to-Many between Element and Equation
element_equation = Table(
    'element_equation',
    Base.metadata,
    Column('element_id', Integer, ForeignKey('elements.id'), primary_key=True),
    Column('equation_id', Integer, ForeignKey('equations.id'), primary_key=True)
)

# Association Table for Many-to-Many between Equation and LightWave
equation_lightwave = Table(
    'equation_lightwave',
    Base.metadata,
    Column('equation_id', Integer, ForeignKey('equations.id'), primary_key=True),
    Column('lightwave_id', Integer, ForeignKey('light_waves.id'), primary_key=True)
)

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    number = Column(Integer, unique=True, index=True, nullable=False)

    elements = relationship('Element', back_populates='group')

class Period(Base):
    __tablename__ = 'periods'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True, nullable=False)

    elements = relationship('Element', back_populates='period')

class Element(Base):
    __tablename__ = 'elements'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    symbol = Column(String, unique=True, index=True, nullable=False)
    atomic_number = Column(Integer, unique=True, index=True, nullable=False)
    electron_configuration = Column(String, nullable=False)
    Z_eff = Column(Float, nullable=False)

    group_id = Column(Integer, ForeignKey('groups.id'))
    period_id = Column(Integer, ForeignKey('periods.id'))

    group = relationship('Group', back_populates='elements')
    period = relationship('Period', back_populates='elements')

    equations = relationship(
        'Equation',
        secondary=element_equation,
        back_populates='elements'
    )

    neutrons = relationship('Neutron', back_populates='element')
    positrons = relationship('Positron', back_populates='element')

class Equation(Base):
    __tablename__ = 'equations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    expression = Column(Text, nullable=False)

    elements = relationship(
        'Element',
        secondary=element_equation,
        back_populates='equations'
    )

    light_waves = relationship(
        'LightWave',
        secondary=equation_lightwave,
        back_populates='equations'
    )

class Neutron(Base):
    __tablename__ = 'neutrons'

    id = Column(Integer, primary_key=True, index=True)
    mass = Column(Float, nullable=False)
    spin = Column(Float, nullable=False)
    isotope = Column(String, nullable=False)
    element_id = Column(Integer, ForeignKey('elements.id'), nullable=False)

    element = relationship('Element', back_populates='neutrons')

class Positron(Base):
    __tablename__ = 'positrons'

    id = Column(Integer, primary_key=True, index=True)
    mass = Column(Float, nullable=False)
    charge = Column(Float, nullable=False)
    element_id = Column(Integer, ForeignKey('elements.id'), nullable=False)

    element = relationship('Element', back_populates='positrons')

class LightWave(Base):
    __tablename__ = 'light_waves'

    id = Column(Integer, primary_key=True, index=True)
    frequency = Column(Float, nullable=False)
    wavelength = Column(Float, nullable=False)
    amplitude = Column(Float, nullable=False)

    equations = relationship(
        'Equation',
        secondary=equation_lightwave,
        back_populates='light_waves'
    )
