class Participant:
    def __init__(self, participant_id, name):
        self._id = participant_id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
