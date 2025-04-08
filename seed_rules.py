from lotusrpg import create_app, db
from lotusrpg.models import Section, Content
import re

def clean_text(text):
    """Cleans text by removing newlines, non-breaking spaces, and excessive whitespace."""
    if not isinstance(text, str):  
        return text  # Ensure we only process strings

    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()

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
            "title" : "From the Beginning",
            "slug" : "beginning",
            "chapter" : "Introduction",
            "content" : [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": """
                        L.O.T.U.S. is a project that originated in 1993 as an ideation to create a system that was portable in comparison to other tabletop game systems of that era. During its early conception, the game system was referred to as Mind Games and developed into a quick-paced RPG allowing scenes that could be run during short break intervals while carrying minimal gamer paraphernalia.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        In its original incarnation, the system was a loose-knit D20 Versus System. Unfortunately, despite the relatively simplistic game mechanics, it was found to be problematic because a d20 cannot readily be rolled on any surface. While there are now technological alternatives to this, many players still love the feel of casting the dice, and we built our system to uphold that tradition.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        Regardless, this phase of game development was put on hold due to life events, including military service, college, and family building. For a long time, the system remained untouched but never forgotten, as one is always a gamer, and our passion for role-playing always comes full circle. After engaging in a series of LARP conventions, an interest was rekindled by a desire to refine the game mechanics to provide a solid and consistent system that overcame the fundamental shortcomings of LARP with a set of rules that was intrinsically reverse compatible with tabletop gameplay.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        This led to a series of successes and failures where the game development was forced to bypass a 2d6 Versus System because the Die Roll Increment Range was not varied enough for suitable gameplay. Eventually, this transitioned L.O.T.U.S. to its current format of a DD10 Versus System, providing a wider range of roll increments that could reasonably be rolled on any surface.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        The acronym L.O.T.U.S. was chosen for the RPG and stands for Live-action Or Tabletop Universal System. The mechanics herein are designed to provide a consistent, stable medium that does not require variance or change when crossing different styles of role-playing.
                    """.replace("\n", " ").strip()
                }
            ]
        },
        {
            "title": "Welcome to L.O.T.U.S.",
            "slug": "welcome",
            "chapter": "Introduction",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": """
                        Welcome to L.O.T.U.S.—the Live-action Or Tabletop Universal System! If you're new to role-playing games or a seasoned gamer looking for something simple and fun, you've come to the right place. L.O.T.U.S. is designed to be played anytime, anywhere, with minimal setup and just a couple of dice. Whether you're into acting out adventures live (LARP) or sitting around a table with friends (tabletop), L.O.T.U.S. makes it easy for everyone to join the fun.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        Think of this Core Book as your handy guide, packed with everything you need to dive into exciting stories. You'll create and play your own unique character, interacting within a world brought to life by your Storyteller. Forget about complicated rules and lengthy preparations—L.O.T.U.S. keeps things straightforward, relying on creativity, role-play, and simple dice rolls using just two ten-sided dice (2d10).
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        For tabletop games, you can choose to use visual aids like marker boards, digital maps, or miniature figures to help visualize your adventures. These aren't mandatory, but they can add clarity and fun to the storytelling experience.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        If you're playing LARP, you'll be physically moving around, acting out your character’s actions and reactions in real-time. L.O.T.U.S. is designed to make this easy and accessible, letting you jump into the action without worrying about complicated setups or props.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        No matter how you choose to play, the Storyteller is there to guide you, responding to your character's decisions, creating exciting challenges, and narrating consequences. With just two simple dice, you'll quickly resolve any challenges, keeping the adventure flowing and the excitement high.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        At its heart, L.O.T.U.S. is all about creating unforgettable stories together with your friends. So gather around, roll some dice, and start your adventure—your story is waiting to be told!
                    """.replace("\n", " ").strip()
                }
            ]
        },
        {
            "title": "How To Use These Rules",
            "slug": "how-to-use",
            "chapter": "Introduction",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": """
                        Now that you're familiar with what L.O.T.U.S. is all about, let's talk about how to use this book. This Core Mechanics book gives you everything you need to start your adventures, no matter what kind of setting you've chosen—or even if you're crafting your own unique world.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        We've broken things down into three easy-to-follow sections:
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        Character Genesis: This is your starting point, guiding you step-by-step through creating characters perfectly suited for the simple yet versatile 2d10 system. We recommend everyone—players and Storytellers alike—take their time with this section first. As you learn to build your characters, you'll naturally become familiar with the concepts and key terms we'll use throughout the rest of the book, setting you up for smooth gameplay later on.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        Playing the Game: Here’s where you'll learn how the game works in practice—from using your abilities and skills to embarking on adventures and engaging in thrilling combat. Don't worry if this is your first dice-based role-playing experience. We've made sure to keep the rules clear, easy to follow, and streamlined, so you can focus on the fun and excitement of the game.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        Storyteller’s Guide: Lastly, this section is dedicated to the Storytellers—the creative hearts of any role-playing game. You'll find helpful tips and extensive guidance on world-building, managing player interactions, and keeping everyone engaged and immersed in the game. Whether you've been a Game Master before or this is your very first time leading a game, our Storyteller’s Guide will help you feel confident and ready to bring your world and stories to life.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        Now that you know what's in store, let's dive in and start creating amazing adventures together!
                    """.replace("\n", " ").strip()
                }
            ]
        },
        {
            "title": "Character Creation",
            "slug": "character-creation",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        Ready to dive into the world of L.O.T.U.S. RPG? Let's get you started with a character that truly resonates with your style! If you're eager to jump right in, flipping to the back of any or the l.o.t.u.s setting books lets you pick from a variety of ready-made characters. Opting for a pre-made character is quick and ensures you're set up with a mechanically solid persona, but nothing beats the thrill of crafting your own character from scratch. This way, you develop a deeper connection as you shape their history and define their motivations.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                            In the upcoming sections, we'll help you sculpt your character from concept to fully playable hero. You'll find practical suggestions on building your character's identity, a step-by-step guide to character creation, and clear explanations of every aspect you'll encounter on your character sheet. We'll also introduce you to the maturation system—our approach to character growth—and guide you in discovering your character's calling, choosing relevant abilities, and picking the right skills. Let’s make your character truly memorable!
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "heading",
                    "order": 4,
                    "data": "Defining Your Character",
                    "class": "h2"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        Before you begin character creation, it's important to gather a clear vision of your character. Reflect carefully on the genre and setting you'll be playing in, and consider having a 'Session Zero' with your Storyteller and fellow players. Session Zero is a fantastic opportunity to collaborate and ensure everyone is aligned, helping you craft an immersive and exciting campaign experience.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        As you explore this process, think about who your character is within the world: their background, their moral compass, and their relationships. In the following sections, you'll find plenty of inspiring ideas and helpful tools to build out these details:
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "Philosophies: These will help shape your character's morals and beliefs.",
                        "Backgrounds: These offer a foundation for your character's place in the world, giving depth and realism to their past and present.",
                        "Races and Bloodlines: These can define key relationships with NPCs and deepen your connection to the game world."
                ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": """
                        Taking the time to define these elements early on will greatly enhance your role-playing experience, ensuring your character is both memorable and meaningful.
                    """.replace("\n", " ").strip()
                }
            ]
        },
        {
            "title": "Creating Your Character",
            "slug": "creating-character",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Step-by-Step Guide",
                    "class": "h2"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        Follow these steps as a quick reference for character creation. Each step is explained thoroughly, with detailed examples, throughout this chapter. Additionally, visiting the L.O.T.U.S. website provides access to helpful tools like the online character creator, complete with automated calculations. Joining the website also gives you access to session zero materials, downloadable resources, and further guidance from the community.
                        """.replace("\n", " ").strip()
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Step 1: General Character Setup",
                    "class": "h3"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Choose Species/Subspecies. Noting maturation cost (deduct from step 7)."
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Maturation Cost for Races",
                    "class": "h2"
                },
                {
                    "type": "table",
                    "order": 6,
                    "data": {
                        "headers": ["Race", "Subrace", "Cost"],
                        "rows": [
                        ["Faeyr", "Dylithat", "40"],
                        ["", "Miaki", "40"],
                        ["", "Tiermalain", "40"],
                        ["Human", "Akkadian", "0"],
                        ["", "Midian", "0"],
                        ["", "Sutherlander", "0"],
                        ["", "Ennocean", "0"],
                        ["Romling", "-", "20"],
                        ["Svar", "Dargnan", "40"],
                        ["", "Kargathi", "40"],
                        ["", "Mordron", "40"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-600 w-full text-left"
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "*Descriptions of the core races are included on pg #*",
                    "style_class": "text-sm italic"
                },
                {
                    "type": "heading",
                    "order": 10,
                    "data": "Select Philosophical Approach",
                    "class": "h3"
                },
                {
                    "type": "list",
                    "order": 11,
                    "data": [
                        {
                        "text": "Law-abiding",
                        "link": "/core/law-abiding"
                        },
                        {
                        "text": "Honorable",
                        "link": "/core/honorable"
                        },
                        {
                        "text": "Righteous",
                        "link": "/core/righteous"
                        },
                        {
                        "text": "Pragmatic",
                        "link": "/core/pragmatic"
                        },
                        {
                        "text": "Malkavian",
                        "link": "/core/machiavellian"
                        },
                        {
                        "text": "Anarchist",
                        "link": "/core/anarchist"
                        }
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": """
                        These can also be chosen before or after establishing your background.
                    """.replace("\n", " ").strip()
                },
                                {
                    "type": "list",
                    "order": 13,
                    "data": [
                        "Select Calling (using L.O.T.U.S. Darkholme settings), note any Specialization and associated maturation cost (deduct from step 7).",
                        "Choose a Culture/Bloodline (examples from Darkholme)"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 14,
                    "data": "Step 2: Place Abilities",
                    "style_class": "h3"
                },
                {
                    "type": "list",
                    "order": 15,
                    "data": [
                        "Distribute 12 ability tiers among Strength, Endurance, Reflexes, Chakra, Perception, Intellect, Manipulation, and Control.",
                        "All abilities start at Tier 1 and cannot exceed Tier 5 at creation."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 16,
                    "data": "Step 3: Place Skill Traits",
                    "style_class": "h3"
                },
                {
                    "type": "list",
                    "order": 17,
                    "data": [
                        "Allocate 15 skill tiers among available skills (starting at Tier 0).",
                        "No skill may exceed Tier 6 initially.",
                        "Skills may vary by setting; the Storyteller can adjust accordingly."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 18,
                    "data": "Step 4: Select Scholarly Knowledges",
                    "style_class": "h3"
                },
                {
                    "type": "list",
                    "order": 19,
                    "data": [
                        "Choose 1 scholar at Tier 5, 1 at Tier 3, and 1 at Tier 1.",
                        "Remaining scholar traits start at Tier 0.",
                        "Choices should reflect your character’s background and require Storyteller approval."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 20,
                    "data": "Step 5: Place Backgrounds",
                    "style_class": "h3"
                },
                {
                    "type": "list",
                    "order": 21,
                    "data": [
                        "Backgrounds include Assets, Associates (Contacts/Minions), Comeliness, Income, Legacy, and Rank.",
                        "Select 1 background at Tier 5, 1 at Tier 3, and 1 at Tier 1.",
                        "All others start at Tier 0."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 22,
                    "data": "Step 6: Select Banes and Boons",
                    "style_class": "h3"
                },
                {
                    "type": "list",
                    "order": 23,
                    "data": [
                        "Choose up to 10 points worth of Boons (max of 6 total).",
                        "Select up to 6 Banes to offset Boon costs.",
                        "Unbalanced selections incur penalties: 5 maturation points or 1 misfortune per difference."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 24,
                    "data": "Step 7: Expend Maturation Points",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "list",
                    "order": 25,
                    "data": [
                        "Starting Campaign: Begin with 100 Maturation XP.",
                        "Experienced Campaign: Begin with 200 Maturation XP.",
                        "Strong Starting Campaign: Begin with 400 Maturation XP.",
                        "All maturation costs are cumulative (reference provided tables here)."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 26,
                    "data": "Step 8: Calculate Expendable Traits",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "list",
                    "order": 27,
                    "data": [
                        "Calculate expendable traits (reference provided table here)."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 28,
                    "data": "Step 9: Fill in Cosmetic Information",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "list",
                    "order": 29,
                    "data": [
                        "Using all the details you’ve gathered, complete your character’s cosmetic details: Age, Hair Color, Eye Color, Height, and Weight.",
                        "Adding a picture or artwork for reference can greatly inspire your role-play and help others visualize your character."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "By following these detailed steps, you’ll create an engaging and mechanically sound character ready for your L.O.T.U.S. RPG adventure!"
                }

            ]
        },
        {
            "title": "Approaches: Utilizing Living Philosophies",
            "slug": "approaches",
            "chapter": "Character Genesis",
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
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        To elevate your experience and foster a deeper sense of character individuality in L.O.T.U.S. RPG, we’ve embraced a dynamic concept called “Living Philosophies.” This framework moves beyond the conventional binary of good versus evil, which often leads to subjective interpretations and player conflicts over character actions. Instead, Living Philosophies provide a nuanced framework to shape your character’s core reactive values, guiding you to respond not as you would personally, but as your character would, enriching the authenticity of your role-playing.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        Living Philosophies in L.O.T.U.S. RPG encompass a diverse spectrum: Law-abiding, Pragmatic, Honorable, Righteous, Machiavellian, and Anarchistic. Each philosophy offers unique paths and potential developments for your character, allowing you to tailor their motivations and actions based on a coherent set of principles.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        The structure of Living Philosophy is twofold, designed both to guide and to incentivize. We start with the “Approach”—where each philosophy may branch into one or two paths, offering a tailored direction for character development. To add further depth, there’s an optional layer we call “Virtue, Failings, Vice & Balance.” This mechanism isn’t just about adding complexity; it’s about enhancing your character’s narrative and unlocking potential in-game rewards for stellar role-play.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        Game Masters have the flexibility to implement this second layer as they see fit, using it as a tool to encourage specific behaviors and enrich the gaming experience. Whether you choose to delve into these optional traits or stick with the fundamental Approach based on one of the Living Philosophies, you’re setting the stage for building a distinct and memorable character.
                    """.replace("\n", " ").strip()
                },
            ]

        },
        {
            "title": "Law Abiding",
            "slug": "law-abiding",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "container",
                    "order": 1,
                    "data": "open",
                    "style_class": "flex flex-col items-start mb-6 lg:flex-row"
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": """
                        Law-abiding members of society obey the laws, traditions, customs of their chosen culture and as their affiliated organization directs them. Lawful adherents believe in a strong, well-ordered government, whether an acceptable government is a tyranny or benevolent democracy is based on their focus. The need for stable organization and regimentation outweigh any moral questions and they will seek to uphold the law regardless of whether it is considered just or not. If ethics call for a change of the practice of the government, then they must use legal means of getting those laws changed.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "image",
                    "order": 2,
                    "data": {
                        "file_path": "/static/images/law_abiding.jpg",
                        "alt_text": "Law-Abiding Philosophy Chart",
                        "class_name": "mx-auto w-40 mb-4 lg:mx-0 lg:ml-4 flex-shrink-0"
                    }   
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "close"
                },
                # Parent flex container for lists
                {
                    "type": "container",
                    "order": 3,
                    "data": "open",
                    "style_class": "flex flex-col gap-12 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                # First column container
                {
                    "type": "container",
                    "order": 4,
                    "data": "open",
                    "style_class": "w-full sm:w-3/5"
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Disciplined",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 6,
                    "data": [
                        "Honor - Adhere to laws, oaths, customs and their intent.",
                        "Duplicity - Lies are unbecoming in a civilized society.",
                        "Theft - A crime to be reported or stopped.",
                        "Helpless - Civilians shall be protected in a legal manner.",
                        "Torture - Performed sparingly in accordance with the law.",
                        "Killing - Life should only be taken as a necessary resort.",
                        "Benevolence - The system provides and assists others.",
                        "Authority - The laws and customs provide structure and protection for all and must be upheld at all cost."
                    ],
                    "style_class": "list-disc pl-6"
                },
                # Close first column
                {
                    "type": "container",
                    "order": 7,
                    "data": "close"
                },
                # Second column container
                {
                    "type": "container",
                    "order": 8,
                    "data": "open",
                    "style_class": "w-full sm:w-3/5"
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Appointed",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 10,
                    "data": [
                        "Honor - Use or seek change to the law and act accordingly.",
                        "Duplicity - Nuances and loopholes should be used.",
                        "Theft - A crime, but civil forfeiture is permissible.",
                        "Helpless - Civilian lives may be lost upholding justice.",
                        "Torture - Interrogation may be used to pursue justice.",
                        "Killing - Acceptable but use the law to justify your actions.",
                        "Benevolence - The system provides and assists others.",
                        "Authority - The law is the means to an end, work within the law regardless how far you must stretch it."
                    ],
                    "style_class": "list-disc pl-6"
                },
                # Close second column
                {
                    "type": "container",
                    "order": 11,
                    "data": "close"
                },
                # Close parent flex container
                {
                    "type": "container",
                    "order": 12,
                    "data": "close"
                }
            ]
        },
        {
            "title": "Honorable",
            "slug": "honorable",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "container",
                    "order": 1,
                    "data": "open",
                    "style_class": "flex flex-col items-start mb-6 lg:flex-row"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Honorable people behave in accordance with their chosen code and are guided by their sense of obligation. This may be as strict as bushido’s rigid expectations or a loose knit codified system of conduct. Laws and fleeting morals are not the focus. The code of honor remains the same regardless of outside factors. Other adherents to the code are granted special privileges in dealing with other honorable individuals though these guidelines have limitation to those who operate outside of these behavior expectations.",
                },
                {
                    "type": "image",
                    "order": 1,
                    "data": {
                        "file_path": "/static/images/honorable.jpg",
                        "alt_text": "Law-Abiding Philosophy Chart",
                        "class_name": "mx-auto pr-2 w-40 mb-4 lg:mx-0 lg:ml-4 flex-shrink-0"
                    }
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 3,
                    "data": "open",
                    "style_class": "flex flex-col gap-12 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 4,
                    "data": "open",
                    "style_class": "w-full sm:w-3/5"
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Bushido",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 6,
                    "data": [
                        "Honor - Your word is your bond and your oaths are unbreakable as honor is everything",
                        "Duplicity - Would rather remain silent then lie",
                        "Theft - Never steal. It is the coward's way, better to be a beggar on the street",
                        "Helpless - Protect the children and unarmed unless ordered not to by an esteemed superior.",
                        "Torture - Never torture but allow one's subordinates to do what is necessary.",
                        "Killing - Death is merely another aspect of life. Killing to defend honor is always acceptable.",
                        "Benevolence - Help others but retain dignity and station.",
                        "Authority - Only break the law is ordered to by an esteemed superior."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "container",
                    "order": 7,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 8,
                    "data": "open",
                    "style_class": "w-full sm:w-3/5"
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Scoundrel ",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 10,
                    "data": [
                        "Honor - Always keep your word.",
                        "Duplicity - Only lie and cheat those unworthy of respect",
                        "Theft - Take from those who are unworthy",
                        "Helpless - Will not protect those who will not protect themselves",
                        "Torture - Will resort to inhumane treatment of prisoners or conquered civilians",
                        "Killing - Never kills for pleasure, only for necessity.",
                        "Benevolence - Assist those in need, but rarely without expecting something in return.",
                        "Authority - Only ones code of honor holds any significance; all other laws are irrelevant."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "container",
                    "order": 11,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 12,
                    "data": "close"
                }
            ]
        },
        {
            "title": "Righteous",
            "slug": "righteous",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "container",
                    "order": 1,
                    "data": "open",
                    "style_class": "flex flex-col items-start mb-6 lg:flex-row"
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Righteous upstanding individuals make decisions in accordance with justifiable behavior of what can be considered morally correct in accordance with their personal code, faith, and affiliated organization. The just know that even the most well-ordered government shall fall short of necessary expectations, or it is rendered ineffective upon its own bloated bureaucracy over time. Moral questions are the only questions, and the cause is above all.",
                },
                {
                    "type": "image",
                    "order": 2,
                    "data": {
                        "file_path": "/static/images/righteous.jpg",
                        "alt_text": "Righteous Philosophy Chart",
                        "class_name": "mx-auto w-40 mb-4 lg:mx-0 lg:ml-4 flex-shrink-0"
                    }
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 3,
                    "data": "open",
                    "style_class": "flex flex-col gap-12 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 4,
                    "data": "open",
                    "style_class": "w-full sm:w-3/5"
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Diabolic",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 6,
                    "data": [
                        "Honor - It is honorable to reach your goals through any means called for by the service.",
                        "Duplicity - The truth serves the greater good as do the appropriate lies.",
                        "Theft - What are material possessions except for a means to the end to serve the higher purpose.",
                        "Helpless - The innocent suffer enough only when purging the truly most vile is adding to that suffering acceptable.",
                        "Torture - Interrogation may be used to pursue a night purpose.",
                        "Killing - High service often comes with a high cost.",
                        "Benevolence - The innocent cannot be saved until the proper order is restored.",
                        "Authority - The law of lesser authorities should be committed to memory to prepare for opposition against the higher authority that you serve."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "container",
                    "order": 7,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 8,
                    "data": "open",
                    "style_class": "w-full sm:w-3/5"
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Pious",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 10,
                    "data": [
                        "Honor - This is the path of the Righteous, but evil deserves no such consideration.",
                        "Duplicity - Truth will forever serve the hand of good more than lies ever will.",
                        "Theft - Leave none in wanting from your hand.",
                        "Helpless - You will protect and guide the innocent to be weak.",
                        "Torture - Inflicting suffering upon men is inherently wrong, but monsters are not men.",
                        "Killing - The destruction of evil but weights the sin of murder.",
                        "Benevolence - The penitent man is humble and kneels before the higher power. Helping others is a key tenet of a pious man.",
                        "Authority - The laws of the high good is greater than that of mortals."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "container",
                    "order": 11,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 12,
                    "data": "close"
                }
            ]
        },
        {
            "title": "Pragmatic",
            "slug": "pragmatic",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "container",
                    "order": 1,
                    "data": "open",
                    "style_class": "flex flex-col items-start mb-6 lg:flex-row"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Pragmatic freethinkers always act in a sensible and realistic manner without focusing on the overarching legality or morality of the means. Practical realists are concerned with their own well-being, organization and the group which aids them. They tend to always act ethically with those they consider friends and allies regardless of focus but are likely to act maliciously against those who have brought harm to them or their group unless such behavior brings undue repercussions. Every situation should be analyzed to determine if the costs outweigh the gains."
                },
                {
                    "type": "image",
                    "order": 1,
                    "data": {
                        "file_path": "/static/images/pragmatic.jpg",
                        "alt_text": "Pragmatic Philosophy Chart",
                        "class_name": "mx-auto w-40 mb-4 pr-2 lg:mx-0 lg:ml-4 flex-shrink-0"
                    }
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "close"
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Realist",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Honor - Always keep your word to the letter given.",
                        "Duplicity - Lie and cheat those whose actions make them unworthy of respect.",
                        "Theft - Take what you can if the profits outweigh the cost.",
                        "Helpless - May or may not protect, kill, or kidnap but never for cheap thrills",
                        "Torture - Inhumane treatment or torture is sometimes a necessity.",
                        "Killing - Never kills for fun but business is business.",
                        "Benevolence - May or may not help someone in need depending on the cost.",
                        "Authority - The law and its adherence only matters so much."
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Machiavellian",
            "slug": "machiavellian", 
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "container",
                    "order": 1,
                    "data": "open",
                    "style_class": "flex flex-col items-start mb-6 lg:flex-row"
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Machiavellian operates with a singular focus on their own gains, disregarding the legality or morality of their methods. They understand that laws are mutable and that public opinion, easily influenced, can be shaped through strategic planning and a charismatic presence. Efficient allies and subordinates are to be rewarded, while those lacking in competence should be penalized or removed. This principle extends to leadership: capable and astute leaders should be both respected and feared, whereas ineffective ones ought to be supplanted by more qualified individuals. By prioritizing strong, effective personalities over the unfit, a robust social order is established."
                },
                {
                    "type": "image",
                    "order": 2,
                    "data": {
                        "file_path": "/static/images/machiavellian.jpg",
                        "alt_text": "Machiavellian Philosophy Chart",
                        "class_name": "mx-auto w-40 mb-4 lg:mx-0 lg:ml-4 flex-shrink-0"
                    }
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "close"
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Amoralist",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Honor - Keep promises to those you respect or fear, act freely with others unworthy",
                        "Duplicity - Lying and cheating are common tactics to be used for your benefit",
                        "Theft - Avoid theft unless you can manage the consequences",
                        "Helpless - All pawns have there use",
                        "Torture - Torture is a tool, one you may excel with",
                        "Killing - Killing can be the most effective means to secure your objectives",
                        "Benevolence - Assists others only when there is a clear benefit or to cultivate loyalty",
                        "Authority - Use or break the law as it suits your designs"
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Anarchistic",
            "slug": "anarchistic",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "container",
                    "order": 1,
                    "data": "open",
                    "style_class": "flex flex-col items-start mb-6 lg:flex-row"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Anarchistic philosophers are often in a temporary state as they search for a sustainable living philosophy. During this period, their critical views on authority lead them to reject any form of enforced hierarchy, which can isolate them from mainstream society. Although they sometimes appoint a representative for external interactions, their primary goal is to prevent the consolidation of power and authority, often resorting to violence. The anarchist prioritizes personal freedom above all, occasionally at the expense of others' freedoms, creating a paradoxical situation. Typically, they operate in small groups and only for brief periods until they either pass away or adopt a more enduring philosophy."
                },
                {
                    "type": "image",
                    "order": 1,
                    "data": {
                        "file_path": "/static/images/anarchistic.jpg",
                        "alt_text": "Anarchistic Philosophy Chart",
                        "class_name": "mx-auto w-40 mb-4 pr-2 lg:mx-0 lg:ml-4 flex-shrink-0"
                    }
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "close"
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Iconoclast",
                    "style_class": "underline text-2xl font-semibold mt-6"
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Honor - Views promises as tools often breaks them if it undermines established norms or serves their goals",
                        "Duplicity - Regularly employs deception to dismantle or disrupt societal structures justifying all actions as means to an end",
                        "Theft - Actively endorses stealing from institutional powers as a form of protest and redistribution",
                        "Helpless - Rejects traditional protections for specific groups, arguing that all societal roles should be challenged and disrupted",
                        "Torture - Considered a viable tactic to break down the psychological barriers of societal norms",
                        "Killing - Seen as a radical but necessary action to eliminate figures who uphold or are symbols of oppressive systems",
                        "Benevolence - Never practiced any help given is strategic aimed at weakening societal structures rather than genuine altruism",
                        "Authority - Deeply mistrusts all forms of established authority viewing laws and governance as manipulative tools of control to be actively fought against"
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Abilities, Skills & Core Mechanics",
            "slug": "section-two",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "When characterizing individuals in role-playing games like L.O.T.U.S. RPG, we often attribute qualities like strength, charm, or intelligence, associating them with tasks they excel in. Assigning stats to these skills and abilities serves several key purposes that enhance the role-playing experience by providing a structured framework to define characters' competencies and potential actions. Here's how this mechanism aids in the role-playing process:"
                },
                {
                    "type": "list",
                    "order": 3,
                    "data": [
                        "Defining Character Capabilities: Stats quantitatively define what a character can and cannot do, setting realistic expectations for their performance in various situations. For instance, a character with high intelligence but low physical strength will excel in problem-solving and possibly magical tasks but struggle in hand-to-hand combat.",
                        "Guiding Decision-Making: Understanding their character’s skills and abilities helps players make informed decisions that align with their character’s profile, adding depth to the game and encouraging creative solutions within character constraints.",
                        "Conflict Resolution: The stats provide a clear, unbiased method to resolve actions during gameplay. Whether attempting to climb a wall, negotiate a deal, or cast a spell, outcomes are determined by dice rolls plus relevant skill modifiers, adding suspense and chance to the game.",
                        "Enhancing Storytelling: Characters' strengths and flaws can drive the narrative, create dramatic tension, and introduce challenges that are integral to the plot development, making the story more engaging for everyone involved."
                    ],
                    "style_class": "list-decimal pl-6 pb-6 space-y-2"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "By integrating stats into skills and abilities, L.O.T.U.S. RPG effectively merges strategic gameplay with narrative development, making each session both a game and a collaborative storytelling experience. This structured approach helps players conceptualize their characters' capabilities and limitations, providing a comprehensive framework for what a character can successfully achieve within the game."
                }
            ]
        },
        {
            "title": "Abilities",
            "slug": "abilities",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "In our exploration of character capabilities within the game, we categorize abilities into three sub-groups: Physical, Mental, and Social."
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "The Physical category includes attributes such as strength, endurance, reflexes, and chakra, which govern the bodily aspects of a character. The Mental category encompasses perception and intellect, focusing on the cognitive traits. The Social category includes manipulation and control, psychological traits that influence how a character interacts with the world and manipulates their environment."
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "To effectively quantify and understand the extent to which each character possesses these abilities, we use the Ability Benchmark system. This system assigns a numerical value, ranging from 1 to 15+, to each level of ability, with each number corresponding to a specific descriptor that illustrates the character's competency in that area."
                },
                {
                    "type": "list",
                    "order": 5,
                    "data": [
                        "1 - Impaired",
                        "2 - Inept",
                        "3 - Weak",
                        "4 - Below Average",
                        "5 - Average",
                        "6 - Above Average",
                        "7 - Remarkable",
                        "8 - Exceptional",
                        "9 - Outstanding",
                        "10 - Truly Gifted",
                        "11 - Extraordinary",
                        "12 - Phenomenal",
                        "13 - Legendary",
                        "14 - Pinnacle",
                        "15+ - Supranatural"
                    ],
                    "style_class": "list-none pb-6"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "As an example, let’s delve deeper into the Physical category using strength as our focal point to illustrate each benchmark level:"
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "Impaired: The character struggles with even the lightest objects and may require assistance for basic physical tasks.",
                        "Inept: Difficulty in lifting items that most would handle easily; basic physical actions are more laborious.",
                        "Weak: Capable of performing everyday tasks but quickly tires and is unable to manage heavy lifting or prolonged strenuous activities.",
                        "Below Average: Slightly weaker than the average individual, facing challenges with moderately heavy loads.",
                        "Average: Adequately manages standard physical tasks such as moving furniture or carrying groceries.",
                        "Above Average: Displays a degree of strength greater than the norm, facilitating easier participation in physical labor or sports.",
                        "Remarkable: Exhibits notable power, capable of lifting heavy weights that would be challenging for many.",
                        "Exceptional: Distinguished strength that stands out, enabling the lifting and moving of significantly heavy objects.",
                        "Outstanding: Possesses superior strength crucial in situations that demand substantial physical power; capable of handling extreme weights.",
                        "Truly Gifted: A rare level of strength that might qualify the character for high-level competitive strength events.",
                        "Extraordinary: Shows almost superhuman capabilities, capable of astonishing feats of strength.",
                        "Phenomenal: Near the peak of human potential, able to perform in extraordinary ways that may set records.",
                        "Legendary: Epic strength often celebrated in stories or capable of historical athletic feats.",
                        "Pinnacle: Represents the highest humanly achievable level of strength, observed only in the strongest individuals throughout history.",
                        "Supranatural: Exceeds the boundaries of human capabilities, venturing into the realms of fantasy or superhuman powers, dealing with physical challenges well beyond ordinary human capacity."
                    ],
                    "style_class": "list-none space-y-2"
                },
            ]    
        },
        {
            "title": "Physical Abilities",
            "slug": "physical-abilities",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "subheading",
                    "order": 2,
                    "data": "Strength (STR):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Measures the capability of exerting or resisting force and power."
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Damage dealt by melee or thrown attacks.",
                        "Athletics feats such as power lifting, running, jumping, climbing, or swimming.",
                        "Static actions such as carrying capacity."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 5,
                    "data": "Endurance (END):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Overall physical health and resilience."
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "Resisting damage from melee or ranged attacks.",
                        "Stamina feats such as long-distance running or resisting poison and disease.",
                        "Static actions such as recovering from injury and illness."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 8,
                    "data": "Reflexes (REF):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "Coordination involving agility, speed, manual dexterity, and balance."
                },
                {
                    "type": "list",
                    "order": 10,
                    "data": [
                        "Striking with melee or avoiding being struck by melee and ranged attacks via parry or dodge.",
                        "Acrobatics or Stealth feats such as minimizing falling damage, tumbling, avoiding visual detection, or losing a person in a crowd.",
                        "Static actions such as maintaining balance or reacting quickly to avoid clumsy mishaps."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 11,
                    "data": "Chakra (CHA):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "Internally harnessed energy allowing for feats beyond the human norm."
                },
                {
                    "type": "list",
                    "order": 13,
                    "data": [
                        "Activating and powering unique equipment and gear.",
                        "Bio Control feats such as slowing heart rate, controlling breathing, and other bodily control acts.",
                        "Activation of Techniques."
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Mental Abilities",
            "slug": "mental-abilities",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "subheading",
                    "order": 2,
                    "data": "Perception (PER):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Mental awareness and the speed at which information is processed."
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Striking with ranged attacks.",
                        "Mental aggressive challenges.",
                        "Investigative feats such as spotting, deciphering, or damage dealt by melee or thrown attacks.",
                        "Static actions such as initiative, spotting abnormalities, and noting how people react."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 5,
                    "data": "Intellect (INT):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Reasoning and information retention that may be utilized to devise, formulate, or solve a scientific issue in cerebral matters. It may also be used to develop, build, or repair mechanical and technological advances."
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "Mental defensive challenges.",
                        "Awareness, Artisan, Demolition feats such as spotting, deciphering, crafting, or detonating.",
                        "Static actions such as recalling history, technical, or mechanical information."
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Social Abilities",
            "slug": "social-abilities",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "subheading",
                    "order": 2,
                    "data": "Manipulation (MAN):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Influencing others through force of personality, leadership, and critical behaviors designed to control others."
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Social aggressive challenges.",
                        "Persuasion, Performance, or Intimidation feats such as debating, seduction, singing, dancing, interrogation, etc.",
                        "Static actions such as remembering names or details about a person’s preferences."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 5,
                    "data": "Control (CON):",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Confidence and self-awareness that allows for the resistance to subtle or forceful manipulations of others."
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "Social defensive challenges.",
                        "Willpower, Piloting, Sailing, and Vehicle Operation feats, such as resisting interrogation, intimidation, seduction, or maintaining control of vessels under adverse conditions.",
                        "Static actions such as maintaining composure or a poised demeanor regardless of the environment."
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Age Categories & Effects",
            "slug": "age-effects",
            "chapter": "Character Genesis",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Age",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "The abilities of a person change as they age and mature. Being exceptionally young or aging past a species' prime shifts certain traits, some beneficial, some detrimental. Child, Adult, Middle Aged, and Elder. Each setting may have Species who live differing lengths of time and are factored into that Species' starting cost. Every year after the Elder category, they must make a Difficult Uncontested Challenge of (Athletics Sum - Cumulative Years of Elder) or perish."
                },
                {
                    "type": "subheading",
                    "order": 3,
                    "data": "Short Life Span (50 Years)",
                    "style_class": "text-lg font-semibold mt-4 text-red-500"
                },
                {
                    "type": "list",
                    "order": 4,
                    "data": [
                        "Child: ≤ 5 (+2 to Dodge Sum.)",
                        "Adult: 6-25 (No Mods: Loses +2 to Dodge Sum)",
                        "Middle Aged: 26-40 (+2 to Martial Arts & Willpower Sum, -2 to Power, Acrobatics Sum)",
                        "Elder: 40-50 (+2 to Scholar & Medicine Sum, -2 to Power & Athletic Sum.)"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 5,
                    "data": "Average Life Span (80 Years)",
                    "style_class": "text-lg font-semibold mt-4 text-purple-500"
                },
                {
                    "type": "list",
                    "order": 6,
                    "data": [
                        "Child: ≤ 16 (+2 to Dodge Sum.)",
                        "Adult: 17-39 (No Mods: Loses +2 to Dodge Sum)",
                        "Middle Aged: 40-64 (+2 to Martial Arts & Willpower Sum, -2 to Power & Acrobatics Sum)",
                        "Elder: 65-80 (+2 to Scholar & Medicine Sum, -2 to Power & Athletic Sum.)"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 7,
                    "data": "Long Life Span (250 Years)",
                    "style_class": "text-lg font-semibold mt-4 text-red-500"
                },
                {
                    "type": "list",
                    "order": 8,
                    "data": [
                        "Child: ≤ 20 (+2 to Dodge Sum.)",
                        "Adult: 21-124 (No Mods: Loses +2 to Dodge Sum)",
                        "Middle Aged: 125-224 (+2 to Martial Arts & Willpower Sum, -2 to Power & Acrobatics Sum)",
                        "Elder: 225-250 (+2 to Scholar & Medicine Rolls, -2 to Power & Athletic Rolls.)"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 9,
                    "data": "Venerable Life Span (500 Years)",
                    "style_class": "text-lg font-semibold mt-4 text-purple-500"
                },
                {
                    "type": "list",
                    "order": 10,
                    "data": [
                        "Child: ≤ 20 (+2 to Dodge Sum.)",
                        "Adult: 21-249 (No Mods: Loses +2 to Dodge Sum)",
                        "Middle Aged: 250-474 (+2 to Martial Arts & Willpower Sum, -2 to Power & Acrobatics Sum)",
                        "Elder: 475-500 (+2 to Scholar & Medicine Rolls, -2 to Power & Athletic Rolls.)"
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "How The Game Works",
            "slug": "how-the-game-works",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "subheading",
                    "order": 2,
                    "data": "Quick Math",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "ALL numbers in this game are rounded or set for tabletop compatibility. This was chosen for ease of play over precision. Also, all Imperial Standards are translated to Rounded Metrics to help metric players."
                },
                {
                    "type": "subheading",
                    "order": 4,
                    "data": "Distance",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "list",
                    "order": 5,
                    "data": [
                        "1 in or 1\" = 2.5 cm",
                        "1 ft or 1' = 30 cm (1' x 1' or 30cm x 30cm is referred to as 1 Cube)",
                        "5 ft or 5' = 150 cm or 1.5 m (5' x 5' or 150cm x 150cm is referred to as 5 Cube)",
                        "1 Mi = 1.5 km"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 6,
                    "data": "Weight",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "1 lb = 0.5 Kilograms"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 8,
                    "data": "Game Board Distance",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "list",
                    "order": 9,
                    "data": [
                        "1 Board Square = 5' or 1.5 Meters",
                        "Actual Size: 1 Board Square Measures 1' or 2.54 cm"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 10,
                    "data": "Dice Mechanics",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "To play L.O.T.U.S. RPG you need a minimum of two ten-sided dice. These dice are available at most game and hobby stores."
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "The standard annotation “d#” denotes the number of sides, “d10” for ten-sided dice. The notation of “d#” is preceded by an integer (1d10, 2d10, 3d10, etc.). This integer is the number of dice that must be rolled."
                },
                {
                    "type": "paragraph",
                    "order": 13,
                    "data": "Example: 3d10 means that three ten-sided dice should be rolled. There are two methods used in the DD10 System: the Percentile Method and the Summing Method."
                },
                {
                    "type": "subheading",
                    "order": 14,
                    "data": "Percentile Method",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "You generate a number between 1 and 100 by rolling two different colored ten-sided dice. One is the tens column or the high die. The other is the ones column or low die. This designation shall be announced before you roll and should be kept for the duration of the game session for consistency. Results are determined as follows:"
                },
                {
                    "type": "list",
                    "order": 16,
                    "data": [
                        "High Die 0 & Low Die 1 = 1%",
                        "High Die 5 & Low Die 0 = 50%",
                        "High Die 0 & Low Die 0 = 100%"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "subheading",
                    "order": 17,
                    "data": "Summing Method",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "Summing rolls are cumulative rolls acquired by rolling the declared dice and adding the results to Abilities, Skills, and any modifiers as applicable to the Challenge being made. This is referred to as a Sum or Sum Roll. All primary Challenge rolls utilize 2d10."
                },
                {
                    "type": "subheading",
                    "order": 19,
                    "data": "Summing Critical Botches",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "If a 1 is rolled on both D10, then a critical botch has occurred. A critical botch not only causes automatic failure of the attempted task, but the storyteller shall assign an appropriate penalty or consequence. If a Critical Success was initially rolled, then chain success rolls may not Critically Botch. This may be changed via 2 Wyld Die expenditures."
                },
                {
                    "type": "subheading",
                    "order": 21,
                    "data": "Summing Critical Success",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 22,
                    "data": "If a 10 is rolled on both D10, then a critical success has occurred. The roll receives a +10 and the rules of a chain success are applied; an additional positive outcome occurs at the GM's discretion."
                },
                {
                    "type": "subheading",
                    "order": 23,
                    "data": "Summing Critical Chain",
                    "style_class": "text-lg font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 24,
                    "data": "When a Critical occurs, a chain success is initiated. Every 10 rolled allows another D10 to be rolled, every time a 10 comes up. This process is repeated and summed cumulatively. (i.e., If a player is attempting to take an action, they roll 2D10. Two 10s are rolled; the follow-up rolls result in a 10 and a 5. The 10 is re-rolled and added to the previous sum. The re-roll results in a 3. The total added to the associated Skill Sum would be 48.)"
                },
                {
                    "type": "table",
                    "order": 25,
                    "data": {
                        "headers": ["Initial Roll", "Critical Success Bonus", "Chain Success Bonus Roll", "Continued Chain Success Bonus Roll", "Sum"],
                        "rows": [
                            ["10 + 10", "+10", "+10 + 5", "+3", "= 48"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-400 mt-4"
                }
            ]
        },
        {
            "title": "Challenges & Difficulty Levels",
            "slug": "challenges-difficulty-levels",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Challenges",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Challenges utilize Summing Rolls and are either contested or uncontested."
                },
                {
                    "type": "subheading",
                    "order": 3,
                    "data": "Challenge (Contested)",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "A contested challenge is a challenge that pits two contesting forces against each other. Whether it is PC(s) versus PC(s) or NPC(s) versus PC(s), this type of challenge requires a contested challenge. (I.e., If a PC attempts to strike another PC/NPC or if a PC attempts to hack into an AI counter-intrusion system, then a contested challenge will be required.)"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Both contestants roll 2D10 and add this to the Skill, Abilities, and other applicable modifiers relevant to the contested challenge. Whoever possesses a higher score is successful, while a tie calls for a reroll. Difficulties are set with the premise that a person has some training or understanding of a task, because what is easy for some is not easy for others."
                },
                {
                    "type": "subheading",
                    "order": 6,
                    "data": "Challenge (Contested, Extended)",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "Not all challenges are resolved in a single roll. Extended Challenges are utilized during truly important or difficult courses of action. This is very helpful in lengthy contests, high-stakes negotiations, or other critical story moments that should be summed up more dramatically than a single roll of the dice."
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "When faced with an Extended Challenge, the Game Master determines the number of successes each side needs to achieve victory. During each phase of the Extended Challenge, each side describes their actions and/or words before each Contested roll. Based on the actions or words chosen by each side, the Game Master may place modifiers on either side."
                },
                {
                    "type": "subheading",
                    "order": 9,
                    "data": "Challenge (Uncontested Simple)",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "If the PC’s Skill Sum relevant to the challenge is equal to the difficulty of the challenge, then success is automatic, and no test is required."
                },
                {
                    "type": "subheading",
                    "order": 11,
                    "data": "Challenge (Uncontested Difficulty-Based)",
                    "style_class": "text-xl font-semibold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "If a PC engages in a challenge that is more difficult than a simple challenge but does not consist of opposing forces at work, then they must engage in a difficulty-based challenge."
                },
                {
                    "type": "heading",
                    "order": 13,
                    "data": "Difficulty Level Ranges",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "table",
                    "order": 14,
                    "data": {
                        "headers": ["Difficulty Level", "Range", "Description"],
                        "rows": [
                            ["Simple", "<10", "A task so simple that even a person with little or no Skill could quite possibly complete it with ease."],
                            ["Very Easy", "10-14", "A task that a minimally skilled person could possibly complete."],
                            ["Easy", "15-20", "These are what compromise most of our daily tasks."],
                            ["Moderate", "21-30", "Tasks of this nature require skill, effort, and concentration."],
                            ["Difficult", "31-40", "Difficult tasks are hard, and an average person will have problems succeeding."],
                            ["Very Difficult", "41-50", "Only the most talented of individuals have any chance of success."],
                            ["Heroic", "51-60", "Impossible for normal people and exceedingly difficult even for heroes."],
                            ["Legendary", "61+", "Beyond the measure of mortal men and truly worthy of myths and legends."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-400 mt-4 pb-6"
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "Please note that the difficulty of a task may be increased due to environmental factors, including but not limited to bad weather conditions, sensory distractions, personal injury, great stress (arguments with a loved one, being trapped in a burning room or under ranged fire), and improper equipment or tools required to complete the task."
                }
            ]
        },
        {
            "title": "Carrying Capacity",
            "slug": "carrying-capacity",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Determines how much a character can lift and what weight slows them down. The Carrying Capacity table lists character lift capability based on (Strength + Power) x 1/2 Creature Size."
                },
                {
                    "type": "list",
                    "order": 2,
                    "data": [
                        "(UL) Unencumbered / (LL) Light Load: No penalties.",
                        "Heavy Load: -5 to Dodge & Double AP Costs.",
                        "Push or Drag: Up to Double their Max Load at ½ Speed."
                    ],
                    "style_class": "list-disc pl-6 pb-6"
                },
                {
                    "type": "container",
                    "order": 3,
                    "data": "open",
                    "style_class": "flex justify-center gap-8"
                },
                {
                    "type": "container",
                    "order": 4,
                    "data": "open",
                    "style_class": "flex flex-col items-center"
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Carrying Capacity Index (Lbs.)",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "table",
                    "order": 6,
                    "data": {
                        "headers": ["Total Power", "Light Load", "Heavy Load", "Over Press", "Dead Lift", "Bench Press"],
                        "rows": [
                            ["1", "10", "50", "25", "50", "50"],
                            ["2", "20", "100", "50", "100", "100"],
                            ["3", "30", "150", "100", "200", "150"],
                            ["4", "40", "200", "150", "300", "200"],
                            ["5", "50", "250", "200", "400", "250"],
                            ["6", "60", "300", "250", "500", "300"],
                            ["7", "70", "350", "275", "550", "350"],
                            ["8", "80", "400", "300", "600", "400"],
                            ["9", "90", "450", "325", "650", "450"],
                            ["10", "100", "500", "350", "700", "500"],
                            ["11", "110", "550", "375", "750", "550"],
                            ["12", "120", "600", "400", "800", "600"],
                            ["13", "130", "650", "425", "850", "650"],
                            ["14", "140", "700", "450", "900", "700"],
                            ["15", "150", "750", "475", "950", "750"],
                            ["16", "160", "800", "500", "1000", "800"],
                            ["17", "170", "850", "525", "1050", "850"],
                            ["18", "180", "900", "550", "1100", "900"],
                            ["19", "190", "950", "575", "1150", "950"],
                            ["20", "200", "1000", "600", "1200", "1000"],
                            ["21", "210", "1100", "650", "1300", "1100"],
                            ["22", "220", "1200", "700", "1400", "1200"],
                            ["23", "230", "1300", "750", "1500", "1300"],
                            ["24", "240", "1400", "800", "1600", "1400"],
                            ["25", "250", "1500", "850", "1700", "1500"],
                            ["26+", "+50", "+250", "+125", "+250", "+250"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "container",
                    "order": 7,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 8,
                    "data": "open",
                    "style_class": "flex flex-col items-center"
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Carrying Capacity Index (Kilos)",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "table",
                    "order": 10,
                    "data": {
                        "headers": ["Total Power", "Light Load", "Heavy Load", "Over Press", "Dead Lift", "Bench Press"],
                        "rows": [
                            ["1", "20", "100", "50", "100", "100"],
                            ["2", "40", "200", "100", "200", "200"],
                            ["3", "60", "300", "200", "400", "300"],
                            ["4", "80", "400", "300", "600", "400"],
                            ["5", "100", "500", "400", "800", "500"],
                            ["6", "120", "600", "500", "1000", "600"],
                            ["7", "140", "700", "550", "1100", "700"],
                            ["8", "160", "800", "600", "1200", "800"],
                            ["9", "180", "900", "650", "1300", "900"],
                            ["10", "200", "1000", "700", "1400", "1000"],
                            ["11", "220", "1100", "750", "1500", "1100"],
                            ["12", "240", "1200", "800", "1600", "1200"],
                            ["13", "260", "1300", "850", "1700", "1300"],
                            ["14", "280", "1400", "900", "1800", "1400"],
                            ["15", "300", "1500", "950", "1900", "1500"],
                            ["16", "320", "1600", "1000", "2000", "1600"],
                            ["17", "340", "1700", "1050", "2100", "1700"],
                            ["18", "360", "1800", "1100", "2200", "1800"],
                            ["19", "380", "1900", "1150", "2300", "1900"],
                            ["20", "400", "2000", "1200", "2400", "2000"],
                            ["21", "420", "2200", "1300", "2600", "2200"],
                            ["22", "440", "2400", "1400", "2800", "2400"],
                            ["23", "460", "2600", "1500", "3000", "2600"],
                            ["24", "480", "2800", "1600", "3200", "2800"],
                            ["25", "500", "3000", "1700", "3400", "3000"],
                            ["26+", "100", "500", "250", "500", "500"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "container",
                    "order": 11,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 12,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 13,
                    "data": "open",
                    "style_class": "flex justify-center gap-8"
                },
                {
                    "type": "container",
                    "order": 14,
                    "data": "open",
                    "style_class": "w-1/2"
                },
                {
                    "type": "heading",
                    "order": 15,
                    "data": "Creature Size & Reach",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "Small and Medium-sized creatures have a 5 ft. reach and take up a 5’x5’ space, which means the creature can make a melee attack at any target up to 5 ft. away or lunge at an additional 5’ beyond their reach. Larger and smaller characters have a longer or shorter reach and take up differing amounts of space as shown."
                },
                {
                    "type": "container",
                    "order": 17,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 18,
                    "data": "open",
                    "style_class": "w-1/2"
                },
                {
                    "type": "heading",
                    "order": 19,
                    "data": "Creature Size & Reach",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "Small and Medium-sized creatures have a 150 cm reach and take up a 1.5 m space, which means the creature can make a melee attack at any target up to 5 ft. away or lunge at an additional 5’ beyond their reach. Larger and smaller characters have a longer or shorter reach and take up differing amounts of space as shown."
                },
                {
                    "type": "container",
                    "order": 21,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 22,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 23,
                    "data": "open",
                    "style_class": "flex justify-center gap-8"
                },
                {
                    "type": "container",
                    "order": 24,
                    "data": "open",
                    "style_class": "w-1/2"
                },
                {
                    "type": "heading",
                    "order": 25,
                    "data": "Creature Size & Reach Index (Feet)",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "table",
                    "order": 26,
                    "data": {
                        "headers": ["Creature Size", "Reach / Lunge", "Space (5' Squares)"],
                        "rows": [
                            ["Gargantuan S10", "25’ / 30’", "8 x 16"],
                            ["Colossal S8", "20’ / 25’", "4 x 8"],
                            ["Huge S6", "15’ / 20’", "2 x 4"],
                            ["Large S4", "10’ / 15’", "1 x 2"],
                            ["Medium S2", "5’ / 10’", "1 x 1"],
                            ["Small S1", "5’ / 10’", "1 x 1"],
                            ["Tiny S0", "0’ / 5’", ".5 x .5"],
                            ["Diminutive S00", "0’ / 5’", ".25 x .25"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "container",
                    "order": 27,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 28,
                    "data": "open",
                    "style_class": "w-1/2"
                },
                {
                    "type": "heading",
                    "order": 29,
                    "data": "Creature Size & Reach Index (Meters)",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "table",
                    "order": 30,
                    "data": {
                        "headers": ["Creature Size", "Reach / Lunge", "Space (1.5 m Squares)"],
                        "rows": [
                            ["Gargantuan S10", "7.5 m / 9 m", "8 x 16"],
                            ["Colossal S8", "6 m / 7.5 m", "4 x 8"],
                            ["Huge S6", "4.5 m / 6 m", "2 x 4"],
                            ["Large S4", "3 m / 4.5 m", "1 x 2"],
                            ["Medium S2", "1.5 m / 3 m", "1 x 1"],
                            ["Small S1", "1.5 m / 3 m", "1 x 1"],
                            ["Tiny S0", "0 m / 1.5 m", ".5 x .5"],
                            ["Diminutive S00", "0 m / 1.5 m", ".25 x .25"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "container",
                    "order": 31,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 32,
                    "data": "close"
                }                
            ]
        },
        {
            "title": "Fear",
            "slug": "fear",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "When an individual experiences an event that the Game Master or Storyteller decides warrants a Fear Check or a Power/Ability is used that invokes Fear then either an Uncontested or a Contested Roll is made."
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "In a scenario that warrants a Fear Check then the Storyteller sets a Fear Rating based on how terrifying the events that transpire are. The Player Characters that are affected must Roll Bio Control + ML. Characters that roll below this predetermined amount must roll on Fear Reaction Table I, those who tie are considered Shaken while those who pass are unaffected. Individuals who botch automatically roll on Fear Reaction Table II. The Storyteller may feel free to apply conditional modifiers based on circumstances."
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "In the event of a Contested Roll use the rules as defined under the Skill or Power."
                },
                {
                    "type": "container",
                    "order": 4,
                    "data": "open",
                    "style_class": "flex justify-center gap-8"
                },
                {
                    "type": "container",
                    "order": 5,
                    "data": "open",
                    "style_class": "w-1/2"
                },
                {
                    "type": "heading",
                    "order": 6,
                    "data": "Fear Reaction Table I",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "table",
                    "order": 7,
                    "data": {
                        "headers": ["Roll", "Effect", "Description"],
                        "rows": [
                            ["5 to 17", "Shaken", "-5 to all Non-Dodge or Running Rolls for the next 5 Rounds."],
                            ["3, 4, 18 or 19", "Scared", "-10 to all Non-Dodge or Running Rolls for the next 5 Rounds."],
                            ["2 or 20", "Bad Reaction", "Roll on Fear Reaction Table II."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "container",
                    "order": 8,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 9,
                    "data": "open",
                    "style_class": "w-1/2"
                },
                {
                    "type": "heading",
                    "order": 10,
                    "data": "Fear Reaction Table II",
                    "style_class": "text-xl font-bold text-center"
                },
                {
                    "type": "table",
                    "order": 11,
                    "data": {
                        "headers": ["Roll", "Effect", "Description"],
                        "rows": [
                            ["6 to 16", "Terrified", "Flee away from source of terror at top speed for 2d10 Rounds."],
                            ["5 or 17", "Petrified", "Too terrified to move. Characters can only stand still screaming until the source of fear is removed, leaves, or successfully attacks the character."],
                            ["4 or 18", "Catatonic", "You collapse into a whimpering ball, taking no actions for 1d10 Minutes as your mind withdraws from reality."],
                            ["3 or 19", "Black Out", "Your system has shut itself down to avoid damage as you black out for 2d10 minutes."],
                            ["2 or 20", "Traumatized", "Having experienced more fear than the body can handle, you experience severe emotional trauma. Roll 2d10—on any result except a 2 or 20, you black out for 2d10 minutes and remain catatonic for 2d10 days. If you roll a 2 or 20, your heart seizes up, causing death unless you make an Uncontested Heroic (DL: 60-69) Bio Control Roll."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "container",
                    "order": 12,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 13,
                    "data": "close"
                }
            ]
        },
        {
            "title": "Immortality",
            "slug": "immortality",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Immortals are creatures that do not live or truly die but become a part of reality much like the sun rising or the moon setting. They simply exist unless their energy moves on to the next host or their immortality is intentionally wrested from them; a process that is very difficult to do without very rare and esoteric resources and the intervention of other Immortals."
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Pseudo Immortals are creatures that have tethered a portion of their energy in either a state of Mortem or Vita by utilizing their unique connection often in conjunction with the consumption of the energy of others to strengthen and maintain their tether. This often includes creatures such as abominations, angels, avatars, demons, devils, nephilim, liches, mummies, sphinxes, primordials, and vampires."
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Static Reality",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Static Reality is a rule applicable only to Immortal and Pseudo Immortal creatures as they have become a fixed point in reality, this makes them more difficult for others to alter. Effectively this grants them a degree of protection from external effects such as Alter Age, Polymorph, Alter Sex, Change Size, or any power that would attempt to change their fixed point."
                },
                {
                    "type": "table",
                    "order": 5,
                    "data": {
                        "headers": ["Creature Type", "Resistance per Century"],
                        "rows": [
                            ["Immortal Creatures", "5% cumulative resistance"],
                            ["Pseudo Immortals", "2% cumulative resistance"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                }
            ]
        },
        {
            "title": "Line of Sight",
            "slug": "line-of-sight",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "All creatures have spectrums and distances at which they can clearly see in daylight, light sources, low light, and in the dark."
                },
                {
                    "type": "heading",
                    "order": 2,
                    "data": "Spectrums",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Aura is limited to the distances listed below but shows creatures and objects shrouded in a light spectrum glow akin to infrared. It is limited to beings that have abilities to perceive this spectrum."
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Visible is the normal method of observation for creatures that cannot or are not currently perceiving an aura and functions as normal human vision."
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Distance",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Daylight distance is the baseline based on midday lighting levels and is determined by the Game Master dependent on environmental conditions such as terrain and fog."
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "Light Source distance overrides the Low Light and Darkvision baselines listed below and sets the new range for all within its radius."
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "Low Light is the baseline of vision capability based on being in twilight, moonlight, or in a poorly lit structure."
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "Darkvision is the baseline of vision based on being in a moonless night or inside of an unlit darkened structure."
                },
                {
                    "type": "table",
                    "order": 10,
                    "data": {
                        "headers": ["Vision Type", "Description"],
                        "rows": [
                            ["Daylight", "Baseline vision distance based on midday lighting levels, affected by environmental conditions."],
                            ["Light Source", "Overrides Low Light and Darkvision, setting a new range for all within its radius."],
                            ["Low Light", "Vision capability in twilight, moonlight, or a dimly lit structure."],
                            ["Darkvision", "Vision capability in a moonless night or inside an unlit darkened structure."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                }
            ]
        },
        {
            "title": "Luck",
            "slug": "luck",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Luck is the random chaos that seems to surround heroes and villains, often allowing them the chance to succeed where others would fail."
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Characters gain one permanent Luck every Mastery Level. A Player may expend a Luck Trait to Re-Roll any Roll that has just been made or to add 1d10 to their current Roll or Reroll. Additionally, the Roll affected by Luck is treated as if all 10s function as a Chain Success."
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Expended Luck Traits are gone until that character has rested and slept in an environment that is not inherently dangerous, requiring vigilance and guard duty rotations."
                }
            ]
        },
        {
            "title": "Movement",
            "slug": "movement",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "The GM determines when movement is important enough to measure. During non-combat scenes, movement is fluid and paced at the GM's discretion. During time-sensitive moments or combat, the distance will usually be measured."
                },
                {
                    "type": "heading",
                    "order": 2,
                    "data": "Classifications",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "list",
                    "order": 3,
                    "data": [
                        "Type: Character Movement is either Engaged or Disengaged.",
                        "Pace: The Pace of movement is related to Normal, Push, All Out, or Restricted pace.",
                        "Table-Top: 1 Movement = 1 Square = 1” = 2.54 cm",
                        "LARP: 1 Movement = 1 Physical Step"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 4,
                    "data": "Disengaged (Outside of Combat)",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Normal/Push (Includes CAP Fraction)",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 6,
                    "data": {
                        "headers": ["Measurement", "Formula"],
                        "rows": [
                            ["MPH", "((MAP * 1800) / 5280)"],
                            ["KPH", "(((MAP * 1800) / 5280) / 1.5)"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "heading",
                    "order": 7,
                    "data": "All Out",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "Requires 3 consecutive rounds of Push Movement."
                },
                {
                    "type": "table",
                    "order": 9,
                    "data": {
                        "headers": ["Measurement", "Formula"],
                        "rows": [
                            ["MPH", "((MAP * 1800) / 5280) * All Out Multiplier"],
                            ["KPH", "(((MAP * 1800) / 5280) / 1.5) * All Out Multiplier"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "heading",
                    "order": 10,
                    "data": "Disengaged, All Out Multiplier",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "The Default All Out Multipliers are 1.25, though special abilities may increase this. Animals, vehicles, and other supernatural creatures may have different All Out Speed Modifiers."
                },
                {
                    "type": "heading",
                    "order": 12,
                    "data": "Disengaged Sustained Speed",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "heading",
                    "order": 13,
                    "data": "Normal/Push (Includes CAP Fraction)",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 14,
                    "data": "Athletics Roll Hourly. Failure results in CAP & MAP values cumulatively being cut in half until Respite, Sleep, or Interrupted Sleep occurs."
                },
                {
                    "type": "table",
                    "order": 15,
                    "data": {
                        "headers": ["Difficulty Formula"],
                        "rows": [
                            ["MPH", "MPH * Hours"],
                            ["KPH", "(KPH / 1.5) * Hours"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "heading",
                    "order": 16,
                    "data": "All Out",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 17,
                    "data": "Athletics Roll Every 10 Minutes. Failure results in CAP & MAP values cumulatively being cut in half until Respite, Sleep, or Interrupted Sleep occurs."
                },
                {
                    "type": "table",
                    "order": 18,
                    "data": {
                        "headers": ["Difficulty Formula"],
                        "rows": [
                            ["MPH", "MPH + (5 x 10 Minute Increments)"],
                            ["KPH", "(KPH / 1.5) + (5 x 10 Minute Increments)"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 pb-6"
                },
                                {
                    "type": "paragraph",
                    "order": 18,
                    "data": ""
                },
                                {
                    "type": "heading",
                    "order": 19,
                    "data": "Calculated Values",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 19,
                    "data": {
                        "headers": ["Disengaged MAP", "MPH", "KPH", "All Out MPH", "All Out KPH"],
                        "rows": [
                            ["3", "1.02", "1.53", "1.28", "1.92"],
                            ["4", "1.36", "2.05", "1.70", "2.56"],
                            ["5", "1.70", "2.56", "2.13", "3.20"],
                            ["6", "2.05", "3.07", "2.56", "3.84"],
                            ["7", "2.39", "3.58", "2.98", "4.47"],
                            ["8", "2.73", "4.09", "3.41", "5.11"],
                            ["9", "3.07", "4.60", "3.84", "5.73"],
                            ["10", "3.41", "5.11", "4.26", "6.39"],
                            ["11", "3.75", "5.63", "4.69", "7.03"],
                            ["12", "4.09", "6.14", "5.11", "7.67"],
                            ["13", "4.43", "6.65", "5.54", "8.31"],
                            ["14", "4.77", "7.16", "5.97", "8.95"],
                            ["15", "5.11", "7.67", "6.39", "9.59"],
                            ["16", "5.45", "8.18", "6.82", "10.23"],
                            ["17", "5.80", "8.69", "7.24", "10.87"],
                            ["18", "6.14", "9.20", "7.67", "11.51"],
                            ["19", "6.48", "9.72", "8.10", "12.14"],
                            ["20", "6.82", "10.23", "8.52", "12.78"],
                            ["21", "7.16", "10.74", "8.95", "13.42"],
                            ["22", "7.50", "11.25", "9.38", "14.06"],
                            ["23", "7.84", "11.76", "9.80", "14.70"],
                            ["24", "8.18", "12.27", "10.23", "15.34"],
                            ["25", "8.52", "12.78", "10.65", "15.98"],
                            ["26", "8.86", "13.30", "11.08", "16.62"],
                            ["27", "9.20", "13.81", "11.51", "17.26"],
                            ["28", "9.55", "14.32", "11.93", "17.90"],
                            ["29", "9.89", "14.83", "12.36", "18.54"],
                            ["30", "10.23", "15.34", "12.78", "19.18"],
                            ["31", "10.57", "15.85", "13.21", "19.82"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 pt-12 pb-12"
                },
                {
                    "type": "heading",
                    "order": 20,
                    "data": "Engaged (In Combat)",
                    "style_class": "text-xl font-bold mt-16"
                },
                {
                    "type": "heading",
                    "order": 21,
                    "data": "Normal",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 22,
                    "data": "1 MAP Expenditure = 1 Movement."
                },
                {
                    "type": "heading",
                    "order": 23,
                    "data": "Push",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "list",
                    "order": 24,
                    "data": [
                        "1 MAP Expenditure = 1 Movement.",
                        "2 CAP Expenditure = 1 Movement.",
                        "-2 to Combat Attacks."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 25,
                    "data": "All Out",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "list",
                    "order": 26,
                    "data": [
                        "Requires 3 Consecutive Rounds of Push Movement.",
                        "1 MAP Expenditure = 1 Movement.",
                        "2 CAP Expenditure = 1 Movement. (Must Use All.)",
                        "May NOT Attack.",
                        "Adds All Out Multiplier to Speed."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 27,
                    "data": "Jumping",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 28,
                    "data": "Jumping is a subtype of movement, based on your Athletics Sum. Distance moved by jumping counts as part of your normal movement in a round."
                },
                {
                    "type": "table",
                    "order": 29,
                    "data": {
                        "headers": ["Jump Type", "Formula"],
                        "rows": [
                            ["Running Long Jump", "Athletics Sum + 10"],
                            ["Standing Long Jump", "Athletics Sum"],
                            ["Vertical Jump", "Athletics Sum - 5"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "*Round all distances down to the nearest foot, limited by AP Expenditure."
                },
                {
                    "type": "paragraph",
                    "order": 31,
                    "data": "If you fail a long jump by a distance equal to your height or less, you may attempt an Easy Acrobatics Sum (DL: 20 to 29) to grab the desired edge. A Very Easy Athletics (DL: 10-19) roll is required to pull yourself up without assistance. You may hang on for a number of rounds equal to Endurance + Athletics + Bio Control Roll."
                },
                {
                    "type": "heading",
                    "order": 32,
                    "data": "Swimming",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 33,
                    "data": "Swimming is a subtype of movement, based on your (Athletics Sum / 4). Distance moved by swimming consumes MAP."
                },
                {
                    "type": "heading",
                    "order": 34,
                    "data": "Drowning",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 35,
                    "data": "A character can hold their breath for a number of rounds equal to a Bio Control roll before they begin drowning. When drowning, a character is immediately incapacitated and must make an Uncontested Athletics Roll equal to the # of rounds Drowning x 5 or perish."
                }
            ]
        },
        {
            "title": "Movement Restrictions",
            "slug": "movement-restrictions",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Obstacles",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "table",
                    "order": 2,
                    "data": {
                        "headers": ["Obstacle", "Movement Modifier"],
                        "rows": [
                            ["Climbing Tree", "Total x 0.75"],
                            ["Wall (Grip Points Available)", "Total x 0.50"],
                            ["Wall (Smooth)", "Total x 0.25"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Opposed & Restricted Movement",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Opposed: An adjustable movement based on needs and scenarios including combat and foot races. Opposed movement is based on Action Point expenditures."
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Restricted: Difficult terrain, reduced visibility, or other obstructions hamper movement. When movement is restricted, the Action Point Cost is doubled and the movement speed total is reduced. Restricted movement may require an Uncontested Simple Roll."
                },
                {
                    "type": "heading",
                    "order": 6,
                    "data": "Terrain Modifiers",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "table",
                    "order": 7,
                    "data": {
                        "headers": ["Terrain", "Movement Modifier"],
                        "rows": [
                            ["Moderate Undergrowth", "Total x 0.75"],
                            ["Heavy Undergrowth", "Total x 0.50"],
                            ["Steep Incline", "Total x 0.75"],
                            ["Unstable/Slippery Surface (Sand/Mud/Ice)", "Total x 0.75"],
                            ["Unstable/Slippery Incline Surface", "Total x 0.50"],
                            ["Waist Deep Swamp/Snow", "Total x 0.25"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "heading",
                    "order": 8,
                    "data": "Visibility Modifiers",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "table",
                    "order": 9,
                    "data": {
                        "headers": ["Visibility", "Movement Modifier"],
                        "rows": [
                            ["Lessened Visibility (Light Fog/Dim)", "Total x 0.75"],
                            ["Low Visibility (Heavy Fog/Darkness)", "Total x 0.50"],
                            ["Blindness", "Total x 0.25"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "If engaging in sustained Opposed or Restricted Movement, you can continue this for several minutes equal to Endurance + Athletics + Bio Control before having to reduce movement to half of max AP expenditure capability. This process continues until you are unable to run."
                }
            ]
        },
        {
            "title": "Optional Movement Method",
            "slug": "optional-movement-method",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Disengaged (Outside of Combat) - Optional SED Method",
                    "style_class": "text-xl font-bold text-center mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "This method focuses on simplicity and roleplay over precision. It sets a number of encounters based on the distance traveled by the group, creating opportunities for adventure and immersion without bogging down gameplay. Flavor text and descriptors add depth, making travel feel more epic and adventurous."
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Set Encounters",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Encounters are key components of the SED, encompassing anything that happens during the journey. The number of encounters is determined by the distance category (see below). Each encounter type focuses on enriching the narrative through different gameplay styles."
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Encounter Types",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "heading",
                    "order": 6,
                    "data": "Combat",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "Combat encounters create a sense of danger and urgency. These can be tied to the story or serve as standalone challenges, showcasing the perils of travel."
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "**Example:** As your group crests a hill, the rhythmic sound of boots crunching gravel comes from below. A band of brigands emerges, a swarthy figure in poorly kempt chain bellows, 'These roads are closed, the toll be your silver and whatever else we see fit to take!' Weapons glint in the fading light, and you know there’s little chance for escape without a fight."
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Roleplay",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "Roleplay encounters bring the world to life, offering opportunities to explore cultures, regional customs, or character relationships. They may shift into other encounter types depending on player choices."
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "**Example:** The caravan halts as an old man wearing patchwork clothing approaches, arms wide in greeting. 'Travelers!' they exclaim. 'Might you be interested in trade or tales of this land? Perhaps you seek rarities only found in these parts?' The figure’s bright eyes suggest one who is excited to finally have a moment’s company."
                },
                {
                    "type": "heading",
                    "order": 12,
                    "data": "Skill",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 13,
                    "data": "Skill challenges highlight the landscape and demand clever solutions to obstacles or hazards. These scenarios allow players to use their abilities to navigate, survive, or resolve problems."
                },
                {
                    "type": "paragraph",
                    "order": 14,
                    "data": "**Example:** The slick and crumbling mossy rock path ahead crosses a roaring river that churns ominously. Safe passage may require the proper tools or deft footwork. Who will lead the way, and how?"
                },
                {
                    "type": "heading",
                    "order": 15,
                    "data": "Combination",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "Combination encounters weave combat, roleplay, and skill challenges together, creating layered scenarios that engage all characters’ strengths. By choosing other options, the players might even be able to utilize Skills to shift a Combat into Roleplay or vice versa, depending on their actions."
                },
                {
                    "type": "heading",
                    "order": 17,
                    "data": "Distance and Encounter Frequency",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "table",
                    "order": 18,
                    "data": {
                        "headers": ["Distance Category", "Number of Encounters", "Example Flavor Text"],
                        "rows": [
                            ["Nearby", "1", "You can see the spires of the old watchtower in the distance, but between here and there, a dense thicket writhes with strange noises."],
                            ["Short Trip", "1-2", "The sun is high when you come across a cluster of ruins hidden by overgrowth. The air is eerily still. Do you explore or move on? Later, as the town’s gates come into view, a pair of guards halts you, demanding to see your travel permits."],
                            ["Distant Journey", "2-3", "On the second night, howling wolves circle your camp, their glowing eyes watching from the tree line. By morning, a collapsed bridge blocks your path, leaving you to choose between fording the river or taking a perilous detour through troll-infested woods."],
                            ["Far-Flung Adventure", "3-5", "Days blend together as your party crosses fields, forests, and mountains. In a small village, an old herbalist begs you to retrieve a stolen amulet, warning of its dark curse. You find an encircled caravan beset by marauding Fel’dren. Do you use the distraction to quietly pass by, or do you lend aid and hope a rescued caravan might offer a reward?"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300"
                },
                {
                    "type": "heading",
                    "order": 19,
                    "data": "Tips for Game Masters",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "list",
                    "order": 20,
                    "data": [
                        "Use Dynamic Descriptions: Enhance immersion by describing the sights, sounds, and smells of each encounter.",
                        "Vary Encounter Types: Avoid monotony by mixing combat, roleplay, and skill challenges.",
                        "Incorporate Player Backstories: Tie encounters to characters’ pasts or goals for greater investment.",
                        "Foreshadow Future Events: Use encounters to plant seeds for later story arcs."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "paragraph",
                    "order": 21,
                    "data": "By using the SED method with these examples and flavor text, you can transform simple travel into memorable, high-adventure storytelling."
                }
            ]
        },
        {
            "title": "Resting",
            "slug": "resting",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Resting is the means by which a character naturally recovers Chakra and Battle Hit Points (BHP). There are three primary types of rest: Respite, Recovery, and Sleep, with a subcategory of Interrupted Sleep."
                },
                {
                    "type": "heading",
                    "order": 2,
                    "data": "Recovery",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Recovery represents the body’s natural healing over time while active. An active person not engaging in Interrupted Sleep, Respite, or Sleep recovers 1 Chakra per hour and 1 BHP per hour."
                },
                {
                    "type": "heading",
                    "order": 4,
                    "data": "Respite",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Respite is a short period of rest or relief. It requires those partaking to cease all activities except those that can be engaged in while reposing, such as snacking, reading, or vulnerary activities, for half an hour. It can be performed no more than twice between completed Sleep/Interrupted Sleep cycles. The benefits are as follows:"
                },
                {
                    "type": "list",
                    "order": 6,
                    "data": [
                        "Chakra is restored an amount equal to the character’s CHP.",
                        "BHP is restored an amount equal to SHP."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 7,
                    "data": "Sleep",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "Sleep is a long period of rest. It requires those partaking to cease all activities. It can be performed once per twenty-four-hour period and requires that a person remain undisturbed for seven or more hours uninterrupted. The benefits are as follows:"
                },
                {
                    "type": "list",
                    "order": 9,
                    "data": [
                        "Chakra is restored an amount equal to the character’s ((CHP x Hours of Rest) x 2).",
                        "BHP is restored an amount equal to ((SHP x Hours of Rest) x 2)."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 10,
                    "data": "Interrupted Sleep",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "Interrupted Sleep occurs when normal sleep is cut short or disturbed before reaching the seven-hour minimum. However, it still requires that a person remain undisturbed for at least four hours uninterrupted. The benefits are as follows:"
                },
                {
                    "type": "list",
                    "order": 12,
                    "data": [
                        "Chakra is restored an amount equal to the character’s (CHP x Hours of Rest).",
                        "BHP is restored an amount equal to (SHP x Hours of Rest)."
                    ],
                    "style_class": "list-disc pl-6"
                }
            ]
        },
        {
            "title": "Throwing",
            "slug": "throwing",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Characters can throw any object they can lift with a Power Sum. All distances are measured in 1\" / 2.5cm squares (5' or 1.5M)."
                },
                {
                    "type": "table",
                    "order": 2,
                    "data": {
                        "headers": ["Object Type", "Difficulty Level (DL)", "Throw Distance Formula"],
                        "rows": [
                            ["Object Designed for Throwing", "Easy (DL: 15-20)", "Distance = Double (Power)"],
                            ["Light Weight Object", "Moderate (DL: 21-30)", "Distance = (Power)"],
                            ["Light Load Object", "Difficult (DL: 31-40)", "Distance = (0.5 x Power)"],
                            ["Heavy Load Object", "Heroic (DL: 51-60)", "Distance = (0.25 x Power)"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                }
            ]
        },
        {
            "title": "Traits & Action Points",
            "slug": "traits-action-points",
            "chapter": "Core Mechanics",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Traits, Expendable",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Species/Subtype, Calling, Culture, Abilities, Boons, and Banes are utilized to calculate Traits."
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Action Points",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "When a PC attempts to perform an action utilizing challenges, there is a chance of failure. Action Points are required to be expended to take this chance."
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Combat Action Points (CAP)",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Combat Action Points (CAP) are equal to the sum of ((Strength + Endurance + Reflexes + Perception + Control) / 2) + Boons - Banes."
                },
                {
                    "type": "heading",
                    "order": 7,
                    "data": "Combat Action Points Base Cost",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "list",
                    "order": 8,
                    "data": [
                        "Unarmed - 3 Action Points per attack.",
                        "Armed - Varies per weapon."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Combat Action Points Non-Combat Actions Use",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 10,
                    "data": {
                        "headers": ["Difficulty Level (DL)", "Action Point Cost", "Example"],
                        "rows": [
                            ["Easy (DL: 15-20)", "1 Action Point", "Jumping over a minor obstacle or popping a loaded magazine into a gun."],
                            ["Moderate (DL: 21-30)", "2 Action Points", "Opening an unlocked door or loading a revolver without a speed loader."],
                            ["Difficult (DL: 31-40)", "3 Action Points", "Picking a pocket or unlocking a door with a key."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 11,
                    "data": "Movement Action Points (MAP)",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "Movement Action Points (MAP) are equal to the sum of ((Strength + Endurance + Reflexes + Intellect + Manipulation) / 2) + Boons - Banes."
                },
                {
                    "type": "heading",
                    "order": 13,
                    "data": "Traits, Hit Points",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 14,
                    "data": "Battle Hit Points (BHP) is calculated by the formula (SHP + ML) * (Endurance + CHP). *See Combat Section for Use."
                },
                {
                    "type": "heading",
                    "order": 15,
                    "data": "BHP Condition (Optional Rule)",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "To determine if an ally or enemy is damaged, the player may ask. This tentative scale helps avoid metagaming while providing an idea of an ally or enemy's condition:"
                },
                {
                    "type": "list",
                    "order": 17,
                    "data": [
                        "Roughed Up - Down less than 20% of BHP",
                        "Battered & Bruised - Down 20%+ of BHP",
                        "Bloodied - Down 60%+ of BHP"
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "heading",
                    "order": 18,
                    "data": "Calling Hit Points (CHP)",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 19,
                    "data": "CHP is determined at character creation based on the (Calling Bonus + Boons - Banes) selected by the player. *See Combat Section for Use."
                },
                {
                    "type": "heading",
                    "order": 20,
                    "data": "Species Hit Points (SHP)",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "paragraph",
                    "order": 21,
                    "data": "SHP is determined at character creation based on the (Species SHP Rating + Boons - Banes) selected by the player. *See Combat Section for Use."
                },
                {
                    "type": "heading",
                    "order": 22,
                    "data": "Structural Battle Hit Points",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 23,
                    "data": "Used to determine the toughness of an object or structure, calculated based on thickness and classification. Formula: (Classification) x (1\" or 2.5 cm of Thickness). Objects gain +3 Soak or Damage per classification difference."
                },
                {
                    "type": "table",
                    "order": 24,
                    "data": {
                        "headers": ["Class", "SBHP", "Material Example"],
                        "rows": [
                            ["SSS Class", "300 SBHP", "Cursed Infernal Alloy or Adamantine"],
                            ["SS Class", "250 SBHP", "Graphene or Mithril"],
                            ["S Class", "200 SBHP", "Titanium or Dragon Quenched Steel"],
                            ["A Class", "150 SBHP", "Metallic Glass or Syntha Ceramics"],
                            ["B Class", "100 SBHP", "Vanadium 'Krimmerian' Steel or Carbon Fiber"],
                            ["C Class", "75 SBHP", "Steel, Reinforced Concrete or Dense Stone"],
                            ["D Class", "50 SBHP", "Dense Plastic or Hard Wood"],
                            ["F Class", "25 SBHP", "Plastic or Soft Wood"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 25,
                    "data": "Traits, Non-Expendable",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 26,
                    "data": "Traits that cannot be expended represent the core development and mastery of a character and are broken into Tiers. No Tier can exceed 10. The following mechanics possess Tiers: Abilities, Backgrounds, Mastery, Powers, Scholar, Skills, Spheres, and Techniques."
                }
            ]
        },
        {
            "title": "Scenario Guidelines",
            "slug": "scenario-guidelines",
            "chapter": "Scenario Guidelines",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Quick Reference Scenario Examples",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "heading",
                    "order": 2,
                    "data": "Action Urban",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 3,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Breaking Down Door", "Uncontested Power vs. Door Rating. Attempt every minute."],
                            ["Breaking Through a Wall", "Uncontested Power vs. Door Rating. Attempt every minute."],
                            ["Escaping When Tied Up", "Contested Sleight of Hand vs. Security of Trusser. Attempt every six hours."],
                            ["Jumping from Elevation into Water", "Uncontested Athletics vs. Distance (DL 5 per 5’ / 1.5 m)."],
                            ["Jumping from a Height", "Uncontested Athletics vs. Distance (DL 10 per 5’ / 1.5 m)."],
                            ["Jumping onto a Moving Object", "Uncontested Athletics vs. Speed (DL 1 per 1 MPH or 1.5 KPH)."],
                            ["Jumping from Rooftop to Rooftop", "Uncontested Athletics vs. Distance (DL 10 per 5’ / 1.5 m Leapt)."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Failure < 5: They catch the edge. Make a Difficult (DL: 40-49) Power Roll to pull themselves up. 3 Failures & they Fall."
                },
                {
                    "type": "heading",
                    "order": 5,
                    "data": "Analysis",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 6,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Determining the Type of Trap", "Uncontested Analysis vs. DL of Trap."],
                            ["Determining Technological Function", "Uncontested Analysis + Scholar vs. Complexity Rating."],
                            ["Determining Arcane Function", "Contested or Uncontested Analysis + Arcane Scholar."],
                            ["Determining Medical Condition", "Contested or Uncontested Analysis + Medicine."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 7,
                    "data": "Bio Control",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 8,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Weathering a Sandstorm", "Uncontested Bio Control vs. Terrain DL."],
                            ["Escaping Quicksand", "Uncontested Bio Control vs. Terrain DL."],
                            ["Holding Your Breath", "Uncontested Bio Control: Duration."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Environmental",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 10,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Falling Damage", "2d10 + 2 BHP per 5’ Fallen vs. Soak."],
                            ["Falling Damage Soft Landing", "1 BHP per 5’ Fallen vs. Soak."],
                            ["Heat Exhaustion or Hypothermia", "2d10 + Cumulative 5 BHP per 10 Minutes vs. Soak."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 11,
                    "data": "Fear",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 12,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Close Proximity to Mild Phobia", "Willpower or Bio Control (DL 10)"],
                            ["Directly Exposed to Mild Phobia", "Willpower or Bio Control (DL: 15)"],
                            ["Close Proximity to Severe Phobia", "Willpower or Bio Control (DL: 20)"],
                            ["Directly Exposed to Severe Phobia", "Willpower or Bio Control (DL: 25)"],
                            ["Lesser Nightmare Creature", "Willpower or Bio Control (DL: 30)"],
                            ["Adult Dragon", "Willpower or Bio Control (DL: 35)"],
                            ["Greater Nightmare Creature", "Willpower or Bio Control (DL: 40)"],
                            ["Great Ancient Dragon", "Willpower or Bio Control (DL: 45)"],
                            ["Master Nightmare Creatures", "Willpower or Bio Control (DL: 50)"],
                            ["An Old One, First Fallen or the Void", "Willpower or Bio Control (DL: 60)"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 13,
                    "data": "Mechanical",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 14,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Basic Carpentry", "Uncontested Mechanical Repair vs. DL 10."],
                            ["Basic Electrical", "Uncontested Mechanical Repair vs. DL 15."],
                            ["Basic Plumbing", "Uncontested Mechanical Repair vs. DL 10."],
                            ["Basic Welding", "Uncontested Mechanical Repair vs. DL 15."],
                            ["Changing a Tire", "Uncontested Mechanical Repair vs. DL 10."],
                            ["Rebuilding an Engine", "Uncontested Mechanical Repair vs. DL 20."],
                            ["Repairing an Engine", "Uncontested Mechanical Repair vs. Extent of Damage DL."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 15,
                    "data": "Medical Emergencies",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 16,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Broken Bones", "Uncontested Medicine vs. DL 30."],
                            ["Burns", "Uncontested Medicine vs. DL 10 + Severity."],
                            ["Heart Attack", "Uncontested Medicine vs. DL 30."],
                            ["Heat Exhaustion or Hypothermia", "Uncontested Medicine vs. DL 15."],
                            ["Lodged Object Removal", "Uncontested Medicine vs. DL 20."],
                            ["Resuscitating a Drowning Victim", "Uncontested Medicine vs. DL # of Rounds Drowning x 5."],
                            ["Stabilizing", "Uncontested Medicine vs. DL 20."],
                            ["Stitches, External", "Uncontested Medicine vs. DL 10."],
                            ["Stitches, Internal", "Uncontested Medicine vs. DL 30."],
                            ["Tracheotomy", "Uncontested Medicine vs. DL 20."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 17,
                    "data": "Navigation",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 18,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Navigation With a Map and Compass", "Uncontested Navigation vs. 1/2 Terrain DL."],
                            ["Navigation Without a Map or Compass", "Uncontested Navigation vs. Terrain DL."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 19,
                    "data": "Security",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 20,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Simple Padlock", "Uncontested Security vs. DL of 20-29."],
                            ["Moderate Lock", "Uncontested Security vs. DL 30-39."],
                            ["Complex Lock", "Uncontested Security vs. DL of 40-49."],
                            ["Masterwork Lock", "Uncontested Security vs. DL of 50-59."],
                            ["Disabling a Simple Trap", "Uncontested Security vs. DL of 20-29."],
                            ["Disabling a Moderate Trap", "Uncontested Security vs. DL of 30-39."],
                            ["Disabling a Complex Trap", "Uncontested Security vs. DL of 40-49."],
                            ["Disabling a Masterwork Trap", "Uncontested Security vs. DL of 50-59."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 21,
                    "data": "Social Anywhere",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 22,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Haggling for a Better Deal", "Contested Scrounge vs. Scrounge. (Winning lowers price 20-25%, losing raises price 20-25%.)"],
                            ["Lying", "2D10 + Performance Sum - Credibility of Lie. (Failure creates a telling behavior, PCs or NPCs may roll Analyze.)"],
                            ["Passing a Bribe", "Contested Persuasion or Intimidation vs. Willpower. (Exceptionally high/low bribes may modify the roll.)"],
                            ["Picking Pockets", "Contested Sleight of Hand vs. Awareness."],
                            ["Running a Scam", "Contested Performance vs. Analyze."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 23,
                    "data": "Survival",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 24,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Avoiding Dehydration & Starvation", "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."],
                            ["Avoiding Hypothermia", "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."],
                            ["Avoiding Heat Exhaustion", "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."],
                            ["Building a Shelter Without Supplies", "Uncontested Primal Instinct or Artisan vs. Terrain DL."],
                            ["Finding Water", "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."],
                            ["Fishing Without a Rod", "Uncontested Primal Instinct vs. Terrain DL."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 25,
                    "data": "Technical",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 26,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Building a Computer", "Uncontested Tech Repair vs. DL 20."],
                            ["Diffusing a Bomb", "Contested Roll: Demolition vs. Demolition or Security."],
                            ["Hacking a Network", "Contested Roll: Technical Op vs. Technical Op or Uncontested Roll: Technical Op vs. Security DL."],
                            ["Hotwiring a Car", "Uncontested Technical Repair vs. DL 20 or Car Security DL."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 27,
                    "data": "Transportation",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 28,
                    "data": {
                        "headers": ["Scenario", "Check Type"],
                        "rows": [
                            ["Bad Weather", "Add 10 to 30 DL = Storm Severity."],
                            ["Piloting", "Aviation, Mecha Operation, or Space Flight."],
                            ["Riding", "Living Creatures or 1-3 Wheeled/Propulsion Vehicles."],
                            ["Seafaring", "Vessels that Operate On or Under Liquid."],
                            ["Vehicles", "Ground-Based Tread or 4+ Wheeled Vehicles."],
                            ["Transportation Docking", "Uncontested Skill vs. DL 10."],
                            ["Transportation Takeoff/Touchdown", "Uncontested Skill vs. DL 15."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 29,
                    "data": "Transportation Crash Landing",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 30,
                    "data": {
                        "headers": ["Type", "DL & Damage Impact"],
                        "rows": [
                            ["Piloting", "DL 40 to 60 | 2 BHP per DL in Damage Post Impact."],
                            ["Riding", "DL 20 to 40 | 2 BHP per DL in Damage Post Impact."],
                            ["Seafaring", "DL 30 to 70 | 1 BHP per DL in Damage Post Impact."],
                            ["Vehicles", "DL 10 to 60 | 2 BHP per DL in Damage Post Impact."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 31,
                    "data": "Transportation Jumping to Ground",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 32,
                    "data": {
                        "headers": ["Type", "DL & Damage Impact"],
                        "rows": [
                            ["Piloting (Parachute)", "DL 25 | Failure Changes Roll to No Parachute."],
                            ["Piloting (No Parachute)", "DL 60 | 3 BHP per DL in Damage Post Impact."],
                            ["Riding", "DL 30 to 50 | 2 BHP per DL in Damage Post Impact."],
                            ["Seafaring (Ground)", "DL 30 to 40 | 2 BHP per DL in Damage Post Impact."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                },
                {
                    "type": "heading",
                    "order": 33,
                    "data": "Transportation Thrown From",
                    "style_class": "text-lg font-semibold"
                },
                {
                    "type": "table",
                    "order": 34,
                    "data": {
                        "headers": ["Type", "DL & Damage Impact"],
                        "rows": [
                            ["Slow Speed & Short Fall", "DL 20 to 30 | 2 BHP per DL in Damage Post Impact."],
                            ["Moderate Speed & Short Fall", "DL 30 to 40 | 2 BHP per DL in Damage Post Impact."],
                            ["Fast Speed & Short Fall", "DL 40+ | 2 BHP per DL in Damage Post Impact."],
                            ["Moderate Speed & Moderate Fall", "DL 30 to 40 | 2 BHP per DL in Damage Post Impact."],
                            ["Moderate Speed & Long Fall", "DL 40+ | 2 BHP per DL in Damage Post Impact."],
                            ["Fast Speed & Moderate Fall", "DL 40+ | 2 BHP per DL in Damage Post Impact."],
                            ["Fast Speed & Long Fall", "DL 60+ | 2 BHP per DL in Damage Post Impact."],
                            ["Seafaring (Into Liquid)", "DL 20 to 30 | 1 BHP per DL in Damage Post Impact."],
                            ["Seafaring (Onto Land)", "DL 20 to 30 | 1 BHP per DL in Damage Post Impact."]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-300 w-full text-left"
                }
            ]
        },
        {
            "title": "Skills",
            "slug": "skills",
            "chapter": "Skills",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Skills are Ability focuses that characters develop through rigorous practice allowing them greater chances of success than the untrained. Skill Rolls are performed by rolling 2d10 and adding the Associated Ability + Skill + Additional Modifiers. All Skills have an oppositional skill listed which is used in Contested Rolls or are rolled against a set Difficulty: See Section 3 Game Mechanics for details."
                },
                {
                    "type": "table",
                    "order": 2,
                    "data": {
                        "headers": ["Skill", "Associated Ability", "Typical Oppositional Skill"],
                        "rows": [
                            ["Acrobatics", "Reflexes", "Acrobatics or Difficulty"],
                            ["Analyzation", "Perception", "Difficulty"],
                            ["Archery", "Perception", "Dodge"],
                            ["Artillery", "Perception", "Difficulty"],
                            ["Artisan", "Intellect", "Difficulty"],
                            ["Athletics", "Endurance", "Athletics or Difficulty"],
                            ["Awareness", "Perception", "Difficulty"],
                            ["Bio Control", "Chakra", "Difficulty"],
                            ["Cultures", "Perception", "Difficulty"],
                            ["Demolitions", "Intellect", "Demolitions, Dodge or Difficulty"],
                            ["Dodge", "Reflexes", "Firearms or Archery"],
                            ["Exoceric", "Control", "Dodge"],
                            ["Firearms", "Control", "Dodge"],
                            ["Gambling", "Control", "Gambling, Sleight of Hand or Difficulty"],
                            ["Intimidation", "Manipulation", "Willpower"],
                            ["Linguistics", "Intellect", "Difficulty"],
                            ["Martial Arts", "Reflexes", "Parry"],
                            ["Mechanical", "Intellect", "Difficulty"],
                            ["Medicine", "Intellect", "Difficulty"],
                            ["Melee (Exoceric)", "Reflexes", "Parry"],
                            ["Melee (Traditional)", "Reflexes", "Parry"],
                            ["Navigation", "Intellect", "Difficulty"],
                            ["Occult", "Intellect", "Varies or Difficulty"],
                            ["Parry", "Reflexes", "Melee"],
                            ["Performance", "Manipulation", "Analyzing"],
                            ["Persuasion", "Manipulation", "Willpower"],
                            ["Piloting", "Control", "Piloting or Difficulty"],
                            ["Power", "Strength", "Power or Difficulty"],
                            ["Primal Instinct", "Perception", "Primal Instinct or Difficulty"],
                            ["Riding", "Reflexes", "Riding or Difficulty"],
                            ["Scholar", "Intellect", "Difficulty of Lore"],
                            ["Scrounge", "Perception", "Scrounge or Difficulty"],
                            ["Seafaring", "Control", "Sailing or Difficulty"],
                            ["Security", "Perception", "Security or Difficulty"],
                            ["Sleight of Hand", "Reflexes", "Awareness"],
                            ["Stealth", "Control", "Awareness"],
                            ["Technical", "Intellect", "Tech Op or Difficulty"],
                            ["Vehicles", "Control", "Vehicle Op or Difficulty"],
                            ["Willpower", "Control", "Difficulty"]
                        ]
                    },
                    "style_class": "table-auto border-collapse border border-gray-600 w-full text-left"
                },
                {
                    "type": "subheading",
                    "order": 3,
                    "data": "Acrobatics",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "“Balance internal, leads to balance external, such is the way of being a true warrior, the sex is also better.” ~ Z. G., Darkholme & Lost Galaxies",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "You possess a grace and agility that is only matched by your keen sense of balance. You are able to perform aerial maneuvers, cartwheels, back-flips and walk a tight-rope."
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Critical Botch: [2D10 + Difficulty Level in BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 7,
                    "data": "Analyzation",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "“It seemed to me that a careful examination of the room and the lawn might possibly reveal some traces of this mysterious individual. You know my methods, Watson. There was not one of them which I did not apply to the inquiry. And it ended by my discovering traces, but very different ones from those which I had expected.” ~ Sherlock Holmes, The Crooked Man",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "You have developed an approach and methods that allow your intuition and attention to discern useful information to form an overviewing scenario. There are two types of analysis: Cursory and In-depth. Cursory may be performed visually without coming into contact or manipulating the object to determine more intricate details. This type of analysis only provides the most rudimentary information and never advanced functions or detrimental side effects. In-depth requires extensive handling and examination involving contact and manipulation of the object to determine its capabilities and any potential risks."
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "Critical Botch: [Red Herring: Your observations have taken a wrong turn. No further Analyzing Rolls may be made until the false trail is resolved and you cannot be convinced this is a false trail.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 11,
                    "data": "Archery",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "“Death is like an arrow that is already in flight, and your life lasts only until it reaches you.” ~ Georg Hermes",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 13,
                    "data": "You possess the capability to utilize ranged piercing-based weapons such as the long bow, mechanical crossbow, dagger, harpoon, javelin or even the spear."
                },
                {
                    "type": "paragraph",
                    "order": 14,
                    "data": "Critical Botch: The bow string snaps (Watch your eyes!) anyone around you is in danger. [Roll a new Attack roll on a friendly target selected by storyteller]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 15,
                    "data": "Artillery",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "“This is the QRZ-750 automated gun tower. It is capable of locking on to a human-sized target in pitch darkness at a distance of up to 2.2 kilometers... I highly suggest that you familiarize yourself with its operation.” ~ Tiari Dreadnock Le’Shay, Lost Galaxies",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 17,
                    "data": "The character is proficient in the use of mounted weapons systems. In modern or future settings, this includes mounted vehicle weapons or stationary weapon systems, while in more archaic settings, this refers to ballistae, catapults, etc."
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "Critical Botch: [Weapon Malfunction: Difficult (DL: 40-49) Mechanical Repair Roll to bring the weapon back online.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 19,
                    "data": "Artisan",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "“I can tell you with no ego, this is my finest sword. If on your journey, you should encounter God…God will be cut.” ~ Hattori Hanzo, Kill Bill Vol. 1",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 21,
                    "data": "You possess the ability to work with a variety of materials to produce both functional and aesthetically pleasing items. Examples include blacksmith, cook, weaponsmith, mason, cobbler, seamstress, milliner, woodworker, etc."
                },
                {
                    "type": "paragraph",
                    "order": 22,
                    "data": "Critical Botch: [Project Fails. Materials are wasted and may not be used again.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 23,
                    "data": "Athletics",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 24,
                    "data": "“How long can you go without sleep or sustenance? How long can you run or persevere during a life-or-death moment? The stamina of athletic training determines that and the ability to climb, jump, run and swim.”",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 25,
                    "data": "Climbing, jumping, running and swimming."
                },
                {
                    "type": "paragraph",
                    "order": 26,
                    "data": "Critical Botch: [2D10 + Difficulty Level in BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 27,
                    "data": "Awareness",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 28,
                    "data": "“I come in here and the first thing I’m doing is I’m catching the sight lines and looking for an exit. I can tell you the license plate numbers of all six cars outside. I can tell you that our waitress is left-handed, and the guy sitting at the counter weighs 215 pounds and knows how to handle himself...” ~ Jason Bourne, The Bourne Identity",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 29,
                    "data": "Your power of subconscious observation allows you to notice and catalogue the environment, people and how they are interacting while simultaneously mapping out your surroundings."
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "Critical Botch: [You may make no more Awareness Rolls for the scene.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 31,
                    "data": "Bio Control",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 32,
                    "data": "“Once you have learned how to breathe it becomes apparent that you cannot always control what goes on outside, but you can always exhibit mastery over what transpires within.” ~ Master Grey, Darkholme",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 33,
                    "data": "A master is in control of not only their emotions but their body. The harmony of being one with ourselves, where we cease to be at war with ourselves and seek harmony in the world around us. Holding your breath, ignoring pain or feigning death are all aspects of Bio Control."
                },
                {
                    "type": "paragraph",
                    "order": 34,
                    "data": "Critical Botch: [1D10 + Difficulty Level in BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 35,
                    "data": "Cultures",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 36,
                    "data": "“Many of our customs seem strange to you; and the same is true of yours. For example, not to introduce yourself is considered extremely rude, even among enemies.” ~ General Katsumoto, The Last Samurai",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 37,
                    "data": "The intricacies of other cultures are readily apparent. Through study and observation, you know what is considered acceptable instead of taboo. This allows you to behave in a civil manner in the culture that currently surrounds you."
                },
                {
                    "type": "paragraph",
                    "order": 38,
                    "data": "Critical Botch: [You accidentally made a dire insult and created a more hostile environment.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 39,
                    "data": "Demolitions",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 40,
                    "data": "Charlie: “You, okay?” Left Ear: “Just give me a moment.” “I’m about to insert this pin into this detonator tube, and if the brass touches the sides, we’ll both be the last people we ever see.” ~ Charlie & Left Ear, The Italian Job (2000)",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 41,
                    "data": "You possess the knowledge to set or disarm explosive charges without getting hurt or inflicting undesirable collateral damage. This ability does not allow an individual to create explosive compounds."
                },
                {
                    "type": "paragraph",
                    "order": 42,
                    "data": "Critical Botch: The bomb goes off: [ST shift scene and damage as appropriate]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 43,
                    "data": "Dodge",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 44,
                    "data": "“1000 nations of the Persian empire descend upon you. Our arrows will blot out the sun!” “Then we will fight in the shade.” ~ Persian & Stelios, 300",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 45,
                    "data": "You have the agility and skill to position yourself where there is minimal chance of being struck by projectiles or shrapnel."
                },
                {
                    "type": "paragraph",
                    "order": 46,
                    "data": "Critical Botch: [-10 to Soak.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 47,
                    "data": "Exoergic",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 48,
                    "data": "“Ancient weapons and hokey religions are no match for a good blaster at your side, kid.” ~ Han Solo, Star Wars: A New Hope",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 49,
                    "data": "You are capable of loading, aiming, firing, and cleaning Energy Firearms. This includes any weapon that requires a battery as an ammo source, produces a blast of energy toward a target, and is handheld in nature."
                },
                {
                    "type": "paragraph",
                    "order": 50,
                    "data": "Critical Botch: [Weapon Jams: Spend 10 AP to un-jam the firearm.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 51,
                    "data": "Intimidation",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 52,
                    "data": "“Boys, you don’t want to shoot me. You know me. You know what I’ll do to you if you do.” ~ Broc Sampson, Venture Bros.: The Incredible Mr. Brisby",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 53,
                    "data": "You know how to use body language, tone of voice, gestures and a few carefully chosen words to instill fear. This could be used scare someone badly enough where they back off or do something against their better judgment."
                },
                {
                    "type": "paragraph",
                    "order": 54,
                    "data": "Critical Botch: [Hostile Response: Your target attacks you.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 55,
                    "data": "Linguistics",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 56,
                    "data": "“If language is not correct, then what is said is not what is meant; if what is said is not what is meant, then what must be done remains undone... Hence there must be no arbitrariness in what is said. This matters above everything.” ~ Confucius",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 57,
                    "data": "You possess the ability to read and write in addition to your native tongue. You receive 1 Fluent Language per Level of Linguists (No Roll). If you possess traits in Linguistics, then you may attempt to communicate with someone whom you do not share a common language. The difficulty of the translation depends on the complexity of the idea being expressed. Communicating that you are hungry and would like food is easy while conveying technical specifications of a multi-tiered analytical computer system would be legendary."
                },
                {
                    "type": "paragraph",
                    "order": 58,
                    "data": "Critical Botch: [Lost In Translation: You have offended those with whom you are communicating.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 59,
                    "data": "Martial Arts",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 60,
                    "data": "“Martial arts… ultimately, no matter what type it is, the objective is how to efficiently destroy your opponents. After that, it just depends on the heart of the fighter.” ~ Hayato Furinj, Kenichi",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 61,
                    "data": "You have spent years in the pursuit of perfection of yourself by establishing muscle memory, internal conditioning and creation of a combat mindset through rigorous training and repetitive combat simulation. This skill allows for both offensive and defensive hand-to-hand combat tactics."
                },
                {
                    "type": "paragraph",
                    "order": 62,
                    "data": "Critical Botch: [Suffer 2D10 in BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 63,
                    "data": "Mechanical",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 64,
                    "data": "“In America, the professor talks to the mechanic. They are in the same category.” ~ Noam Chomsky",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 65,
                    "data": "You possess the ability, knowledge, and skills necessary to assemble or repair mechanical machines and devices. Everything from a simple gear function to precision hydraulic piston movement can be worked on with this skill if the proper tools and equipment are available."
                },
                {
                    "type": "paragraph",
                    "order": 66,
                    "data": "Critical Botch: [Quick Fix: System functions for now but will break at a critical point determined by the Game Master.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 67,
                    "data": "Medicine",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 68,
                    "data": "“GSW. That is what the hospitals call it. Gun Shot Wounds. Doctors are required to report it to the police. That makes it hard for guys in my line of work to get, what I call, quality healthcare.” ~ Porter, Payback",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 69,
                    "data": "You know anatomy and the basic procedures required to save someone’s life or provide advanced surgical procedure once you possess Medicine 5."
                },
                {
                    "type": "paragraph",
                    "order": 70,
                    "data": "Critical Botch: [He’s Dead Jim: Inflict 2d10 in BHP. If this exceeds their Athletics Sum then they die under the knife.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 71,
                    "data": "Melee (Exoergic)",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 72,
                    "data": "“Not as random or clumsy as a blaster. An elegant weapon… for a more civilized age.” ~ Obi-Wan Kenobi, Star Wars: A New Hope",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 73,
                    "data": "The Energy Blades are very efficient. They never need sharpening, and they can cut through almost anything. Special training is required to wield these magnificent weapons correctly without harming oneself. With this skill you are capable of offensive maneuvers with Melee (Energy) weapons."
                },
                {
                    "type": "paragraph",
                    "order": 74,
                    "data": "Critical Botch: [Suffer: 2D10+5 in Unsoakable BHP Damage or you apply your Attack Roll against all allies within range.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 75,
                    "data": "Melee (Traditional)",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 76,
                    "data": "“You win battles by knowing the enemy’s timing and using a timing which the enemy does not expect.” ~ Miyamoto Musashi",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 77,
                    "data": "Basically, you are using the leverage and momentum of your body, enhanced by a crushing instrument to split someone’s skull in. This skill allows offensive maneuvers with Melee (Blunt) weapons."
                },
                {
                    "type": "paragraph",
                    "order": 78,
                    "data": "Critical Botch: WTF? You either suffer [2D10 in Unsoakable BHP Damage.] or you apply your Attack Roll against all allies within range.",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 79,
                    "data": "Navigation",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 80,
                    "data": "“For sure, you have to be lost to find a place that can’t be found, else ways everyone would know where it was.” ~ Captain Hector Barbossa, At World’s End",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 81,
                    "data": "You have either the training or an inherent sense of direction that seldom steers you wrong. You can follow directions, landmarks, maps or celestial navigation to get where you are going. You can find any direction and, depending on your training or specialization, around the entire universe."
                },
                {
                    "type": "paragraph",
                    "order": 82,
                    "data": "Critical Botch: [Slight Error: The Game Master can place your ship anywhere they see fit to mold their storyline or create a side branch adventure of miserable fun.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 83,
                    "data": "Occult",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 84,
                    "data": "“Prophecy is most dangerous when you try to make it happen... The Pattern weaves itself around you, but when you try to weave it, even you cannot hold it.” ~ Moiraine Damodred, The Shadow Rising",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 85,
                    "data": "This world contains many unexplained things. It is an old world and has many bad memories. But for those who know exactly what is out there, there are as many mysteries to be unlocked as there are memories. This knowledge can be priceless to the right person as it can be used to break the 'rules' as we know them."
                },
                {
                    "type": "paragraph",
                    "order": 86,
                    "data": "Critical Botch: [Price of Power: The Natural Order has caught up to you and it is time for you to pay the toll. The extent of the price is up to the Game Master.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 87,
                    "data": "Parry",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 88,
                    "data": "Dread Pirate Roberts: “There is something I ought to tell you.” Inigo Montoya: “Tell me.” Dread Pirate Roberts: “I’m not left-handed either.” ~ Wesley & Inigo, The Princess Bride",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 89,
                    "data": "Some know how to swing a club or poke with a dagger. You have learned the far more necessary skill of subconsciously predicting and deflecting such weapons. Whereas some may freeze or cringe at a crucial moment, you are constantly shifting your footing and the angle of your body to deflect not just this attack but the many obvious ones to follow."
                },
                {
                    "type": "paragraph",
                    "order": 90,
                    "data": "Critical Botch: [Misstep: Take 10 Additional Damage after soak.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 91,
                    "data": "Performance",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 92,
                    "data": "“The dance is a poem of which each movement is a word.” ~ Mata Hari",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 93,
                    "data": "Acting, singing, recitals, dancing, playing an instrument or even holding a stimulating conversation. These are all parts of performance. Whether through a natural talent or years of rigorous study, you have learned the subtle art of looking good at everything you do."
                },
                {
                    "type": "paragraph",
                    "order": 94,
                    "data": "Critical Botch: [Unforgettable Performance: Unfortunately, it’s attached to laughter and scorn.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 95,
                    "data": "Persuasion",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 96,
                    "data": "“Don’t raise your voice, improve your argument.” ~ Desmond Tutu",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 97,
                    "data": "Debating and arguing is all well and good… but unless you can sway someone to your point of view… it is not very helpful. Persuasion is part empathy and part logic… struggling to make a connection with someone and making them see your viewpoint… convincing them that your way is the best or making them see that their actions are the wrong ones."
                },
                {
                    "type": "paragraph",
                    "order": 98,
                    "data": "Critical Botch: Just walk away before she calls the cops.",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 99,
                    "data": "Piloting",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 100,
                    "data": "“Within all of us is a varying amount of space lint and star dust, the residue from our creation... It is strongest in those of us who fly and is responsible for an unconscious, subtle desire to slip into some wings and try for the elusive boundaries of our origin.” ~ K.O. Eckland",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 101,
                    "data": "Within the atmosphere of a planet or the depths of space there are numerous factors to account for. These variances are vast but can be accounted for by a good pilot’s experience. This skill is required for all gravitation-resistant operations that are 5 ft. above the ground or higher including planes, power armor suits or massive robotic frames."
                },
                {
                    "type": "paragraph",
                    "order": 102,
                    "data": "Critical Botch: [System Malfunction: Ship structure suffers 2D10 in Unsoakable Hull Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 103,
                    "data": "Power",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 104,
                    "data": "“Everybody pities the weak; jealousy you have to earn.” ~ Arnold Schwarzenegger",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 105,
                    "data": "This Skill is derived from training to lift more than is normal for a person of similar size and build. Proper stance, grip placement and posture is what allows a person to break, lift, hold something in place or throw it."
                },
                {
                    "type": "paragraph",
                    "order": 106,
                    "data": "Critical Botch: [Poor Posture: Suffer 2D10 in Unsoakable BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 107,
                    "data": "Primal Instinct",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 108,
                    "data": "“I’m the best there is at what I do and what I do isn’t very nice...” ~ Len Wein’s, Wolverine",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 109,
                    "data": "Natural animal empathy and the ability to sense when something is wrong or abnormal. Basically, you are closer to your animal nature than others, trusting your finely tuned instincts more than your logical thought processes. This can be used for Animal Handling in lieu of Scholar; Wilderness Survival or as an alternative to Awareness."
                },
                {
                    "type": "paragraph",
                    "order": 110,
                    "data": "Critical Botch: [Oblivious: No Awareness or Primal Instinct Rolls for the remainder of the day.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 111,
                    "data": "Riding",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 112,
                    "data": "“They say princes learn no art truly but the art of horsemanship. The reason is the brave beast is no flatterer. He will throw a prince as soon as his groom.” ~ Ben Jonson",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 113,
                    "data": "You are proficient in use of any animals or vehicles that require balance to ride. All anti-gravity operations in this skill are only applicable less than 5 feet."
                },
                {
                    "type": "paragraph",
                    "order": 114,
                    "data": "Critical Botch: [Forcefully Dismounted: 2D10 in Unsoakable BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 115,
                    "data": "Scrounge",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 116,
                    "data": "“It figures. First time on the core, and what do I get to do? Dig through trash. Couldn’t he send me shopping at the Triplex or... Oh! Synchronizers!” ~ Kay Lee, Firefly (Ariel)",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 117,
                    "data": "You never know what you might find if you know what to look for. This combined with a working knowledge of the value of 'junk' allows you to haggle for some exceptional deals."
                },
                {
                    "type": "paragraph",
                    "order": 118,
                    "data": "Critical Botch: [Last One in Stock: Found it but the price is double and no more are available.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 119,
                    "data": "Seafaring",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 120,
                    "data": "“Confronting a storm is like fighting God. All the powers in the universe seem to be against you and, in an extraordinary way, your irrelevance is at the same time both humbling and exalting.” ~ Francis LeGrande",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 121,
                    "data": "You are proficient in the operation and operations of sea-based vehicles that do not require balance to operate."
                },
                {
                    "type": "paragraph",
                    "order": 122,
                    "data": "Critical Botch: [Collision: Debris impact causes 2D10 in Unsoakable BHP Damage to the Ship.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 123,
                    "data": "Security",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 124,
                    "data": "“Security is an attempt to try to make the universe static so that we feel safe.” ~ Anne Wilson Schaef",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 125,
                    "data": "Your working knowledge of security systems can be used to secure or break into another secured area."
                },
                {
                    "type": "paragraph",
                    "order": 126,
                    "data": "Critical Botch: [Bad Installation: Security System looks great but an Easy Roll to bypass it.] [Tight Security: Whatever Security was present has been activated.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 127,
                    "data": "Sleight of Hand",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 128,
                    "data": "“Every great magic trick consists of three parts or acts. The Pledge, The Turn, and The Prestige.” ~ Cutter, The Prestige",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 129,
                    "data": "Just like a stage magician or a pickpocket, you have a canny ability to manipulate objects in your hands. You can make a small object disappear, reappear without anyone being able to see where it has gone."
                },
                {
                    "type": "paragraph",
                    "order": 130,
                    "data": "Critical Botch: [Busted: You are caught outright and must deal with the consequences.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 131,
                    "data": "Stealth",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 132,
                    "data": "“The Assassin moved quietly from roof to roof until he was well away from the excitement around the Watch House. His movements could be called cat-like, except that he did not stop to spray urine up against things.” ~ Terry Pratchett’s, Night Watch",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 133,
                    "data": "The art of silent movement has been a coveted skill used by soldiers, burglars, assassins, and teenagers sneaking back into their house after curfew beyond memory. You have a working knowledge of camouflage, camera timing, and subtle movement to pass without being noticed though movement is cut in half."
                },
                {
                    "type": "paragraph",
                    "order": 134,
                    "data": "Critical Botch: [What’s That: You have been seen and/or heard.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 135,
                    "data": "Technical",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 136,
                    "data": "“Cyberspace. A consensual hallucination experienced daily by billions of legitimate operators, in every nation, by children being taught mathematical concepts... A graphic representation of data abstracted from banks of every computer in the human system. Unthinkable complexity. Lines of light ranged in the non-space of the mind, clusters and constellations of data. Like city lights, receding... “ ~ William Gibson’s, Neuromancer",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 137,
                    "data": "You have the proper training and knowledge for the operation of technical devices. Computers, PDAs, and Commlinks are all examples of technical devices. You can operate them to specifications and sometimes beyond."
                },
                {
                    "type": "paragraph",
                    "order": 138,
                    "data": "Critical Botch: [Arc & Spark: 2D10 + Difficulty Level in BHP Damage.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 139,
                    "data": "Vehicles",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 140,
                    "data": "“The deal was transportation for 3 men with a combined weight of 254 kilos. An extra 80 kilos means we’ll not make your destination on the gas I have allotted. Every stop we make exposes us. Every exposure increases the risk of getting caught... I don’t want to get caught. You don’t want to get caught.” ~ Frank Martin, The Transporter",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 141,
                    "data": "You are proficient in the operation and operations of land-based vehicles that do not require balance to operate."
                },
                {
                    "type": "paragraph",
                    "order": 142,
                    "data": "Critical Botch: [Crash: 2D10 in Unsoakable BHP Damage to the Vehicle.]",
                    "style_class": "text-red-500 font-bold"
                },
                {
                    "type": "subheading",
                    "order": 143,
                    "data": "Willpower",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 144,
                    "data": "“Whoever fights monsters should see to it that in the process he does not become a monster. And if you gaze long enough into an abyss the abyss will gaze back into you.” ~ Friedrich Nietzsche",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "paragraph",
                    "order": 145,
                    "data": "Psychological Attacks, Arcane Spells, Fear. There are many ways in which the spirit or mind of someone can be broken and drowned. But it is the Will to act and to overcome these things that is the token of the Willpower ability. You can resist and overcome almost anything that would hinder your actions."
                },
                {
                    "type": "paragraph",
                    "order": 146,
                    "data": "Critical Botch: [Broken Will: You gain an uncommon derangement that requires three successful Willpower Rolls when exposed to the Trigger to overcome.]",
                    "style_class": "text-red-500 font-bold"
                }
            ]
        },
        {
            "title": "Backgrounds",
            "slug": "backgrounds",
            "chapter": "Backgrounds",
            "content": [
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Backgrounds are awarded at character creation and earned or lost through game play. Assets are only awarded at character creation and allow a player to enter the game with slightly better gear, a vehicle, or a home in exchange for debt."
                },
                {
                    "type": "subheading",
                    "order": 3,
                    "data": "Assets",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Often players will want access to facilities and gear that is beyond a couple of weapons, tools, and the clothes on their back. The Assets background is a Debt Notation on the character sheet that allows a player to purchase or make down payments on expensive items at character creation, if approved by the Game Master. The core types of Assets are Gear, Transportation, and Structure. Some settings also possess Lesser Arcana, Fetishes, Cybernetics, and other categories as starting Assets. *See Setting Books."
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Basically, the player starts off the game in debt to afford items. The player pays a 20% monthly interest rate, and the equipment financed in this manner is only valued at 10% of its listed price until the balance is paid in full. If the player abuses creditors or fails to maintain their payments in a reasonable manner, they gain the Bad Credit (2pt. Bane) without benefit and the property will be repossessed. *See Income for details."
                },
                {
                    "type": "subheading",
                    "order": 6,
                    "data": "Associates - Contacts & Minions",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "Associates are individuals who may be called upon for assistance. Any time an Associate is purchased, it is determined if it is a Contact or Minion. After character creation, additional associates can only be purchased if agreeable relations are developed through continued role-play. When a player calls upon an Associate, the player makes a 2d10 + Manipulation + Level of Associate. The level of success determines the amount of assistance that an Associate may provide to a character if they choose to accept. A character can always choose a lesser level of help and associated debt. It is important to remember that Associates are people, and lying about the danger of a given job or constantly physically or verbally abusing or endangering these associates may result in the loss of an Associate and the points spent to acquire them without recompense."
                },
                {
                    "type": "subheading",
                    "order": 8,
                    "data": "Contacts",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "These associates comprise a network of information and service brokers who are generally helpful within the scope of their field of study, which should also be described as thoroughly as possible by the player. Contacts will rarely, if ever, accompany a team on missions. Instead, they act as a resource to help provide players with critical data and services that the players may be lacking, helping to build a better story. When a player wishes to call upon a contact, they must roll based on the difficulty of the information they wish to receive. Each point spent in this background equals one Major Contact and a different field of expertise."
                },
                {
                    "type": "subheading",
                    "order": 10,
                    "data": "Minions",
                    "style_class": "text-xl font-bold mt-4"
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "Servants, pilots, grunts, personal assistants, and paid bodyguards are all examples of a minion. Although generally loyal, minions are little more than hired help, and if treated poorly, then betrayal is a likely side effect. These assistants, like other “NPC” backgrounds, should be described in full by the player. Every Level in Minion provides a new minion and increases the power of existing minions to the listed stat block."
                },
                {
                    "type": "table",
                    "order": 12,
                    "data": {
                        "headers": ["LVL", "Minion Stat Block", "Total Minions"],
                        "rows": [
                            ["L1", "2 PHP, 1 CHP, 3 in all Abilities and +2 to 3 Non-Combat & +1 to 1 Combat Skill.", "L1"],
                            ["L2", "2 PHP, 2 CHP, 3 in all Abilities and +2 to 3 Non-Combat & +1 to 1 Combat Skill.", "L1&2"],
                            ["L3", "3 PHP, 2 CHP, 3 in all Abilities and +3 to 3 Non-Combat & +1 to 2 Combat Skills.", "L1,2&3"],
                            ["L4", "3 PHP, 3 CHP, 3 in all Abilities and +3 to 3 Non-Combat & +1 to 2 Combat Skills.", "L1,2,3&4"],
                            ["L5", "4 PHP, 3 CHP, 4 in all Abilities and +4 to 4 Non-Combat & +2 to 2 Combat Skills.", "L1,2,3,4&5"],
                            ["L6", "4 PHP, 4 CHP, 4 in all Abilities and +4 to 4 Non-Combat & +2 to 2 Combat Skills.", "L1,2,3,4,5&6"],
                            ["L7", "5 PHP, 4 CHP, 4 in all Abilities and +5 to 4 Non-Combat & +3 to 2 Combat Skills.", "L1,2,3,4,5,6&7"],
                            ["L8", "5 PHP, 5 CHP, 5 in all Abilities and +5 to 4 Non-Combat & +3 to 2 Combat Skills.", "L1,2,3,4,5,6,7&8"],
                            ["L9", "6 PHP, 5 CHP, 5 in all Abilities and +6 to 5 Non-Combat & +4 to 2 Combat Skills.", "L1,2,3,4,5,6,7,8&9"],
                            ["L10", "6 PHP, 6 CHP, 6 in all Abilities and +6 to 5 Non-Combat & +4 to 2 Combat Skills.", "L1,2,3,4,5,6,7,8,9&10"]
                        ]
                    }
                },
                {
                    "type": "subheading",
                    "order": 13,
                    "data": "The Results of the Associate Use Roll: (Persuasion + Level of Associate)",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 14,
                    "data": "Very Easy (DL: 10-14): Considered a Failure: Contacts are unable or unwilling to provide information or service. Minions balk at being sent into situations alone that are even remotely dangerous, though they will still follow you into such situations but suffer a -6 to all Challenges."
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "Easy (DL: 15-20): Considered a Very Minor Success: Contacts can provide minimal information, and no real services of value. Minions will grudgingly go forth into remotely dangerous situations but suffer a -4 to all Challenges."
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "Moderate (DL: 21-30): Considered a Moderate Success: Contacts can provide basic services and mildly useful information for less than the usual cost. Minions willingly accompany you into dangerous situations where there is a reasonable chance of survival but suffer a -2 to all Challenges."
                },
                {
                    "type": "paragraph",
                    "order": 17,
                    "data": "Difficult (DL: 31-40): Considered a Success: Contacts can provide moderate information and minor services for less than the usual cost. Minions willingly go alone into dangerous situations understanding that a few of them may not make it."
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "Very Difficult (DL: 41-50): Considered Very Successful: Contacts can provide solid information and basic services for less than the usual cost. Minions understand that what they are being asked to do is potentially suicidal, but the ends justify the means regardless of the cost, and they are granted a +2 to all Challenges."
                },
                {
                    "type": "paragraph",
                    "order": 19,
                    "data": "Heroic (DL: 51-60): Considered Exceptionally Successful: Contacts are able to provide detailed information and high-end services for less than the usual cost. Minions understand that what they are being asked to do is potentially suicidal, but the ends justify the means regardless of the cost, and they receive a +4 to all Challenges."
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "Legendary (DL: 61+): Successful Beyond Expectations: Contacts can provide rare or classified information and major high-end services for less than the usual cost. Minions understand that what they are being asked to do is a no-win or return situation and have accepted their fate, receiving a +6 to all Challenges."
                },
                {
                    "type": "subheading",
                    "order": 21,
                    "data": "Cost of Associate Assistance",
                    "style_class": "text-2xl font-bold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 22,
                    "data": "A typical cost range is expenditure of Tiers of Income for that play session and the next to repay Contacts and Minions for services rendered. Failure to repay debts not only removes availability of the Associate until the debt and interest are paid, but if the issue is grievous enough, then a powerful enemy may be made."
                },
                {
                    "type": "table",
                    "order": 23,
                    "data": {
                        "headers": ["Difficulty", "Tier Cost"],
                        "rows": [
                            ["Easy", "2 Tiers"],
                            ["Moderate", "3 Tiers"],
                            ["Difficult", "4 Tiers"],
                            ["Very Difficult", "5 Tiers"],
                            ["Heroic", "6 Tiers"],
                            ["Legendary", "8 Tiers"]
                        ]
                    }
                },
                {
                    "type": "paragraph",
                    "order": 24,
                    "data": "Debt repayment can be spaced out, but it requires that Income Tiers be consumed for three times as long. I.E., an Easy Debt not paid immediately would be three months of 1 Tier worth of payment instead of one month of 2 Tier payments, as interest-bearing accounts have their own price to pay. This debt can also be paid or offset by performing services or paying equivalent monetary value at the Game Master's discretion."
                },
                {
                    "type": "heading",
                    "order": 26,
                    "data": "Comeliness"
                },
                {
                    "type": "paragraph",
                    "order": 27,
                    "data": "This Background represents social standards of physical beauty, sublime horror or attractive ruggedness and may be used in manipulation rolls when the situation is right granting a +1 to the roll per level of Comeliness."
                },
                {
                    "type": "heading",
                    "order": 28,
                    "data": "Income"
                },
                {
                    "type": "paragraph",
                    "order": 29,
                    "data": "This Background represents regular income. Players should decide the source of their income such as an inheritance, owning a business, winning the lottery on a monthly payout or some other form of long-term finances. The Monthly Currency Draw amounts listed below double if the character has a Scholar Finances Skill of equal value to the Tier of Income utilized. A character has access to this income in addition to the Basic Expenses listed unless Tiers have been consumed for Associate use. They may attempt to make a monthly roll (Intellect + Income Tier) for Monthly Currency Draw, which is absorbed by the player’s investments, but any funds not utilized are automatically reinvested and lost before the next currency draw."
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "Furthermore, at the GM’s discretion the player may purchase an item and remain in-debt to afford a very pricey item. The player may purchase an item equal to their Max Loan Rating but must pay the original amount plus an addition interest above the total. The equipment financed in this manner is only valued at 10% of its listed price until the balance is paid in full through Monthly Currency Draws or outside currency acquisitions. Furthermore, the players Income is reduced by Tiers based on the amount borrowed unless they possess the Scholar Finances Skill which reduces this penalty a single Tier. If forces are actively working against a player, then the difficulty may increase without providing additional benefit."
                },
                {
                    "type": "paragraph",
                    "order": 31,
                    "data": "If the player abuses creditors, they gain Bad Credit (2pt. Bane) without benefit and the property will be repossessed. Major purchases cannot be attempted more than once per month. Characters may still accumulate wealth through other means normally which may be invested to justify buying Income Background after character creation. Also, the GM is always permitted to decline to offer credit based on availability, character behavior or story disruption.",
                    "style_class": "italic text-gray-500"
                },
                {
                    "type": "table",
                    "order": 32,
                    "data": {
                        "headers": ["Difficulty Rating", "Monthly Draw", "Max Loan", "Tiers Reduced", "Interest"],
                        "rows": [
                            ["Very Easy (DL: 10–14)", "100", "Up to 100,000", "1", "30%"],
                            ["Easy (DL: 15–24)", "250", "Up to 250,000", "2", "25%"],
                            ["Moderate (DL: 25–34)", "500", "Up to 500,000", "2", "25%"],
                            ["Difficult (DL: 35–44)", "1000", "Up to 1,000,000", "3", "20%"],
                            ["Very Difficult (DL: 45–54)", "5000", "Up to 5,000,000", "3", "20%"],
                            ["Heroic (DL: 65–74)", "25,000", "Up to 25,000,000", "4", "15%"],
                            ["Legendary (DL: 75+)", "50,000", "Up to 50,000,000", "4", "10%"]
                        ]
                    }
                },
                {
                    "type": "heading",
                    "order": 33,
                    "data": "Legacy"
                },
                {
                    "type": "paragraph",
                    "order": 34,
                    "data": "Notoriety or Fame is the realm of reputation that engulfs popular movie stars, models, war heroes, professional athletes, and their ilk or even descendants. It is also a measure of their reputation within a certain society. Players must describe what they are famous or infamous for. The more points in Legacy that a character possesses, grants them more tolerance from others of their eccentricities because of their reputation. After spending five points in the Legacy Background, every additional point grants another environment that the character is accommodated within. (I.E. Legacy 6 grants acknowledgment in 2 environments at Level 5 while Legacy 7 grants acknowledgment in 3 environments at Level 5, etc.) Environments should be generally specific such as Night Club Scene, Goth, Hard Core, Aristocratic or Redneck Scene and should vaguely reflect the reason for them being famous. Such as a War Veteran might be well received amongst Rednecks, or a Movie Star would be indulged by Aristocrats."
                },
                {
                    "type": "paragraph",
                    "order": 35,
                    "data": "A Legacy allows a character to get into social events that they may not otherwise have been capable of getting into. In addition to social events, fans, and businesses often lavish gifts on the famous, such as free meals, rentals, etc. Additionally, a character can attempt to “Cause a Scene” in populated areas, drawing a crowd of people. Like real world fame, characters with the public Legacy background are easy to recognize, which can draw unwanted attention. A public Legacy figure receives a +1 per level of Legacy to gain access to closed social events or to “Cause a Scene.” Please note that it is VERY DIFFICULT for a person with a high Legacy to go unnoticed in public. A GM should apply penalties as they seem appropriate to any situations where the Character is attempting to move about unnoticed. All Rolls involving Legacy benefits are Performance + Legacy. A Botch on a Legacy Roll ends up in a complication in getting your “freebies” or where you get arrested for “Causing a Scene.”"
                },
                {
                    "type": "list",
                    "order": 36,
                    "data": [
                        "Very Easy (DL: 10–14): Getting into public events concerning your environment of recognition without waiting in line or getting a meal “on the house” in your hometown.",
                        "Easy (DL: 15–20): Getting into public events outside your environment of recognition without waiting in line or treating you and your close friend to a meal “on the house” while on the road at a low-end establishment.",
                        "Moderate (DL: 21–30): Getting “Face Time” at an open public event within your environment of recognition or being served complimentary drinks at establishments within your environment of recognition. You may also now “Cause a Scene” in a heavily populated area in your environment of recognition.",
                        "Difficult (DL: 31–40): Getting access to private events composed of influential people in your environment of recognition or getting “Face Time” at events outside your environment. High class establishments now gift you with complimentary drinks and other freebies in exchange for gracing their establishment. You may also choose to “Cause a Scene” outside your environment of recognition in a highly populated area.",
                        "Very Difficult (DL: 41–50): Getting access to private events of influential people outside your environment of recognition. Establishments provide free meals, beverages, and other accommodations merely so you will be seen dining or partying there.",
                        "Heroic (DL: 51–60): Getting into closed events, far outside your environment of recognition. Establishments now pay not only for your meals, beverages, and several gifts but they provide personal staff to meet your needs."
                    ]
                },
                {
                    "type": "heading",
                    "order": 37,
                    "data": "Rank"
                },
                {
                    "type": "paragraph",
                    "order": 38,
                    "data": "Rank is direct power in a corporate organization, highly structured agency, or military branch. This becomes important in game settings where players need to know who outranks who. Rank is directly tied to the position a character has within the organization. This may be lost or advanced through game play and is an immensely powerful tool that designates the power of command and access to information and supplies requisitions. A player should detail what organization they have Rank in and what branch of that entity they serve under. Rank should be limited at character creation to the mid-lower rankings for ease of play and limiting player power levels. The Enlisted Chart may be bought at standard cost but the Officers Chart costs double. Rank is a fluid mechanic that may be temporarily lost, when additional rank is granted, it must be paid for, or the character passes up the opportunity for advancement."
                },
                {
                    "type": "heading",
                    "order": 39,
                    "data": "Enlisted Chart",
                    "style_class": "text-center"
                },
                {
                    "type": "table",
                    "order": 39,
                    "data": {
                        "headers": ["", "Marines / Army", "Navy / Space", "Law Enforcement Agency", "Organized Crime"],
                        "rows": [
                            ["E1", "Private", "Recruit", "Cadet", "Associate"],
                            ["E2", "PVT 1st", "Apprentice", "Police Officer", "Soldiers or Assassins"],
                            ["E3", "Lance Corporal", "Seaman / Specialist", "Detective", "Capo or Captain"],
                            ["E4", "Corporal", "Petty Officer 3rd Class", "Sergeant", "Operative"],
                            ["E5", "Sergeant", "Petty Officer 2nd Class", "Lieutenant", "Consigliere or Underboss"],
                            ["E6", "Staff Sergeant", "Petty Officer 1st Class", "Captain", "Don or Boss"],
                            ["E7", "Gunnery Sergeant", "Chief", "Commander", "Adjudicator"],
                            ["E8", "Master Sergeant", "Senior Chief", "Deputy Chief", "The High Table"],
                            ["E9", "Sergeant Major", "Master Chief", "Chief", "The Elder"]
                        ]
                    }
                },
                {
                    "type": "heading",
                    "order": 40,
                    "data": "Officers Chart",
                    "style_class": "text-center"
                },
                {
                    "type": "table",
                    "order": 41,
                    "data": {
                        "headers": ["", "Marines / Army", "Navy / Space", "Federal Agency", "Theological Institute"],
                        "rows": [
                            ["O1", "2nd Lieutenant", "Ensign / Ensign", "Junior Agent", "Deacon"],
                            ["O2", "1st Lieutenant", "Lt. JG / Lt. JG", "Agent", "Priest"],
                            ["O3", "Captain", "Lieutenant", "Senior", "Vicar Forane"],
                            ["O4", "Major", "Lt. Commander", "Specialist / Scientist", "Monsignor"],
                            ["O5", "Lt. Colonel", "Commander", "Field Supervisor", "Bishop"],
                            ["O6", "Colonel", "Captain", "Ops Supervisor", "Primate"],
                            ["O7", "Brigadier General", "Rear Admiral Lower", "Department Head", "Archbishop"],
                            ["O8", "Major General", "Rear Admiral Upper", "Division Director", "Cardinal"],
                            ["O9", "Lt. General", "Vice Admiral", "Branch Director", "Patriarchs/Matriarchs"],
                            ["O10", "General", "Admiral", "Deputy Director", "Pope"],
                            ["O11", "-", "Fleet Admiral", "Director", "-"],
                            ["O12", "-", "Grand Admiral", "-", "-"]
                        ]
                    }
                }
            ]
        },
        {
            "title": "Banes",
            "slug": "banes",
            "chapter": "Banes & Boons",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Abusive S.O. (3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "You are aware of reality, and you are hit with it regularly. You have an abusive significant other who seems to take delight in venting their frustrations on you. The problem is that you love them and cannot seem to leave them no matter how much they hurt or force themselves upon you. You could call the law to avoid a beating, but you know it will only make things worse since restraining orders are not worth the paper they’re written on. She already taught you that once before. Remember?"
                },
                {
                    "type": "subheading",
                    "order": 4,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Every game day roll 1d10. On a roll of 1-7 nothing happens, and you can go about your business as normal. On a roll of 8-9 you start the day at a -2 to all Acrobatics and Athletics Rolls due to the aches and bruises that wrack your body. On a roll of a 10 your Endurance for calculating BHP maximum is treated as if it were 2 lower in addition to other penalties."
                },
                {
                    "type": "heading",
                    "order": 6,
                    "data": "Addiction (1pt.–3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "You are addicted to a substance that is dangerous to your health. The value of your addiction is based on its cost, availability, and legality.\n\n1pt. is addiction to a non-impairing legal substance such as cigarettes or coffee.\n2pt. is addiction to a moderately impairing but semi-legal substance such as opioids, alcohol, or cannabis.\n3pt. is addiction to a dangerous impairing illegal substance such as heroin, cocaine, or methamphetamines."
                },
                {
                    "type": "subheading",
                    "order": 9,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "Every day you must make a Difficult (DL: 40-49) Willpower Roll or partake of your addiction at some point throughout the day as determined by the GM. Select an appropriate Narcotic from the Equipment Section as appropriate per relative setting and suffer all appropriate penalties while under its influence."
                },
                {
                    "type": "heading",
                    "order": 11,
                    "data": "Amnesia (6pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 13,
                    "data": "You have few recollections before the past few months. Your history is a blank slate and only your GM knows who you really are and what enemies are lying in wait for your return."
                },
                {
                    "type": "subheading",
                    "order": 14,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "You may not purchase Culture, Demolition, Knowledge, Linguistics, Medicine, Programming, Piloting, Repair, Scholar, Security, Tech Op or Vehicles Skills during character creation and the GM may choose to keep some negative background hidden from you."
                },
                {
                    "type": "heading",
                    "order": 16,
                    "data": "Aroma of the Crypt (Ash’dren) (2pt Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 17,
                    "data": "Setting: Darkholme"
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "You exude a palpable aroma of dampened earth, soil or minerals. Created with heighten sense of smell or the Sharpened Sense Merit can easily mark, identify, and track you."
                },
                {
                    "type": "subheading",
                    "order": 19,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "Those tracking you receive a +5 to Primal Instinct Rolls to do so. If you do not wear perfume, tinctures, or other means of concealing this odor it inflicts a -2 in social situations and you may attract flies."
                },
                {
                    "type": "heading",
                    "order": 21,
                    "data": "Bad Credit (2pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 22,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 23,
                    "data": "Somewhere down the line you let your credit slip away from you and as a result you have trouble getting loans, rentals or even new purchases."
                },
                {
                    "type": "subheading",
                    "order": 24,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 25,
                    "data": "Basically, you are stuck on the cash for service basis and even legitimate bank transactions offer you only exceptionally high interest rates or charges when you do have to use them."
                },
                {
                    "type": "heading",
                    "order": 26,
                    "data": "Black and White (3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 27,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 28,
                    "data": "You see all situations in black and white or good and evil, etc. There is a right and a wrong way for all things in existence. Few others understand that there is no middle ground."
                },
                {
                    "type": "subheading",
                    "order": 29,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "The ends do not justify the means and every action must be accounted for, your views are always the most strickly extreme interpretation of the situation without consideration of mitigating factors. Theft is theft; it doesn’t matter if they were stealing to feed their family or if they were doing it for kicks. The punishment is the same."
                },
                {
                    "type": "heading",
                    "order": 31,
                    "data": "Black-listed (2pt. or 4pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 32,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 33,
                    "data": "You’ve been blacklisted by the government or very influential organizations. You are usually unemployable and seem to have problems taking jobs that require personal identification. This tends to leave you working for cash usually in the field of manual labor. This may have happened to you for political reasons, past crimes or merely because someone powerful just doesn't like you. In some cases, this may also bar you from entering certain establishments or events hosted by the entities you have displeased."
                },
                {
                    "type": "subheading",
                    "order": 34,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 35,
                    "data": "2pt. Bane you’ve been banned from legitimate employment your field of expertise and many closely related fields.\n\n4pt. Bane the character is unemployable at any legit business where personal identification is required."
                },
                {
                    "type": "heading",
                    "order": 36,
                    "data": "Blind (5pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 37,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 38,
                    "data": "Your eyes have ceased to function."
                },
                {
                    "type": "subheading",
                    "order": 39,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 40,
                    "data": "You automatically fail all Awareness & Analysis Rolls based purely on sight. You receive a -10 on all Short & Long Range Striking Rolls."
                },
                {
                    "type": "heading",
                    "order": 41,
                    "data": "Bloodlust (Kith Daemon) (2pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 42,
                    "data": "Setting: Darkholme"
                },
                {
                    "type": "paragraph",
                    "order": 43,
                    "data": "You require the sanguine life force of other sentient intelligent living creatures to sustain yourself. You must consume blood; your Skills reflect if you have met your fill."
                },
                {
                    "type": "subheading",
                    "order": 44,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 45,
                    "data": "If you have consumed no blood in the past five days then you suffer a -4, if you have consumed a minimum of 10 BHP of blood then you suffer a -1, if you have consumed a minimum of 20 BHP then you suffer no penalty, but if you consumed over 20 BHP and draw the last life blood of a creature, killing them you are granted a +1."
                },
                {
                    "type": "heading",
                    "order": 46,
                    "data": "Caraca’s Verdict (Kith) (3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 47,
                    "data": "Setting: Darkholme"
                },
                {
                    "type": "paragraph",
                    "order": 48,
                    "data": "You see things not as they are but as they shall be. Your eyes have a sickly golden yellow sheen, and you see constantly a fluctuation in reality as things shift between what they are and what they shall be. Any creature that is within a century of a natural death as dying, diseased or even skeletal while creations appear to be ready to crumble and disperse into the wind. This perception of the world causes an awkwardness when socializing with other creatures."
                },
                {
                    "type": "subheading",
                    "order": 49,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 50,
                    "data": "You suffer a -2 to all Social interactions and bonuses due to Comeliness are increased by a +3 when attempts to intimidate you are made as you find the shimmering changes of these creatures to be exceptionally disturbing."
                },
                {
                    "type": "heading",
                    "order": 51,
                    "data": "Chronically Late (1pt Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 52,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 53,
                    "data": "In contrast to those who are always on time, you are always late. Whether through poor personal habits or just an inability to track time, it seems that you are unable to show up in a timely manner. Even if your comrades start telling you an earlier time to be there to ensure your promptness it just happens that events transpire that still make you late."
                },
                {
                    "type": "subheading",
                    "order": 54,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 55,
                    "data": "You are always at least 10 minutes late."
                },
                {
                    "type": "heading",
                    "order": 56,
                    "data": "Color Blind (1pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 57,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 58,
                    "data": "You can see only in varying shades of gray, which may make some Rolls more difficult and Demolitions nearly impossible. (Note: In real life color blindness makes you unable to perceive only a certain portion of the color spectrum, but this rule is designed for simplicity.)"
                },
                {
                    "type": "subheading",
                    "order": 59,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 60,
                    "data": "You perceive Black, White normally and Blue/Purple/Green as Dark Gray while Red/Yellow/Orange appears as Light Gray."
                },
                {
                    "type": "heading",
                    "order": 61,
                    "data": "Criminal Entanglements (2pt. Or 4pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 62,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 63,
                    "data": "You owe someone, and you owe them big. Somewhere you got in some trouble and a “friend” offered to help you out. At the time you didn’t think it was such a big deal but now you’re not certain if you made the right decision."
                },
                {
                    "type": "subheading",
                    "order": 64,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 65,
                    "data": "2pt. Bane this means you must pay roughly 250 a month or 25% of your revenue, whichever is more and do some odd jobs to pay the interest on what you owe, just to keep the goons from shaking you down and roughing you up a little.\n\n4pt. Bane you’re someone’s bitch, at their beck and call. You’ve found that it doesn’t seem to matter how much you pay, but you’re always behind and they’re more than willing to remind you of that regardless of how many bones it takes."
                },
                {
                    "type": "heading",
                    "order": 66,
                    "data": "Criminal Record (2pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 67,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 68,
                    "data": "You have a record that states you were convicted of crimes. The truth behind this is irrelevant. The public believes that you’re a criminal and you suffer the appropriate legal restrictions. You may not possess firearm and you have trouble finding honest employment."
                },
                {
                    "type": "subheading",
                    "order": 69,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 70,
                    "data": "You suffer a -1 penalty to all Manipulation Rolls with law enforcement once they are aware of your record."
                },
                {
                    "type": "heading",
                    "order": 71,
                    "data": "Cripple (4pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 72,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 73,
                    "data": "Your legs have been damaged, and you require a cane to move."
                },
                {
                    "type": "subheading",
                    "order": 74,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 75,
                    "data": "All movement costs double Action Points."
                },
                {
                    "type": "heading",
                    "order": 76,
                    "data": "Curse of Aphasia (3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 77,
                    "data": "Setting: Darkholme"
                },
                {
                    "type": "paragraph",
                    "order": 78,
                    "data": "Once upon a time you or a member of your family drew the ire of Aphasia, and that curse was passed down to you. You are very attractive to people who you do not wish to attract, and these detestable individuals overlook any signs of rejection because they are keenly interested in your “alure”. Those who you might wish to attract treat you with a bit of contempt as they perceive you as vain and shallow. You may not be faithful to the deity Aphasia as she turns a blind eye to your ugly advances."
                },
                {
                    "type": "subheading",
                    "order": 79,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 80,
                    "data": "You suffer a -2 on Manipulation Social interactions to persuade those whom the DM believes that you find disgusting and detestable when trying to persuade them to interact with others instead of yourself. You suffer a -4 to persuade or seduce any that the DM believes that you find attractive."
                },
                {
                    "type": "heading",
                    "order": 81,
                    "data": "Cursed (2pt. or 4pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 82,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 83,
                    "data": "You have been cursed either by your own actions in the breaking of a Geas or by someone or something that you have inflicted grave wrongs upon. The curse is specific in nature and cannot be easily dispelled through common magic. There may be a means to atone for your sins, but the methods and the means are both up to the GM and should be a long, arduous task that reflects upon the nature that led to your affliction in the first place."
                },
                {
                    "type": "subheading",
                    "order": 84,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 85,
                    "data": "2pt. Curse is annoying. It can moderately affects preselected Powers, Techniques, Social Interactions and worse. The effect of your curse can be problematic enough where it tends to mildly damage relationships and subtly lowers the success of your endeavors.\n\n4pt. Curse is potentially deadly. It affects Powers, Techniques, Social Interactions and worse at the Game Masters discretion as the curse is powerful enough to not be contained to a mild incovenience. The effect of your curse can be problematic enough where it tends to or end damage relationships and lowers your success as well as the prosperity of those who keep your company."
                },
                {
                    "type": "heading",
                    "order": 86,
                    "data": "Deadly Metabolism (4pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 87,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 88,
                    "data": "Something is wrong with your body. You process nourishment at a dangerous rate. You must consume at least double the amount of food of others of your species though even this leaves you feeling slightly hungry."
                },
                {
                    "type": "subheading",
                    "order": 89,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 90,
                    "data": "Suffer -2 to all Athletics and Power Rolls when you have not consumed enough to meet your needs."
                },
                {
                    "type": "heading",
                    "order": 91,
                    "data": "Deaf (3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 92,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 93,
                    "data": "Your audible sense has been lost."
                },
                {
                    "type": "subheading",
                    "order": 94,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 95,
                    "data": "You automatically fail any Rolls that rely on audible sound."
                },
                {
                    "type": "heading",
                    "order": 96,
                    "data": "Dyslexic (2pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 97,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 98,
                    "data": "You have problems with words, symbols and numbers and their correct order. This makes reading and comprehending information troublesome."
                },
                {
                    "type": "subheading",
                    "order": 99,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 100,
                    "data": "Suffer a -2 penalty for all Technical Operation or Scholar, and it takes you a substantial while longer to learn what you’re looking for."
                },
                {
                    "type": "heading",
                    "order": 101,
                    "data": "Easily Lost (3pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 102,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 103,
                    "data": "You seem to always believe that you’re headed in the right direction but that seldom, if ever, is the result."
                },
                {
                    "type": "subheading",
                    "order": 104,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 105,
                    "data": "Suffer a -2 to all Navigation Rolls. Once per game session, the GM may call for a Navigation check. Failure indicates you lead the party astray, or get seperated from the group."
                },
                {
                    "type": "heading",
                    "order": 106,
                    "data": "Eclectic Subculture (2pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 107,
                    "data": "Setting: Core"
                },
                {
                    "type": "paragraph",
                    "order": 108,
                    "data": "Everything about you screams High Society, Goth, Punk, Hard Core or Emo. Inside your subculture everything is gravy but when dealing with those outside of your special little group."
                },
                {
                    "type": "subheading",
                    "order": 109,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 110,
                    "data": "Suffer a -1 to Manipulation Rolls outside of your subculture."
                },
                {
                    "type": "heading",
                    "order": 111,
                    "data": "Endless Hunt (4pt. Bane)"
                },
                {
                    "type": "paragraph",
                    "order": 112,
                    "data": "Setting: Darkholme"
                },
                {
                    "type": "paragraph",
                    "order": 113,
                    "data": "You live for the hunt. You may stalk and toy with your prey, but once you mark them as a target you will not cease until you have collected your trophy or they have singlehandedly bested you. In case of the latter you shall give them a year’s reprieve before resuming the hunt."
                },
                {
                    "type": "subheading",
                    "order": 114,
                    "data": "Mechanics",
                    "style_class": "text-xl italic mt-2 text-gray-400"
                },
                {
                    "type": "paragraph",
                    "order": 115,
                    "data": "The trigger for Endless Hunt should be discussed with the GM during character creation. Once the conditions of the hunt are triggered, each week you avoid hunting the target grants a cumulate -1 to all Skill checks until it reaches a -10.\n\nEngaging in the hunt removes the Skill modifiers at the rate of 1 per week. Traveling or seeking out your prey counts as engaging in the hunt. If your target is killed when you are not present then make a DL 35 Willpower Roll, if you fail then the one who stole your kill becomes the new focus of your hunt."
                }
            ]
        },
        {
            "title": "The Virtues, Failings, Vices & Balance",
            "slug": "virtues-vices", 
            "chapter": "Customization Options",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Optional Rule: Advanced Players",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": """
                        Virtues are the best part of human nature. Each person has a virtue that is inherent to their core. Those who epitomize their inner strength develops the ability to bring out greater potential in others while a person who fails to maintain balance loses contact with their inner self devolves into degrees of insanity. Losing contact with oneself occurs through failings or overindulgence in vices. Failings are actions that detract from one’s virtues and vices are enjoyable acts, but constant indulgence causes one to grow further detached from the more noble aspects of their nature.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "container",
                    "order": 3,
                    "data": "open",
                    "style_class": "flex flex-col items-center justify-center max-w-4xl mx-auto px-8"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Virtues are the best part of human nature. Each person has a virtue that is inherent to their core. Those who epitomize their inner strength develops the ability to bring out greater potential in others while a person who fails to maintain balance loses contact with their inner self devolves into degrees of insanity. Losing contact with oneself occurs through failings or overindulgence in vices. Failings are actions that detract from one's virtues and vices are enjoyable acts, but constant indulgence causes one to grow further detached from the more noble aspects of their nature.",
                    "style_class": "text-center mb-8"
                },
                {
                    "type": "container",
                    "order": 5,
                    "data": "open",
                    "style_class": "flex justify-between items-start w-full gap-4"
                },
                {
                    "type": "container",
                    "order": 6,
                    "data": "open",
                    "style_class": "flex flex-col items-center w-1/3"
                },
                {
                    "type": "heading",
                    "order": 7,
                    "data": "Virtues",
                    "style_class": "underline text-2xl font-semibold mb-4 text-center"
                },
                {
                    "type": "list",
                    "order": 8,
                    "data": [
                        "Justice",
                        "Balance",
                        "Courage",
                        "Sincerity",
                        "Diligence",
                        "Selflessness",
                        "Temperance"
                    ],
                    "style_class": "text-center list-none space-y-2"
                },
                {
                    "type": "container",
                    "order": 9,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 10,
                    "data": "open",
                    "style_class": "flex items-center justify-center w-1/3"
                },
                {
                    "type": "image",
                    "order": 11,
                    "data": {
                        "file_path": "/static/images/sword.jpg",
                        "alt_text": "Virtues Chart",
                        "class_name": "w-16 h-auto"
                    }
                },
                {
                    "type": "container",
                    "order": 12,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 13,
                    "data": "open",
                    "style_class": "flex flex-col items-center w-1/3"
                },
                {
                    "type": "heading",
                    "order": 14,
                    "data": "Vices",
                    "style_class": "underline text-2xl font-semibold mb-4 text-center"
                },
                {
                    "type": "list",
                    "order": 15,
                    "data": [
                        "Lust",
                        "Envy",
                        "Greed",
                        "Pride",
                        "Wrath",
                        "Apathy",
                        "Gluttony"
                    ],
                    "style_class": "text-center list-none space-y-2"
                },
                {
                    "type": "container",
                    "order": 16,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 17,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 18,
                    "data": "close"
                },
                {
                    "type": "heading",
                    "order": 19,
                    "data": "Advanced Virtue",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": """
                        To advance a Tier in a virtue the character must constantly act in accordance with a higher standard as role-playing opportunities present themselves. If a character maintains these standards consistently, then they are advanced a single step in the appropriate Virtue at the Game Masters discretion.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "heading",
                    "order": 21,
                    "data": "Losing Virtue",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 22,
                    "data": """
                        If a failing or vice has occurred, then it takes significantly more effort to advance ones Balance. This is representative of the internal struggles of the character over abdicating their conscious. To avoid players mathematically working the system it merely takes one significant failing or a gross gorging indulgence to automatically gain a Step or even a Tier of a Failing or Vice. This same rule can be inversely applied to Virtues if the actions are grievous enough. The benefit of being virtuous are hard to obtain and even more difficult to maintain and this should always be considered.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "heading",
                    "order": 23,
                    "data": "Virtue Balance",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 24,    
                    "data": """
                        Even as a virtue-less person is indifferent to their own shortcomings, those that seek to cultivate and grow in their virtue it becomes easier to fall short of the expectations that one sets for themself. but the more one engages in their Vice the harder it becomes to resist which causes one to lose focus on their better aspects.
                    """.replace("\n", " ").strip()
                }, 
                {
                    "type": "list",
                    "order": 25,
                    "data": [
                        "Virtue Balance 4 - Cannot condone what they see as aspects of their associated Vice in their presence, tolerating such automatically drops their Virtuous Act by one",
                        "Virtue Balance 3 - May not perform the Vice but may condone the Vice in others without accumulating a Vice Indulgence. A single oppositional action to their Virtue requires a Uncontested Difficult (DL: 31-40) Willpower to avoid losing a Virtuous Act",
                        "Virtue Balance 2 - May perform the Vice once per Game Setting Monthly Cycle without accumulating a Vice Indulgence. A single oppositional action to their Virtue requires a Uncontested Moderate (DL: 21-30) Willpower to avoid losing a Virtuous Act",
                        "Virtue Balance 1 - May perform the Vice twice per Game Setting Monthly Cycle without accumulating a Vice Indulgence. A single oppositional action to their Virtue requires a Uncontested Easy (DL: 15-20) Willpower to avoid losing a Virtuous Act",
                        "Virtue Balance 0 - Indifferent Vices and Virtues and may actively engage in as they have not spiritually developed enough to understand the repercussions of their actions",
                        "Virtue Balance -1 - Has learned to appreciate the Vice, indulging fulfils their needs. Uncontested Easy (DL: 15-20) Willpower to avoid indulging each time exposed. To remove an indulgence, they must abstain from two Vice opportunities over the course of a game setting month-long penance",
                        "Virtue Balance -2 - Enjoys the Vice and has difficulties declining participation or observance, even if this requires that they encourage others to indulge to satiate their needs. Moderate (DL: 21-30) Willpower to avoid indulging each time exposed. To remove an indulgence, they must abstain from six Vice opportunities over the course of three game setting month-long penances",
                        "Virtue Balance -3 - Addicted to the Vice and has difficulties declining participation or observance, even if this requires that they encourage others to indulge to satiate their needs. Uncontested Difficult (DL: 31-40) Willpower to avoid indulging if exposed or avoiding being angry if others refuse to participate. To remove an indulgence, they must abstain from nine Vice opportunities over the course of six game setting month-long penances",
                        "Virtue Balance -4 - Lives for the Vice and actively seeks participation in the immortality of their actions while forcing others to engage. Uncontested Very Difficult (DL: 41-50) Willpower to avoid indulging or avoid forcing others if they refuse to participate. To remove an indulgence, they must abstain from twelve Vice opportunities over the course of a game setting year-long penances"
                    ],
                    "style_class": "space-y-8 max-w-3xl mx-auto px-8 py-6 [&>*]:border-b [&>*]:border-gray-700 [&>*]:pb-6 [&>*:last-child]:border-0 font-medium text-lg"
                }
            ]
        },
        {
            "title": "Benefits of Virtue",
            "slug": "benefits-virtue",
            "chapter": "Customization Options",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": """
                        The benefit of possessing high virtue in this game is primarily manifested through the ability to perform Virtue Checks during critical moments of the narrative. These moments are typically life-or-death situations where the objectives transcend personal ambitions. The opportunity to make a Virtue Check is at the discretion of the game master or storyteller, who determines the appropriateness based on the circumstances presented in the gameplay.
                    """.replace("\n", " ").strip()
                },
                                {
                    "type": "container",
                    "order": 2,
                    "data": "open",
                    "style_class": "pl-10 w-2/3"
                },
                {
                    "type": "heading",
                    "order": 3,
                    "data": "Rallying Cry",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "When a player believes their character’s actions align with a high-tier virtue they possess, specifically Tier 4, they can request to give a Rallying Cry."
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "To initiate a Rallying Cry, the character performs a Virtue Check by rolling (2d10 + Virtue Score) against a Moderate Difficulty Level (DL: 21-30)."
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "If successful, all allies within hearing range benefit from the Virtue's specific bonus until the event's conclusion. Each virtue offers a unique combat bonus, enhancing the group's capabilities in strategic ways:"
                },
                {
                    "type": "list",
                    "order": 7,
                    "data": [
                        "Courage: +2 to Attack & Martial Arts Rolls per Tier.",
                        "Balance: +2 to Damage & Awareness Rolls per Tier.",
                        "Selflessness: +2 to Attack & Awareness Rolls per Tier.",
                        "Righteous: +2 to all Damage & Power Rolls per Tier.",
                        "Sincerity: +2 to Aggressive Combat & Power Rolls per Tier.",
                        "Diligence: +2 to Defense & Willpower Rolls per Tier.",
                        "Temperance: +2 to Defensive & Martial Arts Rolls per Tier."
                    ],
                    "style_class": "list-disc pl-6"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "It is important to note that a character can only benefit from one Rallying Cry at a time."
                },  
                {
                    "type": "heading",
                    "order": 9,
                    "data": "Divine Providence:",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "Characters adhering to the tenets of their faith may receive blessings, known as Divine Providence. The nature of these blessings is determined collaboratively between the game master and the player, depending on the game's setting. These blessings are designed to reflect the character's devotion and the thematic elements of the game's universe."
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "For instance, in Darkholme, a Divine Providence may be a token..."
                },
                {
                    "type": "heading",
                    "order": 17,
                    "data": "Judicial Favor",
                    "style_class": "text-2xl font-semibold mt-6"
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "Across cultures within the game world, various Orders have been established, uniting individuals with similar values and objectives. These Orders are more than mere alliances; they are bound by a deep commitment to a set of shared Virtues and specific causes."
                },
                {
                    "type": "paragraph",
                    "order": 19,
                    "data": "Membership in an Order requires demonstrated dedication to its Virtues and adherence to its rules, which often dictate the defensive and offensive strategies during gameplay."
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "The benefits of being part of an Order are multifaceted, potentially influencing a character's social standing, strategic abilities, and access to resources within the game."
                },
                                {
                    "type": "container",
                    "order": 21,
                    "data": "close",
                },
                {
                    "type": "paragraph",
                    "order": 21,
                    "data": "This structured approach to virtues and organizational affiliations in the game not only enhances character development but also enriches the interaction between players and the game master, providing a layered and immersive role-playing experience."
                }
            ],
        },
        {
            "title": "Dangers of Losing Balance",
            "slug": "dangers-losing-balance",
            "chapter": "Customization Options",
            "content": [
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Balance is the quality that separates a creature and their actions from those of mindless lesser beasts. Complete loss of a Virtue or overwhelming accumulation of Vice is the first step in dehumanizing a creature causing it to revert to a more primal state. Each step into the negative of Balance causes a derangement. The trigger of the derangement is set by the presiding game master and is related to the incident that caused the negative Balance. If a character continues sliding, then for each additional loss the player must make a Willpower Sum Roll or lose control of their character forever. There is an ever-increasing chance that the creature goes irrevocably insane and either kills itself or becomes so dangerous that others must end its existence for the safety of all."
                },
                {
                    "type": "list",
                    "order": 3,
                    "data": [
                        "-1 Balance: Easy (DL: 15-20) Roll to Retain Character | Penalty: Associated Condition + Obsession",
                        "-2 Balance: Moderate (DL: 21-30) Roll to Retain Character | Penalty: Associated Condition + Psychopathic",
                        "-3 Balance: Difficult (DL: 31-40) Roll to Retain Character | Penalty: Associated Condition + Schizophrenia",
                        "-4 Balance: Very Difficult (DL: 41-50) Roll to Retain Character | Penalty: Associated Condition + Nihilism",
                        "-5 Balance: Heroic (DL: 51-60) Roll to Retain Character | Penalty: Associated Condition + Complete Insanity"
                    ],
                    "style_class": "list-none pl-10 space-y-2"
                }
            ]
        }
    ]






    #images class for tailwind: ="float-right ml-4 mb-4 w-1/3"; // Tailwind styles

    # Seed the database with sections and their content
    for section_data in sections:
        print(f"Adding section: {section_data['title']}")
        section = Section(
            title=section_data["title"],
            slug=section_data["slug"],
            chapter=section_data["chapter"]
        )
        db.session.add(section)
        db.session.commit()  # Commit to generate the section ID

        for content_data in section_data["content"]:
            print(f"Adding content: {content_data['type']} with order {content_data['order']}")
            content = Content(
                section_id=section.id,
                content_type=content_data["type"],
                content_order=content_data["order"],
                content_data=clean_text(content_data["data"]),  # Clean before inserting
                style_class=clean_text(content_data.get("style_class", ""))
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