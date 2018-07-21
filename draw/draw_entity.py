
from abc import *

class DrawEntity(ABC):

    @abstractmethod
    def put(self, screen):
        pass

    @abstractmethod
    def draw(self, screen, color, form):
        pass