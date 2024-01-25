import random

class InteractiveStoryGenerator:
    def __init__(self):
        # Initialize the InteractiveStoryGenerator with default values
        self.story_template = (
            "Once upon a time, in the mystical land of {}, there lived a brave adventurer named {}. "
            "One day, {} discovered a {} that granted them the power to {}. Excited to test their newfound ability, "
            "{} decided to explore the {}.\n\n"
            "As {} ventured deeper into the forest, they encountered a {}. Here, you can choose:\n"
            "1. Try to befriend the creature.\n"
            "2. Confront the creature.\n\n"
            "Your choice: {}"
        )
        self.user_inputs = {}

    def get_user_input(self, prompt):
        # Get user input for a specific prompt
        user_input = input(prompt)
        return user_input.strip()

    def generate_story(self):
        # Generate a unique story based on user input
        location = self.get_user_input("Enter a mystical location: ")
        character_name = self.get_user_input("Enter the name of the adventurer: ")
        magical_object = self.get_user_input("Enter a magical object: ")
        special_ability = self.get_user_input("Enter a special ability granted by the magical object: ")
        mysterious_forest = self.get_user_input("Enter the name of a mysterious forest: ")
        mythical_creature = self.get_user_input("Enter the name of a mythical creature: ")

        # Store user inputs for later use
        self.user_inputs = {
            'location': location,
            'character_name': character_name,
            'magical_object': magical_object,
            'special_ability': special_ability,
            'mysterious_forest': mysterious_forest,
            'mythical_creature': mythical_creature,
        }

        # Generate the story template with user inputs
        story = self.story_template.format(
            location, character_name, character_name, magical_object, special_ability,
            character_name, mysterious_forest, character_name, mythical_creature, self.get_user_choice()
        )

        return story

    def get_user_choice(self):
        # Get user choice for confronting or befriending the mythical creature
        return self.get_user_input("Your choice (1 or 2): ")

    def generate_outcome(self):
        # Generate the outcome based on the user's choice
        user_choice = self.user_inputs.get('user_choice', '')
        if user_choice == '1':
            return f"{self.user_inputs['mythical_creature']}, impressed by {self.user_inputs['character_name']}'s bravery, became their loyal companion. Together, they explored the {self.user_inputs['mysterious_forest']} and uncovered hidden treasures."
        elif user_choice == '2':
            return f"{self.user_inputs['character_name']} bravely confronted the {self.user_inputs['mythical_creature']} and discovered the ancient secret of the {self.user_inputs['mysterious_forest']}."

if __name__ == '__main__':
    # Example usage
    story_generator = InteractiveStoryGenerator()

    # Generate the story
    story = story_generator.generate_story()

    # Display the story to the user
    print("\nGenerated Story:\n")
    print(story)

    # Generate the outcome based on user's choice
    outcome = story_generator.generate_outcome()
    print("\nOutcome:\n")
    print(outcome)
