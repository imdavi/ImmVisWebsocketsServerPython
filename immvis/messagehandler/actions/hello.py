from .action_result import ActionResult
from .action import Action
from pandas import DataFrame
from kim import field


class HelloAction(Action):
    def process(self, data_frame: DataFrame) -> ActionResult:
        return ActionResult('HelloAction', data_frame)
