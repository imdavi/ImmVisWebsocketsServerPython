from .action_result import ActionResult
from .action import Action
from pandas import DataFrame
from os import listdir
from os.path import isdir
from ...utils.data.datasets_folder import get_datasets_folder

class ListAvailableDatasets(Action):

    def process(self, data_frame: DataFrame) -> ActionResult:
        datasets_folder_path = get_datasets_folder()

        available_datasets = []
        
        if isdir(datasets_folder_path):
            filenames = listdir(datasets_folder_path)
            
            for filename in filenames:
                if filename.endswith('.csv'):
                    available_datasets.append(filename)

        return ActionResult('list_datasets_result', available_datasets)
