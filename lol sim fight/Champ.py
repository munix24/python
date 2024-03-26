from get_champ_stats import get_champ_stats

class Champ:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.stats = get_champ_stats(name)

        # Initialize current stats based on level
        self.maxhp = self.calculate_stat_at_level(self.stats.get("hp"), self.stats.get("hpperlevel"))
        self.hp = self.maxhp
        self.armor = self.calculate_stat_at_level(self.stats.get("armor"), self.stats.get("armorperlevel"))
        self.spellblock = self.calculate_stat_at_level(self.stats.get("spellblock"), self.stats.get("spellblockperlevel"))
        self.attackdamage = self.calculate_stat_at_level(self.stats.get("attackdamage"), self.stats.get("attackdamageperlevel"))
        self.attackspeed = self.calculate_stat_at_level(self.stats.get("attackspeed"), self.stats.get("attackspeedperlevel"))

        self.attack_cd = 0  # Initialize attack cooldown to 0

    def attack(self, opponent):
        if not opponent.is_defeated():
            opponent.receive_damage(self.attackdamage)
            self.attack_cd += 1 / self.attackspeed

    def receive_damage(self, damage):
        self.hp -= damage

    def calculate_stat_at_level(self, base_stat, increase_per_level):
        return base_stat + (self.level - 1) * increase_per_level

    def is_defeated(self):
        return self.hp <= 0

    def reset(self):
        self.hp=self.maxhp
        self.attack_cd=0

    def print_stats(self):
        print(self.name)
        
