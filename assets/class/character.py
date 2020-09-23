class Character:
    def __init__(self, elements):
        # User settings definition
        self.username = elements['username']
        self.account = elements['account']

        # Character settings

        # Heart
        self.start_heart = elements['start_heart']
        self.heart = elements['heart']

        # Treatment
        self.treatment = elements['treatment']
        self.treatment_number = elements['treatment_number']

        # Dodge
        self.dodge = elements['dodge']
        self.dodge_is_charge = elements['dodge_is_charge']

        # Attack
        self.attack = elements['attack']

        # Special Attack
        self.special_attack = elements['special_attack']
        self.special_number = elements['special_number']
        self.special_attack_is_charge = elements['special_attack_is_charge']

        # Event
        self.event = elements['event']

    def treatment(self):
        if self.treatment_number > 0:
            self.treatment_number -= 1
            self.heart += self.treatment
            
            if self.heart > self.start_heart:
                self.heart = self.start_heart
        else:
            return 'Erreur: vous n\'avez plus de soin possible!'

    def dodge_charge(self):
        if self.dodge > 0:
            self.dodge -= 1
            self.dodge_is_charge = True
        else:
            return 'Erreur: vous n\'avez plus d\'esquives disponibles!'

    def attack(self, opponent): # No finished
        if not opponent.dodge_is_charge:
            opponent.heart -= self.attack
            opponent.event = 'Vous avez été attaqué par votre adversaire!'
        else:
            opponent.event = 'Vous avez esquivé une attaque de votre adversaire!'

    def special_attack(self, opponent):
        if not opponent.dodge_is_charge:
            if self.special_attack_is_charge:
                opponent.heart -= self.special_attack
                opponent.event = 'Vous avez été attaqué par votre adversaire!'
            else:
                return 'Erreur: Vous avez pas chargé d\'attaque spéciale!'
        else:
            opponent.event = 'Vous avez esquivé une attaque de votre adversaire!'