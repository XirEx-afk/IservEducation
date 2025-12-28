class Doctor:
    def __init__(self, name, patient_list):
        self._name = name
        self.patient_list = patient_list

    def get_activity(self):
        print(f"Доктор {self._name} проводит операцию")