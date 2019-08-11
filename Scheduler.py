class Doctor:

    def __init__(self, name):
        self.name = name

        self.number_of_patient = []
        self.availability = []

    def __str__(self):
        return "Hi, this is Dr. {a}".format(a=self.name)

    def add_patient(self, patient):
        for dates in self.availability:
            if len(self.number_of_patient) < 4:
                self.number_of_patient.append(patient)
                pring(dates)
            else:
                print("Dr. {a} has no more appointment for today".format(a=self.name))

    def remove_patient(self, patient):
        for dates in self.availability:
            if len(self.number_of_patient) == 0 and self.availability[dates]:
                print("There is no patient left")
            else:
                self.number_of_patient.remove(patient.name)

    def add_days(self, *dates):
        self.availability.append(dates)

    def remove_days(self, *date):
        for num in range(len(self.availability[1])):
            if date == self.availability:
                self.availability.remove(date)

    def print_list_of_patient(self, date):
        print("Dr. {a} patient's list for {b}:\n".format(a=self.name, b=date))



class Patient:

    def __init__(self, name, sickness, date_of_appointment):
        self.name = name
        self.sickness = sickness
        self.date = date_of_appointment

    def __str__(self):
        return "Name: {a}\n Sickness: {b}\n\n".format(a=self.name, b=self.sickness)


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
bob = Patient('Bob', 'Flu', '18 August')
anilla = Patient ('Anilla', 'Pink Eye', '6 August')
sharon = Patient ('Sharon', 'Too Cute', '7 August')
phil = Patient('Phil', 'Flu', '10 August')
andrew = Patient('Andrew', 'Flu', '11 August')
jace = Patient('Jace', 'too fat', '10 August')
anthony.add_days('7 August', '8 August', '9 August', '10 August')
print(dates for dates in anthony.availability)
anthony.print_list_of_patient('7 August')
