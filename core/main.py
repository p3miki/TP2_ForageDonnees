from .loader import loader
from .view import viewer
from .parser import parser


class Main:
    """Used to contain the assembly and starts the project"""

    def __init__(self, job):
        self.data_frame = ""
        self.start(job)

    def start(self, job):
        """Starts the application"""
        path = './core/loader/data.csv'
        if job == 2:
            path = './core/loader/anime.csv'

        self.data_frame = loader.load_file(path, job)
        new_data_frame = parser.parse_data(self.data_frame, job)
        viewer.update_view(new_data_frame, job)
