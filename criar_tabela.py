from banco import engine
from modelo import Base

Base.metadata.create_all(engine)
