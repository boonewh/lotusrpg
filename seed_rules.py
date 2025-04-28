from lotusrpg import create_app, db
from lotusrpg.models import Section, Content
import re

def clean_text(text): 
    if not isinstance(text, str):  
        return text
    return re.sub(r"\s+",
" ", text.replace("\xa0",
" ")).strip()

def seed_rules():
    print("Seeding rules...")

    db.session.query(Content).delete()
    db.session.query(Section).delete()
    db.session.commit()

    # Define sections and rules
    sections = [
    {
        "title": "From the Beginning",
        "slug": "beginning",
        "chapter": "Introduction",
        "content": [
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
                                We've broken things down into three easy-to-follow sections: """.replace("\n", " ").strip()
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
                                As you explore this process, think about who your character is within the world: their background, their moral compass, and their relationships. In the following sections, you'll find plenty of inspiring ideas and helpful tools to build out these details: """.replace("\n", " ").strip()
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
                    "headers": [
                        "Race",
                        "Subrace",
                        "Cost"
                    ],
                    "rows": [
                        [
                            "Faeyr",
                            {
                                "text": "Dylithar",
                                "url": "/core/dylithar"
                            },
                            "40"
                        ],
                        [
                            "",
                            {
                                "text": "Miaki",
                                "url": "/core/miaki"
                            },
                            "40"
                        ],
                        [
                            "",
                            {
                                "text": "Tiermalain",
                                "url": "/core/tiermalain"
                            },
                            "40"
                        ],
                        [
                            "Human",
                            {
                                "text": "Akkadian",
                                "url": "/core/akkadian"
                            },
                            "0"
                        ],
                        [
                            "",
                            {
                                "text": "Midian",
                                "url": "/core/midian"
                            },
                            "0"
                        ],
                        [
                            "",
                            {
                                "text": "Sutherlander",
                                "url": "/core/sutherlander"
                            },
                            "0"
                        ],
                        [
                            "",
                            {
                                "text": "Ennocean",
                                "url": "/core/ennocean"
                            },
                            "0"
                        ],
                        [
                            {
                                "text": "Romling",
                                "url": "/core/romling"
                            },
                            "-",
                            "20"
                        ],
                        [
                            "Svar",
                            {
                                "text": "Dargnan",
                                "url": "/core/dargnan"
                            },
                            "40"
                        ],
                        [
                            "",
                            {
                                "text": "Kargathi",
                                "url": "/core/kargathi"
                            },
                            "40"
                        ],
                        [
                            "",
                            {
                                "text": "Mordron",
                                "url": "/core/mordron"
                            },
                            "40"
                        ]
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
                        "url": "/core/law-abiding"
                    },
                    {
                        "text": "Honorable",
                        "url": "/core/honorable"
                    },
                    {
                        "text": "Righteous",
                        "url": "/core/righteous"
                    },
                    {
                        "text": "Pragmatic",
                        "url": "/core/pragmatic"
                    },
                    {
                        "text": "Malkavian",
                        "url": "/core/machiavellian"
                    },
                    {
                        "text": "Anarchistic",
                        "url": "/core/anarchistic"
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
                    "headers": [
                        "Initial Roll",
                        "Critical Success Bonus",
                        "Chain Success Bonus Roll",
                        "Continued Chain Success Bonus Roll",
                        "Sum"
                    ],
                    "rows": [
                        [
                            "10 + 10",
                            "+10",
                            "+10 + 5",
                            "+3",
                            "= 48"
                        ]
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
                    "headers": [
                        "Difficulty Level",
                        "Range",
                        "Description"
                    ],
                    "rows": [
                        [
                            "Simple",
                            "<10",
                            "A task so simple that even a person with little or no Skill could quite possibly complete it with ease."
                        ],
                        [
                            "Very Easy",
                            "10-14",
                            "A task that a minimally skilled person could possibly complete."
                        ],
                        [
                            "Easy",
                            "15-20",
                            "These are what compromise most of our daily tasks."
                        ],
                        [
                            "Moderate",
                            "21-30",
                            "Tasks of this nature require skill, effort, and concentration."
                        ],
                        [
                            "Difficult",
                            "31-40",
                            "Difficult tasks are hard, and an average person will have problems succeeding."
                        ],
                        [
                            "Very Difficult",
                            "41-50",
                            "Only the most talented of individuals have any chance of success."
                        ],
                        [
                            "Heroic",
                            "51-60",
                            "Impossible for normal people and exceedingly difficult even for heroes."
                        ],
                        [
                            "Legendary",
                            "61+",
                            "Beyond the measure of mortal men and truly worthy of myths and legends."
                        ]
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
                    "headers": [
                        "Total Power",
                        "Light Load",
                        "Heavy Load",
                        "Over Press",
                        "Dead Lift",
                        "Bench Press"
                    ],
                    "rows": [
                        [
                            "1",
                            "10",
                            "50",
                            "25",
                            "50",
                            "50"
                        ],
                        [
                            "2",
                            "20",
                            "100",
                            "50",
                            "100",
                            "100"
                        ],
                        [
                            "3",
                            "30",
                            "150",
                            "100",
                            "200",
                            "150"
                        ],
                        [
                            "4",
                            "40",
                            "200",
                            "150",
                            "300",
                            "200"
                        ],
                        [
                            "5",
                            "50",
                            "250",
                            "200",
                            "400",
                            "250"
                        ],
                        [
                            "6",
                            "60",
                            "300",
                            "250",
                            "500",
                            "300"
                        ],
                        [
                            "7",
                            "70",
                            "350",
                            "275",
                            "550",
                            "350"
                        ],
                        [
                            "8",
                            "80",
                            "400",
                            "300",
                            "600",
                            "400"
                        ],
                        [
                            "9",
                            "90",
                            "450",
                            "325",
                            "650",
                            "450"
                        ],
                        [
                            "10",
                            "100",
                            "500",
                            "350",
                            "700",
                            "500"
                        ],
                        [
                            "11",
                            "110",
                            "550",
                            "375",
                            "750",
                            "550"
                        ],
                        [
                            "12",
                            "120",
                            "600",
                            "400",
                            "800",
                            "600"
                        ],
                        [
                            "13",
                            "130",
                            "650",
                            "425",
                            "850",
                            "650"
                        ],
                        [
                            "14",
                            "140",
                            "700",
                            "450",
                            "900",
                            "700"
                        ],
                        [
                            "15",
                            "150",
                            "750",
                            "475",
                            "950",
                            "750"
                        ],
                        [
                            "16",
                            "160",
                            "800",
                            "500",
                            "1000",
                            "800"
                        ],
                        [
                            "17",
                            "170",
                            "850",
                            "525",
                            "1050",
                            "850"
                        ],
                        [
                            "18",
                            "180",
                            "900",
                            "550",
                            "1100",
                            "900"
                        ],
                        [
                            "19",
                            "190",
                            "950",
                            "575",
                            "1150",
                            "950"
                        ],
                        [
                            "20",
                            "200",
                            "1000",
                            "600",
                            "1200",
                            "1000"
                        ],
                        [
                            "21",
                            "210",
                            "1100",
                            "650",
                            "1300",
                            "1100"
                        ],
                        [
                            "22",
                            "220",
                            "1200",
                            "700",
                            "1400",
                            "1200"
                        ],
                        [
                            "23",
                            "230",
                            "1300",
                            "750",
                            "1500",
                            "1300"
                        ],
                        [
                            "24",
                            "240",
                            "1400",
                            "800",
                            "1600",
                            "1400"
                        ],
                        [
                            "25",
                            "250",
                            "1500",
                            "850",
                            "1700",
                            "1500"
                        ],
                        [
                            "26+",
                            "+50",
                            "+250",
                            "+125",
                            "+250",
                            "+250"
                        ]
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
                    "headers": [
                        "Total Power",
                        "Light Load",
                        "Heavy Load",
                        "Over Press",
                        "Dead Lift",
                        "Bench Press"
                    ],
                    "rows": [
                        [
                            "1",
                            "20",
                            "100",
                            "50",
                            "100",
                            "100"
                        ],
                        [
                            "2",
                            "40",
                            "200",
                            "100",
                            "200",
                            "200"
                        ],
                        [
                            "3",
                            "60",
                            "300",
                            "200",
                            "400",
                            "300"
                        ],
                        [
                            "4",
                            "80",
                            "400",
                            "300",
                            "600",
                            "400"
                        ],
                        [
                            "5",
                            "100",
                            "500",
                            "400",
                            "800",
                            "500"
                        ],
                        [
                            "6",
                            "120",
                            "600",
                            "500",
                            "1000",
                            "600"
                        ],
                        [
                            "7",
                            "140",
                            "700",
                            "550",
                            "1100",
                            "700"
                        ],
                        [
                            "8",
                            "160",
                            "800",
                            "600",
                            "1200",
                            "800"
                        ],
                        [
                            "9",
                            "180",
                            "900",
                            "650",
                            "1300",
                            "900"
                        ],
                        [
                            "10",
                            "200",
                            "1000",
                            "700",
                            "1400",
                            "1000"
                        ],
                        [
                            "11",
                            "220",
                            "1100",
                            "750",
                            "1500",
                            "1100"
                        ],
                        [
                            "12",
                            "240",
                            "1200",
                            "800",
                            "1600",
                            "1200"
                        ],
                        [
                            "13",
                            "260",
                            "1300",
                            "850",
                            "1700",
                            "1300"
                        ],
                        [
                            "14",
                            "280",
                            "1400",
                            "900",
                            "1800",
                            "1400"
                        ],
                        [
                            "15",
                            "300",
                            "1500",
                            "950",
                            "1900",
                            "1500"
                        ],
                        [
                            "16",
                            "320",
                            "1600",
                            "1000",
                            "2000",
                            "1600"
                        ],
                        [
                            "17",
                            "340",
                            "1700",
                            "1050",
                            "2100",
                            "1700"
                        ],
                        [
                            "18",
                            "360",
                            "1800",
                            "1100",
                            "2200",
                            "1800"
                        ],
                        [
                            "19",
                            "380",
                            "1900",
                            "1150",
                            "2300",
                            "1900"
                        ],
                        [
                            "20",
                            "400",
                            "2000",
                            "1200",
                            "2400",
                            "2000"
                        ],
                        [
                            "21",
                            "420",
                            "2200",
                            "1300",
                            "2600",
                            "2200"
                        ],
                        [
                            "22",
                            "440",
                            "2400",
                            "1400",
                            "2800",
                            "2400"
                        ],
                        [
                            "23",
                            "460",
                            "2600",
                            "1500",
                            "3000",
                            "2600"
                        ],
                        [
                            "24",
                            "480",
                            "2800",
                            "1600",
                            "3200",
                            "2800"
                        ],
                        [
                            "25",
                            "500",
                            "3000",
                            "1700",
                            "3400",
                            "3000"
                        ],
                        [
                            "26+",
                            "100",
                            "500",
                            "250",
                            "500",
                            "500"
                        ]
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
                    "headers": [
                        "Creature Size",
                        "Reach / Lunge",
                        "Space (5' Squares)"
                    ],
                    "rows": [
                        [
                            "Gargantuan S10",
                            "25’ / 30’",
                            "8 x 16"
                        ],
                        [
                            "Colossal S8",
                            "20’ / 25’",
                            "4 x 8"
                        ],
                        [
                            "Huge S6",
                            "15’ / 20’",
                            "2 x 4"
                        ],
                        [
                            "Large S4",
                            "10’ / 15’",
                            "1 x 2"
                        ],
                        [
                            "Medium S2",
                            "5’ / 10’",
                            "1 x 1"
                        ],
                        [
                            "Small S1",
                            "5’ / 10’",
                            "1 x 1"
                        ],
                        [
                            "Tiny S0",
                            "0’ / 5’",
                            ".5 x .5"
                        ],
                        [
                            "Diminutive S00",
                            "0’ / 5’",
                            ".25 x .25"
                        ]
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
                    "headers": [
                        "Creature Size",
                        "Reach / Lunge",
                        "Space (1.5 m Squares)"
                    ],
                    "rows": [
                        [
                            "Gargantuan S10",
                            "7.5 m / 9 m",
                            "8 x 16"
                        ],
                        [
                            "Colossal S8",
                            "6 m / 7.5 m",
                            "4 x 8"
                        ],
                        [
                            "Huge S6",
                            "4.5 m / 6 m",
                            "2 x 4"
                        ],
                        [
                            "Large S4",
                            "3 m / 4.5 m",
                            "1 x 2"
                        ],
                        [
                            "Medium S2",
                            "1.5 m / 3 m",
                            "1 x 1"
                        ],
                        [
                            "Small S1",
                            "1.5 m / 3 m",
                            "1 x 1"
                        ],
                        [
                            "Tiny S0",
                            "0 m / 1.5 m",
                            ".5 x .5"
                        ],
                        [
                            "Diminutive S00",
                            "0 m / 1.5 m",
                            ".25 x .25"
                        ]
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
                    "headers": [
                        "Roll",
                        "Effect",
                        "Description"
                    ],
                    "rows": [
                        [
                            "5 to 17",
                            "Shaken",
                            "-5 to all Non-Dodge or Running Rolls for the next 5 Rounds."
                        ],
                        [
                            "3, 4, 18 or 19",
                            "Scared",
                            "-10 to all Non-Dodge or Running Rolls for the next 5 Rounds."
                        ],
                        [
                            "2 or 20",
                            "Bad Reaction",
                            "Roll on Fear Reaction Table II."
                        ]
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
                    "headers": [
                        "Roll",
                        "Effect",
                        "Description"
                    ],
                    "rows": [
                        [
                            "6 to 16",
                            "Terrified",
                            "Flee away from source of terror at top speed for 2d10 Rounds."
                        ],
                        [
                            "5 or 17",
                            "Petrified",
                            "Too terrified to move. Characters can only stand still screaming until the source of fear is removed, leaves, or successfully attacks the character."
                        ],
                        [
                            "4 or 18",
                            "Catatonic",
                            "You collapse into a whimpering ball, taking no actions for 1d10 Minutes as your mind withdraws from reality."
                        ],
                        [
                            "3 or 19",
                            "Black Out",
                            "Your system has shut itself down to avoid damage as you black out for 2d10 minutes."
                        ],
                        [
                            "2 or 20",
                            "Traumatized",
                            "Having experienced more fear than the body can handle, you experience severe emotional trauma. Roll 2d10—on any result except a 2 or 20, you black out for 2d10 minutes and remain catatonic for 2d10 days. If you roll a 2 or 20, your heart seizes up, causing death unless you make an Uncontested Heroic (DL: 60-69) Bio Control Roll."
                        ]
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
                    "headers": [
                        "Creature Type",
                        "Resistance per Century"
                    ],
                    "rows": [
                        [
                            "Immortal Creatures",
                            "5% cumulative resistance"
                        ],
                        [
                            "Pseudo Immortals",
                            "2% cumulative resistance"
                        ]
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
                    "headers": [
                        "Vision Type",
                        "Description"
                    ],
                    "rows": [
                        [
                            "Daylight",
                            "Baseline vision distance based on midday lighting levels, affected by environmental conditions."
                        ],
                        [
                            "Light Source",
                            "Overrides Low Light and Darkvision, setting a new range for all within its radius."
                        ],
                        [
                            "Low Light",
                            "Vision capability in twilight, moonlight, or a dimly lit structure."
                        ],
                        [
                            "Darkvision",
                            "Vision capability in a moonless night or inside an unlit darkened structure."
                        ]
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
                    "headers": [
                        "Measurement",
                        "Formula"
                    ],
                    "rows": [
                        [
                            "MPH",
                            "((MAP * 1800) / 5280)"
                        ],
                        [
                            "KPH",
                            "(((MAP * 1800) / 5280) / 1.5)"
                        ]
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
                    "headers": [
                        "Measurement",
                        "Formula"
                    ],
                    "rows": [
                        [
                            "MPH",
                            "((MAP * 1800) / 5280) * All Out Multiplier"
                        ],
                        [
                            "KPH",
                            "(((MAP * 1800) / 5280) / 1.5) * All Out Multiplier"
                        ]
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
                    "headers": [
                        "Difficulty Formula"
                    ],
                    "rows": [
                        [
                            "MPH",
                            "MPH * Hours"
                        ],
                        [
                            "KPH",
                            "(KPH / 1.5) * Hours"
                        ]
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
                    "headers": [
                        "Difficulty Formula"
                    ],
                    "rows": [
                        [
                            "MPH",
                            "MPH + (5 x 10 Minute Increments)"
                        ],
                        [
                            "KPH",
                            "(KPH / 1.5) + (5 x 10 Minute Increments)"
                        ]
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
                    "headers": [
                        "Disengaged MAP",
                        "MPH",
                        "KPH",
                        "All Out MPH",
                        "All Out KPH"
                    ],
                    "rows": [
                        [
                            "3",
                            "1.02",
                            "1.53",
                            "1.28",
                            "1.92"
                        ],
                        [
                            "4",
                            "1.36",
                            "2.05",
                            "1.70",
                            "2.56"
                        ],
                        [
                            "5",
                            "1.70",
                            "2.56",
                            "2.13",
                            "3.20"
                        ],
                        [
                            "6",
                            "2.05",
                            "3.07",
                            "2.56",
                            "3.84"
                        ],
                        [
                            "7",
                            "2.39",
                            "3.58",
                            "2.98",
                            "4.47"
                        ],
                        [
                            "8",
                            "2.73",
                            "4.09",
                            "3.41",
                            "5.11"
                        ],
                        [
                            "9",
                            "3.07",
                            "4.60",
                            "3.84",
                            "5.73"
                        ],
                        [
                            "10",
                            "3.41",
                            "5.11",
                            "4.26",
                            "6.39"
                        ],
                        [
                            "11",
                            "3.75",
                            "5.63",
                            "4.69",
                            "7.03"
                        ],
                        [
                            "12",
                            "4.09",
                            "6.14",
                            "5.11",
                            "7.67"
                        ],
                        [
                            "13",
                            "4.43",
                            "6.65",
                            "5.54",
                            "8.31"
                        ],
                        [
                            "14",
                            "4.77",
                            "7.16",
                            "5.97",
                            "8.95"
                        ],
                        [
                            "15",
                            "5.11",
                            "7.67",
                            "6.39",
                            "9.59"
                        ],
                        [
                            "16",
                            "5.45",
                            "8.18",
                            "6.82",
                            "10.23"
                        ],
                        [
                            "17",
                            "5.80",
                            "8.69",
                            "7.24",
                            "10.87"
                        ],
                        [
                            "18",
                            "6.14",
                            "9.20",
                            "7.67",
                            "11.51"
                        ],
                        [
                            "19",
                            "6.48",
                            "9.72",
                            "8.10",
                            "12.14"
                        ],
                        [
                            "20",
                            "6.82",
                            "10.23",
                            "8.52",
                            "12.78"
                        ],
                        [
                            "21",
                            "7.16",
                            "10.74",
                            "8.95",
                            "13.42"
                        ],
                        [
                            "22",
                            "7.50",
                            "11.25",
                            "9.38",
                            "14.06"
                        ],
                        [
                            "23",
                            "7.84",
                            "11.76",
                            "9.80",
                            "14.70"
                        ],
                        [
                            "24",
                            "8.18",
                            "12.27",
                            "10.23",
                            "15.34"
                        ],
                        [
                            "25",
                            "8.52",
                            "12.78",
                            "10.65",
                            "15.98"
                        ],
                        [
                            "26",
                            "8.86",
                            "13.30",
                            "11.08",
                            "16.62"
                        ],
                        [
                            "27",
                            "9.20",
                            "13.81",
                            "11.51",
                            "17.26"
                        ],
                        [
                            "28",
                            "9.55",
                            "14.32",
                            "11.93",
                            "17.90"
                        ],
                        [
                            "29",
                            "9.89",
                            "14.83",
                            "12.36",
                            "18.54"
                        ],
                        [
                            "30",
                            "10.23",
                            "15.34",
                            "12.78",
                            "19.18"
                        ],
                        [
                            "31",
                            "10.57",
                            "15.85",
                            "13.21",
                            "19.82"
                        ]
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
                    "headers": [
                        "Jump Type",
                        "Formula"
                    ],
                    "rows": [
                        [
                            "Running Long Jump",
                            "Athletics Sum + 10"
                        ],
                        [
                            "Standing Long Jump",
                            "Athletics Sum"
                        ],
                        [
                            "Vertical Jump",
                            "Athletics Sum - 5"
                        ]
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
                    "headers": [
                        "Obstacle",
                        "Movement Modifier"
                    ],
                    "rows": [
                        [
                            "Climbing Tree",
                            "Total x 0.75"
                        ],
                        [
                            "Wall (Grip Points Available)",
                            "Total x 0.50"
                        ],
                        [
                            "Wall (Smooth)",
                            "Total x 0.25"
                        ]
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
                    "headers": [
                        "Terrain",
                        "Movement Modifier"
                    ],
                    "rows": [
                        [
                            "Moderate Undergrowth",
                            "Total x 0.75"
                        ],
                        [
                            "Heavy Undergrowth",
                            "Total x 0.50"
                        ],
                        [
                            "Steep Incline",
                            "Total x 0.75"
                        ],
                        [
                            "Unstable/Slippery Surface (Sand/Mud/Ice)",
                            "Total x 0.75"
                        ],
                        [
                            "Unstable/Slippery Incline Surface",
                            "Total x 0.50"
                        ],
                        [
                            "Waist Deep Swamp/Snow",
                            "Total x 0.25"
                        ]
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
                    "headers": [
                        "Visibility",
                        "Movement Modifier"
                    ],
                    "rows": [
                        [
                            "Lessened Visibility (Light Fog/Dim)",
                            "Total x 0.75"
                        ],
                        [
                            "Low Visibility (Heavy Fog/Darkness)",
                            "Total x 0.50"
                        ],
                        [
                            "Blindness",
                            "Total x 0.25"
                        ]
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
                    "headers": [
                        "Distance Category",
                        "Number of Encounters",
                        "Example Flavor Text"
                    ],
                    "rows": [
                        [
                            "Nearby",
                            "1",
                            "You can see the spires of the old watchtower in the distance, but between here and there, a dense thicket writhes with strange noises."
                        ],
                        [
                            "Short Trip",
                            "1-2",
                            "The sun is high when you come across a cluster of ruins hidden by overgrowth. The air is eerily still. Do you explore or move on? Later, as the town’s gates come into view, a pair of guards halts you, demanding to see your travel permits."
                        ],
                        [
                            "Distant Journey",
                            "2-3",
                            "On the second night, howling wolves circle your camp, their glowing eyes watching from the tree line. By morning, a collapsed bridge blocks your path, leaving you to choose between fording the river or taking a perilous detour through troll-infested woods."
                        ],
                        [
                            "Far-Flung Adventure",
                            "3-5",
                            "Days blend together as your party crosses fields, forests, and mountains. In a small village, an old herbalist begs you to retrieve a stolen amulet, warning of its dark curse. You find an encircled caravan beset by marauding Fel’dren. Do you use the distraction to quietly pass by, or do you lend aid and hope a rescued caravan might offer a reward?"
                        ]
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
                    "headers": [
                        "Object Type",
                        "Difficulty Level (DL)",
                        "Throw Distance Formula"
                    ],
                    "rows": [
                        [
                            "Object Designed for Throwing",
                            "Easy (DL: 15-20)",
                            "Distance = Double (Power)"
                        ],
                        [
                            "Light Weight Object",
                            "Moderate (DL: 21-30)",
                            "Distance = (Power)"
                        ],
                        [
                            "Light Load Object",
                            "Difficult (DL: 31-40)",
                            "Distance = (0.5 x Power)"
                        ],
                        [
                            "Heavy Load Object",
                            "Heroic (DL: 51-60)",
                            "Distance = (0.25 x Power)"
                        ]
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
                    "headers": [
                        "Difficulty Level (DL)",
                        "Action Point Cost",
                        "Example"
                    ],
                    "rows": [
                        [
                            "Easy (DL: 15-20)",
                            "1 Action Point",
                            "Jumping over a minor obstacle or popping a loaded magazine into a gun."
                        ],
                        [
                            "Moderate (DL: 21-30)",
                            "2 Action Points",
                            "Opening an unlocked door or loading a revolver without a speed loader."
                        ],
                        [
                            "Difficult (DL: 31-40)",
                            "3 Action Points",
                            "Picking a pocket or unlocking a door with a key."
                        ]
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
                    "headers": [
                        "Class",
                        "SBHP",
                        "Material Example"
                    ],
                    "rows": [
                        [
                            "SSS Class",
                            "300 SBHP",
                            "Cursed Infernal Alloy or Adamantine"
                        ],
                        [
                            "SS Class",
                            "250 SBHP",
                            "Graphene or Mithril"
                        ],
                        [
                            "S Class",
                            "200 SBHP",
                            "Titanium or Dragon Quenched Steel"
                        ],
                        [
                            "A Class",
                            "150 SBHP",
                            "Metallic Glass or Syntha Ceramics"
                        ],
                        [
                            "B Class",
                            "100 SBHP",
                            "Vanadium 'Krimmerian' Steel or Carbon Fiber"
                        ],
                        [
                            "C Class",
                            "75 SBHP",
                            "Steel, Reinforced Concrete or Dense Stone"
                        ],
                        [
                            "D Class",
                            "50 SBHP",
                            "Dense Plastic or Hard Wood"
                        ],
                        [
                            "F Class",
                            "25 SBHP",
                            "Plastic or Soft Wood"
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Breaking Down Door",
                            "Uncontested Power vs. Door Rating. Attempt every minute."
                        ],
                        [
                            "Breaking Through a Wall",
                            "Uncontested Power vs. Door Rating. Attempt every minute."
                        ],
                        [
                            "Escaping When Tied Up",
                            "Contested Sleight of Hand vs. Security of Trusser. Attempt every six hours."
                        ],
                        [
                            "Jumping from Elevation into Water",
                            "Uncontested Athletics vs. Distance (DL 5 per 5’ / 1.5 m)."
                        ],
                        [
                            "Jumping from a Height",
                            "Uncontested Athletics vs. Distance (DL 10 per 5’ / 1.5 m)."
                        ],
                        [
                            "Jumping onto a Moving Object",
                            "Uncontested Athletics vs. Speed (DL 1 per 1 MPH or 1.5 KPH)."
                        ],
                        [
                            "Jumping from Rooftop to Rooftop",
                            "Uncontested Athletics vs. Distance (DL 10 per 5’ / 1.5 m Leapt)."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Determining the Type of Trap",
                            "Uncontested Analysis vs. DL of Trap."
                        ],
                        [
                            "Determining Technological Function",
                            "Uncontested Analysis + Scholar vs. Complexity Rating."
                        ],
                        [
                            "Determining Arcane Function",
                            "Contested or Uncontested Analysis + Arcane Scholar."
                        ],
                        [
                            "Determining Medical Condition",
                            "Contested or Uncontested Analysis + Medicine."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Weathering a Sandstorm",
                            "Uncontested Bio Control vs. Terrain DL."
                        ],
                        [
                            "Escaping Quicksand",
                            "Uncontested Bio Control vs. Terrain DL."
                        ],
                        [
                            "Holding Your Breath",
                            "Uncontested Bio Control: Duration."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Falling Damage",
                            "2d10 + 2 BHP per 5’ Fallen vs. Soak."
                        ],
                        [
                            "Falling Damage Soft Landing",
                            "1 BHP per 5’ Fallen vs. Soak."
                        ],
                        [
                            "Heat Exhaustion or Hypothermia",
                            "2d10 + Cumulative 5 BHP per 10 Minutes vs. Soak."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Close Proximity to Mild Phobia",
                            "Willpower or Bio Control (DL 10)"
                        ],
                        [
                            "Directly Exposed to Mild Phobia",
                            "Willpower or Bio Control (DL: 15)"
                        ],
                        [
                            "Close Proximity to Severe Phobia",
                            "Willpower or Bio Control (DL: 20)"
                        ],
                        [
                            "Directly Exposed to Severe Phobia",
                            "Willpower or Bio Control (DL: 25)"
                        ],
                        [
                            "Lesser Nightmare Creature",
                            "Willpower or Bio Control (DL: 30)"
                        ],
                        [
                            "Adult Dragon",
                            "Willpower or Bio Control (DL: 35)"
                        ],
                        [
                            "Greater Nightmare Creature",
                            "Willpower or Bio Control (DL: 40)"
                        ],
                        [
                            "Great Ancient Dragon",
                            "Willpower or Bio Control (DL: 45)"
                        ],
                        [
                            "Master Nightmare Creatures",
                            "Willpower or Bio Control (DL: 50)"
                        ],
                        [
                            "An Old One, First Fallen or the Void",
                            "Willpower or Bio Control (DL: 60)"
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Basic Carpentry",
                            "Uncontested Mechanical Repair vs. DL 10."
                        ],
                        [
                            "Basic Electrical",
                            "Uncontested Mechanical Repair vs. DL 15."
                        ],
                        [
                            "Basic Plumbing",
                            "Uncontested Mechanical Repair vs. DL 10."
                        ],
                        [
                            "Basic Welding",
                            "Uncontested Mechanical Repair vs. DL 15."
                        ],
                        [
                            "Changing a Tire",
                            "Uncontested Mechanical Repair vs. DL 10."
                        ],
                        [
                            "Rebuilding an Engine",
                            "Uncontested Mechanical Repair vs. DL 20."
                        ],
                        [
                            "Repairing an Engine",
                            "Uncontested Mechanical Repair vs. Extent of Damage DL."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Broken Bones",
                            "Uncontested Medicine vs. DL 30."
                        ],
                        [
                            "Burns",
                            "Uncontested Medicine vs. DL 10 + Severity."
                        ],
                        [
                            "Heart Attack",
                            "Uncontested Medicine vs. DL 30."
                        ],
                        [
                            "Heat Exhaustion or Hypothermia",
                            "Uncontested Medicine vs. DL 15."
                        ],
                        [
                            "Lodged Object Removal",
                            "Uncontested Medicine vs. DL 20."
                        ],
                        [
                            "Resuscitating a Drowning Victim",
                            "Uncontested Medicine vs. DL # of Rounds Drowning x 5."
                        ],
                        [
                            "Stabilizing",
                            "Uncontested Medicine vs. DL 20."
                        ],
                        [
                            "Stitches, External",
                            "Uncontested Medicine vs. DL 10."
                        ],
                        [
                            "Stitches, Internal",
                            "Uncontested Medicine vs. DL 30."
                        ],
                        [
                            "Tracheotomy",
                            "Uncontested Medicine vs. DL 20."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Navigation With a Map and Compass",
                            "Uncontested Navigation vs. 1/2 Terrain DL."
                        ],
                        [
                            "Navigation Without a Map or Compass",
                            "Uncontested Navigation vs. Terrain DL."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Simple Padlock",
                            "Uncontested Security vs. DL of 20-29."
                        ],
                        [
                            "Moderate Lock",
                            "Uncontested Security vs. DL 30-39."
                        ],
                        [
                            "Complex Lock",
                            "Uncontested Security vs. DL of 40-49."
                        ],
                        [
                            "Masterwork Lock",
                            "Uncontested Security vs. DL of 50-59."
                        ],
                        [
                            "Disabling a Simple Trap",
                            "Uncontested Security vs. DL of 20-29."
                        ],
                        [
                            "Disabling a Moderate Trap",
                            "Uncontested Security vs. DL of 30-39."
                        ],
                        [
                            "Disabling a Complex Trap",
                            "Uncontested Security vs. DL of 40-49."
                        ],
                        [
                            "Disabling a Masterwork Trap",
                            "Uncontested Security vs. DL of 50-59."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Haggling for a Better Deal",
                            "Contested Scrounge vs. Scrounge. (Winning lowers price 20-25%, losing raises price 20-25%.)"
                        ],
                        [
                            "Lying",
                            "2D10 + Performance Sum - Credibility of Lie. (Failure creates a telling behavior, PCs or NPCs may roll Analyze.)"
                        ],
                        [
                            "Passing a Bribe",
                            "Contested Persuasion or Intimidation vs. Willpower. (Exceptionally high/low bribes may modify the roll.)"
                        ],
                        [
                            "Picking Pockets",
                            "Contested Sleight of Hand vs. Awareness."
                        ],
                        [
                            "Running a Scam",
                            "Contested Performance vs. Analyze."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Avoiding Dehydration & Starvation",
                            "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."
                        ],
                        [
                            "Avoiding Hypothermia",
                            "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."
                        ],
                        [
                            "Avoiding Heat Exhaustion",
                            "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."
                        ],
                        [
                            "Building a Shelter Without Supplies",
                            "Uncontested Primal Instinct or Artisan vs. Terrain DL."
                        ],
                        [
                            "Finding Water",
                            "Uncontested Primal Instinct or Scholar Science vs. Terrain DL."
                        ],
                        [
                            "Fishing Without a Rod",
                            "Uncontested Primal Instinct vs. Terrain DL."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Building a Computer",
                            "Uncontested Tech Repair vs. DL 20."
                        ],
                        [
                            "Diffusing a Bomb",
                            "Contested Roll: Demolition vs. Demolition or Security."
                        ],
                        [
                            "Hacking a Network",
                            "Contested Roll: Technical Op vs. Technical Op or Uncontested Roll: Technical Op vs. Security DL."
                        ],
                        [
                            "Hotwiring a Car",
                            "Uncontested Technical Repair vs. DL 20 or Car Security DL."
                        ]
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
                    "headers": [
                        "Scenario",
                        "Check Type"
                    ],
                    "rows": [
                        [
                            "Bad Weather",
                            "Add 10 to 30 DL = Storm Severity."
                        ],
                        [
                            "Piloting",
                            "Aviation, Mecha Operation, or Space Flight."
                        ],
                        [
                            "Riding",
                            "Living Creatures or 1-3 Wheeled/Propulsion Vehicles."
                        ],
                        [
                            "Seafaring",
                            "Vessels that Operate On or Under Liquid."
                        ],
                        [
                            "Vehicles",
                            "Ground-Based Tread or 4+ Wheeled Vehicles."
                        ],
                        [
                            "Transportation Docking",
                            "Uncontested Skill vs. DL 10."
                        ],
                        [
                            "Transportation Takeoff/Touchdown",
                            "Uncontested Skill vs. DL 15."
                        ]
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
                    "headers": [
                        "Type",
                        "DL & Damage Impact"
                    ],
                    "rows": [
                        [
                            "Piloting",
                            "DL 40 to 60 | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Riding",
                            "DL 20 to 40 | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Seafaring",
                            "DL 30 to 70 | 1 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Vehicles",
                            "DL 10 to 60 | 2 BHP per DL in Damage Post Impact."
                        ]
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
                    "headers": [
                        "Type",
                        "DL & Damage Impact"
                    ],
                    "rows": [
                        [
                            "Piloting (Parachute)",
                            "DL 25 | Failure Changes Roll to No Parachute."
                        ],
                        [
                            "Piloting (No Parachute)",
                            "DL 60 | 3 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Riding",
                            "DL 30 to 50 | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Seafaring (Ground)",
                            "DL 30 to 40 | 2 BHP per DL in Damage Post Impact."
                        ]
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
                    "headers": [
                        "Type",
                        "DL & Damage Impact"
                    ],
                    "rows": [
                        [
                            "Slow Speed & Short Fall",
                            "DL 20 to 30 | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Moderate Speed & Short Fall",
                            "DL 30 to 40 | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Fast Speed & Short Fall",
                            "DL 40+ | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Moderate Speed & Moderate Fall",
                            "DL 30 to 40 | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Moderate Speed & Long Fall",
                            "DL 40+ | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Fast Speed & Moderate Fall",
                            "DL 40+ | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Fast Speed & Long Fall",
                            "DL 60+ | 2 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Seafaring (Into Liquid)",
                            "DL 20 to 30 | 1 BHP per DL in Damage Post Impact."
                        ],
                        [
                            "Seafaring (Onto Land)",
                            "DL 20 to 30 | 1 BHP per DL in Damage Post Impact."
                        ]
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
                    "headers": [
                        "Skill",
                        "Associated Ability",
                        "Typical Oppositional Skill"
                    ],
                    "rows": [
                        [
                            "Acrobatics",
                            "Reflexes",
                            "Acrobatics or Difficulty"
                        ],
                        [
                            "Analyzation",
                            "Perception",
                            "Difficulty"
                        ],
                        [
                            "Archery",
                            "Perception",
                            "Dodge"
                        ],
                        [
                            "Artillery",
                            "Perception",
                            "Difficulty"
                        ],
                        [
                            "Artisan",
                            "Intellect",
                            "Difficulty"
                        ],
                        [
                            "Athletics",
                            "Endurance",
                            "Athletics or Difficulty"
                        ],
                        [
                            "Awareness",
                            "Perception",
                            "Difficulty"
                        ],
                        [
                            "Bio Control",
                            "Chakra",
                            "Difficulty"
                        ],
                        [
                            "Cultures",
                            "Perception",
                            "Difficulty"
                        ],
                        [
                            "Demolitions",
                            "Intellect",
                            "Demolitions, Dodge or Difficulty"
                        ],
                        [
                            "Dodge",
                            "Reflexes",
                            "Firearms or Archery"
                        ],
                        [
                            "Exoceric",
                            "Control",
                            "Dodge"
                        ],
                        [
                            "Firearms",
                            "Control",
                            "Dodge"
                        ],
                        [
                            "Gambling",
                            "Control",
                            "Gambling, Sleight of Hand or Difficulty"
                        ],
                        [
                            "Intimidation",
                            "Manipulation",
                            "Willpower"
                        ],
                        [
                            "Linguistics",
                            "Intellect",
                            "Difficulty"
                        ],
                        [
                            "Martial Arts",
                            "Reflexes",
                            "Parry"
                        ],
                        [
                            "Mechanical",
                            "Intellect",
                            "Difficulty"
                        ],
                        [
                            "Medicine",
                            "Intellect",
                            "Difficulty"
                        ],
                        [
                            "Melee (Exoceric)",
                            "Reflexes",
                            "Parry"
                        ],
                        [
                            "Melee (Traditional)",
                            "Reflexes",
                            "Parry"
                        ],
                        [
                            "Navigation",
                            "Intellect",
                            "Difficulty"
                        ],
                        [
                            "Occult",
                            "Intellect",
                            "Varies or Difficulty"
                        ],
                        [
                            "Parry",
                            "Reflexes",
                            "Melee"
                        ],
                        [
                            "Performance",
                            "Manipulation",
                            "Analyzing"
                        ],
                        [
                            "Persuasion",
                            "Manipulation",
                            "Willpower"
                        ],
                        [
                            "Piloting",
                            "Control",
                            "Piloting or Difficulty"
                        ],
                        [
                            "Power",
                            "Strength",
                            "Power or Difficulty"
                        ],
                        [
                            "Primal Instinct",
                            "Perception",
                            "Primal Instinct or Difficulty"
                        ],
                        [
                            "Riding",
                            "Reflexes",
                            "Riding or Difficulty"
                        ],
                        [
                            "Scholar",
                            "Intellect",
                            "Difficulty of Lore"
                        ],
                        [
                            "Scrounge",
                            "Perception",
                            "Scrounge or Difficulty"
                        ],
                        [
                            "Seafaring",
                            "Control",
                            "Sailing or Difficulty"
                        ],
                        [
                            "Security",
                            "Perception",
                            "Security or Difficulty"
                        ],
                        [
                            "Sleight of Hand",
                            "Reflexes",
                            "Awareness"
                        ],
                        [
                            "Stealth",
                            "Control",
                            "Awareness"
                        ],
                        [
                            "Technical",
                            "Intellect",
                            "Tech Op or Difficulty"
                        ],
                        [
                            "Vehicles",
                            "Control",
                            "Vehicle Op or Difficulty"
                        ],
                        [
                            "Willpower",
                            "Control",
                            "Difficulty"
                        ]
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
                    "headers": [
                        "LVL",
                        "Minion Stat Block",
                        "Total Minions"
                    ],
                    "rows": [
                        [
                            "L1",
                            "2 PHP, 1 CHP, 3 in all Abilities and +2 to 3 Non-Combat & +1 to 1 Combat Skill.",
                            "L1"
                        ],
                        [
                            "L2",
                            "2 PHP, 2 CHP, 3 in all Abilities and +2 to 3 Non-Combat & +1 to 1 Combat Skill.",
                            "L1&2"
                        ],
                        [
                            "L3",
                            "3 PHP, 2 CHP, 3 in all Abilities and +3 to 3 Non-Combat & +1 to 2 Combat Skills.",
                            "L1,2&3"
                        ],
                        [
                            "L4",
                            "3 PHP, 3 CHP, 3 in all Abilities and +3 to 3 Non-Combat & +1 to 2 Combat Skills.",
                            "L1,2,3&4"
                        ],
                        [
                            "L5",
                            "4 PHP, 3 CHP, 4 in all Abilities and +4 to 4 Non-Combat & +2 to 2 Combat Skills.",
                            "L1,2,3,4&5"
                        ],
                        [
                            "L6",
                            "4 PHP, 4 CHP, 4 in all Abilities and +4 to 4 Non-Combat & +2 to 2 Combat Skills.",
                            "L1,2,3,4,5&6"
                        ],
                        [
                            "L7",
                            "5 PHP, 4 CHP, 4 in all Abilities and +5 to 4 Non-Combat & +3 to 2 Combat Skills.",
                            "L1,2,3,4,5,6&7"
                        ],
                        [
                            "L8",
                            "5 PHP, 5 CHP, 5 in all Abilities and +5 to 4 Non-Combat & +3 to 2 Combat Skills.",
                            "L1,2,3,4,5,6,7&8"
                        ],
                        [
                            "L9",
                            "6 PHP, 5 CHP, 5 in all Abilities and +6 to 5 Non-Combat & +4 to 2 Combat Skills.",
                            "L1,2,3,4,5,6,7,8&9"
                        ],
                        [
                            "L10",
                            "6 PHP, 6 CHP, 6 in all Abilities and +6 to 5 Non-Combat & +4 to 2 Combat Skills.",
                            "L1,2,3,4,5,6,7,8,9&10"
                        ]
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
                    "headers": [
                        "Difficulty",
                        "Tier Cost"
                    ],
                    "rows": [
                        [
                            "Easy",
                            "2 Tiers"
                        ],
                        [
                            "Moderate",
                            "3 Tiers"
                        ],
                        [
                            "Difficult",
                            "4 Tiers"
                        ],
                        [
                            "Very Difficult",
                            "5 Tiers"
                        ],
                        [
                            "Heroic",
                            "6 Tiers"
                        ],
                        [
                            "Legendary",
                            "8 Tiers"
                        ]
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
                    "headers": [
                        "Difficulty Rating",
                        "Monthly Draw",
                        "Max Loan",
                        "Tiers Reduced",
                        "Interest"
                    ],
                    "rows": [
                        [
                            "Very Easy (DL: 10–14)",
                            "100",
                            "Up to 100,000",
                            "1",
                            "30%"
                        ],
                        [
                            "Easy (DL: 15–24)",
                            "250",
                            "Up to 250,000",
                            "2",
                            "25%"
                        ],
                        [
                            "Moderate (DL: 25–34)",
                            "500",
                            "Up to 500,000",
                            "2",
                            "25%"
                        ],
                        [
                            "Difficult (DL: 35–44)",
                            "1000",
                            "Up to 1,000,000",
                            "3",
                            "20%"
                        ],
                        [
                            "Very Difficult (DL: 45–54)",
                            "5000",
                            "Up to 5,000,000",
                            "3",
                            "20%"
                        ],
                        [
                            "Heroic (DL: 65–74)",
                            "25,000",
                            "Up to 25,000,000",
                            "4",
                            "15%"
                        ],
                        [
                            "Legendary (DL: 75+)",
                            "50,000",
                            "Up to 50,000,000",
                            "4",
                            "10%"
                        ]
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
                    "headers": [
                        "",
                        "Marines / Army",
                        "Navy / Space",
                        "Law Enforcement Agency",
                        "Organized Crime"
                    ],
                    "rows": [
                        [
                            "E1",
                            "Private",
                            "Recruit",
                            "Cadet",
                            "Associate"
                        ],
                        [
                            "E2",
                            "PVT 1st",
                            "Apprentice",
                            "Police Officer",
                            "Soldiers or Assassins"
                        ],
                        [
                            "E3",
                            "Lance Corporal",
                            "Seaman / Specialist",
                            "Detective",
                            "Capo or Captain"
                        ],
                        [
                            "E4",
                            "Corporal",
                            "Petty Officer 3rd Class",
                            "Sergeant",
                            "Operative"
                        ],
                        [
                            "E5",
                            "Sergeant",
                            "Petty Officer 2nd Class",
                            "Lieutenant",
                            "Consigliere or Underboss"
                        ],
                        [
                            "E6",
                            "Staff Sergeant",
                            "Petty Officer 1st Class",
                            "Captain",
                            "Don or Boss"
                        ],
                        [
                            "E7",
                            "Gunnery Sergeant",
                            "Chief",
                            "Commander",
                            "Adjudicator"
                        ],
                        [
                            "E8",
                            "Master Sergeant",
                            "Senior Chief",
                            "Deputy Chief",
                            "The High Table"
                        ],
                        [
                            "E9",
                            "Sergeant Major",
                            "Master Chief",
                            "Chief",
                            "The Elder"
                        ]
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
                    "headers": [
                        "",
                        "Marines / Army",
                        "Navy / Space",
                        "Federal Agency",
                        "Theological Institute"
                    ],
                    "rows": [
                        [
                            "O1",
                            "2nd Lieutenant",
                            "Ensign / Ensign",
                            "Junior Agent",
                            "Deacon"
                        ],
                        [
                            "O2",
                            "1st Lieutenant",
                            "Lt. JG / Lt. JG",
                            "Agent",
                            "Priest"
                        ],
                        [
                            "O3",
                            "Captain",
                            "Lieutenant",
                            "Senior",
                            "Vicar Forane"
                        ],
                        [
                            "O4",
                            "Major",
                            "Lt. Commander",
                            "Specialist / Scientist",
                            "Monsignor"
                        ],
                        [
                            "O5",
                            "Lt. Colonel",
                            "Commander",
                            "Field Supervisor",
                            "Bishop"
                        ],
                        [
                            "O6",
                            "Colonel",
                            "Captain",
                            "Ops Supervisor",
                            "Primate"
                        ],
                        [
                            "O7",
                            "Brigadier General",
                            "Rear Admiral Lower",
                            "Department Head",
                            "Archbishop"
                        ],
                        [
                            "O8",
                            "Major General",
                            "Rear Admiral Upper",
                            "Division Director",
                            "Cardinal"
                        ],
                        [
                            "O9",
                            "Lt. General",
                            "Vice Admiral",
                            "Branch Director",
                            "Patriarchs/Matriarchs"
                        ],
                        [
                            "O10",
                            "General",
                            "Admiral",
                            "Deputy Director",
                            "Pope"
                        ],
                        [
                            "O11",
                            "-",
                            "Fleet Admiral",
                            "Director",
                            "-"
                        ],
                        [
                            "O12",
                            "-",
                            "Grand Admiral",
                            "-",
                            "-"
                        ]
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "data": "You are addicted to a substance that is dangerous to your health. The value of your addiction is based on its cost, availability, and legality."
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "1pt. is addiction to a non-impairing legal substance such as cigarettes or coffee."
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "2pt. is addiction to a moderately impairing but semi-legal substance such as opioids, alcohol, or cannabis."
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "3pt. is addiction to a dangerous impairing illegal substance such as heroin, cocaine, or methamphetamines."
            },
            {
                "type": "subheading",
                "order": 9,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 35,
                "data": "2pt. Bane you’ve been banned from legitimate employment your field of expertise and many closely related fields."
            },
            {
                "type": "paragraph",
                "order": 35,
                "data": "4pt. Bane the character is unemployable at any legit business where personal identification is required."
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 65,
                "data": "2pt. Bane this means you must pay roughly 250 a month or 25% of your revenue, whichever is more and do some odd jobs to pay the interest on what you owe, just to keep the goons from shaking you down and roughing you up a little."
            },
            {
                "type": "paragraph",
                "order": 65,
                "data": "4pt. Bane you’re someone’s bitch, at their beck and call. You’ve found that it doesn’t seem to matter how much you pay, but you’re always behind and they’re more than willing to remind you of that regardless of how many bones it takes."
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 85,
                "data": "2pt. Curse is annoying. It can moderately affects preselected Powers, Techniques, Social Interactions and worse. The effect of your curse can be problematic enough where it tends to mildly damage relationships and subtly lowers the success of your endeavors."
            },
            {
                "type": "paragraph",
                "order": 85,
                "data": "4pt. Curse is potentially deadly. It affects Powers, Techniques, Social Interactions and worse at the Game Masters discretion as the curse is powerful enough to not be contained to a mild incovenience. The effect of your curse can be problematic enough where it tends to or end damage relationships and lowers your success as well as the prosperity of those who keep your company."
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
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
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 115,
                "data": "The trigger for Endless Hunt should be discussed with the GM during character creation. Once the conditions of the hunt are triggered, each week you avoid hunting the target grants a cumulate -1 to all Skill checks until it reaches a -10."
            },
            {
                "type": "paragraph",
                "order": 115,
                "data": "Engaging in the hunt removes the Skill modifiers at the rate of 1 per week. Traveling or seeking out your prey counts as engaging in the hunt. If your target is killed when you are not present then make a DL 35 Willpower Roll, if you fail then the one who stole your kill becomes the new focus of your hunt."
            },
            {
                "type": "heading",
                "order": 116,
                "data": "Fatigued Physique (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 117,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 118,
                "data": "You are painfully out of shape."
            },
            {
                "type": "subheading",
                "order": 119,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 120,
                "data": "Whenever you engage in Athletics Rolls your Endurance score is considered half of its current value rounded up."
            },
            {
                "type": "heading",
                "order": 121,
                "data": "Geas (2pt. or 4pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 122,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 123,
                "data": "You are bound by an oath taken either by yourself or your ancestors that has placed restrictions upon your actions. If you break these restrictions, then you are cursed with a corresponding 2pt. or 4pt. Bane."
            },
            {
                "type": "subheading",
                "order": 124,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 125,
                "data": "2pt. Bane is a restriction requiring you to not engage in something. It could be as simple as service to a cause, the inability to eat pork or celibacy. The exact restriction is determined by the Player and Game Master."
            },
            {
                "type": "paragraph",
                "order": 125,
                "data": "4pt. Bane is a requirement to always engage in something. Every time it is proffered whether prayer to your faith, drinking, sex or seeking approval from a faction head, you must partake."
            },
            {
                "type": "paragraph",
                "order": 125,
                "data": "Breaking the Geas results in it being transformed into a curse of the equivalent point value."
            },
            {
                "type": "heading",
                "order": 126,
                "data": "Glowing Eyes (Kith Daemonkin) (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 127,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 128,
                "data": "There is the night sheen of bestial eyes or other odd traits but your eyes blaze with the infernal energies that gave birth to your kind. You find it difficult to pass as a non-infernal creature and your eyes may cause situational social penalties in the presence of the fearful or superstitious."
            },
            {
                "type": "subheading",
                "order": 129,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 130,
                "data": "You suffer a -2 to all Manipulation Rolls against those who are fearful or superstitious of Daemon or their kin. It also grants a -5 to stealth within 30’ of other creatures while in darkness as their eyes are clearly visible in the distance away."
            },
            {
                "type": "heading",
                "order": 131,
                "data": "Graceless (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 132,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 133,
                "data": "You always look awkward, no matter what you’re doing."
            },
            {
                "type": "subheading",
                "order": 134,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 135,
                "data": "Suffer a -2 to all Acrobatics and Athletics Rolls."
            },
            {
                "type": "heading",
                "order": 136,
                "data": "Hannibal's Hunger (4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 137,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 138,
                "data": "You desire the rarest and most forbidden of delicacies in the form of sentient intelligent creature’s flesh. The flesh is best when harvested personally the longer you go without consuming such the less steady of hand and stable of mind you become."
            },
            {
                "type": "subheading",
                "order": 139,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 140,
                "data": "Each week you avoid consumption grants a cumulate -1 to all Skill checks until it reaches a -10."
            },
            {
                "type": "heading",
                "order": 141,
                "data": "Heavy Sleeper (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 142,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 143,
                "data": "You sleep like the dead. Loud noises and various environmental disturbances are unlikely to arouse you from your slumber unless you have gotten a full 8 hours of sleep. Only if someone physically shakes you or you have gotten a full night’s sleep are you even remotely likely to awaken to the sound of an alarm."
            },
            {
                "type": "subheading",
                "order": 144,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 145,
                "data": "Suffer a -1 to all Perception, Dodge & Initiative Rolls for an hour after waking up or until you’ve had a chance to stimulate yourself such as a cup of coffee or a cold shower."
            },
            {
                "type": "heading",
                "order": 146,
                "data": "Hemophiliac (4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 147,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 148,
                "data": "Your blood is especially thin and the low platelet count in your blood stream requires that your body work harder than normal to close even the most basic of injuries."
            },
            {
                "type": "subheading",
                "order": 149,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 150,
                "data": "After you receive BHP damage you begin to bleed and will continue to do so inflicting 1 SHP Counter per round until your wounds are bound with a Moderate (DL: 30-39) Medicine Roll. If your Counters equal your SHP, then you die."
            },
            {
                "type": "heading",
                "order": 151,
                "data": "Hero Worship (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 152,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 153,
                "data": "You idolize, and we mean absolutely idolize someone. You are prone to angry or violent outbursts if someone questions the motives behind your hero’s actions."
            },
            {
                "type": "subheading",
                "order": 154,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 155,
                "data": "Disobeying them requires a Very Difficult (DL: 50-59) Willpower Roll at a -2 penalty"
            },
            {
                "type": "heading",
                "order": 156,
                "data": "Hunted Down (3pt., 4pt., 5pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 157,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 158,
                "data": "You have made enemies. Unfortunately, the people that you have upset are extremely dangerous and/or influential and have decided to use the resources at their disposal to see you hunted down for your sins and brought to justice. Whether they want you legally punished, broken or killed is up to the GM to decide based on your background and the point value of the Bane."
            },
            {
                "type": "subheading",
                "order": 159,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 160,
                "data": "3pt. Bane you have offended an influential person who is either connected in criminal or political circles who sees that your life is made into a living hell. Your residences will be vandalized, bounty hunters seem to appear bi-annually and people who associate with you seem to be frequently harassed. Those sent to harry you are of equal power and experience while possessing a hostile viewpoint."
            },
            {
                "type": "paragraph",
                "order": 160,
                "data": "4pt. Bane you have made enemies with an organization with vast backing. Assassins and bounty hunters plague you every few months and you have problems settling down within any place that their fingers can reach, while those who would befriend you are always in potential danger. Those sent to harass you possess more power and experience (+25%) and possess a hostile disposition."
            },
            {
                "type": "paragraph",
                "order": 160,
                "data": "5pt. Bane you have made governmental enemies in high places. Your funds may periodically be frozen for periods of time, assassins and bounty hunters plague you every few months and you have problems settling down within any place that their fingers can reach, while those who would befriend you are always in potential danger. Those sent to take your life possess significantly more power and experience (+50%) and possess a hostile disposition."
            },
            {
                "type": "heading",
                "order": 161,
                "data": "Hypoglycemic (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 162,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 163,
                "data": "Your body regularly suffers from low blood sugar, which occurs when your blood glucose (blood sugar) level drops too low to provide enough energy for your body’s activities. To prevent this, you must eat four regular meals a day and have light snacks in between or the inner fatigue begins to affect your actions."
            },
            {
                "type": "subheading",
                "order": 164,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 165,
                "data": "Suffer -1 to all Perception and Control Rolls and are more prone to angry outbursts when you haven’t managed your diet properly."
            },
            {
                "type": "heading",
                "order": 166,
                "data": "Illiterate (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 167,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 168,
                "data": "Normally when you speak a language you automatically read and write it. You have trouble grasping the written word."
            },
            {
                "type": "subheading",
                "order": 169,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 170,
                "data": "You must utilize a second linguistics slot to be proficient in reading and writing a language that you speak."
            },
            {
                "type": "heading",
                "order": 171,
                "data": "Inept (1pt. or 2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 172,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 173,
                "data": "Sometimes there are things in life that no matter how much we try, we are always just horribly bad at."
            },
            {
                "type": "subheading",
                "order": 174,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 175,
                "data": "Choose a Skill which its Base cannot be raised above a 3."
            },
            {
                "type": "paragraph",
                "order": 175,
                "data": "1pt. Bane if it is a Non-Combat related Skill."
            },
            {
                "type": "paragraph",
                "order": 175,
                "data": "2pt. Bane if it is a Combat related Skill."
            },
            {
                "type": "heading",
                "order": 176,
                "data": "Intolerance (2 pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 177,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 178,
                "data": "You hate and/or fear something so much that you seek to either avoid it or remove it at any cost."
            },
            {
                "type": "subheading",
                "order": 179,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 180,
                "data": "Remaining in the presence of your intolerance without acting requires a Very Difficult (DL: 50-59) Willpower Roll. If this roll fails, then you must either leave immediately without explanation OR burst out in tirade against that which you are fanatically against."
            },
            {
                "type": "heading",
                "order": 181,
                "data": "Kirishikk’s Kiss (Lillian) (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 182,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 183,
                "data": "There is no ecstasy in your Embrace - only terror and pain."
            },
            {
                "type": "subheading",
                "order": 184,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 185,
                "data": "Those whom you seek to feed upon struggle and shriek as you attempt to feed, requiring you to maintain a contested grapple with them each round that you consume their blood, even then they cry out loudly unless they are knocked unconscious."
            },
            {
                "type": "heading",
                "order": 186,
                "data": "Low Tolerance (1pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 187,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 188,
                "data": "You cannot seem to handle your liquor or any toxic substance to be honest. The nicest thing they say about you is that you are a lightweight. Everyone understands if you can’t take it, some girls are just born that way."
            },
            {
                "type": "subheading",
                "order": 189,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 190,
                "data": "This Bane gives you a-2 to all Rolls to resist the effects of alcohol or other toxins."
            },
            {
                "type": "heading",
                "order": 191,
                "data": "Loyalty to the Cause (3 pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 192,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 193,
                "data": "You have chosen an organization that you support its ideal and goals 110%. You do not act in a manner that is not in the organization’s best interests and you perceive outsiders to your organization with suspicion and distrust."
            },
            {
                "type": "subheading",
                "order": 194,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 195,
                "data": "You receive -2 to all Cultures, Persuasion and Scrounge Rolls involving those outside of your organization."
            },
            {
                "type": "heading",
                "order": 196,
                "data": "Medication Dependent (2pt. Or 4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 197,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 198,
                "data": "You’ve been sick for a long time, and you need your medicine to get you through the day."
            },
            {
                "type": "subheading",
                "order": 199,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 200,
                "data": "2pt. Dependency requires that you take your medicine daily. Your medicine is common and easily acquired under normal circumstances. If you fail to take your medication, then you are down 2 SHP and suffer a -1 to Athletics and Perception Rolls for the day."
            },
            {
                "type": "paragraph",
                "order": 200,
                "data": "4pt. Dependency requires that you take your medicine daily. Your medicine is uncommon and more expensive. If you fail to take your medication, then you are down 4 SHP and suffer a -3 to Athletics and Perception Rolls for the day."
            },
            {
                "type": "heading",
                "order": 201,
                "data": "Mentally Unstable (4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 202,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 203,
                "data": "Ok, let’s get something clear here. Insane characters are usually poorly played and often screw up a game. Cutesy fluffy stuffed animal concepts do not apply. Sanity and its subsequent loss are scary, so it is up to you: take this Bane and do it justice! Think of Dark Knight™ with Heath Ledger’s performance as the Joker™ or Silence of the Lambs™ with Anthony Hopkin’s performance as Hannibal Lecter™. These people are scary and prone to bursts of insanity or super sanity as some may argue."
            },
            {
                "type": "subheading",
                "order": 204,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 205,
                "data": "This Bane is meant to bring sublime terror to the game and not give players permission to act like a childish idiot. Unless you continually roleplay this condition then, each game session the Game Master can instruct you to act upon your psychosis and inflict appropriate penalties based on the scenario."
            },
            {
                "type": "heading",
                "order": 206,
                "data": "Monologuing (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 207,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 208,
                "data": "You have a problem; you can’t seem to keep your success to yourself. Anytime you have beaten, bested or downed your foes, it seems that you must explain why they failed, why you’re better than them or what you’re going to do now that they are out of the way."
            },
            {
                "type": "subheading",
                "order": 209,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 210,
                "data": "To resist the urge to Monologue requires a Difficult (DL: 40-49) Willpower Roll."
            },
            {
                "type": "heading",
                "order": 211,
                "data": "Motion Sickness (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 212,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 213,
                "data": "You don’t seem to handle motion well; the nausea and disorientation makes all activities difficult for you."
            },
            {
                "type": "subheading",
                "order": 214,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 215,
                "data": "When traveling by train, ship or plane the turbulence you must make a Very Difficult (DL: 50-59) Willpower Roll to move or act. Even if this save is successful you suffer a -2 to all Rolls and -1 traits during and for the first half hour after departing this mode of transportation. You may take medication for this which negates the saving throughs, but it only reduces the penalty by 1."
            },
            {
                "type": "heading",
                "order": 216,
                "data": "Mute (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 217,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 218,
                "data": "Your vocal cords are either damaged or have been removed."
            },
            {
                "type": "subheading",
                "order": 219,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 220,
                "data": "You cannot speak and must use writing or sign language to communicate. This ability does not allow you to use True Magic, but Faith and Psionics are still open to you based on the setting."
            },
            {
                "type": "heading",
                "order": 221,
                "data": "Nailed It (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 222,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 223,
                "data": "You believe in your abilities perhaps a bit more than your abilities believe in you. Once per Scene you may seek to call upon your inner reservoir to attempt to guarantee success or at least your belief in success in a non-combat situation. Regardless of the outcome, you TRULY believe that your crafted item, performance, etc. was the greatest feat of achievement to have ever been created and you cannot be persuaded otherwise."
            },
            {
                "type": "subheading",
                "order": 224,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 225,
                "data": "Before your non-combat related action both you and the Game Master guess what the first 1d10 sum shall be. If you are correct, then you are granted an explosive success die to your roll, if the Game Master is correct then you suffer from a Critical Botch. If both of you are incorrect then you suffer a -1 to your roll."
            },
            {
                "type": "heading",
                "order": 226,
                "data": "Necrotic (Ash’dren) (4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 227,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 228,
                "data": "Your flesh is cool to the touch and while normal injuries may be healed normally each time you are damaged there is a chance when you are struck a serious blow or struck down that the injury required grotesquely visible injury that requires permanent stitches or artificial mechanisms to hold together."
            },
            {
                "type": "subheading",
                "order": 229,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 230,
                "data": "Anytime a single blow strikes you for more than half of your total BHP or if you are knocked below 0 BHP you suffer a garish wound of exposed bone or internal organs requiring either a Moderate Medicine rolls (DL: 25-34) to stitch and mostly conceal or the injury must be held together with artificial mechanisms such as rivets, strap, chains or other binding agents requiring an Easy Artisan roll (DL: 15-24) but this may difficult to conceal depending on the nature of the injury."
            },
            {
                "type": "heading",
                "order": 231,
                "data": "Odd Complexion (Kith) (1pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 232,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 233,
                "data": "Whether infernally marked, obviously elemental, metallic toned, fluffy, furry, patterned, scaled or hairlessly smooth you have a distinctive appearance that is very difficult to conceal. Unless in the company of other Kith or in an area where such are very common this tends to cause situations social issues and associated penalties, especially in smaller less exposed to the outer world communities."
            },
            {
                "type": "subheading",
                "order": 234,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 235,
                "data": "Suffer a -2 in most areas and -4 in extremely isolated ones. Each addition Bane of Permanent Fangs, Horns, Tail, Eyes, Odd Complexion or Odd Eyes increases this penalty by 1. This penalty may be reduced through exposure overtime, but the transition is slow and may take years. It requires a Performance DL: 35 and a makeup kit to conceal your fangs."
            },
            {
                "type": "heading",
                "order": 236,
                "data": "Odd Eyes (Kith) (1pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 237,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 238,
                "data": "Whether your pupils are infernally marked, bestial, rectangular, oval, slitted, or tapetum lucidum, you have distinctive eyes that are very difficult to conceal. Unless in the company of other Kith or in an area where such are very common this tends to cause situations social issues and associated penalties, especially in smaller less exposed to the outer world communities."
            },
            {
                "type": "subheading",
                "order": 239,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 240,
                "data": "Suffer a -2 in most areas and -4 in extremely isolated ones. Each addition Bane of Permanent Fangs, Horns, Tail, Eyes, Odd Complexion or Odd Eyes increases this penalty by 1. This penalty may be reduced through exposure overtime, but the transition is slow and may take years. It requires a Performance DL: 35 and glasses, goggles or other eye covers to conceal your eyes."
            },
            {
                "type": "heading",
                "order": 241,
                "data": "Pansexual (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 242,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 243,
                "data": "Pansexuality is about the heart being open to love without boundaries. Someone who is pansexual may find themselves attracted to a person's spirit and personality, regardless of that person's gender. It's a way of seeing beyond the labels to the individual within. This orientation highlights deep, meaningful connections that are not confined by traditional gender roles. In essence, for pansexual people, love knows no limits."
            },
            {
                "type": "subheading",
                "order": 244,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 245,
                "data": "All creatures are granted their comeliness bonus on social rolls against you as you find all intelligent creatures attractive."
            },
            {
                "type": "heading",
                "order": 246,
                "data": "Partially Deaf (1pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 247,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 248,
                "data": "Your hearing has either been damaged or was weak upon birth."
            },
            {
                "type": "subheading",
                "order": 249,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 250,
                "data": "Suffer a -2 to all Perception Rolls involving hearing."
            },
            {
                "type": "heading",
                "order": 251,
                "data": "Perception: Farsighted (1pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 252,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 253,
                "data": "You were born or suffered head trauma that has cursed you with imperfect vision unless corrected with either glasses or contacts you suffer one effect chosen at character creation:"
            },
            {
                "type": "subheading",
                "order": 254,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 255,
                "data": "Farsighted then you suffer a -2 to all Perception Rolls within 5ft."
            },
            {
                "type": "heading",
                "order": 256,
                "data": "Perception: Nearsighted (1pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 257,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 258,
                "data": "You were born or suffered head trauma that has cursed you with imperfect vision unless corrected with either glasses or contacts you suffer one effect chosen at character creation:"
            },
            {
                "type": "subheading",
                "order": 259,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 260,
                "data": "Nearsighted: Suffer a -2 to all Perception Rolls more than 5ft. Away."
            },
            {
                "type": "heading",
                "order": 261,
                "data": "Perception: One Eye (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 262,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 263,
                "data": "You have lost an eye which affects your field of vision."
            },
            {
                "type": "subheading",
                "order": 264,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 265,
                "data": "Anyone attacking from your bad side receives a +2 to Strike you."
            },
            {
                "type": "heading",
                "order": 266,
                "data": "Permanent Fangs (Kith Chimerian/Daemonkin) (1pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 267,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 268,
                "data": "Your canines are exceptionally long and are barely visible even when your mouth is closed and thus very difficult to conceal. Unless in the company of other Kith or in an area where such are very common this tends to cause situations social issues and associated penalties, especially in smaller less exposed to the outer world communities."
            },
            {
                "type": "subheading",
                "order": 269,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 270,
                "data": "Suffer a -2 in most areas and -4 in extremely isolated ones. Each additional Bane of Permanent Fangs, Horns, Tail, Eyes, Odd Complexion or Odd Eyes increases this penalty by 1. This penalty may be reduced through exposure overtime, but the transition is slow and may take years. It requires a Performance DL: 35 and a makeup kit to conceal your fangs."
            },
            {
                "type": "heading",
                "order": 271,
                "data": "Permanent Horns (Kith Chimerian/Daemonkin) (1pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 272,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 273,
                "data": "You have horns, whether straight or curled they are very difficult to conceal. Unless in the company of other Kith or in an area where such are very common this tends to cause situations social issues and associated penalties, especially in smaller less exposed to the outer world communities."
            },
            {
                "type": "subheading",
                "order": 274,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 275,
                "data": "Suffer a -2 in most areas and -4 in extremely isolated ones. Each addition Bane of Permanent Fangs, Horns, Tail, Eyes, Odd Complexion or Odd Eyes increases this penalty by 1. This penalty may be reduced through exposure overtime, but the transition is slow and may take years. It requires a Stealth DL: 35 to conceal your horns."
            },
            {
                "type": "heading",
                "order": 276,
                "data": "Permanent Tail (Kith Chimerian/Daemonkin) (1pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 277,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 278,
                "data": "Whether fluffy and furry or scaled and smooth you have a long non-prehensile tail that is very difficult to conceal. Unless in the company of other Kith or in an area where such are very common this tends to cause situations social issues and associated penalties, especially in smaller less exposed to the outer world communities."
            },
            {
                "type": "subheading",
                "order": 279,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 280,
                "data": "Suffer a -2 in most areas and -4 in extremely isolated ones. Each addition Bane of Permanent Fangs, Horns, Tail, Eyes, Odd Complexion or Odd Eyes increases this penalty by 1. This penalty may be reduced through exposure overtime, but the transition is slow and may take years. It requires a Stealth DL: 35 to conceal your tail."
            },
            {
                "type": "heading",
                "order": 281,
                "data": "Pervert (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 282,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 283,
                "data": "You are filled with lust and are constantly seeking exposure to all its avarices. You collect dirty pictures, constantly browse the I-NET, and tend to purchase expensive novelty items and collectibles pertaining to your interests."
            },
            {
                "type": "subheading",
                "order": 284,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 285,
                "data": "Suffer a -2 to all Rolls to resist being seduced and you must make a Very Difficult (DL: 40-49) Willpower Roll to avoid purchasing unique items that catch your attention. Furthermore, the GM may randomly subtract finances from your character to represent downtime purchases for your recreational interests."
            },
            {
                "type": "heading",
                "order": 286,
                "data": "Poor Liar (1pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 287,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 288,
                "data": "You’re just not good at deceiving others."
            },
            {
                "type": "subheading",
                "order": 289,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 290,
                "data": "Anytime there is any aspect of untruth is a statement that you make you suffer a -2 to all Persuasion Rolls for the rest of the scene as your presentation presents an air of unbelievably which seems to hurt your credentials."
            },
            {
                "type": "heading",
                "order": 291,
                "data": "Profiled Appearance (1pt.; 2pt.; Or 3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 292,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 293,
                "data": "You share characteristics with a group who is discriminated upon and normal people in the area treat you differently because of who you are. This is a very area dependent Bane."
            },
            {
                "type": "subheading",
                "order": 294,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 295,
                "data": "1pt. Bane: An openly homosexual man in a backwater rural intolerant community that may refuse service or mistreat the individual when the law isn’t around or a right-handed, heterosexual, conservative, white male in a liberal university environment that limits available federal aid, benefits or requires higher scoring accordingly, are both the same level of flaw."
            },
            {
                "type": "paragraph",
                "order": 295,
                "data": "2pt. Bane: The “normal” people around you are constantly watching your every move, making trouble for you when they can get away with it, and otherwise causing you grief. The authorities shake you down on principle, and most 'law abiding' folks won't object to whatever they choose to do to you."
            },
            {
                "type": "paragraph",
                "order": 295,
                "data": "3pt. Bane: A person of different pigmentation, religious preference or caste who is openly ostracized, abused and discriminated against in accordance with the law."
            },
            {
                "type": "heading",
                "order": 296,
                "data": "Property (6pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 297,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 298,
                "data": "You belong to someone or an agency in a nation where ownership of sentient being is still acceptable. Having undergone severe indoctrination, your conditioned behavior prevents individuality."
            },
            {
                "type": "subheading",
                "order": 299,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 300,
                "data": "Operating in a fashion that is against the best interests of your master(s) causes you to receive appropriate penalties as assigned by the GM. Hence, your actions are not your own and should you go against the desires of your owner(s) you willingly accept any punishment regardless of how harsh including corporal punishment, reconditioning or worse. This is a heavy role-playing Bane, and the GM should feel free to severely hinder abusive player."
            },
            {
                "type": "heading",
                "order": 301,
                "data": "Psychological Compulsion (2pt., 4pt. Or 6pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 302,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 303,
                "data": "You are afflicted with a psychological impairment that causes you to irrationally pursue a habit. You choose an obsession:"
            },
            {
                "type": "subheading",
                "order": 304,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 305,
                "data": "2pt. Bane: Leaving calling card, stealing, lying, gambling being a perfectionist or possessing a compulsive disorder. This Bane is worth an additional 2pts. If the nature or severity of your compulsion would require you to follow even through even at the risk of life or limb."
            },
            {
                "type": "paragraph",
                "order": 305,
                "data": "4pt. Bane: Serial killing or equally dangerous acts. This Bane is worth an additional 2pts. If the nature or severity of your compulsion would require you to follow through even at the risk of life or limb."
            },
            {
                "type": "paragraph",
                "order": 305,
                "data": "This must be approved by your storyteller. Any time that you are confronted with your psychological compulsion you must make a Very Difficult (DL: 50-59) Willpower Roll or engage in your mentally afflicted habit."
            },
            {
                "type": "paragraph",
                "order": 305,
                "data": "You receive a penalty based on the severity of the Bane: 2pt. is -4, 4pt. is -8 and 6pt. is -12. This modifier is used in Willpower Rolls to resist engaging in your unusual activity. If a character constantly Rolls to ignore their compulsions, then the GM should force them to buy it off even forcing the player in the hole if necessary."
            },
            {
                "type": "heading",
                "order": 309,
                "data": "Psychotic Ex-Significant Other (1pt., 2pt., Or 4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 310,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 311,
                "data": "One of your lovers from the past has developed or already possessed an obsessive personality."
            },
            {
                "type": "subheading",
                "order": 312,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 313,
                "data": "1pt. Bane: Your Ex is someone who tends to call too often and tends to show up at the most inconvenient of times. Unfortunately, your lingering feelings for them remain, keeping you from just cutting them off completely. They are typically Friendly to Indifferent towards you depending on how you treat them, and they are slightly lesser in power and experience to you (-25%)."
            },
            {
                "type": "paragraph",
                "order": 313,
                "data": "2pt. Bane: Your Ex is someone who tends to attempt to reconnect with you while resenting you for the relationship failing and wants to see you suffer for it. They are typically Neutral to Unfriendly towards you and they are of equal power and experience to you."
            },
            {
                "type": "paragraph",
                "order": 313,
                "data": "4pt. Ex is dangerous and is as likely to set your car on fire in the middle of the night as she is to beg to start going out with her again. Love them or leave them but leaving might have dire consequences. They are typically Hostile towards you, and they are of greater power and experience than you (+25% XP)."
            },
            {
                "type": "heading",
                "order": 314,
                "data": "Rival (1pt., 2pt., or 4pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 315,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 316,
                "data": "Someone in your field of expertise likes to compete with you. While they don’t really wish you dead, they most certainly want to see you fail in a manner than ensures their success. Your Rival should be an XP based equal to your character that varies based on the strength of the rivalry though they should always be a reasonably match and challenge your character in the things you compete for. They will also work behind the scenes to provide themselves with every advantage and edge they can just to see you hang your head in shame at the end of a long day."
            },
            {
                "type": "subheading",
                "order": 317,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 318,
                "data": "1pt. Bane: Your Rival is someone who tends to exuberantly seek one-upmanship and tends to show up at the most inconvenient of times. Whether you take this Rival seriously or not changes whether they are typically Friendly to Indifferent towards you depending on how you treat them, and they are slightly lesser in power and experience to you (-25% XP)."
            },
            {
                "type": "paragraph",
                "order": 318,
                "data": "2pt. Bane: Your Rival is someone who has been had a crossing of interests in the past and resents you for their failure in that endeavor and wants to see you suffer for it. They are typically Neutral to Unfriendly towards you and they are of equal power and experience to you."
            },
            {
                "type": "paragraph",
                "order": 318,
                "data": "4pt. Bane: Your Rival is dangerous and is as likely to set a bomb in your car as they are to gloat at every opportunity that they utilize to show you up. They are typically Hostile towards you, and they are of greater power and experience than you (+25% XP)."
            },
            {
                "type": "heading",
                "order": 319,
                "data": "Scar Tissue (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 320,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 321,
                "data": "You suffer from an old injury. This injury impairs your ability to function as smoothly as you once did."
            },
            {
                "type": "subheading",
                "order": 322,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 323,
                "data": "Suffer -2 penalty on all Athletics, Acrobatics and Dodge Rolls"
            },
            {
                "type": "heading",
                "order": 324,
                "data": "Shadowy Past (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 325,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 326,
                "data": "There are some gaps in your history that makes some a little uncomfortable around you. What is even worse is your tendency to not fill in those gaps. You have a hard time making friends and even your acquaintances often wonder about you."
            },
            {
                "type": "subheading",
                "order": 327,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 328,
                "data": "Suffer -1 to all Manipulation Rolls involving those who are aware of aspects of your past and you are often treated as if you were one Rank lower."
            },
            {
                "type": "heading",
                "order": 329,
                "data": "Sickly (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 330,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 331,
                "data": "You are always pale and often covered in a light sheen of sweat even when you lightly exert yourself."
            },
            {
                "type": "subheading",
                "order": 332,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 333,
                "data": "Suffer -2 to all Athletics & Power Rolls as your weak body often has difficulties dealing with prolonged strain."
            },
            {
                "type": "heading",
                "order": 334,
                "data": "Sleeping with the Enemy (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 335,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 336,
                "data": "You may have a lover, a child, a friend working on the other side of the fence, but regardless of politics you retain a friendly (or more than friendly) relationship. Your close ties to someone on the other side would be regarded as treason by your superiors, and if you are discovered, the penalty may include loss of rank, income, contacts, backers, exile, or imprisonment."
            },
            {
                "type": "subheading",
                "order": 337,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 338,
                "data": "The resulting loss is 9 points of backgrounds. For every background not sacrificed the player is exiled or imprisoned for 1 year."
            },
            {
                "type": "heading",
                "order": 339,
                "data": "Speech Impairment (1pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 340,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 341,
                "data": "You suffer from a speech impediment whether it is mumbling, stuttering, stammering or a lisp."
            },
            {
                "type": "subheading",
                "order": 342,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 343,
                "data": "Suffer -2 on all Persuasion Rolls and should be role-played anytime your character speaks but should not be done in a manner that is offensive to others, especially those who may suffer from real life impairments."
            },
            {
                "type": "heading",
                "order": 344,
                "data": "Sterile (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 345,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 346,
                "data": "Without arcane or alchemical assistance, you cannot reproduce offspring."
            },
            {
                "type": "subheading",
                "order": 347,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 348,
                "data": "You cannot conceive children through normal means, and you also suffer a -2 to Social situations due to social stigma with said condition."
            },
            {
                "type": "heading",
                "order": 349,
                "data": "Surreal (Kith) (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 350,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 351,
                "data": "There is something unnatural about you and it draws the attention of others. Guards may choose to question you or civilians may engage you in random conversations. If someone is randomly picked for an act of inconvenience or nefarious intent then you may rest assured that your presence will be the one that draws their attention."
            },
            {
                "type": "subheading",
                "order": 352,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 353,
                "data": "Whenever the Gamemaster wants to interject this is a free wild card to bring scrutiny to the players activities upon a whim."
            },
            {
                "type": "heading",
                "order": 354,
                "data": "Svar Traditionalist (Svar) (0pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 355,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 356,
                "data": "You are the dwarfiest dwarf who ever held a pick or swung a hammer. Every breath and action you take exudes the time-tested traditions, values, and stereotypes of your people."
            },
            {
                "type": "subheading",
                "order": 357,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 358,
                "data": "This grants you a +2 when dealing with another Svar and a -1 when dealing with non-Svar."
            },
            {
                "type": "heading",
                "order": 359,
                "data": "The Shakes (6pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 360,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 361,
                "data": "When under stress your hands tend to shake. You don’t know why but they always have."
            },
            {
                "type": "subheading",
                "order": 362,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 363,
                "data": "Suffer -2 Traits on all Archery, Firearms, Medicine, Piloting and Repair Rolls unless you’ve had a drink to calm your nerves. You need a drink every hour and suffer the potential effects of alcohol accordingly."
            },
            {
                "type": "heading",
                "order": 364,
                "data": "Twin Link (4pt Bane)"
            },
            {
                "type": "paragraph",
                "order": 365,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 366,
                "data": "You share a psychic spiritual link with one person usually a twin sibling. This is a wonderful feeling of bonding with another person who can truly understand you. The downside to this is that you each suffer the same wounds."
            },
            {
                "type": "subheading",
                "order": 367,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 368,
                "data": "For every 5 BHP of damage after soak, your twin takes 2 BHP of un-soakable damage as well. The upside to this is that you have a heightened awareness of your twin."
            },
            {
                "type": "paragraph",
                "order": 368,
                "data": "On a Very Difficult (DL: 50-59) Awareness Roll you may determine the general direction of your sibling from where you are and your twin has a -10 modifier on all Rolls to lie or misdirect you as you can always feel each other’s emotional state."
            },
            {
                "type": "heading",
                "order": 369,
                "data": "Twisted Heart (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 370,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 371,
                "data": "You lack that natural warmth that helps people accept one another. This sets you apart in the crowd as you tend to find funny what others find disturbing and you are far removed from the normal vibrant warm emotional attachments that others hold dear."
            },
            {
                "type": "subheading",
                "order": 372,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 373,
                "data": "-1 to all non-Intimidation Manipulation Rolls."
            },
            {
                "type": "heading",
                "order": 374,
                "data": "Uncultured (1pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 375,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 376,
                "data": "Even when it comes to basic table manners, your ability to be refined seems to be lacking."
            },
            {
                "type": "subheading",
                "order": 377,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 378,
                "data": "In any Social Roll pertaining to the good use of manners you suffer a -1 penalty."
            },
            {
                "type": "heading",
                "order": 379,
                "data": "Unique Raising (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 380,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 381,
                "data": "You were raised in an isolated community (whether in a governmental social project or merely by strict parents who would not have their child corrupted by the outside world) that has impacted your acceptance of estranged social settings."
            },
            {
                "type": "subheading",
                "order": 382,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 383,
                "data": "You are ill at ease in any social situation that differs from your upbringing and accordingly suffer a -2 to all Social Rolls in such settings."
            },
            {
                "type": "heading",
                "order": 384,
                "data": "Unlucky (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 385,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 386,
                "data": "Some people struggle in life, others a simply unluck. You were born without the same occassional bursts of luck that seems to find others."
            },
            {
                "type": "subheading",
                "order": 387,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 388,
                "data": "Your Luck Expendable Trait Pool is permantly lowered by one."
            },
            {
                "type": "heading",
                "order": 389,
                "data": "Users (3pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 390,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 391,
                "data": "Somewhere down the line through either a desire to help or merely from being too soft hearted you picked up a few leeches. The type of people who say they’re your friend but tend to just take you for everything you’ve got one piece at a time."
            },
            {
                "type": "subheading",
                "order": 392,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 393,
                "data": "At random the GM may utilize part of your resources or basically create little nuances that severely hamper your life based on your willingness to keep supporting these moochers."
            },
            {
                "type": "heading",
                "order": 394,
                "data": "Vulgar Essence (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 395,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 396,
                "data": "Your magic, abilities and skills are always obvious when you utilize or maintain them. It is always noticeable regardless of other skills or abilities that might normally allow you to hide your essence use. All your powers involve loud anime style catch phrases and create majestically stylish images when you cast."
            },
            {
                "type": "subheading",
                "order": 397,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 398,
                "data": "No additional Mechanics."
            },
            {
                "type": "heading",
                "order": 399,
                "data": "Weak Stomach (2pt. Bane)"
            },
            {
                "type": "paragraph",
                "order": 400,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 401,
                "data": "You don’t handle gore very well. Anytime you must deal with blood, wounds or other ghastly injuries you suffer a -1 on all Rolls for the remainder of the scene."
            },
            {
                "type": "subheading",
                "order": 402,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 403,
                "data": "If the GM deems that the scene is disturbing enough then they may ask you to make a Difficult (DL: 40-49) Bio Control Roll to avoid spending the next few rounds retching."
            }
        ]
    },
    {
        "title": "Boons",
        "slug": "boons",
        "chapter": "Banes & Boons",
        "content": [
            {
                "type": "heading",
                "order": 1,
                "data": "Action Hero (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 1,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 1,
                "data": "You are energetic and quick to respond to any situation. You have honed your body and mind to make yourself into a true hero or villain."
            },
            {
                "type": "subheading",
                "order": 1,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 1,
                "data": "Grants +1 Combat Action Point & +1 Movement Action Point."
            },
            {
                "type": "heading",
                "order": 2,
                "data": "Additional Elemental Affinity (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 2,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 3,
                "data": "You are attuned to a wider array of elements than usual and treat 1 additional Element Sphere as if it were in Calling."
            },
            {
                "type": "subheading",
                "order": 4,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 5,
                "data": "This reduces the cost to normal and provides the Calling +4 benefit."
            },
            {
                "type": "heading",
                "order": 6,
                "data": "Alternate Identity (2pt. Or 3pt Boon)"
            },
            {
                "type": "paragraph",
                "order": 7,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "You have managed to build up a solid alternate identity with verifiable backgrounds and credentials. Unlike a normal forged passport or documentation your identity will hold up through extensive background checks and investigations."
            },
            {
                "type": "subheading",
                "order": 9,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "2pt. Boon: Identity will hold up through a Very Difficult (DL: 50-59) Analyzation Roll."
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "3pt. Boon: Identity will require a Heroic (DL: 60-69) Analyzation Roll to pierce its falsified credentials."
            },
            {
                "type": "heading",
                "order": 11,
                "data": "Ambidextrous (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 12,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 13,
                "data": "Most people favor one hand or the other. You may use either hand equally well."
            },
            {
                "type": "subheading",
                "order": 14,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 15,
                "data": "Negates the impairments of offhand use to complete a task and removes striking penalty to Florentine fighting."
            },
            {
                "type": "heading",
                "order": 16,
                "data": "Antecessor (2pt., 3pt. & 4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 17,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 18,
                "data": "You have an ancestor or deceased lover who shadows you and tends to watch over you, especially when you wander into dangerous hauntings."
            },
            {
                "type": "subheading",
                "order": 19,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 20,
                "data": "2pt. Boon: Visions. You receive flashes of insight or visions of harm that may come to your person if you enter a location of substantial danger. At this level, your spiritual guide can only provide such a warning once per game session."
            },
            {
                "type": "paragraph",
                "order": 20,
                "data": "3pt. Boon: Voice. Your antecessor can speak a single short sentence or provide visual clues in the form of ghostly light anomalies. At this level, your spirit guide can only interact twice per game session."
            },
            {
                "type": "paragraph",
                "order": 20,
                "data": "3pt. Boon: Voice. Your antecessor can speak a single short sentence or provide visual clues in the form of ghostly light anomalies. At this level, your spirit guide can only interact twice per game session."
            },
            {
                "type": "paragraph",
                "order": 20,
                "data": "4pt. Boon: Commune. You can have full conversations with your spiritual guide when they are near you and feel they have enough energy to do so. They can see the other side with unique clarity and may advise accordingly. At this level your spirit guide has a 25 percent chance of being present each hour."
            },
            {
                "type": "heading",
                "order": 21,
                "data": "Artemis’ Grace (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 22,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 23,
                "data": "By some natural aptitude or gift of the powers that be you have been blessed with a keen eye and a steady hand. It often seems almost as if the winds shift in your favor and your targets almost step in the path where your arrows fly true."
            },
            {
                "type": "subheading",
                "order": 24,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 25,
                "data": "Grants +1 to all Archery Striking and Damage Rolls."
            },
            {
                "type": "heading",
                "order": 26,
                "data": "Artifact of History (1-3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 27,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 28,
                "data": "You have come into rightful possession of an Artifact of History. This object is beyond the reach of a meager price tag as it is often entangled in history and shrouded in superstition may be of relevance or power. When taking the Artifact Boon, consult with the GM to try and work out an appropriate Artifact is for the setting based on the point value. This Background may be divided into many lesser Artifacts or one powerful Artifact. Anyone who chooses this background must create a feasible story that explains where and how this background was acquired. This background must be approved by the Game Master."
            },
            {
                "type": "subheading",
                "order": 29,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 30,
                "data": "1pt. Boon: Local Importance & Recognizable or Regional Importance & Obscure."
            },
            {
                "type": "paragraph",
                "order": 30,
                "data": "2pt. Boon: Regional Importance & Recognizable or National Important & Obscure."
            },
            {
                "type": "paragraph",
                "order": 30,
                "data": "3pt. Boon: National Importance & Recognizable or Global Importance & Obscure."
            },
            {
                "type": "heading",
                "order": 31,
                "data": "Asexual (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 32,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 33,
                "data": "Asexuality means someone doesn't really feel sexual attraction to anyone. They might still fall in love or form close relationships; they just don't have the desire to make those relationships sexual. They cherish the emotional intimacy and companionship that comes from being close to others. Essentially, it's about loving and being loved in ways that don’t involve a sexual aspect."
            },
            {
                "type": "subheading",
                "order": 34,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 35,
                "data": "Others are not granted their comeliness bonus against you."
            },
            {
                "type": "heading",
                "order": 36,
                "data": "Bestial Affinity (Chimerian)(2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 37,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 38,
                "data": "Blessed by Lumira and descended directly from the Baron, tou are truly attuned to your beast and may take on more bestial characteristics than most."
            },
            {
                "type": "subheading",
                "order": 39,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 40,
                "data": "You may pick an additional characteristic from Reveal the Beast. You may take this Boon repeatedly."
            },
            {
                "type": "heading",
                "order": 41,
                "data": "Berserker (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 42,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 43,
                "data": "A tempest of raw, unbridled fury. You are a warrior embodying the primal wrath of the storm, each howl and roar echoing the chaos of battle. With eyes aflame with the fire of unyielding rage, the berserker wields his weapons with such ferocity that it seems an extension of his very soul. Unconcerned with the finesse of the dance of blades, he plunges headlong into the fray, driven by a singular desire to crush and obliterate, his heart pounding the drumbeat of ancient wars that shall see him to victory or Valhalla."
            },
            {
                "type": "subheading",
                "order": 44,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 45,
                "data": "You can expend an Essence to enter a state of ferocious frenzy. During this moment you must specifically identify those immediately within Line of Sight around you that you are recognizing as “allies”, all other creatures are “enemies”. If these people step between you and all other targets, then they shall also be treated as enemies. Every round you must utilize MAP to engage an “enemy” and expend all CAP on them until they are downed. This process continues until all enemies are felled, the Berserker does not have an enemy within melee or distant attack range, or if the Berserker attempts to end their rage. During their enraged time, they are granted a +2 to Strength Sum, +2 to Endurance Sum. To begin “Winding Down” at the beginning of their turn the Berserker expends an Essence chooses to begin “Winding Down”, at this point they still must utilize all of their MAP and CAP to down enemies but regain control once the last CAP is expended. They also may be healed during this time period. The danger of berserking is that once they are reduced to 0 BHP they may choose to fall unconscious or to continue fighting. If they choose to continue fighting then they gamble their life and can no longer receive healing until the rage has ended. At the start of each initiative, they must expend 2 Essence and successfully make an Athletics Roll with the Difficulty equal to their current negative BHP. Compounding isses they suffer a cumulatic -1 penalty for each additional combat action they take as they continue fighting. If they run out of essence or if they fail their Athletics Roll, they complete their final round of CAP expenditures and fall dead in glorious battle. If all enemies have fallen and they have not failed their Athletics Roll then they may attempt to Wind Down. At the end of their Wind Down they make a final roll with the Difficulty being their negative BHP + Cumulative Penalties. If they pass this, they automatically fall unconscious but are stabilized. If they fail then they perish."
            },
            {
                "type": "heading",
                "order": 46,
                "data": "Blessed of Aphasia (Darkholme) (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 47,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 48,
                "data": "Once upon a time you or a member of your family gained the blessing of Aphasia, and that gift was passed down to you. You are very attractive to people whom you might wish to attract the attention of. While those whose aren’t to your tastes tend to avoid seeking your attention unless they are truly determined. You may not be faithful to any deity except Aphasia as they recognize her mark and respect it."
            },
            {
                "type": "subheading",
                "order": 49,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 50,
                "data": "By spending an essence and declaring a target, you are granted a +2 on Manipulation Social interactions to persuade that individual. You may also expend an essence and declare a target; this requires them to make a Very Difficult DL 41-50 to make social advances towards you as Aphasia fills undesirables with insecurity to protect her blessed. This effect lasts for 1 Hour. You may affect a number of targets equal to your Comeliness."
            },
            {
                "type": "heading",
                "order": 51,
                "data": "Calm Soul (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 52,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 53,
                "data": "You have always been calm of mind and heart which allows you to easily avoid panic and engage in meditation. In situations that require you to maintain outward calmness, a lower heart rate and controlled breathing you maintain your composure quite readily."
            },
            {
                "type": "subheading",
                "order": 54,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 55,
                "data": "Grants +1 to all Bio Control."
            },
            {
                "type": "heading",
                "order": 56,
                "data": "Celestial Navigation (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 57,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 58,
                "data": "Guided by the stars is the maxim you use to describe your innate sense of direction, but the truth is that you have a deep sense of logical direction assisted by an intuitional pull to your desired destination."
            },
            {
                "type": "subheading",
                "order": 59,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 60,
                "data": "Grants +1 to all Navigation and Scholar Geography Rolls."
            },
            {
                "type": "heading",
                "order": 61,
                "data": "Charming Rogue (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 62,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 63,
                "data": "You are a thief, and the lords and ladies love you for your dashing, dastardly, defiance of the law. Of course, being charming may not always be enough, so you’ve developed the skills to take you well on your way to becoming the Prince or Princess of Thieves."
            },
            {
                "type": "subheading",
                "order": 64,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 65,
                "data": "Grants +1 to Acrobatics, Persuasion, Sleight of Hand and Stealth Rolls."
            },
            {
                "type": "heading",
                "order": 66,
                "data": "Child of the Baron (Chimerian) (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 67,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 68,
                "data": "Your personal form is yours to command as biological sex, mass, complexion, and hair color are easily shifted in a few moments. Through expending a essence your flesh ripples and molds itself in one of three ways. Each change requires the expenditure of an essence. You may alter your biological sex between male and female. The two forms have slightly differing facial and build features as chosen at character creation but never differ afterwards. You may adjust your height by up to a foot (30 cm) allowing you to become taller or shorter. You may freely change your hair and skin coloring."
            },
            {
                "type": "subheading",
                "order": 69,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 70,
                "data": "Each of these forms is detected as your true form by normal inspection or arcane means. Though those with a Sharpened Sense of smell may note that aspects of your natural scent carry over to your new form if they have met you and sniffed you in other forms. To do this requires a contested Performance versus Primal Instinct roll."
            },
            {
                "type": "heading",
                "order": 71,
                "data": "Chills (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 72,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 73,
                "data": "You always seem to know when you are being watched. Anytime anyone attempts to observe you, or those whose company you are keeping then you have a chance to sense them."
            },
            {
                "type": "subheading",
                "order": 74,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 75,
                "data": "Observers must make a Contested Roll to avoid you sensing them once every 10 minutes. (2d10 + Awareness vs. 2d10 + Stealth) (Scholar: Arcane v. Stealth)"
            },
            {
                "type": "heading",
                "order": 76,
                "data": "Clearance (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 77,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 78,
                "data": "You must have the Rank background to purchase this, Boon. This can be an extremely dangerous Boon and loss of classified materials can lead to man hunts and death for those who divulge some organizations secrets"
            },
            {
                "type": "subheading",
                "order": 79,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 80,
                "data": "Grants +1 per Rank to all Rolls involving the gathering of classified materials from the organization that you possess rank. A typical Roll to receive classified materials are 2d10 + Manipulation + Rank versus a Difficulty set by the GM based on the secrecy of the information."
            },
            {
                "type": "heading",
                "order": 81,
                "data": "Conviction (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 82,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 83,
                "data": "Some people believe they are hard to break and most of the time they are wrong. You have the determination and most likely the training to not be broken. Upon torture or interrogation, you are the reason they invented that special chamber."
            },
            {
                "type": "subheading",
                "order": 84,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 85,
                "data": "Grants +1 to all Willpower Rolls."
            },
            {
                "type": "heading",
                "order": 86,
                "data": "Crack Shot (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 87,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 88,
                "data": "You are inherently able to predict the movements of your target and adjust your Artillery station’s trajectory accordingly. This intuition matched with the Reflexes necessary to stay on your target allows you to readily mow through enemy targets that get in your way."
            },
            {
                "type": "subheading",
                "order": 89,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 90,
                "data": "Grants +1 to Artillery CAP, Striking and Damage Rolls."
            },
            {
                "type": "heading",
                "order": 91,
                "data": "Curse of Eureka (Female Goblyn or Female Mordron) (5pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 92,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 93,
                "data": "You are a descendant of those chosen by the Old One Eureka when she was released into the world. This blessing also grants the ability to create and potentially build or design infernal machinery, which is a combination of elemental energy and infernal materials. *See Infernal Machinery. The downside is that you are constantly driven to explore, learn and create."
            },
            {
                "type": "subheading",
                "order": 94,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 95,
                "data": "You receive a +1 to Analyze, Artisan, Bio Control, Mechanical, Occult, Scholar, Scrounge, and Willpower. Immediately upon exposure to something new or unexplored in the realms of scientific curiosity, you must make a Difficult Willpower Roll to not investigate. You are bound by the need to improve the world or create those who will. Every week that passes that you spend not inventing, building, or producing the next generation of inventors deteriorates your mind causing you to make a cumulative DC 10 Willpower as you slowly devolve into insanity. Each failure grants you a -1 to Chakra, when your Chakra reaches zero, then you perish as your life force is consumed into the spiraling void of your lost genius. Every week spent inventing, building or produce offspring returns one lost Chakra."
            },
            {
                "type": "paragraph",
                "order": 96,
                "data": "Furthermore, you are held to the Code of the First Inventor, which is biologically imprinted on each inventor and prevents their violation, willful or otherwise. The reason is allegedly known only to the first and they refused to discuss the topic:"
            },
            {
                "type": "list",
                "order": 97,
                "data": [
                    "No invention may cause mass destruction or be combined to cause mass destruction.",
                    "No invention can exceed the destructive output of normal handheld weapons.",
                    "No invention may be used to seduce another against their will.",
                    "Inventions shall be as ethically humane as possible to elementals and preference shall be given to operate in a manner under a premise of consent and/or that minimizes suffering of the entity."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 98,
                "data": "Dangerous When Cornered (Chimerian) (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 99,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 100,
                "data": "An animal is most dangerous when cornered or injured. You reflect that idiom in the most literal of senses."
            },
            {
                "type": "subheading",
                "order": 101,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 102,
                "data": "When flanked, cornered, or reduced to half of your BHP you receive a +2 to Strike and a +2 to Damage."
            },
            {
                "type": "heading",
                "order": 103,
                "data": "Dark Covenant (Dylithar or Daemonkin) (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 104,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 105,
                "data": "Due to strong ancestral ties to Demons and Devils invocations of ancient, profane, and often obscene associations may be used to sway cooperation with such creatures."
            },
            {
                "type": "subheading",
                "order": 106,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 107,
                "data": "Those with this bonus are granted a +2 to all rolls involving occult summoning or social interactions with such creatures and the cost of doing business with such beings is significantly reduced."
            },
            {
                "type": "heading",
                "order": 108,
                "data": "Deadly Aim (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 109,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 110,
                "data": "You understand where to shoot someone to really make it hurt. You understand enough about anatomy and pressure points to inflict insidiously painful wounds on your victims."
            },
            {
                "type": "subheading",
                "order": 111,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 112,
                "data": "Grants +1 to all Archery, Firearms and Thrown (Athletics) Damage Rolls."
            },
            {
                "type": "heading",
                "order": 113,
                "data": "Defensive Nature (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 114,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 115,
                "data": "You are always on guard and prepared for the next incoming attack. You observe and analyze your opponents and deem their most likely method of harming you and react accordingly."
            },
            {
                "type": "subheading",
                "order": 116,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 117,
                "data": "Grants +1 to all Dodge and Parry Rolls."
            },
            {
                "type": "heading",
                "order": 118,
                "data": "Deft Hands (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 119,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 120,
                "data": "You have always been rather smooth at taking things without others noticing. A bit of practice and hard work has made you capable of making items disappear even as they watch."
            },
            {
                "type": "subheading",
                "order": 121,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 122,
                "data": "Grants +1 to all Sleight of Hand Rolls."
            },
            {
                "type": "heading",
                "order": 123,
                "data": "Degree (1pt., 2pt. or 3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 124,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 125,
                "data": "You have attended formal academic training and received a degree of esteem. This Boon allows you to choose the Officer column of the Rank Background without paying double the cost."
            },
            {
                "type": "subheading",
                "order": 126,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 127,
                "data": "1pt. Boon Bachelors: This grants you +1 on all Scholar Rolls."
            },
            {
                "type": "paragraph",
                "order": 128,
                "data": "2pt. Boon Masters: This grants you +1 on all Scholar Rolls and +1 on a selected Skill that represents your area of study at the University."
            },
            {
                "type": "paragraph",
                "order": 129,
                "data": "3pt. Boon Doctorate: This grants you +2 on all Scholar Rolls and +2 on a selected Skill that represents your area of study at the University."
            },
            {
                "type": "heading",
                "order": 130,
                "data": "Discreet Nature (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 131,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 132,
                "data": "You have a talent, regardless of your size, of being able to step back and blend into the background. You know how to remain unnoticed even while others are actively searching for you."
            },
            {
                "type": "subheading",
                "order": 133,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 134,
                "data": "Grants +1 to all Stealth and Sleight of Hand Rolls."
            },
            {
                "type": "heading",
                "order": 135,
                "data": "Divine Aura (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 136,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 137,
                "data": "You must be Faith Sensitive to possess this power. You have been blessed by a healing touch and while this does not let you perform miracles such as curing blindness, disease, and paralysis it does allow you to save lives."
            },
            {
                "type": "subheading",
                "order": 138,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 139,
                "data": "Spend 1 Essence per Target to Activate your aura allowing you to heal those you choose within 10’ for 5 BHP every round for 10 Rounds."
            },
            {
                "type": "heading",
                "order": 140,
                "data": "Double Jointed (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 141,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 142,
                "data": "You may pop your joints in and out of place at will allowing you a great degree of suppleness."
            },
            {
                "type": "subheading",
                "order": 143,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 144,
                "data": "Grants +2 to all Non-Contested Rolls to escape any form of confinement."
            },
            {
                "type": "heading",
                "order": 145,
                "data": "Faint Aura (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 146,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 147,
                "data": "Your aura is rather indistinct."
            },
            {
                "type": "subheading",
                "order": 148,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 149,
                "data": "Attempts to read your aura or track you through arcane means suffer a -2 to all their Rolls."
            },
            {
                "type": "heading",
                "order": 150,
                "data": "Fast Healer (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 151,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 152,
                "data": "Those around you seem to recover faster than most. Whether it’s a minor bruise or a life-threatening injury your chances of recovering quickly and safely are much higher than others."
            },
            {
                "type": "subheading",
                "order": 153,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 154,
                "data": "Grants +2 to all Rolls that involve healing whether naturally recuperating, mystical regenerating through medical assistance."
            },
            {
                "type": "heading",
                "order": 155,
                "data": "Fast Learner (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 156,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 157,
                "data": "You are naturally adept and pick up on things faster than most people. When you apply yourself, you quickly learn faster than your peers and training is often more an act of tedium than a learning experience for you."
            },
            {
                "type": "subheading",
                "order": 158,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 159,
                "data": "The training time required for learning things is cut in half and allows you to train while pursuing other activities."
            },
            {
                "type": "heading",
                "order": 160,
                "data": "Firearms Permit (1pt. Or 2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 161,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 162,
                "data": "You are licensed within certain jurisdictions to always carry a firearm on your person."
            },
            {
                "type": "subheading",
                "order": 163,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 164,
                "data": "1pt. Boon: Permit allows you to carry a small, concealed handgun for personal protection."
            },
            {
                "type": "paragraph",
                "order": 165,
                "data": "2pt. Boon: Permit grants you the authority to carry a firearm in open display while in pursuit of your duties and is most often possessed by law enforcement, bounty hunter, security and private bodyguards. The jurisdiction applies accordingly."
            },
            {
                "type": "heading",
                "order": 166,
                "data": "Firebug (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 167,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 168,
                "data": "Whether it is sheer random destruction or precision demolition, the art of explosives and all that goes boom has always fascinated you. This has led to your choice to (legally or illegally) expand your knowledge in the field of demolition. You are familiar with all basic and many exotic forms of explosives and their associated detonators. You require no roll to identify such components."
            },
            {
                "type": "subheading",
                "order": 169,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 170,
                "data": "Grants +1 to all Demolition Rolls."
            },
            {
                "type": "heading",
                "order": 171,
                "data": "Flirtatious (1pt Boon)"
            },
            {
                "type": "paragraph",
                "order": 172,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 173,
                "data": "You are naturally good at imposing your provocative whims upon others. You know when to speak, when to stay quiet and even when to walk away, merely to wrap someone a little tighter around your finger."
            },
            {
                "type": "subheading",
                "order": 174,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 175,
                "data": "Grants +1 to any Social Roll involving those who might potentially find you attractive."
            },
            {
                "type": "heading",
                "order": 176,
                "data": "Flower Child (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 177,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 178,
                "data": "You were raised in a communal home and often exposed to “better living through chemicals.” While you don’t necessarily advocate such a lifestyle, today it has made your body more tolerant of chemicals."
            },
            {
                "type": "subheading",
                "order": 179,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 180,
                "data": "Grants+1 to all Rolls to resist the effects of toxins and +1 to Scholar Narcotics or Flora/Fauna Rolls."
            },
            {
                "type": "heading",
                "order": 181,
                "data": "Focused Mind (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 182,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 183,
                "data": "You possess the ability to concentrate on arduous tasks and may automatically ignore all negative action modifiers based on outside distractions."
            },
            {
                "type": "subheading",
                "order": 184,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 185,
                "data": "Grants +2 to all Rolls to resist task or spell interruption including counter spells."
            },
            {
                "type": "heading",
                "order": 186,
                "data": "Friends on the Other Side (Daemonkin or Elementalkin (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 187,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 188,
                "data": "Your Contacts and Minions Backgrounds are supernatural in nature. They may be contacted, regardless of your location, by performing a short and concise ritual, unless you are in an areas that specifically prevents this communication."
            },
            {
                "type": "subheading",
                "order": 189,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 190,
                "data": "Perform the brief one-minute ritual and make a Moderate Occult Roll on the Prime Material Plane (DL: 25-34) or a Very Difficult Occult Roll on other Planes of Existence (DL: 35-44). If you succeed you may pass one minutes worth of information to your Contacts and Minions. This may be attempted once per day per category of Contact and Minion."
            },
            {
                "type": "heading",
                "order": 191,
                "data": "Game Master (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 192,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 193,
                "data": "You are the master. You readily perceive and notice trends and mechanics behind all games whether old fashioned card and dice games or MMORPGs. You understand the system well enough where it is often perceived that you either \"must be cheating\" or you are just \"damn lucky\"; in reality you’re simply playing the odds."
            },
            {
                "type": "subheading",
                "order": 194,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 195,
                "data": "Grants +1 to all Gambling and Lying Rolls."
            },
            {
                "type": "heading",
                "order": 196,
                "data": "Hair Trigger (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 197,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 198,
                "data": "Few people understand how to maintain both speed and accuracy. You understand the principles behind speed shooting and how to apply them effectively."
            },
            {
                "type": "subheading",
                "order": 199,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 200,
                "data": "Grants +1 CAP for any actions that require Archery or Firearms Rolls."
            },
            {
                "type": "heading",
                "order": 201,
                "data": "Hand of the Master Mason (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 202,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 203,
                "data": "You have an affinity when it comes to the craft of the artisan. Your sharp eye for detail and artistic sense of balance allows you to create works of wondrous beauty that few craftsmen would willingly compare their work against. Leonardo da Vinci, Claude Monet, Yoshio Okiyama, Salvador Dali, Goro Nyudo Masamune, Phidias, and their peers are those whose works may be compared to that which you craft."
            },
            {
                "type": "subheading",
                "order": 204,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 205,
                "data": "Grants +1 to all Artisan or Scholar: Engineering Rolls."
            },
            {
                "type": "heading",
                "order": 206,
                "data": "Iaijutsu Focus (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 207,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 208,
                "data": "You mind is no longer conscious of the movements of your body. Your ability to Quick Strike is legendary and often feared."
            },
            {
                "type": "subheading",
                "order": 209,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 210,
                "data": "Grants +1 to Initiative Rolls and +1 CAP each round."
            },
            {
                "type": "heading",
                "order": 211,
                "data": "Inquisitor (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 212,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 213,
                "data": "You understand the human spirit and exactly what it takes to break it. Through physical torture or threatening innuendo your victims quickly fall prey to your psychological predations."
            },
            {
                "type": "subheading",
                "order": 214,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 215,
                "data": "Grants +1 to all Intimidation & Scholar: Law Rolls."
            },
            {
                "type": "heading",
                "order": 216,
                "data": "Irish Descent (1pt. Boons)"
            },
            {
                "type": "paragraph",
                "order": 217,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 218,
                "data": "Some can drink but others can really drink. You can kill another man who tries to keep up with you at the boozing table."
            },
            {
                "type": "subheading",
                "order": 219,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 220,
                "data": "Grants +1 to all Endurance Rolls to resist the effects of toxins."
            },
            {
                "type": "heading",
                "order": 221,
                "data": "Jack of All Trades (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 222,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 223,
                "data": "You are a Jack of All Trades yet Master of None."
            },
            {
                "type": "subheading",
                "order": 224,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 225,
                "data": "Grants +2 to all Skill Rolls that you do not already possess a 5 Base Score or higher."
            },
            {
                "type": "heading",
                "order": 226,
                "data": "Kensai (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 227,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 228,
                "data": "Sword Saint is the true meaning of Kensai, though this title may be shared by any who possess mastery over the weapons of their choosing."
            },
            {
                "type": "subheading",
                "order": 229,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 230,
                "data": "Grants +2 to both Striking and Damage to a specific weapon-type (Crushing, Energy, Piercing, Slashing) chosen by the Kensai and grants a +1 to other weapons."
            },
            {
                "type": "heading",
                "order": 231,
                "data": "Kiss of Ashia (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 232,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 233,
                "data": "You age less quickly than others of your species. Whether through genetic manipulation, arcane intervention or ancestral blessing."
            },
            {
                "type": "subheading",
                "order": 234,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 235,
                "data": "The window of time for each of your species' natural age groups of Child, Adult, Middle Aged and Elder is doubled."
            },
            {
                "type": "heading",
                "order": 236,
                "data": "Leaf Upon the Wind (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 237,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 238,
                "data": "You fly by skill, intuition, and the grace of God. There are few turbulent or unusual circumstances that you cannot at the very least bring the craft to a reasonably safe and secure landing."
            },
            {
                "type": "subheading",
                "order": 239,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 240,
                "data": "Grants +1 to all Piloting Rolls."
            },
            {
                "type": "heading",
                "order": 241,
                "data": "Licensed to Kill (6pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 242,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 243,
                "data": "You are sanctioned by an agency whose clearance will allow you to eliminate those whose interests run against your agency and is endorsed within reason by the government. This permission comes with a cost. While oft times you are granted a deal of discretion in eliminating threats, you will be periodically called upon to eliminate targets of the agency itself. Few governmental positions grant this power and they monitor its trustees well. They tend to cover up all sanctioned hits and assist in removing evidence in discretionary kills, if the licensee is not exceptionally sloppy. You can still be held accountable by the law for the murder of innocent civilians."
            },
            {
                "type": "subheading",
                "order": 244,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 245,
                "data": "Those who alienate themselves from the agency lose the benefits of sanctioned murder within hours of their termination or resignation."
            },
            {
                "type": "heading",
                "order": 246,
                "data": "Lightning Fast (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 247,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 248,
                "data": "You are quick and light on your feet. Few people escape you in games of pursuit and fewer still can keep up with you. This Boon allows advanced movement speeds."
            },
            {
                "type": "subheading",
                "order": 249,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 250,
                "data": "Receive an additional 1 MAP per 2 Mastery Levels."
            },
            {
                "type": "heading",
                "order": 251,
                "data": "Lila’s Blessing (Lillian) (6pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 252,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 253,
                "data": "By expending a single essence your flesh ripples and molds itself to your will. You may create several alternate forms limited only by the types of humanoids that you have consumed and your dedication to mastery of the path of Lila. These forms are not divinable as anything but your true form through normal inspection or arcane means."
            },
            {
                "type": "subheading",
                "order": 254,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 255,
                "data": "You may create a number of alternate forms equal to your Performance Sum. You must have consumed the essence of a specific creature type to be able to assume their species' form. I.e. to create a Faeyr form you must have fed off of a Faeyr. Those with a Sharpened Sense of smell may note that aspects of your natural scent carry over to your new form, if they have met you and sniffed you in other forms. To do this requires a contested Performance versus Primal Instinct roll. A player may select their forms at creation, or during play, but doing so during play requires the expenditure of 10 Action Points and the character must have fed upon the target species during that game. The player should keep a log of all of their forms and how they have been used. These selected forms are generally permanent but by expending 2 experience points a form may be discarded to create room for a new form."
            },
            {
                "type": "heading",
                "order": 256,
                "data": "Longevity (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 257,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 258,
                "data": "Some people are genetically prone to live long lives beyond the swiftly ageing mien of others of their species. You are one such being."
            },
            {
                "type": "subheading",
                "order": 259,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 260,
                "data": "Your lifespan is now 1.5 times that of others of your species and you are always treated as one age category younger right until your death."
            },
            {
                "type": "heading",
                "order": 261,
                "data": "Lucky (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 262,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 263,
                "data": "The stars aligned when you were born and you were fated to more readily avoid a series of misfortunate events than others."
            },
            {
                "type": "subheading",
                "order": 264,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 265,
                "data": "You Luck Pool is 1 higher than its normal maximum."
            },
            {
                "type": "heading",
                "order": 266,
                "data": "Lumira's Gift (Kith Chimerian) (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 267,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 268,
                "data": "A bestial figure, endowed with a formidable physique and animalistic instincts, prowls through the urban and wilds with unrivaled ferocity. Natural weapons hint at your predatory nature. Marked by a rugged feral visage, your eyes gleam with a savage intelligence, constantly on the hunt, always ready to pounce on any threat or prey that crosses you. Your presence alone commands respect and fear."
            },
            {
                "type": "subheading",
                "order": 269,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 270,
                "data": "You receive all the bonuses of your beast form without having to shift to it. You possess naturally feral features and you’re granted +1 to all Awareness, Initiative, Power, Intimidation rolls."
            },
            {
                "type": "heading",
                "order": 271,
                "data": "Master of Anatomy (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 272,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 273,
                "data": "You have spent years studying the human body and the physiological aspects of all living things. This has led to a greater understanding of the body and how to both heal and harm it."
            },
            {
                "type": "subheading",
                "order": 274,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 275,
                "data": "Grants +2 to all Medicine and Damage Rolls."
            },
            {
                "type": "heading",
                "order": 276,
                "data": "Master Operator (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 277,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 278,
                "data": "You speak the language of machines, literally or figuratively. Whether operating a Mecha or a computer terminal, you find performing tasks with technology to be easier than most."
            },
            {
                "type": "subheading",
                "order": 279,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 280,
                "data": "Grants +1 to all Technical Repair and Tech Operation Rolls."
            },
            {
                "type": "heading",
                "order": 281,
                "data": "Matchstick Man (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 282,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 283,
                "data": "Even as a child you had a way with words and convincing others to do as you wish. Much like Tom Sawyer, you can make the most tedious of tasks seem interesting and persuade others to perform them even against their best interests."
            },
            {
                "type": "subheading",
                "order": 284,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 285,
                "data": "Grants +1 to all Persuasion Rolls."
            },
            {
                "type": "heading",
                "order": 286,
                "data": "Mr. Fixit (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 287,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 288,
                "data": "Some people think they are special or elite because they can operate a machine, but only someone who truly understand machinery can fix the problems and not the symptoms. You are one of those people."
            },
            {
                "type": "subheading",
                "order": 289,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 290,
                "data": "Grants +2 to all Mechanical rolls."
            },
            {
                "type": "heading",
                "order": 291,
                "data": "Mystic Knowledge (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 292,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 293,
                "data": "You were either reared with a strong foundation of hearth lore and belief in the occult or some drastic moment in your life drove you to seek out and research that which cannot be understood. Regardless, you now possess a practical working occult knowledge base that assists you in seeking out the universe’s mystic little secrets."
            },
            {
                "type": "subheading",
                "order": 294,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 295,
                "data": "Grants +2 to all Occult Rolls."
            },
            {
                "type": "heading",
                "order": 296,
                "data": "Natural Athlete (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 297,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 298,
                "data": "Whether through rare genetics or refined breeding you possess the body of a natural athlete. You are quick, graceful, and strong in the areas of tumbling, running, climbing, jumping and swimming."
            },
            {
                "type": "subheading",
                "order": 299,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 300,
                "data": "Grants +1 to all Acrobatic and Athletics Rolls."
            },
            {
                "type": "heading",
                "order": 301,
                "data": "Natural Cartographer (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 302,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 303,
                "data": "You can always seem to find your way back to someplace you have been before. Also, you are astute at giving directions on how to get somewhere."
            },
            {
                "type": "subheading",
                "order": 304,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 305,
                "data": "Regardless of how twisted the path may become you can always trace your way back to some place you have already been unless it has physically moved."
            },
            {
                "type": "heading",
                "order": 306,
                "data": "Natural Linguist (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 307,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 308,
                "data": "You have come to recognize the universal traits of language. You claim a strong familiarity with more languages than most and are able to readily adapt and translate languages that you are unfamiliar with."
            },
            {
                "type": "subheading",
                "order": 309,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 310,
                "data": "Grants +1 to all Linguistic Rolls and doubles the number of languages naturally spoken."
            },
            {
                "type": "heading",
                "order": 324,
                "data": "Natural Predator (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 325,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 326,
                "data": "You are in touch with your inner beast. Animals understand your place in the natural order of things and more readily submit to your dominance."
            },
            {
                "type": "subheading",
                "order": 327,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 328,
                "data": "Grants +1 to all Primal Instinct and Intimidation Rolls."
            },
            {
                "type": "heading",
                "order": 329,
                "data": "Not Completely Inhuman (Devourer) (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 330,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 331,
                "data": "You have adapted, and your tentacles no longer cover or surround your mouth. Instead, the tentacles rest upon your scalp almost like a medusa’s serpents. They may be easily stylized, concealed, or hidden. You have a normal human mouth, though you still do not have a traditional human nose."
            },
            {
                "type": "subheading",
                "order": 332,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 333,
                "data": "It takes a Very Difficult (DL: 45) Analyze roll to determine that you are a Devourer and not an Elemental Kith."
            },
            {
                "type": "heading",
                "order": 334,
                "data": "Oathsworn (Templar/Dark Templar) (4 pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 335,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 336,
                "data": "You have sworn an oath and forces either divine or infernal have taken heed. In exchange you are granted additional power for as long as you uphold your oath. Those who are oath sworn are known as Paladins. Each Oath has four tenets that must be upheld, those who break their tenets are cast out and known as an Oathbreaker."
            },
            {
                "type": "subheading",
                "order": 337,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 338,
                "data": "Varies per Oath."
            },
            {
                "type": "heading",
                "order": 339,
                "data": "Oath: Chivalry"
            },
            {
                "type": "paragraph",
                "order": 340,
                "data": "An oath that binds one to higher standards of conduct and appearance. Courtly etiquette binds your behavior as you shall act with honor in pursuit of noblesse oblige while seeking to hold the rest of the world to that standard."
            },
            {
                "type": "list",
                "order": 341,
                "data": [
                    "Prowess: You do not shy from conflict and show bravery, strength, skill and the wisdom to know when to engage.",
                    "Compassion: You defend the innocent, respect the opposite sex, exemplify generosity and loyalty to your friends, family and liege.",
                    "Mercy: You accept sincere surrender and will take them into custody.",
                    "Fearless: Your life is less than the greater good and you shall not forsake it for your own preservation."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 342,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 343,
                "data": "You receive a +1 to Cultures, Melee, Riding and Athletics. Against Fear you receive a +10 to avoid the repercussions."
            },
            {
                "type": "heading",
                "order": 344,
                "data": "Oath: Divine"
            },
            {
                "type": "paragraph",
                "order": 345,
                "data": "You have an oath with a specific deity, infernal, celestial, or old one whom you represent their path. You seek to expand their dominion and obtain their desires. Mortal needs matter little because you are fueled by a higher purpose."
            },
            {
                "type": "list",
                "order": 346,
                "data": [
                    "Vigilance: You are ever on the lookout for opposition that needs crushed or support that needs nurtured to expand the domain of your benefactor.",
                    "Fearless: Your life is less than the greater good and you shall not forsake it for your own preservation.",
                    "Prowess: You do not shy from conflict and show bravery, strength, skill and the wisdom to know when to engage.",
                    "Loyalty: You serve and unwaveringly carry out their commands."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 347,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 348,
                "data": "You receive a +1 to Bio Control, Melee, Parry and Scholar: Theology Religion. Furthermore, you are blessed with a +1 to an Ability Score of your choosing as you are favored by the powers that be."
            },
            {
                "type": "heading",
                "order": 349,
                "data": "Oath: Fealty"
            },
            {
                "type": "paragraph",
                "order": 350,
                "data": "Fealty and seeking to uphold the interests of that allegiance is the core principle of your path. You are their knight, and you behave accordingly as you represent both them and their decrees. Some may not see the nobility of such a path but everyone who shines in the light must have a hand that is willing to reach into the muck for them."
            },
            {
                "type": "list",
                "order": 351,
                "data": [
                    "Loyalty: You choose a regent with higher Legacy and Rank than your own to serve and unwaveringly carry out their commands.",
                    "Duty: You deal with the consequences and fallout of the commands you follow.",
                    "Respect: You command respect for your regent and will guard their honor from being besmirched.",
                    "Discipline: You are your regent’s shield, and your blade must be forever sharp and ready to act in their name."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 352,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 353,
                "data": "You receive a +1 to Intimidation, Persuasion, Melee, and Willpower. Additionally, you receive +2 modifier to CAP, MAP and CHP."
            },
            {
                "type": "heading",
                "order": 354,
                "data": "Oath: Revenge"
            },
            {
                "type": "paragraph",
                "order": 355,
                "data": "A solemn oath to punish those whose existence is a grievous sin. Whether this is a nation, organization, culture, guild or more ambiguous classifications such as celestials, chimeric, curses, draconic, elemental, faeyr, humans, infernal, monsters, old ones, romlings, svar or undying creatures you shall not rest until they are scourged from the realm."
            },
            {
                "type": "list",
                "order": 356,
                "data": [
                    "Fight the Good Fight: You always seek to destroy those you’ve sworn vengeance against before all other enemies.",
                    "No Mercy: You do not accept the surrender of those you’ve sworn vengeance against.",
                    "Dirty Tactics: Use any means at your disposal to destroy your sworn enemies without remorse or regret.",
                    "Right the Wrong: Pay for damages caused by your sworn foes that were caused by your tactics."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 357,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 358,
                "data": "You receive a +1 to Archery, Melee, Martial Arts and Power. Also, you inflict 5 additional BHP of damage against those you have a sworn enmity with."
            },
            {
                "type": "heading",
                "order": 359,
                "data": "Oathbroken"
            },
            {
                "type": "paragraph",
                "order": 360,
                "data": "You have broken your oath and lost part of the blessings associated with it."
            },
            {
                "type": "subheading",
                "order": 361,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 362,
                "data": "You no longer are bound by tenets, but you now only receive the skill bonus of your previous oath and receive a -2 on all Social Rolls involving Oathsworn. It is possible to redeem yourself or take up a new oath, but this should be an arduous path as few trusts an Oathbreaker."
            },
            {
                "type": "heading",
                "order": 363,
                "data": "Oh! So You Know… (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 364,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 365,
                "data": "You know people and if you don’t know people then you know people they know and you do love to name drop and share stories to ensure your acceptance in society."
            },
            {
                "type": "subheading",
                "order": 366,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 367,
                "data": "Once per Session you may reroll a failed social roll with a NPC as you bring up a mutual acquaintance and a short tale to establish a moment of fellowship with the individual."
            },
            {
                "type": "heading",
                "order": 368,
                "data": "Ornery Sumnabitch (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 369,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 370,
                "data": "You tend to have a coarse side that is built upon a solid set of convictions and beliefs. You know what is right and what is wrong, and you have no problems acting rude, crude, cruel and unsophisticated to any asinine individual who deserves it."
            },
            {
                "type": "subheading",
                "order": 371,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 372,
                "data": "Grants +1 all Intimidation, Firearms or Melee, Martial Arts, Power, Primal Instincts and Athletics Rolls. In contrast though this belligerent nature which allows you to carry on when others would have failed also give you a -1 to all Persuasion and Cultures Rolls."
            },
            {
                "type": "heading",
                "order": 373,
                "data": "Powerhouse (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 374,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 375,
                "data": "You are insanely strong and often accidentally break things when angered. Whether through good genetics or a great workout ethic you have the strength to make others step back and take notice."
            },
            {
                "type": "subheading",
                "order": 376,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 377,
                "data": "Grants +1 to all Power and Intimidation Rolls. You are also granted +1 to all Melee or Martial Arts Damage Rolls. If your Strength is above a 5 then you may wield a 2-Handed Weapon in 1 Hand."
            },
            {
                "type": "heading",
                "order": 378,
                "data": "Prehensile Tail (Requires a Tail) (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 379,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 380,
                "data": "You can control your tail with a great degree of accuracy. In many ways it functions like a third hand, allowing you to pick up and manipulate small objects."
            },
            {
                "type": "subheading",
                "order": 381,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 382,
                "data": "In general, it may be utilized for any non-combat associated Skill."
            },
            {
                "type": "heading",
                "order": 383,
                "data": "Punctual (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 384,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 385,
                "data": "You are obsessed with being on time. Your punctuality is a great boon in maintaining both your professional and adventurous life."
            },
            {
                "type": "subheading",
                "order": 386,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 387,
                "data": "Basically, this Boon ensures that you will arrive on time at all pre-planned meetings and appointments. The only exception to this guideline is if the player chooses to engage in activities that are highly likely to prevent their attendance or if they choose not to attend their pre-arranged plans."
            },
            {
                "type": "heading",
                "order": 388,
                "data": "Ranger (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 389,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 390,
                "data": "You are at home in the wild and you understand it almost as well as it understands you."
            },
            {
                "type": "subheading",
                "order": 391,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 392,
                "data": "Grants+1 to all Archery Striking, Archery Damage, Awareness, and Primal Instinct Rolls."
            },
            {
                "type": "heading",
                "order": 393,
                "data": "Riding Sense (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 394,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 395,
                "data": "You are sharply attuned to animals, surrounding landscape and the subtle changes in your mount’s gait, allowing you to shift your position to avoid being thrown. You inherently know the desires and condition of your mount and adjust your riding style accordingly. This allows you to work well under almost any circumstance and any environment; these skills may even be used with a motorcycle."
            },
            {
                "type": "subheading",
                "order": 396,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 397,
                "data": "Grants +1 to all Riding Rolls."
            },
            {
                "type": "heading",
                "order": 398,
                "data": "Scientific Mind (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 399,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 400,
                "data": "The realms of science and understanding it comes easily to you. Whereas many stumble over basic principles, the complexes inner workings of the scientific community form the cornerstones of your thought processes."
            },
            {
                "type": "subheading",
                "order": 401,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 402,
                "data": "Grants +1 to two selected Science Scholars Rolls."
            },
            {
                "type": "heading",
                "order": 403,
                "data": "Seasoned Street Rat (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 404,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 405,
                "data": "You have been there and done that and probably in several different countries. You understand how the streets generally work and where to go to acquire necessary survival tools of the trade."
            },
            {
                "type": "subheading",
                "order": 406,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 407,
                "data": "Grants +1 to all Culture & Scholar: Guild or Criminal Organizations."
            },
            {
                "type": "heading",
                "order": 408,
                "data": "Scout (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 409,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 410,
                "data": "You have made a lifetime career out of surveying and running messages between cut off destinations. These skills make you an asset and an often highly paid individual."
            },
            {
                "type": "subheading",
                "order": 411,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 412,
                "data": "Grants +1 to all Bio Control, Navigation, Athletics and Stealth Rolls."
            },
            {
                "type": "heading",
                "order": 413,
                "data": "Sharpened Sense (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 414,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 415,
                "data": "One of your senses is exceptionally sharp. You choose one of the basic senses of touch, sight, smell, hearing or taste."
            },
            {
                "type": "subheading",
                "order": 416,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 417,
                "data": "Grants +1 to all Rolls involving your selected sense. This Boon may be purchased multiple times."
            },
            {
                "type": "heading",
                "order": 418,
                "data": "Sharpshooter (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 419,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 420,
                "data": "Pipping the ace. It’s what you do, and your accuracy is unquestionable. Whether through a naturally sharp eye or regular practice you have honed your ranged combat skills with a firearm."
            },
            {
                "type": "subheading",
                "order": 421,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 422,
                "data": "Grants +1 to all Firearms & Firearms (Energy) Striking and Damage Rolls."
            },
            {
                "type": "heading",
                "order": 423,
                "data": "Silent Killer (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 424,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 425,
                "data": "You are well versed in the skills of assassination. Killing comes as naturally as breathing and some nights mayhap a little more so."
            },
            {
                "type": "subheading",
                "order": 426,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 427,
                "data": "Grants +2 to all Stealth Rolls. Spend 1 Essence: Declare technique or regular attack and add 10 BHP damage to an attack."
            },
            {
                "type": "heading",
                "order": 428,
                "data": "Silent Running (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 429,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 430,
                "data": "Some must move very slowly to avoid being detected. You have mastered the art of swiftly but silently crossing the rice paper without making your passage noticeable."
            },
            {
                "type": "subheading",
                "order": 431,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 432,
                "data": "You may move at your normal speed while stealthed."
            },
            {
                "type": "heading",
                "order": 433,
                "data": "Sixth Sense (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 434,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 435,
                "data": "To many, it seems as if you possess a 6th sense that allows you to see the futur, as you are often aware of things before they occur. In truth you have honed your naturally sharp senses to the point where, through casual observations, you notice minute details that often elude others. Simply by looking around, listening, smelling, or touching your environment, you become difficult to surprise or hide things from."
            },
            {
                "type": "subheading",
                "order": 436,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 437,
                "data": "Grants +1 to all Awareness & Primal Instinct Rolls."
            },
            {
                "type": "heading",
                "order": 438,
                "data": "Slayer (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 439,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 440,
                "data": "You don’t go hunting, you go killing. Your entire life has been spent dedicated towards the extermination of others. You have mastered several skills that help prevent your prey from escaping and several more to ensure that you can finish the job once they’re cornered."
            },
            {
                "type": "subheading",
                "order": 441,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 442,
                "data": "Grants +1 to all Awareness, Athletics, Melee Striking and Melee Damage Rolls."
            },
            {
                "type": "heading",
                "order": 443,
                "data": "Sleuth (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 444,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 445,
                "data": "Your attention to detail is keen and you quickly note that which does not belong somewhere. This enables you to quickly shift through the facts and arrive at a conclusion."
            },
            {
                "type": "subheading",
                "order": 446,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 447,
                "data": "Grants +1 to all Awareness & Analyze Rolls."
            },
            {
                "type": "heading",
                "order": 448,
                "data": "Species Similarity (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 449,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 450,
                "data": "You can “pass” for a member of another similar species chosen at character creation. Under any circumstance but the deepest of up-close scrutiny as you are generally indistinguishable from normal members of that species."
            },
            {
                "type": "subheading",
                "order": 451,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 452,
                "data": "It requires a DL 40 Analysis Roll within 5 ft. to determine something is amiss. If you have makeup or surgery, then you may add your Performance sum to this DL to prevent detection."
            },
            {
                "type": "heading",
                "order": 453,
                "data": "Stone Gaze (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 454,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 455,
                "data": "The intensity of your gaze often makes others uneasy as if their secrets are being peeled away layer by layer."
            },
            {
                "type": "subheading",
                "order": 456,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 457,
                "data": "All rolls to deceive you suffer a -2 penalty and the Credibility of a Lie now requires the Roll to be greater than 30 for there to be behavior as they are more prone to exhibit nervous behavior under your steely gaze."
            },
            {
                "type": "heading",
                "order": 458,
                "data": "Stonewall (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 459,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 460,
                "data": "Some describe you as a mountain. You are difficult to move and even more difficult to hurt. The only time someone makes you get out of their way if when you’re ready to move."
            },
            {
                "type": "subheading",
                "order": 461,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 462,
                "data": "This Boon doubles your weight for any attempts of others to move you. If someone can throw you it also grants you +1 to any Strength related Rolls that involve being thrown or throwing others. Finally, it grants you +5 to all Soak & +3 to Unsoakable Damage Absorbtion."
            },
            {
                "type": "heading",
                "order": 463,
                "data": "Strange Luck (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 464,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 465,
                "data": "It seems as if luck is on your side, strange coincidence seems to aid you in avoiding inherent disasters. You may slip just in time to avoid a bullet, or the doorway may jam delaying your exit just long enough to keep you outside of the blast radius of an explosive device."
            },
            {
                "type": "subheading",
                "order": 466,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 467,
                "data": "Grants +1 to all Dodge & Parry Rolls."
            },
            {
                "type": "heading",
                "order": 468,
                "data": "Sugar Daddy/Momma (3pt Boon)"
            },
            {
                "type": "paragraph",
                "order": 469,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 470,
                "data": "You have someone who looks out for your best interests. This is not an endless stream of wealth or fortune, instead it is a series of small gifts to aid one in their endeavours."
            },
            {
                "type": "subheading",
                "order": 471,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 472,
                "data": "Periodic supplies, money, safe haven or other small gifts seem to come when most needed. The terms of the relationship with your beneficiary are strictly up to you, but if the provider is constantly neglected, then the benefits tend to dry up accordingly."
            },
            {
                "type": "heading",
                "order": 473,
                "data": "Third Eye (4pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 474,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 475,
                "data": "You possess an acute natural insight to supernatural deception. You may attempt to pierce any deceptive powers of illusion or trickery."
            },
            {
                "type": "subheading",
                "order": 476,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 477,
                "data": "You merely declare your intent and engage your surroundings with an Awareness Sum versus the Difficulty set by the GM. If you are successful, then you are freed from the misdirection placed upon you. If you possess a supernatural ability that lets you pierce such trickery, then you receive a +2 to that Power’s Roll."
            },
            {
                "type": "heading",
                "order": 478,
                "data": "Tireless Resolves (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 479,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 480,
                "data": "You have built a great degree of cardio-stamina in your life. While others are dropping like flies your breathing is barely elevated and you’re just hitting your second wind."
            },
            {
                "type": "subheading",
                "order": 481,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 482,
                "data": "Grants +1 to all Athletics Rolls."
            },
            {
                "type": "heading",
                "order": 483,
                "data": "Toxin Training (6pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 484,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 485,
                "data": "You are blessed with the ability to shake off mind controlling drugs and powers of mental command."
            },
            {
                "type": "subheading",
                "order": 486,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 487,
                "data": "By spending an Essence Trait you automatically ignore one mind controlling power or influencing substance and receive a +10 to resist any further powers or influencing substances for the rest of the scene. This may only be used once per scene and effects cannot be stacked. This includes pheromones, drugs, powers but not normal Skills such as Persuasion."
            },
            {
                "type": "heading",
                "order": 488,
                "data": "Transporter (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 489,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 490,
                "data": "If it moves you can drive it. It doesn’t matter if its land, sea or exotic mode of transportation, it will get you there and the cargo will be intact and on time."
            },
            {
                "type": "subheading",
                "order": 491,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 492,
                "data": "Grants +1 to all Vehicle & Piloting Rolls."
            },
            {
                "type": "heading",
                "order": 493,
                "data": "Trash n Treasure (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 494,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 495,
                "data": "As they say, “One man’s trash is another man’s treasure.” You epitomize this concept. You are very adept at noting items of intrinsic value amidst piles of junk. You utilize this to meet your needs without necessarily exceeding your budget."
            },
            {
                "type": "subheading",
                "order": 496,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 497,
                "data": "Grants +1 to all Scrounge Rolls."
            },
            {
                "type": "heading",
                "order": 498,
                "data": "Tree Speaking (Tiermalain) (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 499,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 500,
                "data": "Tree speaking is considered a blessing amongst the Tiermalain as it demonstrates ones connection with the ancient heritage trees of the Faeyr. This ability allows for the exchange of rudimentary information through a subtle, intuitive connection formed by touching the tree. This communication manifests as a gentle whisper of the senses rather than clear verbal or visual messages. Individuals with this ability may sense the general health, needs, or distress signals of trees, receiving impressions and feelings rather than detailed information, enabling a basic understanding of their immediate environment, living entities within it or creatures that have passed through it."
            },
            {
                "type": "subheading",
                "order": 501,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 502,
                "data": "The larger and older the tree, the bigger area that it is attuned to as its roots spread deep into the earth and across it. Roll Primal Instinct, the higher the roll the more detailed the information but regardless the information is always vague. It may note that gentle two-legged creatures that took care to not harm the land passed by or that a behemoth creature that knocked over lesser foliage in its path came through. It will also share damage caused to it as if expecting assistance from those that can understand it."
            },
            {
                "type": "heading",
                "order": 503,
                "data": "Velvet Voice (3pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 504,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 505,
                "data": "Your voice is soft, sensual and appeals to the senses of others."
            },
            {
                "type": "subheading",
                "order": 506,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 507,
                "data": "Grants +1 to all Performance, Persuasion and Scrounge Rolls."
            },
            {
                "type": "heading",
                "order": 508,
                "data": "Virtuoso (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 509,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 510,
                "data": "You understand what is artistic and entertaining to others and you prey upon this knowledge to enhance your own performance. Catering to the needs and desires of the audience allows you to enrapture and thoroughly captivate them."
            },
            {
                "type": "subheading",
                "order": 511,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 512,
                "data": "Grants +1 to all Performance Rolls."
            },
            {
                "type": "heading",
                "order": 513,
                "data": "Way of the Warrior (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 514,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 515,
                "data": "You have spent a large part of your life studying the way of the unarmed warrior. This sense of inner strength has provided you with a spiritual calm that exists at your core regardless of the façade which you choose to expose to others. In addition to this benefit the intense training that you underwent as well as your understanding of anatomy and the proper way to apply pain allows you to truly punish your opponents."
            },
            {
                "type": "subheading",
                "order": 516,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 517,
                "data": "Grants +1 to all Martial Arts Striking and Damage Rolls."
            },
            {
                "type": "heading",
                "order": 518,
                "data": "Weird Confessions (Core) (1pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 519,
                "data": "Setting: Darkholme"
            },
            {
                "type": "paragraph",
                "order": 520,
                "data": "People are at ease with you, and sometimes this causes them to share details that perhaps they shouldn’t have shared. Sometimes this is a good thing, but sometimes they realize that they slipped up."
            },
            {
                "type": "subheading",
                "order": 521,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 522,
                "data": "Once per day or at any time per the Game Master’s discretion when you are alone with a NPC and engage in a brief conversation then you roll 1d10. On a roll of 1 they reveal something truly odd and personal about themselves which immediately changes their demeanor into a defensive mindset as they realize you have learned something that could be used against them. On a roll of 2-9 they reveal something usual about the area that most of the locals are aware of. On a roll of a 10 they reveal something potentially odd but personal but fail to notice their slip of the tongue unless you use this information against them."
            },
            {
                "type": "heading",
                "order": 523,
                "data": "Well Rounded Individual (2pt. Boon)"
            },
            {
                "type": "paragraph",
                "order": 524,
                "data": "Setting: Core"
            },
            {
                "type": "paragraph",
                "order": 525,
                "data": "As a child you thoroughly enjoyed reading and that tradition has continued unto this day. Hence your understanding of Basic Studies such as Reading, Writing, Arithmetic, History, Mythology, Cultures, Traditions, General Trivia, and their ilk far exceeds the average person."
            },
            {
                "type": "subheading",
                "order": 526,
                "data": "Mechanics",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 527,
                "data": "Grants +2 to all Scholar Rolls."
            }
        ]
    },
    {
        "title": "Combat Mechanics",
        "slug": "combat",
        "chapter": "Combat",
        "content": [
            {
                "type": "heading",
                "order": 1,
                "data": "Ambush"
            },
            {
                "type": "paragraph",
                "order": 2,
                "data": "There are 3 ways to ambush an opponent:"
            },
            {
                "type": "subheading",
                "order": 3,
                "data": "Surprise",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 4,
                "data": "In a face-to-face encounter prior to the initiation of combat, a Contested Awareness versus Sleight of Hand roll is made. Failure by the defender results in a -2 to Defensive Rolls for the first Round of combat and Damage inflicted from a successful Surprise Attack is increased by +5 BHP. Surprise initiates combat."
            },
            {
                "type": "subheading",
                "order": 5,
                "data": "Snipe",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 6,
                "data": "In a ranged scenario prior to the initiation of combat, a Contested Awareness versus Stealth roll is made. Failure by the defender results in any Damage inflicted from the successful Snipe Attack to be increased by +10 BHP. Sniping initiates combat."
            },
            {
                "type": "subheading",
                "order": 7,
                "data": "Waylay",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "Every waylayer must lay in wait and best the Target(s) in a Contested Roll of Awareness versus Stealth. Failure by the defender results in a -2 to Defensive Rolls for the first round of combat and Damage inflicted by a successful Waylay Attacks is increased by +5 BHP. A Target receives no penalty against or additional damage from an opponent that they successfully bested in the contested roll. Waylay initiates combat."
            },
            {
                "type": "heading",
                "order": 9,
                "data": "Called Shots (Optional Rule)"
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "Humanoid Targets (May only suffer 1 Primary & 1 Secondary Impairment at a time.)"
            },
            {
                "type": "subheading",
                "order": 11,
                "data": "Standard Target Practice",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 12,
                "data": [
                    "Heart of the Eye: -10 to Strike",
                    "Bull’s-Eye: -5 to Strike",
                    "Inner Ring: -2 to Strike",
                    "Middle Ring Standard Difficulty: No Bonus",
                    "Outer Ring: +2 to Strike"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 13,
                "data": "Primary Zones",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 14,
                "data": [
                    "Head (-10 to Strike): Target loses 2 Action Points for 1d6 Rounds. If the roll was a Critical Success, then the Target must make a Athletics v. half of the damage inflicted post soak or the Target is knocked out for 1d10 rounds.",
                    "Stomach (-6 to Strike): Target receives a -3 to all Athletics related Actions for 1d10 Rounds. If this roll is a Critical Success, then treat it as a Non-Critical Success Groin Shot in addition to the standard penalty.",
                    "Leg (-6 to Strike): Target receives a -1 to all Actions using that limb for 1d10 Rounds. If this roll is a Critical Success, then treat it as a Non-Critical Success Foot Shot in addition to the standard penalty.",
                    "Arm (-6 to Strike): Target receives a -1 to all Actions using that limb for 1d10 Rounds. If this roll is a Critical Success, then treat it as a Non-Critical Success Hand Shot in addition to the standard penalty."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 15,
                "data": "Secondary Zones",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 16,
                "data": [
                    "Ear (-12 to Strike): Target is Stunned until they expend 10 Action Points, if the roll was a critical then it's extended to 20 Action Points. The Target must make a Athletics v. the damage inflicted post soak or suffer permanent hearing damage which results in a -2 to all Perception Rolls that involve hearing.",
                    "Eye (-14 to Strike): Target receives a -2 to Perception Rolls for 1d10 Rounds, if the roll was a critical then it's extended to 2d10 Rounds. The Target must make a Athletics v. the damage inflicted post soak or lose the eye.",
                    "Foot (-6 to Strike): Target receives a -2 to all Actions using that limb for 1d10 Rounds, if the roll was a critical then it's extended to 20 Action Points. The Target must make a Athletics v. the damage inflicted post soak or lose the foot.",
                    "Groin (-8 to Strike): Target receives a -2 to all Actions for 1d10 Rounds, if the roll was a critical then it's extended to 2d10 Rounds. The Target must make a Athletics v. the damage inflicted post soak roll or be Stunned for 20 Action Points. This may be performed on men and women.",
                    "Hand (-6 to Strike): Target receives a -2 to all Actions using that limb for 1d10 Rounds, if the roll was a critical then it's extended to 2d10 Rounds. The Target must make a Athletics v. the damage inflicted post soak or lose the hand.",
                    "Kidney (-8 to Strike): Target receives a -4 on their Damage Soak for 1d10 Rounds, if the roll was a critical then it's extended to 2d10 Rounds. The target must make a Athletics v. damage inflicted or receive an additional -8 on their Damage Soak from this Strike.",
                    "Kneecap (-8 to Strike): Target is Stunned until they expend 6 Action Points for 1d10 Rounds, if the roll was a critical then it's extended to 2d10 Rounds. The Target must make a Athletics v. damage inflicted or suffer permanent damage to that limb which causes their movement to cost an additional AP each Round until the injury is repaired with a Moderate (DL: 21-30) Medical roll.",
                    "Throat (-14 to Strike): Target is Stunned until they expend 12 Action Points. The Target must make a Athletics v. the damage inflicted post soak roll, to avoid displacing their trachea preventing the Target from speaking until the trachea is reset with a Moderate (DL: 21-30) Medical Triage roll."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 17,
                "data": "Charge"
            },
            {
                "type": "paragraph",
                "order": 18,
                "data": "Charging allows you to incorporate your movement into an attack. You must move at least 10' (3M) and you strike the side of the opponent you were facing at the start of the charge. You expend 2 extra CAP and gain a +4 to Strike but suffer a -4 on Parry and Dodge."
            },
            {
                "type": "subheading",
                "order": 19,
                "data": "Overrun",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 20,
                "data": "With an overrun, you plow past or over your opponent (move through their area) instead of damaging them. The target may choose to avoid or block you. If they avoid, you keep moving. If they block, make a trip attack. If you succeed, you continue your movement. If you fail and are tripped in return, you fall prone. If you fail but aren’t tripped, you move 5 feet back the way you came, ending your movement there. If that space is occupied, you fall prone as well."
            },
            {
                "type": "subheading",
                "order": 21,
                "data": "Rush",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 22,
                "data": "Rush attempts to push an opponent straight back instead of damaging them. Both you and the target make Opposed Power Rolls. Larger participants gain a bonus equal to their Size Category (e.g., S10 = +10). If you win, the opponent is pushed back a number of feet equal to your margin of success, minimum 5' (1.5M). If you lose, you are pushed back 5 feet instead. If that space is occupied, you fall prone."
            },
            {
                "type": "subheading",
                "order": 23,
                "data": "Ram",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 24,
                "data": "A ram is a charge where you slam into the target with full momentum. Your movement ends when adjacent to the target. Make a Melee or Martial Arts attack and add +2 Damage per 5' (1.5M) moved before impact. Confined spaces limit ram effectiveness."
            },
            {
                "type": "heading",
                "order": 25,
                "data": "Chasing"
            },
            {
                "type": "paragraph",
                "order": 26,
                "data": "During a chase, all participants move per standard rules. At each round’s end, make a Difficult (DL: 31-40) Athletics Roll. Failure limits your next round to half AP for running. When the fleeing party is at a GM-determined distance (20' urban/forest, 50' open), they may attempt a free Stealth vs. Analyzation Contested Roll to escape."
            },
            {
                "type": "paragraph",
                "order": 27,
                "data": "Success means the pursuers lose track. Anyone who fails the contested roll is removed from the chase. Those who succeed may continue pursuit. If pursuers get within striking range, combat resumes and escape attempts must start over."
            },
            {
                "type": "paragraph",
                "order": 28,
                "data": "Note: Even if a fleeing party member is caught, anyone successfully ditched cannot re-engage."
            },
            {
                "type": "heading",
                "order": 29,
                "data": "Combat Situational Modifiers"
            },
            {
                "type": "subheading",
                "order": 30,
                "data": "Ambush",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 31,
                "data": "If a ranged aggressor attacks from concealment with time to aim and the defender is unaware, the aggressor makes the first attack with a +10 bonus."
            },
            {
                "type": "subheading",
                "order": 32,
                "data": "Area of Effect",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 33,
                "data": "AoE attacks ignore target limits but must affect all close-range combatants and any others in range."
            },
            {
                "type": "subheading",
                "order": 34,
                "data": "Combatant Limiter (LARP ONLY)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 35,
                "data": [
                    "Mental: You may be subjected to one HOSTILE mental challenge per round.",
                    "Social: You may be subjected to one HOSTILE social challenge per round.",
                    "Close Range Physical: You may be targeted by two Close Range Physical challenges unless flanked (up to four).",
                    "Distant Physical: Limitations are based on terrain, battlefield layout, and Storyteller discretion."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 36,
                "data": "Note: Combat is not static. Players cannot bypass limiters by claiming unrealistic positional advantages. Your character cannot ‘reach over’ others during a dynamic melee engagement."
            },
            {
                "type": "heading",
                "order": 37,
                "data": "Combat Time Frame"
            },
            {
                "type": "list",
                "order": 38,
                "data": [
                    "Combat Round: Characters act in Initiative order. They may Act or Move & Hold to take a new Initiative slot that round. Unused AP may be spent on Interrupts.",
                    "Combat Action Point Expenditure: Used for Challenges or Non-Movement Actions.",
                    "Interrupt Action: Requires unmet conditions, passed Initiative, and unused AP.",
                    "Movement Action Point Expenditure: Each MAP allows 5' of movement.",
                    "Difficulty-based Action: Requires a challenge per the Storyteller.",
                    "Free Action: No challenge or AP required (except movement).",
                    "Simple Action: Trivial tasks with nearly no failure chance (DL: 10–14)."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 39,
                "data": "Conditions"
            },
            {
                "type": "paragraph",
                "order": 40,
                "data": "Conditions are special adverse effects that limit the capacities of the inflicted. In the event that effects conflict or align, the most severe effect applies. If Conditions expire at different rates, then once the most severe is removed, the next still-active Condition is applied."
            },
            {
                "type": "subheading",
                "order": 41,
                "data": "Ability Damaged",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 42,
                "data": "The character has temporarily lost 1 or more ability score points. Lost points return at a rate of 1 per uninterrupted Sleep."
            },
            {
                "type": "subheading",
                "order": 43,
                "data": "Blinded",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 44,
                "data": "The character cannot see at all; everything has total visual concealment. Automatically fail Awareness & Analysis Rolls based on sight. -10 to all Short & Long Range Striking Rolls."
            },
            {
                "type": "subheading",
                "order": 45,
                "data": "Dazed",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 46,
                "data": "Must spend 3 extra CAP and/or MAP per action taken."
            },
            {
                "type": "subheading",
                "order": 47,
                "data": "Dead",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 48,
                "data": "The character is dead and decaying as appropriate to the time since death."
            },
            {
                "type": "subheading",
                "order": 49,
                "data": "Deafened",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 50,
                "data": "Automatically fail any Rolls relying on sound."
            },
            {
                "type": "subheading",
                "order": 51,
                "data": "Debilitated",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 52,
                "data": "One or more ability scores reduced to 0. See Section 2: Reduced and Enhanced Abilities."
            },
            {
                "type": "subheading",
                "order": 53,
                "data": "Disabled",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 54,
                "data": "Legs: All movement costs double MAP. Arms: All actions cost double CAP."
            },
            {
                "type": "subheading",
                "order": 55,
                "data": "Dying",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 56,
                "data": "Unconscious, nearing death. See Section 7: Trauma. Medical/Arcane treatment transitions condition to Unconscious."
            },
            {
                "type": "subheading",
                "order": 57,
                "data": "Entangled",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 58,
                "data": "-2 to Melee, Martial Arts Parry, and Dodge Rolls. If anchored, cannot move. If mobile, half speed and cannot Charge or Move All Out."
            },
            {
                "type": "subheading",
                "order": 59,
                "data": "Exhausted",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 60,
                "data": "Occurs when at 5 or fewer Essence or after failing second prolonged Athletics Roll. +4 MAP per movement, +2 CAP per action."
            },
            {
                "type": "subheading",
                "order": 61,
                "data": "Fascinated",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 62,
                "data": "No actions other than paying attention to the effect. -4 to all Rolls. Broken by hostile actions or expending 3 CAP from an ally."
            },
            {
                "type": "subheading",
                "order": 63,
                "data": "Fatigued",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 64,
                "data": "Occurs when at 5 or fewer Essence or after the first failed prolonged Athletics Roll. +2 MAP and +1 CAP per action."
            },
            {
                "type": "subheading",
                "order": 65,
                "data": "Frightened",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 66,
                "data": "See Core Mechanics: Section Fear."
            },
            {
                "type": "subheading",
                "order": 67,
                "data": "Grappled",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 68,
                "data": "Engaged in close-quarters struggle. May be affected by additional effects or restrictions."
            },
            {
                "type": "subheading",
                "order": 69,
                "data": "Helpless",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 70,
                "data": "Bound, paralyzed, or restrained. Cannot use CAP or MAP. Adjacent enemies may Coup de Grace. Mental/Social defenses allowed."
            },
            {
                "type": "subheading",
                "order": 71,
                "data": "Incorporeal",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 72,
                "data": "No physical form on the plane. Immune to Melee and Martial Arts from corporeal sources. Affected by Mental and Social actions."
            },
            {
                "type": "subheading",
                "order": 73,
                "data": "Invisible",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 74,
                "data": "Requires DL 40 Awareness Roll to detect until interacting with the environment. +2 Strike, +5 Parry, +10 Dodge."
            },
            {
                "type": "subheading",
                "order": 75,
                "data": "Nauseated",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 76,
                "data": "-2 to all Rolls, +4 MAP, +6 CAP per action."
            },
            {
                "type": "subheading",
                "order": 77,
                "data": "Normal",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 78,
                "data": "No conditions. Character acts normally."
            },
            {
                "type": "subheading",
                "order": 79,
                "data": "Paralyzed",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 80,
                "data": "Rigid and helpless, unable to act. Treated as Helpless."
            },
            {
                "type": "subheading",
                "order": 81,
                "data": "Prone",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 82,
                "data": "Lying on the ground. -2 Dodge, Melee, and Martial Arts Attacks. Standing up costs 3 CAP."
            },
            {
                "type": "subheading",
                "order": 83,
                "data": "Sickened",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 84,
                "data": "-1 to all Rolls, +2 MAP, +3 CAP per action."
            },
            {
                "type": "subheading",
                "order": 85,
                "data": "Stable",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 86,
                "data": "No longer dying, but unconscious. Must recover conditions normally."
            },
            {
                "type": "subheading",
                "order": 87,
                "data": "Stunned",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 88,
                "data": "-2 to all actions."
            },
            {
                "type": "subheading",
                "order": 89,
                "data": "Unconscious",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 90,
                "data": "Cannot spend CAP or MAP. May be Coup de Grace'd. Mental and Social rolls suffer -5 to resist."
            },
            {
                "type": "heading",
                "order": 91,
                "data": "Coup de Grace"
            },
            {
                "type": "paragraph",
                "order": 92,
                "data": "Melee attacks against Helpless or Unconscious targets automatically hit unless bypassing armor, which requires a DL 20 Melee Roll. The attacker may add their Medicine, Power, or Sleight of Hand Sum to the damage."
            },
            {
                "type": "heading",
                "order": 93,
                "data": "Cover"
            },
            {
                "type": "paragraph",
                "order": 94,
                "data": "Cover represents tactical use of terrain for defense. There are four levels:"
            },
            {
                "type": "list",
                "order": 95,
                "data": [
                    "Minimal: 25% coverage — +2 to Defense vs. Ranged Attacks",
                    "Marginal: 50% coverage — +4 to Defense vs. Ranged Attacks",
                    "Solid: 75% coverage — +6 to Defense vs. Ranged Attacks",
                    "Optimal: Near-total cover — +10 to Defense vs. Ranged Attacks"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 96,
                "data": "Crowded Areas"
            },
            {
                "type": "paragraph",
                "order": 97,
                "data": "In crowds (five or more people between shooter and target), ranged attacks become difficult. Targets gain +2 Dodge per intervening person. Misses may strike a random bystander. If using an automatic weapon, all intervening characters must Dodge or take stray damage."
            },
            {
                "type": "paragraph",
                "order": 98,
                "data": "Fair escape from a crowd is usually Very Easy (DL: 10–19) unless exits are guarded or blocked."
            },
            {
                "type": "heading",
                "order": 99,
                "data": "Damage Dealt"
            },
            {
                "type": "paragraph",
                "order": 100,
                "data": "On a successful Strike, roll damage versus opponent’s Soak (Endurance Sum + Armor Soak + Modifiers). Use appropriate formula:"
            },
            {
                "type": "list",
                "order": 101,
                "data": [
                    "Archery: 2d10 + Perception Sum + Weapon Damage + Modifiers",
                    "Artillery: 2d10 + Perception Sum + Artillery Weapon Damage + Modifiers",
                    "Exoergic: 2d10 + Control + Exoergic Weapon Damage + Modifiers",
                    "Firearms: 2d10 + Perception + Firearm Weapon Damage + Modifiers",
                    "Martial Arts: 2d10 + Martial Arts Sum + Power + Modifiers",
                    "Melee (Exoergic): 2d10 + Control Sum + Weapon Damage + Modifiers",
                    "Melee (Traditional): 2d10 + Strength Sum + Weapon Damage + Modifiers",
                    "Thrown: 2d10 + Strength + Weapon Damage + Modifiers"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 102,
                "data": "Unsoakable Damage is fully applied after calculation. Only Unsoakable Damage Absorption reduces it."
            },
            {
                "type": "heading",
                "order": 103,
                "data": "Damage Difference (Optional Rule: High Lethality Campaign Only!)"
            },
            {
                "type": "paragraph",
                "order": 104,
                "data": "A Damage Difference represents a well-placed blow with heightened lethality. Subtract the defender's roll from the attacker’s successful Strike roll. Add this difference to the damage roll. Example: If Player A rolls 36 and Player B rolls 24, the 12-point difference is added to Player A’s damage."
            },
            {
                "type": "heading",
                "order": 105,
                "data": "Diceless Mobs"
            },
            {
                "type": "paragraph",
                "order": 106,
                "data": "To speed up gameplay, GMs may apply standardized values for mob actions instead of rolling. Options include Rolling, Partially Diceless, and Diceless."
            },
            {
                "type": "list",
                "order": 107,
                "data": [
                    "Rolling – Use dice for all Offensive, Defensive, Skill, and Damage actions.",
                    "Partially Diceless – Declare which categories will use a Standardized Dice Sum instead of rolls.",
                    "Diceless – Use Standardized Dice Sums for all actions."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 108,
                "data": "Disengage a Foe or Avoiding Seizing the Edge"
            },
            {
                "type": "paragraph",
                "order": 109,
                "data": "To move through an enemy’s space or disengage while they are Seizing the Edge, make a Contested Roll using Athletics, Acrobatics, or Parry against their Melee or Martial Arts. Success allows movement through. Failure yields a free attack from the opponent, costing them 1 CAP. Multiple rolls may be required in poor tactical terrain."
            },
            {
                "type": "heading",
                "order": 110,
                "data": "Drawing/Sheathing a Weapon"
            },
            {
                "type": "paragraph",
                "order": 111,
                "data": "Costs 1 CAP in combat. If a weapon is drawn openly, others may respond by drawing as well."
            },
            {
                "type": "heading",
                "order": 112,
                "data": "Dual Weapon Combat"
            },
            {
                "type": "paragraph",
                "order": 113,
                "data": "You may expend 3 additional CAP to gain a second attack with an offhand weapon. This attack suffers -10 to Strike and deals 15 less Damage."
            },
            {
                "type": "heading",
                "order": 114,
                "data": "Fair Escape (Optional Rule: LARP Only)"
            },
            {
                "type": "paragraph",
                "order": 115,
                "data": "Call Fair Escape to avoid unwanted interaction if no one within range prevents you. You must exit the area within three minutes. Cannot be declared if ambushed or approached within 15 paces. Concealment powers may assist, but enhanced movement powers can counter this. The highest-level power decides the outcome."
            },
            {
                "type": "heading",
                "order": 116,
                "data": "Flanking"
            },
            {
                "type": "paragraph",
                "order": 117,
                "data": "Occurs when two characters position on opposite sides of a target or from a Surprise Attack behind them. Grants +2 to Offensive Rolls. A target with their back to a wall is immune to flanking. Multiple attackers can flank, but modifiers do not stack."
            },
            {
                "type": "heading",
                "order": 118,
                "data": "Grappling"
            },
            {
                "type": "paragraph",
                "order": 119,
                "data": "To initiate a grapple, spend 6 CAP and make an Opposed Martial Arts or Power Roll versus your opponent. The winner may Break, Cease, Place, or Maintain a Grapple Effect."
            },
            {
                "type": "list",
                "order": 120,
                "data": [
                    "Max Grapplers: Size Category + 2 participants per side.",
                    "Only the highest roller per side contests. Others add +2 to support.",
                    "Spend 2 additional CAP to convert a Broken Grapple into a Cease Grapple.",
                    "Size Advantage: Larger creature adds Size Category as bonus (e.g., S10 = +10).",
                    "All grapplers spend 6 CAP per round to maintain.",
                    "All actions during a grapple suffer -2 penalty.",
                    "Weapons with minimum range > 0' may not be used while grappled.",
                    "Armed defenders get a free attack when a Grapple Effect is placed (not maintained).",
                    "S00 creatures can be grappled by only 1 opponent."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 121,
                "data": "Creature Size",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 122,
                "data": [
                    "Diminutive - S00",
                    "Tiny - S0",
                    "Small - S1",
                    "Medium - S2",
                    "Large - S4",
                    "Huge - S6",
                    "Colossal - S8",
                    "Gargantuan - S10"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 123,
                "data": "Grappling Effects",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 124,
                "data": [
                    "Mount: After a Trip or versus a prone target, secure a straddled position. You ignore the -2 penalty, but the target still suffers it.",
                    "Restrain: Target’s movement is reduced to 5' per Power difference. If your Power is higher, they cannot move.",
                    "Choke: Spend 6 CAP to choke. Opponent rolls Bio Control vs. your highest Choke damage. If failed, they pass out. They may act until their Bio Control CAP is spent.",
                    "Pin: After reducing a target to <10% BHP and performing a Trip or Throw, make a Contested Power Roll to pin them and win the contest.",
                    "Trip: Knock your opponent prone.",
                    "Throw: Toss the opponent 5' (1.5M) per 3 Power Sum (rounded down)."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 125,
                "data": "Holding Action Points"
            },
            {
                "type": "paragraph",
                "order": 126,
                "data": "Delaying allows you to act later than your initiative, but before your next turn. You may Delay a single Combat and a single Move Action. Specify the action and triggering condition. If the condition occurs before your next initiative, you may use the action as a reaction. If not used by your next turn, the held action is lost."
            },
            {
                "type": "heading",
                "order": 127,
                "data": "Improvised Weapons"
            },
            {
                "type": "paragraph",
                "order": 128,
                "data": "Exceptional individuals can weaponize unlikely objects using the following guidelines:"
            },
            {
                "type": "list",
                "order": 129,
                "data": [
                    "Weight: Must be no more than a Light Load for the wielder.",
                    "Damage Bonus: Equal to wielder’s Strength Sum.",
                    "Damage Descriptor: Determined by the GM.",
                    "Range Increment: See Throwing (page 18)."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 130,
                "data": "Initiative"
            },
            {
                "type": "paragraph",
                "order": 131,
                "data": "Initiative = 2d10 + Reflexes + Perception. Roll a contested Initiative between all PCs and NPCs. Actions occur in descending initiative order. Characters may hold actions and move to a new place in initiative. Tied initiative is resolved through alternating Action Point expenditures rather than one character acting entirely before another."
            },
            {
                "type": "subheading",
                "order": 132,
                "data": "Alternative Expedited Initiative",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 133,
                "data": "The Game Master and one Player each roll 2d10. PCs, NPCs, and Monsters apply modifiers on a pre-determined grid. All other initiative mechanics remain unchanged."
            },
            {
                "type": "heading",
                "order": 134,
                "data": "Lunge"
            },
            {
                "type": "paragraph",
                "order": 135,
                "data": "You may extend your reach by 5' (1.5 m) or 1\" (2.54 cm) on the grid. After lunging, you suffer -5 to all Defensive Rolls until your next turn."
            },
            {
                "type": "heading",
                "order": 136,
                "data": "Movement"
            },
            {
                "type": "paragraph",
                "order": 137,
                "data": "Movement is performed during a character’s Initiative. You may expend as many Movement Action Points as desired during your turn. Combat and Movement Actions are tracked separately unless altered by a Technique or Power."
            },
            {
                "type": "subheading",
                "order": 138,
                "data": "EXAMPLE",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 139,
                "data": [
                    "Tabletop: Move 5’ (1.5m) per Movement Action Point.",
                    "LARP: Take 1 physical step per Movement Action Point."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 140,
                "data": "Multiple Actions"
            },
            {
                "type": "paragraph",
                "order": 141,
                "data": "After completing your primary action, you may take additional actions as long as you have Combat or Movement Action Points remaining. Continue until all Action Points are depleted."
            },
            {
                "type": "heading",
                "order": 142,
                "data": "Range"
            },
            {
                "type": "paragraph",
                "order": 143,
                "data": "Range is the distance a weapon or attack can reach effectively."
            },
            {
                "type": "subheading",
                "order": 144,
                "data": "Athletic Weapons",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 145,
                "data": [
                    "Designed for Throwing: 5’ per Level of Power Total.",
                    "Not Designed for Throwing: 5’ per 2 Levels of Power Total."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 146,
                "data": "Ranged Weapon Modifiers by Distance"
            },
            {
                "type": "table",
                "order": 147,
                "data": {
                    "headers": [
                        "Range",
                        ">5 ft. (>2 m)",
                        ">25 ft. (>10 m)",
                        ">50 ft. (>20 m)",
                        ">250 ft. (>100 m)",
                        ">500 ft. (>200 m)",
                        ">750 ft. (>300 m)",
                        ">1000 ft. (>400 m)"
                    ],
                    "rows": [
                        [
                            "Archery Weapons",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            ""
                        ],
                        [
                            "Striking Mod.",
                            "0",
                            "-3",
                            "-5",
                            "-7",
                            "-9",
                            "-11",
                            "-13"
                        ],
                        [
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            ""
                        ],
                        [
                            "Firearms (Pistols)",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            ""
                        ],
                        [
                            "Striking Mod.",
                            "0",
                            "-2",
                            "-4",
                            "-6",
                            "-8",
                            "-10",
                            "-12"
                        ],
                        [
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            ""
                        ],
                        [
                            "Firearms (Rifles)",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            ""
                        ],
                        [
                            "Striking Mod.",
                            "0",
                            "-1",
                            "-2",
                            "-3",
                            "-4",
                            "-5",
                            "-6"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "heading",
                "order": 146,
                "data": "Relenting"
            },
            {
                "type": "paragraph",
                "order": 147,
                "data": "At any point before the actual test is performed, a player may choose to acquiesce and automatically fail the challenge. This cannot be done for beneficial effects that require a contested challenge."
            },
            {
                "type": "heading",
                "order": 148,
                "data": "Scaling Combat"
            },
            {
                "type": "paragraph",
                "order": 149,
                "data": "Scaling Damage Modifiers are applied after Soak. For example, a man-sized creature or object must deal 20 points of damage after Soak—including any Structural Battle Hit Point Classification modifiers—in order to inflict 1 point of damage on a space station-sized target."
            },
            {
                "type": "table",
                "order": 150,
                "data": {
                    "headers": [
                        "Attacking Units",
                        "Man or Large Sized Object",
                        "Vehicle Sized Object",
                        "Cruiser Sized Object",
                        "Fortress Sized Object",
                        "Space Station Sized Object"
                    ],
                    "rows": [
                        [
                            "Man or Large Sized",
                            "1:1",
                            "5:1",
                            "10:1",
                            "15:1",
                            "20:1"
                        ],
                        [
                            "Vehicle or Colossal Sized",
                            "1:5",
                            "1:1",
                            "5:1",
                            "10:1",
                            "15:1"
                        ],
                        [
                            "Cruiser or Gargantuan Sized",
                            "1:10",
                            "1:5",
                            "1:1",
                            "5:1",
                            "10:1"
                        ],
                        [
                            "Carrier or Fortress Sized",
                            "1:15",
                            "1:10",
                            "1:5",
                            "1:1",
                            "5:1"
                        ],
                        [
                            "Space Station Sized",
                            "1:20",
                            "1:15",
                            "1:10",
                            "1:5",
                            "1:1"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "table",
                "order": 151,
                "data": {
                    "headers": [
                        "Attacking Units",
                        "Man or Large Sized Object",
                        "Vehicle Sized Object",
                        "Cruiser Sized Object",
                        "Fortress Sized Object",
                        "Space Station Sized Object"
                    ],
                    "rows": [
                        [
                            "Man or Large Sized",
                            "-",
                            "+5",
                            "+10",
                            "+15",
                            "+20"
                        ],
                        [
                            "Vehicle or Colossal Sized",
                            "-5",
                            "-",
                            "+5",
                            "+10",
                            "+15"
                        ],
                        [
                            "Cruiser or Gargantuan Sized",
                            "-10",
                            "-5",
                            "-",
                            "+5",
                            "+10"
                        ],
                        [
                            "Carrier or Fortress Sized",
                            "-15",
                            "-10",
                            "-5",
                            "-",
                            "+5"
                        ],
                        [
                            "Space Station Sized",
                            "-20",
                            "-15",
                            "-10",
                            "-5",
                            "-"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "heading",
                "order": 152,
                "data": "Seizing the Edge"
            },
            {
                "type": "paragraph",
                "order": 153,
                "data": "Moving through or using a ranged weapon in an opponent’s Threat Zone grants that opponent an extra attack. Movement to engage or disengage while still facing the enemy does not trigger Seizing the Edge but costs triple the normal Action Points for movement. The attacker may choose not to take the attack."
            },
            {
                "type": "heading",
                "order": 154,
                "data": "Striking an Opponent"
            },
            {
                "type": "paragraph",
                "order": 155,
                "data": "Use the formulas below when making a Strike against an opponent. Compare against their Parry (for Melee) or Dodge (for Ranged) + any modifiers."
            },
            {
                "type": "list",
                "order": 156,
                "data": [
                    "Archery: 2d10 + Archery Sum + Archery Weapon Striking + Modifiers",
                    "Artillery: 2d10 + Artillery Sum + Artillery Weapon Striking + Modifiers",
                    "Exoergic: 2d10 + Exoergic + Exoergic Weapon Striking + Modifiers",
                    "Firearms: 2d10 + Firearm Sum + Firearm Weapon Striking + Modifiers",
                    "Martial Arts: 2d10 + Martial Arts Sum + Power + Modifiers",
                    "Melee (Exoergic): 2d10 + Reflexes Sum + Weapon Damage + Modifiers",
                    "Melee (Traditional): 2d10 + Strength Sum + Weapon Damage + Modifiers",
                    "Thrown: 2d10 + Martial Arts Sum + Weapon Damage + Modifiers"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 157,
                "data": "Threat Zone"
            },
            {
                "type": "paragraph",
                "order": 158,
                "data": "A person’s Threat Zone is their immediate melee or unarmed defensive perimeter. Passing through this area may provoke an attack via Seizing the Edge. Threat Zones are granted as follows:"
            },
            {
                "type": "list",
                "order": 159,
                "data": [
                    "Immediate Threat Zone: Granted by average-sized melee weapons or basic unarmed techniques.",
                    "Extended Threat Zone: Granted by large weapons or advanced unarmed techniques.",
                    "Ranged weapons do not grant a Threat Zone."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 160,
                "data": "Trauma"
            },
            {
                "type": "paragraph",
                "order": 161,
                "data": "When a character is reduced to 0 BHP or less, they fall unconscious. If reduced to a negative BHP total equal to or greater than their Athletics score, the character dies."
            }
        ]
    },
    {
        "title": "Stances",
        "slug": "stances",
        "chapter": "Combat Mechanics",
        "content": [
            {
                "type": "heading",
                "order": 1,
                "data": "(Optional Rule)"
            },
            {
                "type": "paragraph",
                "order": 2,
                "data": "Stances are postures that can be assumed at the beginning of each player’s turn as a free action, designated by their initiative. Some stances are setting-specific or exclusive to certain organizations. There are eight core stances available in all settings to all characters at no cost. Advanced stances require training and typically combine aspects of the core stances with specialized combat tactics. Without training, only one stance may be used at a time."
            },
            {
                "type": "heading",
                "order": 3,
                "data": "Open or Closed"
            },
            {
                "type": "paragraph",
                "order": 4,
                "data": "This stance classification is based on the lateral distance between the lead and rear foot. Open stances offer more stability but leave the body more exposed, while closed stances minimize target exposure but reduce resistance to unbalancing techniques."
            },
            {
                "type": "list",
                "order": 5,
                "data": [
                    "Closed Stance: -2 to all Rolls to Resist being tripped, rushed, or grappled. +2 to all other Defensive Rolls.",
                    "Open Stance: +2 to all Rolls to Resist being tripped, rushed, or grappled. -2 to all other Defensive Rolls."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 6,
                "data": "Long or Short"
            },
            {
                "type": "paragraph",
                "order": 7,
                "data": "This refers to the axial distance between the lead and rear foot. Short stances improve agility but reduce stability, while long stances increase balance but hinder mobility."
            },
            {
                "type": "list",
                "order": 8,
                "data": [
                    "Short Stance: -2 to all Balance Rolls. +2 to all Athletic Combat Rolls.",
                    "Long Stance: -2 to all Athletic Combat Rolls. +2 to all Balance Rolls."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 9,
                "data": "High or Low"
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "This is determined by how much the knees are bent compared to a more upright posture. Low stances offer more power but reduce movement speed. High stances are fast and mobile but sacrifice raw striking power."
            },
            {
                "type": "list",
                "order": 11,
                "data": [
                    "Low Stance: +2 to all Martial Arts & Melee Damage Rolls. All Movement is Halved.",
                    "High Stance: 2 Free Movement AP each Round. -2 to all Martial Arts & Melee Damage Rolls."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 12,
                "data": "Forward or Backward"
            },
            {
                "type": "paragraph",
                "order": 13,
                "data": "This classification is determined by where 75% of a character’s body weight is placed. Forward-weighted stances emphasize offense, while backward-weighted stances support defensive tactics."
            },
            {
                "type": "list",
                "order": 14,
                "data": [
                    "Forward Weighted Stance: +2 to all Attack Rolls.",
                    "Backward Weighted Stance: +1 to all Damage Rolls & +1 to all Defense Rolls."
                ],
                "style_class": "list-disc pl-6"
            }
        ]
    },
    {
        "title": "Styles",
        "slug": "styles",
        "chapter": "Combat Mechanics",
        "content": [
            {
                "type": "paragraph",
                "order": 2,
                "data": "Martial Art Styles are a diversified tapestry woven from the threads of physical prowess, mental discipline, and sometimes, spiritual enlightenment. Each style, whether it’s the graceful arcs or the sharp strikes, offers a distinct rhythm and philosophy that transcends mere self-defense. Practitioners move in a dance that harmonizes body and mind, turning kicks, punches, and grapples into a language of personal expression and resilience."
            },
            {
                "type": "paragraph",
                "order": 3,
                "data": "As they train, martial artists sculpt their bodies into instruments of precision and power, while their minds are honed with focus and calm, capable of tranquility even in the storm of combat. Many styles, rooted deeply in rich cultural traditions, are not just about fighting but about living—promoting values like respect, honor, and community. For some, the dojo is a place of inner discovery, where each movement and breath deepens their connection to life's rhythms. In this way, martial arts are a journey as much as a practice, offering paths to physical fitness, personal confidence, and even peace."
            },
            {
                "type": "heading",
                "order": 4,
                "data": "Aikijutsu Style"
            },
            {
                "type": "subheading",
                "order": 5,
                "data": "Escape",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 6,
                "data": "Pre-Requisites: Reflexes 2 | Cost: 10 XP | Receive a +5 to Break or Cease a Grapple."
            },
            {
                "type": "subheading",
                "order": 7,
                "data": "Reversal",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "Pre-Requisites: Escape & Reflexes 4 | Cost: 20 XP | Choose to suffer a -5 Penalty to your Break or Cease Grapple Roll. If successful, inflict the effects of the last attempted Grapple Effect upon your opponent and choose to Engage or Disengage."
            },
            {
                "type": "subheading",
                "order": 9,
                "data": "Redirect",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "Pre-Requisites: Escape & Reflexes 6 | Cost: 30 XP | Spend 8 CAP. Any Melee or Martial Arts attack directed at you until your next turn may be affected. If your Defensive Roll exceeds the attacker’s Strike by 15 or more, their weapon may fly from their hand or they may be thrown. Direction is determined by 1d10:"
            },
            {
                "type": "list",
                "order": 10,
                "data": [
                    "1–2: Behind You",
                    "3–4: In Front of You",
                    "5–6: To Your Left",
                    "7–8: To Your Right",
                    "9–10: At Your Feet"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 11,
                "data": "Precise Manipulation",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 12,
                "data": "Pre-Requisites: Redirect & Reflexes 8 | Cost: 40 XP | Spend 2 CAP to double the duration of all Called Shot effects."
            },
            {
                "type": "heading",
                "order": 13,
                "data": "Battojutsu Style"
            },
            {
                "type": "subheading",
                "order": 14,
                "data": "Battojutsu",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 15,
                "data": "Pre-Requisites: Reflexes 4 | Cost: 2 XP | Waives CAP cost to sheathe a slashing weapon. Increases Initiative by 2 at the start of any round where the weapon is sheathed."
            },
            {
                "type": "subheading",
                "order": 16,
                "data": "Battojutsu Mastery",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 17,
                "data": "Pre-Requisites: Battojutsu & Reflexes 4 | Cost: 20 XP | In addition to Battojutsu benefits, inflict 5 BHP of Unsoakable Damage. The weapon is automatically re-sheathed at the end of the attack."
            },
            {
                "type": "subheading",
                "order": 18,
                "data": "Battojutsu Mastery (Greater)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 19,
                "data": "Pre-Requisites: Battojutsu Mastery & Reflexes 6 | Cost: 30 XP | Unsoakable Damage from Iajutsu drawing increases to 8 BHP."
            },
            {
                "type": "subheading",
                "order": 20,
                "data": "Battojutsu Mastery (Grand)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 21,
                "data": "Pre-Requisites: Battojutsu (Greater) & Reflexes 8 | Cost: 40 XP | Unsoakable Damage from Iajutsu drawing increases to 15 BHP."
            },
            {
                "type": "heading",
                "order": 22,
                "data": "Blind Sense Style"
            },
            {
                "type": "subheading",
                "order": 23,
                "data": "Blind Sense",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 24,
                "data": "Pre-Requisites: Perception 2 | Cost: 10 XP | Reduce penalties by 5 for ANY Close-Range Actions in Complete Darkness that do not require distinguishing color."
            },
            {
                "type": "subheading",
                "order": 25,
                "data": "Blind Sense Mastery",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 26,
                "data": "Pre-Requisites: Blind Sense & Perception 4 | Cost: 20 XP | Reduce penalties by 5 for ANY Long-Range Actions in Complete Darkness that do not require distinguishing color."
            },
            {
                "type": "subheading",
                "order": 27,
                "data": "Blind Sense Mastery (Greater)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 28,
                "data": "Pre-Requisites: Blind Sense Mastery & Perception 6 | Cost: 30 XP | Close-Range and Long-Range penalties in Complete Darkness are reduced by 10 if the action does not require distinguishing color."
            },
            {
                "type": "subheading",
                "order": 29,
                "data": "Blind Sense Mastery (Grand)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 30,
                "data": "Pre-Requisites: Blind Sense Mastery (Greater) & Perception 8 | Cost: 40 XP | You suffer no penalties for ANY Actions in Complete Darkness, including those requiring color distinction."
            }
        ]
    },
    {
        "title": "Powers, Techniques & Spheres",
        "slug": "powers-techniques-spheres",
        "chapter": "Powers and Techinques",
        "content": [
            {
                "type": "paragraph",
                "order": 2,
                "data": "Powers are inherent supernatural abilities that utilize essence to accomplish impossible feats. Techniques represent enhanced training and bodily conditioning, focusing chakra pathways to perform supranatural tasks. Spheres are magical in nature—arcane or spiritual—and allow characters to bend or manipulate the laws of nature through the use of essence."
            },
            {
                "type": "paragraph",
                "order": 3,
                "data": "Access to Spheres is restricted by a character’s Calling and/or Specialization. If a character’s Calling or Specialization grants access to a Sphere, it provides one of the following bonuses:"
            },
            {
                "type": "list",
                "order": 4,
                "data": [
                    "Major Sphere Access: +4 bonus to all associated rolls.",
                    "Minor Sphere Access: +2 bonus to all associated rolls."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 5,
                "data": "If both a character’s Calling and Specialization grant access to the same Sphere, the higher bonus is used, regardless of whether that access is Major or Minor."
            },
            {
                "type": "heading",
                "order": 31,
                "data": "Disarm & Deflection Style"
            },
            {
                "type": "subheading",
                "order": 32,
                "data": "Disarm",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 33,
                "data": "Pre-Requisites: Melee 2 | Cost: 10 XP | Spend 6 CAP. Any melee attack directed at you until your next turn may be disarmed. If your Defensive Roll exceeds the attacker’s Strike by 15 or more, the weapon is disarmed and lands 1d10 feet away. Direction: 1–2: Behind You, 3–4: In Front, 5–6: Left, 7–8: Right, 9–10: At Your Feet. If unarmed, take 5 Non-Soaked BHP."
            },
            {
                "type": "subheading",
                "order": 34,
                "data": "Deflection",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 35,
                "data": "Pre-Requisites: Disarm & Melee or Martial Arts 4 | Cost: 20 XP | Spend 6 CAP. Ranged attacks within your Threat Zone that your Defensive Roll exceeds by 15 or more are deflected. If unarmed, take 5 BHP of Non-Soakable Damage."
            },
            {
                "type": "subheading",
                "order": 36,
                "data": "Disarm & Deflection Mastery",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 37,
                "data": "Pre-Requisites: Deflection & Melee or Martial Arts 6 | Cost: 30 XP | Spend 6 CAP. Both Disarm and Deflection are activated. Only need to beat attacker’s roll by 10. Non-Soakable Damage is reduced to 2."
            },
            {
                "type": "subheading",
                "order": 38,
                "data": "Disarm & Deflection Grand Mastery",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 39,
                "data": "Pre-Requisites: Disarm & Deflection Mastery & Melee or Martial Arts 8 | Cost: 40 XP | Spend 4 CAP. Only need to beat attacker’s roll by 5 to disarm/deflect. Non-Soakable Damage is reduced to 0. If you exceed the attacker’s roll by 10, you redirect the attack back at them using their own Strike and Damage stats."
            },
            {
                "type": "heading",
                "order": 40,
                "data": "Dynamic Combat Style"
            },
            {
                "type": "subheading",
                "order": 41,
                "data": "Dynamic Combat",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 42,
                "data": "Pre-Requisites: Riding 2 | Cost: 10 XP | Allows attacking from a mount or vehicle without penalty. Enables charges. Charges require sacrificing additional attacks and moving the mount’s minimum charge distance before making a single weapon attack. If used against a mounted opponent, a Riding or Vehicle Op check avoids being unseated. Against targets on foot, an Athletics or Acrobatics check is used. DL equals post-soak damage dealt."
            },
            {
                "type": "subheading",
                "order": 43,
                "data": "Dynamic Mastery",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 44,
                "data": "Pre-Requisites: Dynamic Combat & Riding 4 | Cost: 20 XP | As above, but +5 Damage on successful charge."
            },
            {
                "type": "subheading",
                "order": 45,
                "data": "Dynamic Mastery (Greater)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 46,
                "data": "Pre-Requisites: Dynamic Combat Mastery & Riding 6 | Cost: 30 XP | Allows spending AP to strike a second target during the charge."
            },
            {
                "type": "subheading",
                "order": 47,
                "data": "Dynamic Mastery (Grand)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 48,
                "data": "Pre-Requisites: Dynamic Combat Mastery & Riding 8 | Cost: 40 XP | No limit to number of targets during charge. +10 to Strike and Damage rolls."
            },
            {
                "type": "heading",
                "order": 49,
                "data": "Florentine Style"
            },
            {
                "type": "paragraph",
                "order": 50,
                "data": "Normally, at the cost of 3 extra CAP, you may make one extra offhand weapon attack each round with -10 Strike and -15 Damage."
            },
            {
                "type": "subheading",
                "order": 51,
                "data": "Florentine",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 52,
                "data": "Pre-Requisites: Melee 2 | Cost: 10 XP | Reduces cost to 2 extra CAP and -8 Strike (0 if Ambidextrous), -10 Damage."
            },
            {
                "type": "subheading",
                "order": 53,
                "data": "Florentine Mastery",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 54,
                "data": "Pre-Requisites: Florentine & Melee 4 | Cost: 20 XP | Reduces cost to 1 extra CAP and -6 Strike (0 if Ambidextrous), -5 Damage."
            },
            {
                "type": "subheading",
                "order": 55,
                "data": "Florentine Mastery (Greater)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 56,
                "data": "Pre-Requisites: Florentine Mastery & Melee 6 | Cost: 30 XP | Cost remains 1 CAP, 0 Strike penalty (0 if Ambidextrous), no Damage penalty."
            },
            {
                "type": "subheading",
                "order": 57,
                "data": "Florentine Mastery (Grand)",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 58,
                "data": "Pre-Requisites: Greater Florentine Mastery & Melee 8 | Cost: 40 XP | Reduces cost to 0 extra CAP, +5 Strike (0 if Ambidextrous), +10 Damage."
            },
            {
                "type": "heading",
                "order": 59,
                "data": "Flowing Strike Style"
            },
            {
                "type": "subheading",
                "order": 60,
                "data": "Pinpoint Weakness",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 61,
                "data": "Pre-Requisites: Perception 2 | Cost: 10 XP | Spend 1 AP on your first initiative while analyzing an opponent. Gain +2 to Strike against them for the remainder of combat."
            },
            {
                "type": "subheading",
                "order": 62,
                "data": "Penetrating Strike",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 63,
                "data": "Pre-Requisites: Pinpoint Weakness & Perception 4 | Cost: 20 XP | Analyzed opponents suffer -2 Soak against your strikes until the end of combat."
            },
            {
                "type": "subheading",
                "order": 64,
                "data": "Flowing Strike",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 65,
                "data": "Pre-Requisites: Penetrating Strike & Perception 6 | Cost: 30 XP | Each time you deal damage, the opponent takes a cumulative 2 BHP of Unsoakable Damage for every non-defensive Combat AP they spend the next round."
            },
            {
                "type": "subheading",
                "order": 66,
                "data": "Grand Master’s Flowing Strike",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 67,
                "data": "Pre-Requisites: Flowing Strike & Perception 8 | Cost: 40 XP | The Unsoakable Damage inflicted by Flowing Strike is increased to 5 BHP."
            },
            {
                "type": "heading",
                "order": 68,
                "data": "Improvised Combat Style"
            },
            {
                "type": "subheading",
                "order": 69,
                "data": "Improvised Combat",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 70,
                "data": "Pre-Requisite: Martial Arts & Melee 2 | Cost: 10 XP | Spend 1 Combat AP to pick up ANY object and treat it as a similarly sized weapon for that combat round."
            },
            {
                "type": "subheading",
                "order": 71,
                "data": "Discombobulating Attacks",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 72,
                "data": "Pre-Requisite: Improvised Combat, Martial Arts & Melee 4 | Cost: 20 XP | Spend 1 Essence to disorient enemies. They suffer -2 to Soak and -2 to Defense for the rest of combat."
            },
            {
                "type": "subheading",
                "order": 73,
                "data": "Flanked Not Flanked",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 74,
                "data": "Pre-Requisite: Discombobulating Attacks, Martial Arts & Melee 6 | Cost: 30 XP | Spend 1 Essence. When flanked, enemies suffer the effects of being flanked instead, due to your confusing movements. Lasts for the rest of combat."
            },
            {
                "type": "subheading",
                "order": 75,
                "data": "Shifting Surfaces",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 76,
                "data": "Pre-Requisite: Flanked Not Flanked, Martial Arts & Melee 8 | Cost: 40 XP | Spend 1 Essence to move up vertical surfaces a distance equal to (Power + Acrobatics) × 2. If the landing zone is occupied by an enemy, gain +5 to Strike and double damage after Soak on the first attack."
            },
            {
                "type": "heading",
                "order": 77,
                "data": "Morote Style"
            },
            {
                "type": "subheading",
                "order": 78,
                "data": "Powerful Blow",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 79,
                "data": "Pre-Requisites: Melee 2 | Cost: 10 XP | Spend 2 additional CAP to deliver a heavy two-handed strike. +3 Damage, but -2 to Strike."
            },
            {
                "type": "subheading",
                "order": 80,
                "data": "Focused Blow",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 81,
                "data": "Pre-Requisites: Powerful Blow, Melee 4 | Cost: 20 XP | Upgrade Powerful Blow to deal +6 Damage instead of +3. Still -2 to Strike."
            },
            {
                "type": "subheading",
                "order": 82,
                "data": "Devastating Strike",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 83,
                "data": "Pre-Requisites: Focused Blow, Melee 6 | Cost: 30 XP | Deal +9 Damage. Strike penalty is reduced to -1."
            },
            {
                "type": "subheading",
                "order": 84,
                "data": "Ikken Hissatsu",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 85,
                "data": "Pre-Requisites: Devastating Blow, Melee 8 | Cost: 30 XP | Add full Power Skill to damage. No longer suffer a penalty to Strike."
            },
            {
                "type": "heading",
                "order": 86,
                "data": "Seizing the Edge Style"
            },
            {
                "type": "subheading",
                "order": 87,
                "data": "Nimble Footing",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 88,
                "data": "Pre-Requisite: Acrobatics & Athletics 2 | Cost: 10 XP | Move through 15 feet (LARP: 3 steps) of Unstable Terrain as if it were normal terrain."
            },
            {
                "type": "subheading",
                "order": 89,
                "data": "Enhancing the Edge",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 90,
                "data": "Pre-Requisites: Nimble Footing, Acrobatics & Athletics 4 | Cost: 20 XP | Expend 1 Essence to double your Threatening Range for Seizing the Edge for the remainder of combat."
            },
            {
                "type": "subheading",
                "order": 91,
                "data": "Engaging Step",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 92,
                "data": "Pre-Requisites: Enhancing the Edge, Acrobatics & Athletics 6 | Cost: 30 XP | When an enemy disengages from you, you may immediately spend 1 Combat AP to move adjacent to them. This movement does not provoke Seizing the Edge from others."
            },
            {
                "type": "subheading",
                "order": 93,
                "data": "Departing Blow",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 94,
                "data": "Pre-Requisites: Engaging Step, Acrobatics & Athletics 8 | Cost: 40 XP | After using Engaging Step, you gain a free Strike against the disengaging enemy."
            },
            {
                "type": "heading",
                "order": 95,
                "data": "Viper's Strike Style"
            },
            {
                "type": "subheading",
                "order": 96,
                "data": "Speed Load",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 97,
                "data": "Pre-Requisite: Perception 2 | Cost: 10 XP | Reloading or Drawing a Ranged Weapon is a Free Action."
            },
            {
                "type": "subheading",
                "order": 98,
                "data": "Point Blank Shot",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 99,
                "data": "Pre-Requisites: Perception & Ranged 4 | Cost: 20 XP | You may perform ranged attacks even while grappled and suffer no penalties when firing within another’s Threat Zone."
            },
            {
                "type": "subheading",
                "order": 100,
                "data": "Critical Spot",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 101,
                "data": "Pre-Requisites: Perception & Ranged 6 | Cost: 30 XP | Increase Ranged Attack Damage by +5."
            },
            {
                "type": "subheading",
                "order": 102,
                "data": "The Distance",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 103,
                "data": "Pre-Requisites: Perception 8 & Ranged 8 | Cost: 40 XP | Increase Ranged Attack Strike by +5."
            }
        ]
    },
    {
        "title": "Currency",
        "slug": "currency",
        "chapter": "Setting Currencies",
        "content": [
            {
                "type": "paragraph",
                "order": 2,
                "data": "Every setting has a series of currencies, but they may generally be broken down into the following baselines:"
            },
            {
                "type": "subheading",
                "order": 3,
                "data": "Fantasy or Steam Punk",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 4,
                "data": "Silver is the standard currency of trade."
            },
            {
                "type": "list",
                "order": 5,
                "data": [
                    "CP = Copper Penny",
                    "SD = Silver Denar",
                    "GC = Gold Crest",
                    "PC = Platinum Crown"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "list",
                "order": 6,
                "data": [
                    "10 CP = 1 SD",
                    "100 SD = 1 GC",
                    "10 GC = 1 PC",
                    "1 PC = 1 Jade Plate",
                    "1 Rod = 10 Coins of Same Material"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 7,
                "data": "Modern or Near Future",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "Dollar is the standard currency of trade."
            },
            {
                "type": "subheading",
                "order": 9,
                "data": "Cyber Punk or Space Faring",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "Credits are the standard currency of trade."
            }
        ]
    },
    {
        "title": "Gear",
        "slug": "gear",
        "chapter": "Equipment",
        "content": [
            {
                "type": "paragraph",
                "order": 2,
                "data": "Equipment has limitations to availability and legality that may vary from setting to setting as well as area to area within a setting. There is also the ability to conceal gear and how much space it takes to do so as well as how many hands are required to utilize a piece of equipment. Limitations to how many storage devices a character can carry as well as the max number and/or weight that can be stowed in a device. Finally there is quality which affects both the cost and has mechanical influences."
            },
            {
                "type": "heading",
                "order": 3,
                "data": "Availability"
            },
            {
                "type": "list",
                "order": 4,
                "data": [
                    "1 - Available Anywhere. (Mundane)",
                    "2 - Occasionally Available in Large Towns. (Common)",
                    "3 - Occasionally Available in Large Cities. (Uncommon)",
                    "4 - Only Available in Designated Areas. (Rare)"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 5,
                "data": "Legality"
            },
            {
                "type": "list",
                "order": 6,
                "data": [
                    "L - (Legal)",
                    "R - (Restricted) Requires a Permit or it is considered an illegal item and is subject to Confiscation and/or a Fines or Short-Term Incarceration.",
                    "X - (Highly Illegal) Subjects to Confiscation, Fines and Long-Term Incarceration."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 7,
                "data": "Conceal Carry"
            },
            {
                "type": "list",
                "order": 8,
                "data": [
                    "CC0 (DC 5 to Conceal) - Can easily be Carried or Concealed.",
                    "CC1 (DC 10 to Conceal) - Can be Concealed in a Pocket or under a Shirt.",
                    "CC2 (DC 20 to Conceal) - Can be Concealed in a Jacket.",
                    "CC3 (DC 30 to Conceal) - Can be Concealed in a Trench Coat, Cloak or Duster.",
                    "CC4 (DC 40 to Conceal) - Can be Concealed in a 5’ x 3’ x 1’ Space.",
                    "CC5 (DC 50 to Conceal) - Can be Concealed by being built into an openly carried object."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 9,
                "data": "Number of Hands Required"
            },
            {
                "type": "list",
                "order": 10,
                "data": [
                    "1H - 1 Handed Item",
                    "2H - 2 Handed Item"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 11,
                "data": "Max Items Worn"
            },
            {
                "type": "list",
                "order": 12,
                "data": [
                    "1 - Head - Bonnet, Hat, Helm, Tiara or Crown",
                    "2 - Head Overlay",
                    "1 - Neck - Necklace, Choker or Collar",
                    "1 - Shoulder - Cloak, Overcoat, Trench Coat",
                    "3 - Back - 1 Backpack & 2 Holster(s), Scabbard(s) or Quiver(s)",
                    "1 - Chest - Armor/Corset + Bandolier, Shirt, Undershirt & Vest",
                    "1 - Chest Overlay & Underlay",
                    "1 - Wristwear - Bracelet, Bracer, Kote",
                    "1 - Handwear Set - Pair of Gloves",
                    "4 - Finger - Rings",
                    "1 - Waist - Belt, Girdle or Suspenders",
                    "3 - Waist Accessories - Holster, Pouch, Purse, Scabbard or Quiver",
                    "2 - Girding - Groin, Hip, Under Arm Pieces, Holster, Sheath",
                    "1 - Leggings - Kilt, Hakama, Skirt, Pants, Shorts, etc.",
                    "1 - Legging Underlay",
                    "2 - Ankle - Boot Sheath or Holster",
                    "1 - Footwear Set - Boots, Shoes, Slippers, etc."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 13,
                "data": "Max Gear Stowage"
            },
            {
                "type": "list",
                "order": 14,
                "data": [
                    "Ankle Sheath/Holster: Holds 1 Weapon of the type it was designed for.",
                    "Back Scabbard/Holster: Holds 1 Weapon of the type it was designed for.",
                    "Bandolier (Ammunition): Holds 30 Rounds of Ammunition of the type it was designed for.",
                    "Bandolier (Weapon): Holds 5 Weapons of the type it was designed for.",
                    "Boot Sheath/Holster: Holds 1 Weapon of the type it was designed for.",
                    "Hip Scabbard/Holster: Holds 1 Weapon of the type it was designed for.",
                    "Mid Back Sheath/Holster: Holds 1 Weapon of the type it was designed for.",
                    "Quiver: Holds 30 Arrows or Bolts.",
                    "Saddle Bags: May contain 2 CC Items & Up to 80 lbs.",
                    "Pack Scabbard/Holster: Holds 1 Weapon of the type it was designed for.",
                    "Messenger Bag: May contain 2 CC Items & 15 lbs.",
                    "Purse: May contain 0.5 CC Items & 15 lbs.",
                    "Waist Pouches: May contain 1 CC Item & 10 lbs.",
                    "Briefcase/Laptop Case/Satchel: May contain 2 CC Items & 30 lbs.",
                    "Small Backpack: May contain 3 CC Items & 60 lbs.",
                    "Full Backpack: May contain 4 CC Items & 120 lbs.",
                    "Chest/Suitcase (Small): May contain 3 CC Items & 200 lbs.",
                    "Chest/Suitcase (Medium): May contain 4 CC Items & 300 lbs.",
                    "Barrel: May contain 5 CC Items & 400 lbs.",
                    "Trunk: May contain 10 CC Items & 500 lbs."
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "heading",
                "order": 15,
                "data": "Quality"
            },
            {
                "type": "subheading",
                "order": 16,
                "data": "Poor Quality",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 17,
                "data": "Reduces Availability Rating by 1 | Reduces Cost | Typically Invokes Penalties"
            },
            {
                "type": "paragraph",
                "order": 17,
                "data": "Provides a -2 Penalty to all associated Rolls unless begging."
            },
            {
                "type": "subheading",
                "order": 18,
                "data": "Average Quality",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 19,
                "data": "Standard Availability Rating | Standard Cost | No Modifiers"
            },
            {
                "type": "paragraph",
                "order": 19,
                "data": "There is no modifier for wearing or using standard clothing, equipment, or transportation unless at a gathering where High Quality or Masterwork Quality clothing is expected or considered the norm in which case a -2 Situational Penalty is applied to Social Rolls when dealing with anyone dressed in higher quality clothing than they themselves."
            },
            {
                "type": "subheading",
                "order": 20,
                "data": "High Quality",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 21,
                "data": "Increases Availability Rating by 1 | Doubles Cost | Provides Bonuses"
            },
            {
                "type": "paragraph",
                "order": 21,
                "data": "If all clothing, equipment, and transportation used by a character is of High Quality, then they receive a minimum of a +2 Situational Bonus on Social Rolls in circumstances where an imposing, official or professional appearance would be of assistance (at the GM’s discretion) unless the target they are attempting to impress is likewise dressed. Equipment and Transportation provides a +1 to all Rolls involving its use."
            },
            {
                "type": "subheading",
                "order": 22,
                "data": "Exceptional Quality",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 23,
                "data": "Increases Availability Rating by 2 | Further increases Cost | Provides Bonuses"
            },
            {
                "type": "paragraph",
                "order": 24,
                "data": "If all clothing, equipment, and transportation used by a character is of Exceptional Quality then they receive a +4 Situational Bonus on Social Rolls in circumstances where a regal, imposing, official or professional appearance are expected or would be of assistance (at the GM’s discretion) unless the target they are attempting to impress is likewise dressed. Equipment and Transportation provides a +2 Bonus to all associated use Rolls."
            },
            {
                "type": "heading",
                "order": 24,
                "data": "Used Items"
            },
            {
                "type": "paragraph",
                "order": 25,
                "data": "Sell Value to a Merchant is 20% of the item's listed value."
            },
            {
                "type": "paragraph",
                "order": 26,
                "data": "Used merchandise or non-regulated goods brought in from the outside are considered high-risk products and their value is significantly less to the merchant community, who will in turn attempt to sell the used product for 75% of its original value."
            }
        ]
    },
    {
        "title": "Weapons & Armor",
        "slug": "weapons-armor",
        "chapter": "Equipment",
        "content": [
            {
                "type": "heading",
                "order": 1,
                "data": "Archaic Weapons & Armor"
            },
            {
                "type": "subheading",
                "order": 2,
                "data": "Archery",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 3,
                "data": {
                    "headers": [
                        "Archery",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "Slots",
                        "Equip & Reload AP",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Bolt",
                            "P",
                            "--",
                            "--",
                            "--",
                            "--",
                            "--",
                            "1",
                            "1",
                            ""
                        ],
                        [
                            "Arrow",
                            "P",
                            "--",
                            "--",
                            "--",
                            "--",
                            "--",
                            "1",
                            "1",
                            ""
                        ],
                        [
                            "Crossbow, Hand",
                            "P",
                            "+4",
                            "+5",
                            "+15",
                            "5",
                            "0-25' (0-8 m)",
                            "2",
                            "1",
                            "Handheld/Pistol Crossbow."
                        ],
                        [
                            "Crossbow, Light",
                            "P",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "10-50' (3-15 m)",
                            "2",
                            "1",
                            "Pull/Push Lever or Stirrup."
                        ],
                        [
                            "Crossbow, Heavy",
                            "P",
                            "0",
                            "+3",
                            "+21",
                            "7",
                            "10-75' (3-23 m)",
                            "2",
                            "3",
                            "Compound, Cranequin or Windlass."
                        ],
                        [
                            "Bow, Short",
                            "P",
                            "+2",
                            "+6",
                            "+12",
                            "5",
                            "10-50' (3-15 m)",
                            "2",
                            "1",
                            ""
                        ],
                        [
                            "Bow, Long",
                            "P",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "10-75' (3-23 m)",
                            "2",
                            "1",
                            "Long or Recurve."
                        ],
                        [
                            "Bow, Heavy",
                            "P",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "10-100' (3-30 m)",
                            "2",
                            "2",
                            "Compound or Daikyu."
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 4,
                "data": "Athletics",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 5,
                "data": {
                    "headers": [
                        "Athletics",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "Slots",
                        "Equip & Reload AP",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Grenade",
                            "E",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "0-50' (0-15 m)",
                            "1",
                            "1",
                            "Explosive Flask, Sticky Grenade or Hand Grenade."
                        ],
                        [
                            "Javelin",
                            "P",
                            "+2",
                            "+5",
                            "+15",
                            "6",
                            "10-75' (3-23 m)",
                            "1",
                            "2",
                            "Harpoon or Thrown Spear."
                        ],
                        [
                            "Net",
                            "--",
                            "+4",
                            "+6",
                            "--",
                            "6",
                            "5-20' (1-6 m)",
                            "1",
                            "1",
                            "Gladiatorial Net"
                        ],
                        [
                            "Sling",
                            "C",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "5-40' (1.5-6 m)",
                            "1",
                            "1",
                            ""
                        ],
                        [
                            "Sling Staff",
                            "C",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "5-50' (1.5-15 m)",
                            "1",
                            "1",
                            ""
                        ],
                        [
                            "Throwing, Crushing",
                            "C",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "5-30' (1.5-9 m)",
                            "1",
                            "1",
                            "Bolas, Boomerang, or Shotput"
                        ],
                        [
                            "Throwing, Edged",
                            "S",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "5-30' (1.5-9 m)",
                            "1",
                            "1",
                            "Chakram, Throwing Axe or Tomahawk."
                        ],
                        [
                            "Throwing, Piercing",
                            "P",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "5-30' (1.5-9 m)",
                            "1",
                            "1",
                            "Blow Dart, Dart, Stiletto, Throwing Spikes or Shuriken."
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 6,
                "data": "Melee, Crushing",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 7,
                "data": {
                    "headers": [
                        "Melee, Crushing",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "Slots",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Chain",
                            "C",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-15' (0-4.5 m)",
                            "1",
                            "2",
                            "Chain, Chained Kama, Flying Blade, Kusarigama, Kyoketsu Shoge or Spiked Chain."
                        ],
                        [
                            "Flail, Small",
                            "C",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "1",
                            "Footman's Flail or Nunchaku."
                        ],
                        [
                            "Flail, Large",
                            "C",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-10' (0-3 m)",
                            "2",
                            "2",
                            "Horseman's Flail or Sansetsukon."
                        ],
                        [
                            "Mace, Small",
                            "C",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "2",
                            "1",
                            "Baton, Club, Footman's Mace or Tonfa."
                        ],
                        [
                            "Mace, Large",
                            "C",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-10' (0-3 m)",
                            "2",
                            "2",
                            "Horseman's Mace, Maul, Morning Star, Tetsubo or Warhammer."
                        ],
                        [
                            "Staves, Short",
                            "C",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "1",
                            "Jo Staff or Short Staff."
                        ],
                        [
                            "Staves, Long",
                            "C",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-10' (0-3 m)",
                            "2",
                            "1",
                            "Bo Staff, Quarterstaff."
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 8,
                "data": "Melee, Piercing",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 9,
                "data": {
                    "headers": [
                        "Melee, Piercing",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Awl",
                            "P",
                            "0",
                            "+4",
                            "+18",
                            "6",
                            "5-15' (1.5-4.5 m)",
                            "2",
                            "Lucerne Hammer, Mancatcher, Military Fork, Ranseur, Spetum or Trident."
                        ],
                        [
                            "Lance",
                            "P",
                            "+4",
                            "+4",
                            "+18",
                            "6",
                            "5-10' (1.5-3 m)",
                            "2",
                            "Riding Lance. Requires Being Mounted or 2 Hands. Concealment: None"
                        ],
                        [
                            "Pick, Small",
                            "P",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "Footman’s Pick or Gaff Hook."
                        ],
                        [
                            "Pick, Large",
                            "P",
                            "0",
                            "+5",
                            "+15",
                            "5",
                            "0-5' (0-1.5 m)",
                            "2",
                            ""
                        ],
                        [
                            "Fencing",
                            "P",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "Rapier, Saber or Sword Cane."
                        ],
                        [
                            "Spear",
                            "P",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-10' (0-3 m)",
                            "2",
                            "Long Spear, Naginata or Spear."
                        ],
                        [
                            "Spike",
                            "P",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "Iron Brush, Jutte or Spike."
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 10,
                "data": "Melee, Slashing",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 11,
                "data": {
                    "headers": [
                        "Melee, Slashing",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Axe, Small",
                            "S",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "Hatchet or Tomahawk."
                        ],
                        [
                            "Axe, Large",
                            "S",
                            "0",
                            "+5",
                            "+15",
                            "5",
                            "0-5' (0-1.5 m)",
                            "2",
                            "Great Axe or Hooked Axe."
                        ],
                        [
                            "Blade, Short",
                            "S",
                            "+4",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "1",
                            "Fighting Fan, Gladius, Kukri, Sickle, Short Sword, Stiletto or Wakizashi."
                        ],
                        [
                            "Blade, Long",
                            "S",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-5' (0-1.5 m)",
                            "1",
                            "Cutlass, Khopesh, Long Sword, Nine-Ring Sword or Scimitar."
                        ],
                        [
                            "Blade, Huge",
                            "S",
                            "0",
                            "+4",
                            "+18",
                            "6",
                            "0-10' (0-3 m)",
                            "2",
                            "Bastard Sword, Claymore, Great Sword, Nodache or Scythe."
                        ],
                        [
                            "Glaive",
                            "S",
                            "0",
                            "+4",
                            "+18",
                            "6",
                            "5-15' (1.5-4.5 m)",
                            "2",
                            "Bardiche, Fauchard, Guisarme, Halberd, Partisan or Voulge."
                        ],
                        [
                            "Whip",
                            "S",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "5-15' (1.5-4.5 m)",
                            "1",
                            "Bull Whip, Nine-Section Whip, Rope Dart or Scourge."
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 12,
                "data": "Traditional Armor",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 13,
                "data": {
                    "headers": [
                        "Traditional Armor",
                        "Soak (C)",
                        "Soak (S)",
                        "Soak (P)",
                        "Soak (E)",
                        "CAP Mod.",
                        "MAP Mod.",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Concealed, Armor",
                            "9",
                            "9",
                            "9",
                            "5",
                            "0",
                            "0",
                            "10",
                            "Hide, Leather or Wood Armor"
                        ],
                        [
                            "Light, Armor",
                            "9",
                            "11",
                            "11",
                            "5",
                            "0",
                            "0",
                            "20",
                            "Brigandine Mail or Studded Leather"
                        ],
                        [
                            "Medium, Armor",
                            "11",
                            "13",
                            "13",
                            "7",
                            "0",
                            "0",
                            "15",
                            "Chainmail or Scale Mail"
                        ],
                        [
                            "Heavy, Armor",
                            "16",
                            "16",
                            "14",
                            "10",
                            "0",
                            "-1",
                            "20",
                            "Banded Mail or Breast Plate"
                        ],
                        [
                            "Cumbersome",
                            "18",
                            "20",
                            "20",
                            "14",
                            "-1",
                            "-2",
                            "50",
                            "Full Plate"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 14,
                "data": "Traditional Shields",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 15,
                "data": {
                    "headers": [
                        "Traditional Shields",
                        "Soak (C)",
                        "Soak (S)",
                        "Soak (P)",
                        "Soak (E)",
                        "CAP Mod.",
                        "MAP Mod.",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Shield, Forearm Strap",
                            "2",
                            "2",
                            "2",
                            "2",
                            "0",
                            "0",
                            "3",
                            "Kote, Forearm & Bracers"
                        ],
                        [
                            "Shield, Medium",
                            "4",
                            "4",
                            "4",
                            "4",
                            "0",
                            "0",
                            "1",
                            "Buckler, Round Shield & Heater"
                        ],
                        [
                            "Shield, Large",
                            "7",
                            "7",
                            "7",
                            "7",
                            "0",
                            "-1",
                            "2",
                            "Tower Shield, Scutum & War Door"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "heading",
                "order": 16,
                "data": "Modern & Future Tech Weapons & Armor"
            },
            {
                "type": "subheading",
                "order": 17,
                "data": "Firearms, Ballistic",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 18,
                "data": {
                    "headers": [
                        "Firearms, Ballistic",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "Slots",
                        "Equip & Reload AP",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Ammo",
                            "P/C/E",
                            "-",
                            "-",
                            "-",
                            "-",
                            "-",
                            "-",
                            "-",
                            "-"
                        ],
                        [
                            "Pistol, Compact",
                            "P",
                            "+1",
                            "+5",
                            "+15",
                            "5",
                            "0-50' (0-15 m)",
                            "1",
                            "1 AP",
                            "10 Round Magazine: Springfield XDS, Kel-Tec PF-9 & Nano"
                        ],
                        [
                            "Pistol, Standard",
                            "P",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-50' (0-15 m)",
                            "2",
                            "1 AP",
                            "20 Round Magazine: Kimber, Taurus 9mm & Sphinx 10mm."
                        ],
                        [
                            "Full Auto Rifle",
                            "P",
                            "+4",
                            "+4",
                            "+18",
                            "6",
                            "5-100' (1.5-20 m)",
                            "1",
                            "2 AP",
                            "30 Round Magazine: AK Models, Beretta ARX 160 & M-16"
                        ],
                        [
                            "Full Auto Combo",
                            "P",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "5-100' (1.5-20 m)",
                            "2",
                            "2 AP",
                            "30 Round Magazine & 1 Launcher Shot"
                        ],
                        [
                            "Launcher",
                            "E",
                            "0",
                            "+3",
                            "+21",
                            "7",
                            "10-150' (3-45 m)",
                            "3",
                            "3 AP",
                            "Connects to Full Auto Combo"
                        ],
                        [
                            "Mini Gun",
                            "P",
                            "0",
                            "+3",
                            "+21",
                            "7",
                            "10-150' (3-45 m)",
                            "3",
                            "5 AP",
                            "10 Attack Bursts"
                        ],
                        [
                            "Rifle, Semi-Auto",
                            "P",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "5-200' (1.5-60 m)",
                            "2",
                            "2 AP",
                            "30 Round Magazine: AR-10, AR-15, Saiga, & M4 Carbine."
                        ],
                        [
                            "Rifle, Standard",
                            "P",
                            "+2",
                            "+5",
                            "+18",
                            "6",
                            "5-250' (1.5-75 m)",
                            "2",
                            "2 AP",
                            "20 Round Magazine: Varmint, Marlin 336XLR, & Henry Big Boy."
                        ],
                        [
                            "Rifle, Sniper",
                            "P",
                            "0",
                            "+3",
                            "+21",
                            "7",
                            "5-300' (1.5-90 m)",
                            "3",
                            "2 AP",
                            "5 Round Magazine: M110, Satevari MSWP & XM2010"
                        ],
                        [
                            "Shotgun, Standard",
                            "C",
                            "+4",
                            "+4",
                            "+14",
                            "5",
                            "0-25' (0-7.5 m)",
                            "3",
                            "3 AP",
                            "10 Shell Tube: Winchester 1887, Remington 870 & Browning Pump"
                        ],
                        [
                            "Shotgun, Tactical",
                            "C",
                            "+4",
                            "+4",
                            "+14",
                            "5",
                            "0-25' (0-7.5 m)",
                            "1",
                            "2 AP",
                            "20 Shell Magazine: Mossberg 500 Persuader, Benelli M4 & Saiga 12"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 19,
                "data": "Firearms, Energy",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 20,
                "data": {
                    "headers": [
                        "Firearms, Energy",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "Slots",
                        "Equip & Reload AP",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Accelerator, Rifle",
                            "E",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "5-50' (1.5-10 m)",
                            "2",
                            "2 AP",
                            "30 Round Magazine"
                        ],
                        [
                            "Disruptor, Rifle",
                            "E",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "5-50' (1.5-10 m)",
                            "2",
                            "2 AP",
                            "100 Shot Cartridge"
                        ],
                        [
                            "AperCoil, Small",
                            "E",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "0-25' (0-7.5 m)",
                            "2",
                            "1 AP",
                            "5 Shot Cartridge"
                        ],
                        [
                            "AperCoil, Hand",
                            "E",
                            "+2",
                            "+5",
                            "+15",
                            "5",
                            "0-50' (0-15 m)",
                            "2",
                            "1 AP",
                            "20 Shot Cartridge"
                        ],
                        [
                            "AperCoil, Rifle",
                            "E",
                            "+2",
                            "+4",
                            "+18",
                            "6",
                            "5-100' (1.5-20 m)",
                            "2",
                            "2 AP",
                            "50 Shot Cartridge"
                        ],
                        [
                            "Plasma, Launcher",
                            "E",
                            "0",
                            "+3",
                            "+21",
                            "7",
                            "25-75 (7.5-22.5)",
                            "3",
                            "3 AP",
                            "5 Shot Cartridge"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 21,
                "data": "Melee, Energy",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 22,
                "data": {
                    "headers": [
                        "Melee, Energy",
                        "Dmg. Type",
                        "Speed Mod.",
                        "Strike Mod.",
                        "Dmg. Mod.",
                        "CAP",
                        "Range",
                        "Slots",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Darkblade",
                            "E",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "2",
                            "-",
                            "-"
                        ],
                        [
                            "Monofil Lash",
                            "E",
                            "+1",
                            "+5",
                            "+15",
                            "5",
                            "0-10' (0-3 m)",
                            "4",
                            "-",
                            "-"
                        ],
                        [
                            "Tri-Pulse, Claws",
                            "E",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "2",
                            "-",
                            "-"
                        ],
                        [
                            "Tri-Pulse, Kukri",
                            "E",
                            "+2",
                            "+6",
                            "+12",
                            "4",
                            "0-5' (0-1.5 m)",
                            "2",
                            "-",
                            "-"
                        ],
                        [
                            "Tri-Pulse, Pike",
                            "E",
                            "+1",
                            "+5",
                            "+15",
                            "5",
                            "0-10' (0-3 m)",
                            "4",
                            "-",
                            "-"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 23,
                "data": "Modern Armor",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 24,
                "data": {
                    "headers": [
                        "Modern Armor",
                        "Soak (C)",
                        "Soak (S)",
                        "Soak (P)",
                        "Soak (E)",
                        "CAP Mod.",
                        "MAP Mod.",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Concealed, Armor",
                            "5",
                            "11",
                            "11",
                            "5",
                            "0",
                            "0",
                            "10",
                            "Concealed Kevlar"
                        ],
                        [
                            "Light, Armor",
                            "7",
                            "13",
                            "13",
                            "7",
                            "0",
                            "0",
                            "20",
                            "Concealed Kevlar with Vital Plates"
                        ],
                        [
                            "Medium, Armor",
                            "11",
                            "15",
                            "15",
                            "9",
                            "0",
                            "0",
                            "15",
                            "Tactical Vest"
                        ],
                        [
                            "Heavy, Armor",
                            "16",
                            "18",
                            "18",
                            "12",
                            "0",
                            "-1",
                            "20",
                            "Tactical Vest with Vital Plates"
                        ],
                        [
                            "Cumbersome",
                            "22",
                            "20",
                            "20",
                            "16",
                            "-1",
                            "-2",
                            "50",
                            "Riot Gear"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 25,
                "data": "Modern Shields",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 26,
                "data": {
                    "headers": [
                        "Modern Shields",
                        "Soak (C)",
                        "Soak (S)",
                        "Soak (P)",
                        "Soak (E)",
                        "CAP Mod.",
                        "MAP Mod.",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Shield, Forearm Strap",
                            "3",
                            "3",
                            "3",
                            "3",
                            "0",
                            "0",
                            "3",
                            "Kote, Arm Shield & Bracers"
                        ],
                        [
                            "Shield, Medium",
                            "5",
                            "5",
                            "5",
                            "5",
                            "0",
                            "0",
                            "1",
                            "Ballistic Shield, Round Shield & 4 Point"
                        ],
                        [
                            "Shield, Large",
                            "8",
                            "8",
                            "8",
                            "8",
                            "0",
                            "-1",
                            "2",
                            "Ballistic Wall Shield & Riot Shield"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 27,
                "data": "Future Tech Armor",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 28,
                "data": {
                    "headers": [
                        "Future Tech Armor",
                        "Soak (C)",
                        "Soak (S)",
                        "Soak (P)",
                        "Soak (E)",
                        "CAP Mod.",
                        "MAP Mod.",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Concealed, Armor",
                            "9",
                            "9",
                            "9",
                            "9",
                            "0",
                            "0",
                            "10",
                            "Skin Mesh Body Suit"
                        ],
                        [
                            "Light, Armor",
                            "9",
                            "13",
                            "13",
                            "9",
                            "0",
                            "0",
                            "20",
                            "Kote Mesh Fiber"
                        ],
                        [
                            "Medium, Armor",
                            "13",
                            "15",
                            "15",
                            "11",
                            "0",
                            "0",
                            "15",
                            "Spacer Vest"
                        ],
                        [
                            "Heavy, Armor",
                            "18",
                            "18",
                            "18",
                            "14",
                            "0",
                            "-1",
                            "20",
                            "Plexiclear Combat Armor"
                        ],
                        [
                            "Cumbersome",
                            "24",
                            "20",
                            "20",
                            "18",
                            "-1",
                            "-2",
                            "50",
                            "Tactical Assault Armor"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
            {
                "type": "subheading",
                "order": 29,
                "data": "Future Tech Shields",
                "style_class": "text-xl italic mt-8 text-blue-400"
            },
            {
                "type": "table",
                "order": 30,
                "data": {
                    "headers": [
                        "Future Tech Shields",
                        "Soak (C)",
                        "Soak (S)",
                        "Soak (P)",
                        "Soak (E)",
                        "CAP Mod.",
                        "MAP Mod.",
                        "AP to Equip",
                        "Examples"
                    ],
                    "rows": [
                        [
                            "Shield, Forearm Strap",
                            "6",
                            "6",
                            "6",
                            "6",
                            "0",
                            "0",
                            "3",
                            "Arm Energy Deflector"
                        ],
                        [
                            "Shield, Medium",
                            "9",
                            "9",
                            "9",
                            "9",
                            "0",
                            "0",
                            "1",
                            "Single Side Expanding Energy Deflector"
                        ],
                        [
                            "Shield, Large",
                            "12",
                            "12",
                            "12",
                            "12",
                            "12",
                            "-1",
                            "2",
                            "360 Expanding Energy Deflector"
                        ]
                    ]
                },
                "style_class": "table-auto border-collapse border border-gray-300"
            },
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
    },
    {
        "title": "Species Creation",
        "slug": "species-creation",
        "chapter": "Customization Options",
        "content": [
            {
                "type": "heading",
                "order": 1,
                "data": "Creation Guidelines"
            },
            {
                "type": "subheading",
                "order": 2,
                "data": "Select Species Name",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "subheading",
                "order": 3,
                "data": "Describe Species",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "subheading",
                "order": 4,
                "data": "Select Weight Multiplier: 1 to 4",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "paragraph",
                "order": 5,
                "data": "A species Weight Multiplier (WM) is based on how dense a creature's skeletal structure and muscle mass is."
            },
            {
                "type": "paragraph",
                "order": 6,
                "data": "This base number is their Fit Weight Multiplier (FWM)."
            },
            {
                "type": "list",
                "order": 7,
                "data": [
                    "FWM - .25 = Slim WM",
                    "FWM - .50 = Emaciated WM",
                    "FWM + .25 = Heavy WM",
                    "FWM + .50 = Muscular WM",
                    "FWM + .75 = Burly WM",
                    "FWM + 1.00 = Obese WM"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 8,
                "data": "Height in 1\" (2.54cm) * Weight Multiplier = Weight"
            },
            {
                "type": "subheading",
                "order": 9,
                "data": "Creation Maturation Point Exchange Rate",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "subheading",
                "order": 10,
                "data": "Life Span:",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 11,
                "data": [
                    "50 Years = -10",
                    "75 Years = 0",
                    "250 Years = 5",
                    "500 Years = 10"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 12,
                "data": "Attributes Bonus:",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 13,
                "data": [
                    "Two +1 Attribute Bonus are Free",
                    "Each Additional +1 Attribute Bonus = 5",
                    "(No more than +4 can be placed in a single Attribute)"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 14,
                "data": "Skill Bonus:",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 15,
                "data": [
                    "Four +1 to Non-Combat Skills are Free",
                    "Two +1 to Non-Combat Skills = 5",
                    "(No more than +2 can be placed in a single skill.)"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 16,
                "data": "Dark Vision:",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 17,
                "data": [
                    "No Dark Vision = -15",
                    "No Low Light Vision = -15",
                    "Darkvision 50' = 0",
                    "Darkvision 75' = 5",
                    "Darkvision 100' = 10",
                    "Darkvision 125' = 15"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 18,
                "data": "Special Powers:",
                "style_class": "text-xl italic mt-2 text-blue-400"
            },
            {
                "type": "list",
                "order": 19,
                "data": [
                    "Charmed Feeding = 5",
                    "Elemental Resistance = 5",
                    "Keen Perception = 10",
                    "Kin",
                    "Airkin = 10",
                    "Earthkin = 10",
                    "Firekin = 10",
                    "Naturekin = 10",
                    "Waterkin = 10",
                    "Natural Retractable Claws = 5",
                    "Stone Talking = 10",
                    "Lesser Stone Talking = 5"
                ],
                "style_class": "list-disc pl-6"
            },
        ]
    },
    {
        "title": "Dylithar",
        "slug": "dylithar",
        "chapter": "Races",
        "content": [
            {
                "type": "paragraph",
                "order": 2,
                "data": "Core, Faeyr | Cost: 40 Maturation | SHP: 4"
            },
            {
                "type": "subheading",
                "order": 3,
                "data": "Attributes Rolls Bonus",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "list",
                "order": 4,
                "data": [
                    "+2 Perception",
                    "+2 Reflexes",
                    "+1 Strength"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 5,
                "data": "Skills Rolls Bonus",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "list",
                "order": 6,
                "data": [
                    "+2 Power",
                    "-2 Cultures",
                    "-2 Riding"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "list",
                "order": 7,
                "data": [
                    "Males: +2 Persuasion",
                    "Females: +2 Occult"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "list",
                "order": 8,
                "data": [
                    "Low Light Vision: 75'",
                    "Darkvision: 125’",
                    "Keen Perception"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 9,
                "data": "Typical Male Height: D10+59\" | Typical Female Height: D10+55\""
            },
            {
                "type": "paragraph",
                "order": 10,
                "data": "System of Government: Federalist Meritocracy-based Anocracy | Native Language(s): Faeyr | Life Span: 500 Years | Age of Adulthood: 20"
            },
            {
                "type": "subheading",
                "order": 11,
                "data": "Backstory",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 12,
                "data": "The Dylithar are descended from an enigmatic otherworldly bloodline of Faeyr, whose turbulent past spans across several planes of existence. Long ago, they suffered under the cruel manipulation of demonic forces until an uprising led by four courageous siblings changed the destiny of the entire species. Their journey brought them to Darkholme, where they seized refuge but ignited wars among immortals and pseudo-immortals. After the intervention of the Weaver, the Dylithar secured their place, reshaping the Isles of Isk'laketh. Today, Dylithar move through realms as navigators, spies, scholars, and wielders of ancient power."
            },
            {
                "type": "subheading",
                "order": 13,
                "data": "Description",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 14,
                "data": "Dylithar possess dark skin ranging from deep ebony to soft violet. Their bodies are adorned with tattoos that react to their emotions and powers. Males are notably agile, excelling in sailing and acrobatics, while females show a slightly stronger frame with a deeper connection to arcane energies, often reflected in gemstone-decorated attire and intricate tattoos."
            },
            {
                "type": "subheading",
                "order": 15,
                "data": "Complexion, Hair, and Eyes",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 16,
                "data": "Skin tones range from night-sky ebony to twilight violet. Hair flows in colors from black and silver to fiery red. Their irises glow in mesmerizing shades of magenta, lavender, or sapphire blue against dark sclera, marking their profound heritage."
            },
            {
                "type": "subheading",
                "order": 17,
                "data": "Accentuations",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 18,
                "data": "Males favor agile, practical clothing; females often wear garments woven with gemstones and arcane embroidery. Each Dylithar wears their lineage like a second skin, blending strength, mysticism, and beauty into a graceful, enigmatic presence."
            },
            {
                "type": "subheading",
                "order": 19,
                "data": "Culture",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 20,
                "data": "Dylithar culture prizes ambition, individuality, and adaptability. Their fluid hierarchies reward influence and arcane prowess over pure birthright, although old bloodlines still weave newcomers into their folds. They are skilled scholars, spies, and masters of illusion, bound by webs of trust and shared secrets."
            },
            {
                "type": "subheading",
                "order": 21,
                "data": "Quirky Fact",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 22,
                "data": "Dylithar cherish facial hair as a rare trait among Faeyr, grooming it with pride. Their skin shifts with the day, lightening under the sun and darkening at night, allowing them to blend effortlessly with their surroundings."
            }
        ]
    },
    {
        "title": "Miaki",
        "slug": "miaki",
        "chapter": "Races",
        "content": [
            {
                "type": "heading",
                "order": 1,
                "data": "Miaki"
            },
            {
                "type": "paragraph",
                "order": 2,
                "data": "Core, Faeyr | Cost: 40 Maturation | SHP: 4"
            },
            {
                "type": "subheading",
                "order": 25,
                "data": "Attributes Rolls Bonus",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "list",
                "order": 26,
                "data": [
                    "+2 Perception",
                    "Males: +2 Reflexes & +4 Strength",
                    "Females: +4 Reflexes & +2 Strength"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 27,
                "data": "Skills Rolls Bonus",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "list",
                "order": 28,
                "data": [
                    "+2 Performance",
                    "+2 Sleight of Hand",
                    "+2 Stealth",
                    "-2 Artisan",
                    "-2 Willpower"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "list",
                "order": 29,
                "data": [
                    "Low Light Vision: 100'",
                    "Darkvision: 100’",
                    "Enslaved",
                    "Keen Perception"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 30,
                "data": "Typical Male Height: D10+57\" | Typical Female Height: D10+53\""
            },
            {
                "type": "paragraph",
                "order": 31,
                "data": "System of Government: Feudalistic Divine Monarchy Under the Empress | Native Language(s): Xi | Life Span: 500 Years | Age of Adulthood: 20"
            },
            {
                "type": "subheading",
                "order": 32,
                "data": "Backstory",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 33,
                "data": "The Miaki were once the wildest and most nature-attuned Faeyr before being subjugated by the Xi through brutal cultural genocide, eugenics, and magical binding rituals. Bound Miaki serve nobility as fiercely loyal protectors, escorts, and spies. Unbound Miaki are a rare and coveted resource. The Miaki see their servitude as a sacred honor, woven deeply into their sense of duty and identity."
            },
            {
                "type": "subheading",
                "order": 34,
                "data": "Description",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 35,
                "data": "Miaki exhibit a harmonious balance of strength and agility. Males are nimble and alert, while females are even more dexterous, though slightly less physically strong. Their movements are deliberate and graceful, a reflection of their bond with nature and their conditioned roles within noble houses."
            },
            {
                "type": "subheading",
                "order": 36,
                "data": "Complexion, Hair, and Eyes",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 37,
                "data": "Their skin tones mirror the earth and changing seasons, ranging from fertile soil brown to autumnal golds and reds. Hair varies from deep earthen hues to fiery autumn tones, while their almond-shaped eyes shimmer in shades of green, blue, and woodland hazel."
            },
            {
                "type": "subheading",
                "order": 38,
                "data": "Accentuations",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 39,
                "data": "Wild Miaki attire blends naturally into their environment for camouflage, while bound Miaki wear garments dictated by the noble houses they serve, often reflecting their master’s wealth and status but always retaining elegance and grace."
            },
            {
                "type": "subheading",
                "order": 40,
                "data": "Culture",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 41,
                "data": "Miaki society is deeply tied to service and loyalty. A Miaki's bond to their noble house is sacred, and they are trained from birth to protect, serve, and uphold the house's honor. Unbound Miaki are seen as a vital resource and must be carefully protected and ceremonially bonded, or risk cultural and personal catastrophe."
            },
            {
                "type": "subheading",
                "order": 42,
                "data": "Quirky Fact",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 43,
                "data": "Miaki cannot be properly bound without the destruction of their Birth Scroll. Loss of the scroll without binding results in death. If left unbound beyond their 18th year, Miaki are doomed to descend into agonizing madness, ultimately leading to suicide unless the binding ritual is completed."
            }
        ]
    },
    {
        "title": "Tiermalain",
        "slug": "tiermalain",
        "chapter": "Races",
        "content": [
            {
                "type": "paragraph",
                "order": 45,
                "data": "Core, Faeyr | Cost: 40 Maturation | SHP: 4"
            },
            {
                "type": "subheading",
                "order": 46,
                "data": "Attributes Rolls Bonus",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "list",
                "order": 47,
                "data": [
                    "+3 Perception",
                    "+2 Reflexes"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "subheading",
                "order": 48,
                "data": "Skills Rolls Bonus",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "list",
                "order": 49,
                "data": [
                    "+2 Athletics",
                    "+2 Awareness",
                    "+1 Occult",
                    "+1 Stealth",
                    "-2 Sailing"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "list",
                "order": 50,
                "data": [
                    "Low Light Vision: 125'",
                    "Darkvision: 75’",
                    "Keen Perception"
                ],
                "style_class": "list-disc pl-6"
            },
            {
                "type": "paragraph",
                "order": 51,
                "data": "Typical Male Height: D10+60\" | Typical Female Height: D10+56\""
            },
            {
                "type": "paragraph",
                "order": 52,
                "data": "System of Government: Nepotistic Anocracy under Nobility Purview | Native Language(s): Faeyr | Life Span: 500 Years | Age of Adulthood: 20"
            },
            {
                "type": "subheading",
                "order": 53,
                "data": "Backstory",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 54,
                "data": "Tiermalain are the last noble Faeyr of Darkholme, deeply entwined with the wilderness and its magic. After the Sundering, which sealed much of Darkholme’s arcane potential and shortened their lives, the Tiermalain became guardians of the old ways. They built libraries, pursued philosophy, and engaged in worldly affairs to protect their heritage against invaders, while some youths sought knowledge, adventure, and artifacts beyond their ancestral lands."
            },
            {
                "type": "subheading",
                "order": 55,
                "data": "Description",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 56,
                "data": "Tiermalain display a versatile athleticism, with robust, well-tanned bodies shaped by their bond to nature. Agile and resilient, both males and females share a balanced physique that blends grace with capability, well-suited to traversing Darkholme's rugged terrains and magical forests."
            },
            {
                "type": "subheading",
                "order": 57,
                "data": "Complexion, Hair, and Eyes",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 58,
                "data": "Their skin ranges from sun-kissed bronze to cool vanilla hues. Hair flows in metallic shades of bronze, gold, or coppery red. Their eyes gleam in hazel, blue, or green tones, reflecting ancient wisdom and their affinity with the magic of Darkholme."
            },
            {
                "type": "subheading",
                "order": 59,
                "data": "Accentuations",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 60,
                "data": "Tiermalain attire harmonizes with nature, featuring earth-toned fabrics adorned with motifs of leaves and vines. Their tattoos tell stories of lineage and deeds, while jewelry of rare Darkholme gemstones ties them spiritually to the land’s deep magic."
            },
            {
                "type": "subheading",
                "order": 61,
                "data": "Culture",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 62,
                "data": "Tiermalain culture reveres the balance between civilization and nature. They are scholars, magisters, and adventurers who seek to defend Darkholme’s sanctity. Education and philosophical reflection are paramount, and journeys into the wider world are rites of passage before returning to serve and protect their ancestral home."
            },
            {
                "type": "subheading",
                "order": 63,
                "data": "Quirky Fact",
                "style_class": "text-xl italic mt-2 text-gray-400"
            },
            {
                "type": "paragraph",
                "order": 64,
                "data": "Some Tiermalain can communicate with Darkholme’s ancient trees through tree-speech, sharing thoughts and gathering wisdom. In times of danger, these sentient trees may awaken ancient magic to assist their Tiermalain kin by binding invaders or bestowing ancient secrets hidden within their roots."
            }
        ]
    }
]


    # Now seed sections and contents
    for section_data in sections:
        section = Section(
            title=section_data[
    "title"
],
            slug=section_data[
    "slug"
],
            chapter=section_data[
    "chapter"
]
        )
        db.session.add(section)
        db.session.commit()

        for content_data in section_data[
    "content"
]:
            if isinstance(content_data[
    "data"
], str):
                cleaned_data = clean_text(content_data[
    "data"
])
            else:
                cleaned_data = content_data[
    "data"
]

            content = Content(
                section_id=section.id,
                content_type=content_data[
    "type"
],
                content_order=content_data[
    "order"
],
                content_data=cleaned_data,
                style_class=clean_text(content_data.get("style_class",
""))
            )
            db.session.add(content)

    db.session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        print("Application context is active.")
        seed_rules()