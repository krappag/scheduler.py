class Doctor:

    def __init__(self, name):
        self.name = name

        self.number_of_patient = []
        self.availability = []

    def __str__(self):
        return "Hi, this is Dr. {a}".format(a=self.name)

    def add_patient(self, patient):
        if len(self.number_of_patient) < 4:
            self.number_of_patient.append(patient)
        else:
            return "Dr. {a} has no more appointment for today".format(a=self.name)

    def remove_patient(self):

        if len(self.number_of_patient) == 0 and self.availability[dates]:
            return "There is no patient left"
        else:
            self.number_of_patient.pop(-1)

    def add_days(self, date):
        self.availability.append(date)

    def remove_days(self, date):
        for num in range(len(self.availability)):
            if date == self.availability[num]:
                self.availability.remove(date)

    def print_list_of_patient(self):
        print("Dr. {a} patient's list:\n".format(a=self.name))
        for names in range(len(self.number_of_patient)):
            print(self.number_of_patient[names])



class Patient:

    def __init__(self, name, sickness):
        self.name = name
        self.sickness = sickness

    def __str__(self):
        return "Name: {a}\n Sickness: {b}\n\n".format(a=self.name, b=self.sickness)


class Calendar:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return "You have appointment on {a}".format(a=self.date)


def set_up_appointment(doctor, patient):
    """
    set_up_appointment(doctor, patient, date)
    doctor = variable name (unique ID)
    patient = variable name (unique ID)
    :return:
    """
    doctor.add_patient(patient)

def cancel_an_appointment(doctor, patient):
    """
    cancel_an_appointment(doctor, patient)
    doctor = variable name (unique ID)
    patient = variable name (unique ID)
    :return:
    """
    for names in range(len(doctor.number_of_patient)):
        if patient.name == doctor.number_of_patient[names].name:
            doctor.remove_patient()

anthony = Doctor('Anthony')
bob = Patient('Bob', 'Flu')
anilla = Patient ('Anilla', 'Pink Eye')
sharon = Patient ('Sharon', 'Too Cute')
phil = Patient('Phil', 'Flu')
andrew = Patient('Andrew', 'Flu')
jace = Patient('jace', 'too fat')
set_up_appointment(anthony, sharon)
set_up_appointment(anthony, bob)
set_up_appointment(anthony, anilla)
set_up_appointment(anthony, andrew)
set_up_appointment(anthony, phil)
set_up_appointment(anthony, jace)
anthony.print_list_of_patient()

