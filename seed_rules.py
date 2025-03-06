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
            "title": "Prelude: Character Concepts & Components",
            "slug": "prelude",
            "chapter": "Character Creation",
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
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": """
                        Before we delve into character creation mechanics, let's first envision who your character will be. 
                        Reflect on the genre and setting, then consider these intriguing questions: Who is your character? Where 
                        did they grow up? What's their occupation? Who are their friends and family? What drives them, and what 
                        are their aspirations, both immediate and long-term?
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": """
                        With their backstory in place, it's time to bring your character to life. Choose their name, height, weight, 
                        gender, age, and give us a snapshot of their appearance. Next, dive into the finer details: Is your character 
                        slim or sturdy? Are they charming or less so? Any distinctive features like tattoos or scars that make them stand out?
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": """
                        You've now laid a solid foundation that will guide you through the mechanics of character creation and enhance your 
                        role-playing experience. Every character we create has a bit of us in them—our unique touch that shines through. As you 
                        build your character, infuse them with qualities that make them unforgettable, all while letting your own personality subtly 
                        influence their essence.
                    """.replace("\n", " ").strip()
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": """
                        In the upcoming sections, we'll not only help you sculpt your character's virtues and vices 
                        but also navigate the technical aspects of bringing your character to life in the L.O.T.U.S. RPG system. 
                        Let's make your character truly memorable!
                    """.replace("\n", " ").strip()
                }
            ]
        },
        {
            "title": "Approaches: Utilizing Living Philosophies",
            "slug": "approaches",
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "title": "The Virtues, Failings, Vices & Balance",
            "slug": "virtues-vices", 
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "title": "Abilities, Skills & Core Mechanics",
            "slug": "section-two",
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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
            "chapter": "Character Creation",
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