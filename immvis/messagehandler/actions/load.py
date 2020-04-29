from .action_result import ActionResult
from .action import TransformAction
from pandas import DataFrame
from kim import field
from ...utils.data import open_dataset_file
from ...utils.data.datasets_folder import get_datasets_folder
from os.path import join, isfile

class LoadDataFrameFromFile(TransformAction):
    file_path: str

    def process(self, data_frame: DataFrame) -> ActionResult:
        path_to_open = self.file_path

        datasets_folder_path = get_datasets_folder()

        path_on_datasets_folder = join(datasets_folder_path, self.file_path)

        if isfile(path_on_datasets_folder):
            path_to_open = path_on_datasets_folder
        
        data_frame = open_dataset_file(path_to_open)

        return ActionResult('load_dataset_result', data_frame)
