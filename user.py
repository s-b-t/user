class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = (self.gold_card_points - amount)

user_1 = User('Steve', 'Tobias', 'sblaket@gmail.com', 29)

user_2 = User('Susie', 'Mars', 'marsnarsbars@gmail.com', 37)

user_3 = User('Blake', 'Tobias', 'blaketobias@microsoft.com', 67)

user_1.enroll()
user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)
user_1.display_info()
user_2.display_info()
user_3.display_info()






