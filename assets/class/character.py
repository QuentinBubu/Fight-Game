class Character:
    def __init__(self, elements):
        # User settings definition
        self.username = elements['username']
        self.account = elements['account']

        # Character settings

        # Heart
        self.start_heart = elements['start_heart']
        self.heart = elements['heart']

        # Attack
        self.attack = elements['attack']

        # Dodge
        self.dodge = elements['dodge']
        self.dodge_is_charge = elements['dodge_is_charge']

        # Treatment
        self.treatment = elements['treatment']
        self.treatment_number = elements['treatment_number']

        # Special Attack
        self.special_attack = elements['special_attack']
        self.special_number = elements['special_number']
        self.special_attack_is_charge = elements['special_attack_is_charge']

        # Event
        self.event = elements['event']
