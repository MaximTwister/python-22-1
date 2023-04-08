from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import (
    Session,
    sessionmaker,
    relationship,
    backref,
)

engine = create_engine("sqlite:///kaliuzhna.db", echo=True)
Base = declarative_base()
session: Session = sessionmaker(bind=engine)()


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    person_name = Column(String(length=50),  index=True)
    birthdate = Column(String)
    ssn = Column(Integer)
    address = Column(String(length=200))
    declaration_id = relationship(
        "Declaration",
        uselist=False,
        backref=backref("person", uselist=False)
    )
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    def __repr__(self):
        return f"Person(id={self.id}, person_name={self.person_name}, birthdate={self.birthdate}, ssn={self.ssn}, " \
               f"address={self.address})>"


class Declaration(Base):
    __tablename__ = "declarations"

    id = Column(Integer, primary_key=True)
    declaration_num = Column(Integer, index=True)
    date_start = Column(String)
    person_id = Column(Integer, ForeignKey("persons.id"))

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    doctor_name = Column(String(length=50),  index=True)
    polyclinic = Column(String(length=200))
    persons = relationship("Person", backref="doctor")

Base.metadata.create_all(engine)

# doctor = Doctor(doctor_name="Мирошниченко Наталія Іванівна", polyclinic='5636/5558', persons= 1)
# person = Person(person_name= 'Величко Олександр Миколайович', birthdate='1970-02-05', ssn='2356898752', address='шосе Герцена, буд. 6, Ялта, 01211', declaration_id=1, doctor_id=1)
# declaration = Declaration(declaration_num='56898855221100', date_start='2020-05-01', person_id=1)
#
# session.add_all([doctor, person, declaration])
session.commit()








