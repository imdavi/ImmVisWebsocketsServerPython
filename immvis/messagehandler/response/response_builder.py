from abc import ABC, abstractmethod
from ..actions.action_result import ActionResult

class ResponseBuilder(ABC):
    @abstractmethod
    def build_response_from_result(self, action_result: ActionResult) -> str:
        pass

    @abstractmethod
    def build_response_from_error(self, error: Exception) -> str:
        pass
    
