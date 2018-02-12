import abc

class grouping_interface(abc.ABC):

    @abc.abstractmethod
    def get_groupings(self):
        pass