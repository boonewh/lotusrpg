from lotusrpg import create_app, db
from lotusrpg.models import Section, Content

def seed_rules():
    # Debug: Print a message to confirm the function starts
    print("Seeding rules...")

    # Clear existing data (optional for a clean reset)
    print("Clearing existing data...")
    db.session.query(Content).delete()
    db.session.query(Section).delete()
    db.session.commit()

    # Define sections and rules

    sections = [
        {
            "title": "Prelude: Character Concepts & Components",
            "slug": "prelude",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Prelude: Character Concepts & Components",
                    "class": "h1"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        Ready to dive into the world of L.O.T.U.S. RPG? Let's get you started with a 
                        character that truly resonates with your style! If you're eager to jump right in, 
                        flipping to the back of any genre book lets you pick from a variety of ready-made characters. 
                        Opting for a pre-made character is quick and ensures you're set up with a mechanically solid persona, 
                        but nothing beats the thrill of crafting your own character from scratch. This way, you develop a deeper 
                        connection as you shape their history and define their motivations.
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        Before we delve into character creation mechanics, let's first envision who your character will be. 
                        Reflect on the genre and setting, then consider these intriguing questions: Who is your character? Where 
                        did they grow up? What's their occupation? Who are their friends and family? What drives them, and what 
                        are their aspirations, both immediate and long-term?
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        With their backstory in place, it's time to bring your character to life. Choose their name, height, weight, 
                        gender, age, and give us a snapshot of their appearance. Next, dive into the finer details: Is your character 
                        slim or sturdy? Are they charming or less so? Any distinctive features like tattoos or scars that make them stand out?
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        You've now laid a solid foundation that will guide you through the mechanics of character creation and enhance your 
                        role-playing experience. Every character we create has a bit of us in them—our unique touch that shines through. As you 
                        build your character, infuse them with qualities that make them unforgettable, all while letting your own personality subtly 
                        influence their essence.
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        In the upcoming sections, we'll not only help you sculpt your character's virtues and vices 
                        but also navigate the technical aspects of bringing your character to life in the L.O.T.U.S. RPG system. 
                        Let's make your character truly memorable!
                    """.strip()
                }
            ]
        },
        {
            "title": "Approaches: Utilizing Living Philosophies",
            "slug": "approaches",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Approaches: Utilizing Living Philosophies",
                    "class": "h1"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        This can be an exceedingly difficult aspect to portray without internally projecting personal values over those of the character. Founding game systems that utilize traditional “Alignments” created a system that causes conflict regarding in-character behavioral versus out-of-character cultural perception. It becomes difficult to understand that a Lawful Evil and Chaotic Good character may perform the exact same act but their reasoning behind it will be vastly different which can be very confusing to new players.
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        To elevate your experience and foster a deeper sense of character individuality in L.O.T.U.S. RPG, we’ve embraced a dynamic concept called “Living Philosophies.” This framework moves beyond the conventional binary of good versus evil, which often leads to subjective interpretations and player conflicts over character actions. Instead, Living Philosophies provide a nuanced framework to shape your character’s core reactive values, guiding you to respond not as you would personally, but as your character would, enriching the authenticity of your role-playing.
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        Living Philosophies in L.O.T.U.S. RPG encompass a diverse spectrum: Law-abiding, Pragmatic, Honorable, Righteous, Machiavellian, and Anarchistic. Each philosophy offers unique paths and potential developments for your character, allowing you to tailor their motivations and actions based on a coherent set of principles.
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        The structure of Living Philosophy is twofold, designed both to guide and to incentivize. We start with the “Approach”—where each philosophy may branch into one or two paths, offering a tailored direction for character development. To add further depth, there’s an optional layer we call “Virtue, Failings, Vice & Balance.” This mechanism isn’t just about adding complexity; it’s about enhancing your character’s narrative and unlocking potential in-game rewards for stellar role-play.
                    """.strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        Game Masters have the flexibility to implement this second layer as they see fit, using it as a tool to encourage specific behaviors and enrich the gaming experience. Whether you choose to delve into these optional traits or stick with the fundamental Approach based on one of the Living Philosophies, you’re setting the stage for building a distinct and memorable character.
                    """.strip()
                },
            ]

        }
    ]

    # Add sections and content to the database
    for section_data in sections:
        # Debug: Print which section is being added
        print(f"Adding section: {section_data['title']}")
        section = Section(title=section_data["title"], slug=section_data["slug"])
        db.session.add(section)
        db.session.commit()  # Commit to generate the section ID

        # Debug: Print the generated section ID
        print(f"Created section with ID: {section.id}")

        for content_data in section_data["content"]:
            # Debug: Print which content is being added
            print(f"Adding content: {content_data['type']} with order {content_data['order']}")
            content = Content(
                section_id=section.id,
                content_type=content_data["type"],
                content_order=content_data["order"],
                content_data=content_data["data"],
                style_class=content_data.get("class")
            )
            db.session.add(content)

    db.session.commit()
    print("Database seeded successfully!")


if __name__ == "__main__":
    app = create_app()  # Create the Flask app instance

    # Activate application context
    with app.app_context():
        print("Application context is active.")
        seed_rules()