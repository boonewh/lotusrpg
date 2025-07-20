from lotusrpg import create_app, db
from lotusrpg.models import Section, Content
import re

def clean_text(text): 
    if not isinstance(text, str):  
        return text
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()

def seed_rules():
    print("Seeding Darkholme rules...")

    db.session.query(Content).filter(Content.section_id.in_(
        db.session.query(Section.id).filter_by(rulebook='darkholme')
    )).delete(synchronize_session=False)

    db.session.query(Section).filter_by(rulebook='darkholme').delete()
    db.session.commit()

    sections = [
        {
            "title": "The World of Darkholme",
            "slug": "darkholme-world",
            "chapter": "Introduction to Darkholme",
            "rulebook": "darkholme",
            "content": [
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Darkholme is a world setting that exists between the realms of high fantasy and seinen action drama. It is a world of powerful characters who can perform extraordinary feats that often defy normal logic. Arcane casters hurl power essence filled magic while elementally endowed warriors take the field performing physical acts beyond our mundane realm. Despite these amazing abilities the times have made it a darkened world after the great fall of civilizations. This collapse was wrought by Demons and Voidlings flooding the realms before being pushed back by combined efforts of the core species of Humans, Faeyr, Svar and Romling. New empires have arisen from this decimation and now that the greater threat is contained for a time, the allies of old have turned their sights upon one another looking to establish a future for their people amidst the introduction of other species vying for their own claims amidst the realm."
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "- Lucien Grey"
                }
            ]
        },
        {
            "title": "Arcane Trinkets, Treasures, & Artifacts ",
            "slug": "arcane-trinkets",
            "chapter": "Items & Crafting",
            "rulebook": "darkholme",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Types"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "Accessories, Belts (Waist), Cravats (Neck), Eye Patches (1 Eye Overlay), Hand Fans (Handheld), Sashes (Chest Overlay), Scarves (Neck), Stockings (Leggings Underlay), Ties (Neck) & Umbrellas (Handheld)"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Armor (Chest), Corset (Chest), Bandoliers (Chest Overlay), Bracers (Wristwear), Kote (Wristwear) & Shields (Handheld)"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Boots (Footwear), Shoes (Footwear), Slippers (Footwear), Pair of Gloves (Handwear), Hat (Headwear), Helm (Headwear), Tiara (Headwear) & Crown (Headwear)"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Cloak (Shoulder), Overcoat (Shoulder), Trench Coat (Shoulder)"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Shirt (Chest Overlay), Undershirt (Chest Underlay), Vest (Chest Overlay), Kilt (Leggings), Hakama (Leggings), Skirt (Leggings), Pants (Leggings) & Shorts (Leggings)"
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "Backpacks (Back), Bags, Barrels, Baskets, Bottles, Buckets, Chests, Clutch Frames, Jugs, Kegs, Pockets, Pouches, Purses, Messenger Bags, Saddlebags, Satchels, Trunks, Wallets, Wineskins & Wristlets"
                },
                {
                    "type": "paragraph",
                    "order": 8,
                    "data": "Bracelets (Wristwear), Cufflinks (Wristwear), Earrings (Head Overlay), Emblems (Overlay), Glasses (Head Overlay), Medallions (Overlay), Necklaces (Neck), Piercings (Overlay), Pins (Overlay), Rings (1 Finger) & Watches (Pocket)"
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "Rods, Staves & Wands (RSW): These items serve as conduits for channeling magical energy, allowing the wielder to cast spells, summon creatures, or manipulate the elements with greater ease and potency."
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "Weapons: Crushing, Piercing, Energy, Slashing Weapons: Magical weapons capable of performing a wide variety of functions based on their design and purpose."
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "Weird: Any item that doesn’t call into the aforementioned categories."
                },
                {
                    "type": "heading",
                    "order": 12,
                    "data": "Creation"
                },
                {
                    "type": "paragraph",
                    "order": 13,
                    "data": "Creating Items requires the expenditure of XP and the creator’s Level of Enchanting = Tier of the Item Created. This Tier is also referenced when selecting the item as the reward for increasing Arcanum Enchantment. Slight variances in the creation process allow the creator to change flavor text aspects of the item though it does not change the purpose or operation. For example, by adding a sapphire into the creation process of a RSW (Rod/Stave/Wand) of Entertaining Pyrotechnics the creator may ensure all pyrotechnics have an azure flame or by integrating Exceptional Quality Hazelnuts into a Depot of Endless Coffee that the coffee produced always has the comforting aroma and taste of hazelnut coffee."
                },
                {
                    "type": "paragraph",
                    "order": 14,
                    "data": "Trinkets are lower tier creations and are considered the weakest and most common of magical items. These may frequently be purchased in large cities. Creation of a Trinket requires:"
                },
                {
                    "type": "list",
                    "order": 15,
                    "data": [
                        "Expenditure of Creation XP.",
                        "100 Copper Pieces in Materials per Tier of Trinket.",
                        "Flavor text components determined by the Game Master to allow for creator item preference variance.",
                        "A teacher or having previously created the item or a creation recipe tome."
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "Treasures are strong arcana items that are of significant value and use in their applied field. These may occasionally be purchased from an extravagant vendor, but the selection is always very limited. Creation of a Treasure requires:"
                },
                {
                    "type": "list",
                    "order": 17,
                    "data": [
                        "Expenditure of Creation XP.",
                        "100 Silver Pieces in Materials per Tier of Treasure.",
                        "Flavor text components determined by the Game Master to allow for creator item preference variance.",
                        "A teacher or having previously created the item or a creation recipe tome.",
                        "All key components listed for the item’s creation."
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "Artifacts are rare, unique, and powerful arcana items that are of exceptional value and use in their applied field. These are never simply found for sale via simple currency transaction. Creation of an Artifact requires:"
                },
                {
                    "type": "list",
                    "order": 19,
                    "data": [
                        "Expenditure of Creation XP.",
                        "Sacrifice 1 Year of Life per Tier of Artifact.",
                        "100 Gold Pieces in Materials per Tier of Treasure.",
                        "Flavor text components determined by the Game Master to allow for creator item preference variance.",
                        "A teacher or having previously created the item or a creation recipe tome.",
                        "All key components listed for the item’s creation."
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                }
            ]
        },
        {
            "title": "Abjuration",
            "slug": "abjuration",
            "chapter": "Arcana",
            "rulebook": "darkholme",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Abjuration"
                },
                {
                    "type": "paragraph",
                    "order": 2,
                    "data": "(Free Content)",
                    "style_class": "text-red-400 italic"
                },
                {
                    "type": "paragraph",
                    "order": 3,
                    "data": "Abjuration is the arcane discipline of protection, suppression, and magical denial. Practitioners of this art shield allies from harm, reinforce barriers both mundane and mystical, and unravel hostile spells before they take hold. While often overlooked compared to more destructive arts, Abjuration is a subtle but indispensable force on the battlefield. Its casters are guardians of the weave — shaping magic not to dazzle or destroy, but to preserve, endure, and defy."
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "(Every Rank of Abjuration Increase All Soak by 1)"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "Use the highest benefit of each Type (Attribute, Skill or Other Bonus). Recurring Types are not cumulative and use the highest value listed."
                },
                {
                    "type": "heading",
                    "order": 6,
                    "data": "1) Arcane Armor",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 7,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 8,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 9,
                    "data": "Spell:  Arcane Armor"
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "PREQs:  Abjuration Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "Range:  Touch"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "AoE:  1 Target"
                },
                {
                    "type": "container",
                    "order": 13,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 14,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "Essence:  1"
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "CAP:  4"
                },
                {
                    "type": "paragraph",
                    "order": 17,
                    "data": "Duration:  20 Minutes per ML"
                },
                {
                    "type": "container",
                    "order": 18,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 19,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "A protective force surrounds you, manifesting as a phantasmal gilding that covers you and your gear. Your soak is increased by 2 per Tier of Abjuration. The color and sheen of the gilding is determined by the caster when this spell is purchased and has signature-like characteristics."
                },
                {
                    "type": "heading",
                    "order": 21,
                    "data": "2) Absorb Element",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 22,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 23,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 24,
                    "data": "Spell:  Absorb Element"
                },
                {
                    "type": "paragraph",
                    "order": 25,
                    "data": "PREQs:  Abjuration Tier 2 & Element Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 26,
                    "data": "Range:  Touch"
                },
                {
                    "type": "paragraph",
                    "order": 27,
                    "data": "AoE:  1 Target"
                },
                {
                    "type": "container",
                    "order": 28,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 29,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "Essence:  2"
                },
                {
                    "type": "paragraph",
                    "order": 31,
                    "data": "CAP:  4"
                },
                {
                    "type": "paragraph",
                    "order": 32,
                    "data": "Duration:  20 Minutes per ML"
                },
                {
                    "type": "container",
                    "order": 33,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 34,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 35,
                    "data": "A protective force surrounds you; manifesting is a phantasmal elemental gilding that covers you and your gear. Your soak against the Associated Element is increased by 2 per Tier of Abjuration. The color and sheen of the gilding is determined by the caster when this spell is purchased and has signature-like characteristics but is reflective of the element being protected against."
                },
                {
                    "type": "paragraph",
                    "order": 36,
                    "data": "Reflect Element Variant (+10 XP to Learn) - PREQ is Abjuration 3 & Associated Element 2"
                },
                {
                    "type": "paragraph",
                    "order": 37,
                    "data": "Increase Essence cost by one to modify the phantasmal elemental gilding of the Absorb Element spell. Every 5 BHP successfully soaked adds 1 BHP of Damage to your next successful attack whether it is Melee or Arcane."
                },
                {
                    "type": "heading",
                    "order": 38,
                    "data": "3) Secure Barrier",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 39,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 40,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 41,
                    "data": "Spell:  Secure Barrier"
                },
                {
                    "type": "paragraph",
                    "order": 42,
                    "data": "PREQs:  Varies: Abjuration Tier 2, 3, 4 & 8"
                },
                {
                    "type": "paragraph",
                    "order": 43,
                    "data": "Range:  Touch"
                },
                {
                    "type": "paragraph",
                    "order": 44,
                    "data": "AoE:  1 Target"
                },
                {
                    "type": "container",
                    "order": 45,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 46,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 47,
                    "data": "Essence:  2 / 3 / 4 / 8"
                },
                {
                    "type": "paragraph",
                    "order": 48,
                    "data": "CAP:  4 / 5 / 5 / 7"
                },
                {
                    "type": "paragraph",
                    "order": 49,
                    "data": "Duration:  1 Hour per ML"
                },
                {
                    "type": "container",
                    "order": 50,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 51,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 52,
                    "data": "Lesser Secure Barrier - PREQ Abjuration Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 53,
                    "data": "You touch a closed door, window, gate, chest, or other means of ingress or egress, and it becomes magically sealed. You and creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this this effect for 1 minute and prevents any Wards from triggering. The barrier may still be broken down but the difficulty to do so is increased and requires the aggressor to make a Power Sum + ML v. Occult Sum + Abjuration + ML, but it cannot be mundanely unlocked."
                },
                {
                    "type": "paragraph",
                    "order": 54,
                    "data": "Secure Barrier (+5 XP to Learn) - PREQ Abjuration Tier 3"
                },
                {
                    "type": "paragraph",
                    "order": 55,
                    "data": "Increase Essence expenditure by 1 making this barrier harder to breach as the barrier is increased by ML +5."
                },
                {
                    "type": "paragraph",
                    "order": 56,
                    "data": "Greater Secure Barrier (+5 XP to Learn) - PREQ Abjuration Tier 4"
                },
                {
                    "type": "paragraph",
                    "order": 57,
                    "data": "Increase Essence expenditure by 2 making this barrier harder to breach as the barrier is increased by ML +10."
                },
                {
                    "type": "paragraph",
                    "order": 58,
                    "data": "True Secure Barrier (+20 XP to Learn) - PREQ Abjuration Tier 8"
                },
                {
                    "type": "paragraph",
                    "order": 59,
                    "data": "Increase Essence expenditure by 6 making this barrier harder to breach as the barrier cannot be broken down by raw force."
                },
                {
                    "type": "paragraph",
                    "order": 60,
                    "data": "Unseal Barrier (+10 XP to Learn) - Unseal Barrier suppresses the barriers security for 1 hour. This requires an Occult Sum + Abjuration Sum + ML v. Intellect + Occult Sum + Abjuration Sum + ML."
                },
                {
                    "type": "paragraph",
                    "order": 61,
                    "data": "Ward Barrier (+20 XP to Learn) - PREQ Secure Barrier & Ward Spell."
                },
                {
                    "type": "paragraph",
                    "order": 62,
                    "data": "Add once a Barrier is secured then add any Ward known by the caster to the barrier. This Ward is activated if the barrier is breached, and the Ward is not magically disrupted."
                },
                {
                    "type": "heading",
                    "order": 63,
                    "data": "4) Counter Spell",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 64,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 65,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 66,
                    "data": "Spell:  Counter Spell"
                },
                {
                    "type": "paragraph",
                    "order": 67,
                    "data": "PREQs:  Abjuration Tier 3"
                },
                {
                    "type": "paragraph",
                    "order": 68,
                    "data": "Range:  10’ (3M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 69,
                    "data": "AoE:  1 Target"
                },
                {
                    "type": "container",
                    "order": 70,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 71,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 72,
                    "data": "Essence:  3"
                },
                {
                    "type": "paragraph",
                    "order": 73,
                    "data": "CAP:  5"
                },
                {
                    "type": "paragraph",
                    "order": 74,
                    "data": "Duration:  Instantaneous: Interrupt"
                },
                {
                    "type": "container",
                    "order": 75,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 76,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 77,
                    "data": "When the caster sees a creature within range casting a spell then they may attempt to disrupt the gathering energy and disperse it back to the weave. If the caster knows the spell, CAP is available, and the Caster has an Abjuration Rank equal to the Highest Arcanum of the spell being cast then they may attempt countering. The caster instinctually knows if they can attempt to counter a spell based on the power of the forces being gathered. To counter a spell, you must make an Occult Sum + Abjuration Sum + ML v. Occult Sum + Spell’s Highest Arcanum Sum + ML."
                },
                {
                    "type": "heading",
                    "order": 78,
                    "data": "5) Disrupt Magic",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 79,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 80,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 81,
                    "data": "Spell:  Disrupt Magic"
                },
                {
                    "type": "paragraph",
                    "order": 82,
                    "data": "PREQs:  Varies: Abjuration Tier 4, 7 & 10"
                },
                {
                    "type": "paragraph",
                    "order": 83,
                    "data": "Range:  10’ (3M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 84,
                    "data": "AoE:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 85,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 86,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 87,
                    "data": "Essence:  4 / 7 / 10"
                },
                {
                    "type": "paragraph",
                    "order": 88,
                    "data": "CAP:  5 / 7 / 8"
                },
                {
                    "type": "paragraph",
                    "order": 89,
                    "data": "Duration:  20 Minutes per ML"
                },
                {
                    "type": "container",
                    "order": 90,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 91,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 92,
                    "data": "Lesser Disrupt Magic - PREQ is Abjuration Tier 4"
                },
                {
                    "type": "paragraph",
                    "order": 93,
                    "data": "Choose a single magical effect within range. A selected spell or magical effect of Arcanum Rank 3 or lower on the target is dispersed. A spell or magical effect of Arcanum Rank 4,5 or 6 is tested against with an Occult Sum + Abjuration Sum + ML v. Occult Sum + Spell’s Highest Arcanum Sum + ML."
                },
                {
                    "type": "paragraph",
                    "order": 94,
                    "data": "Disrupt Magic (+10 XP to Learn) - PREQ is Abjuration Tier 7"
                },
                {
                    "type": "paragraph",
                    "order": 95,
                    "data": "Increase Essence expenditure by 3 and choose a single magical effect within range. A selected spell or magical effect of Arcanum Rank 6 or lower on the target may be selected and dispersed. Each spell of Arcanum Rank 7,8 or 9 is tested against with an Occult Sum + Abjuration Sum + ML v. Occult Sum + Spell’s Highest Arcanum Sum + ML."
                },
                {
                    "type": "paragraph",
                    "order": 96,
                    "data": "True Disruption (+20 XP to Learn) - PREQ is Abjuration Tier 10"
                },
                {
                    "type": "paragraph",
                    "order": 97,
                    "data": "Increase Essence expenditure by 6 Choose a single magical effect within range. Any spell or magical effect of Arcanum Rank 9 or lower on the target is dispersed. Each spell of Arcanum Rank 10 is tested against a single attempt made to disperse the arcane effect with an Occult Sum + Abjuration Sum + ML v. Occult Sum + Spell’s Highest Arcanum Sum + ML."
                }
            ]
        },
        {
            "title": "Conjuration",
            "slug": "conjuration",
            "chapter": "Arcana",
            "rulebook": "darkholme",
            "content": [
                {
                    "type": "heading",
                    "order": 1,
                    "data": "Conjuration"
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "(Free Content)",
                    "style_class": "text-red-400 italic"
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Conjuration is the Arcanum of manifestation — the art of calling forth energy, objects, or elemental force into the physical world. It allows a caster to create bolts of power, conjure sustenance, illuminate darkness, or manipulate environmental elements with precision. As a versatile school of magic, Conjuration bridges the gap between raw arcane force and practical utility. Whether shaping light, summoning elemental fury, or crafting protective wards, Conjuration empowers the caster to bring thought into tangible reality."
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "(Every Rank of Conjuration Increase All Soak by 1)"
                },
                {
                    "type": "paragraph",
                    "order": 1,
                    "data": "Use the highest benefit of each Type (Attribute, Skill or Other Bonus). Recurring Types are not cumulative and use the highest value listed."
                },
                {
                    "type": "heading",
                    "order": 1,
                    "data": "0) Cantrip",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 2,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 3,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 4,
                    "data": "Spell:  Cantrip"
                },
                {
                    "type": "paragraph",
                    "order": 5,
                    "data": "PREQs:  Conjuration Tier 0"
                },
                {
                    "type": "paragraph",
                    "order": 6,
                    "data": "Range:  10’ (3M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 7,
                    "data": "AoE:  1 Target"
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
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 10,
                    "data": "Essence:  1"
                },
                {
                    "type": "paragraph",
                    "order": 11,
                    "data": "CAP:  1"
                },
                {
                    "type": "paragraph",
                    "order": 12,
                    "data": "Duration:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 13,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 14,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 15,
                    "data": "The rudimentary practical techniques developed to align oneself with the most basic esoteric understanding of the Arcanum paths. Because of the repetitive nature of learning Cantrips they are ingrained to the degree where a caster may utilize as many of the Cantrips that they possess in a given round and are only limited by their available action points regardless of other actions taken."
                },
                {
                    "type": "paragraph",
                    "order": 16,
                    "data": "Impressive Mein"
                },
                {
                    "type": "paragraph",
                    "order": 17,
                    "data": "For a moment of theatrics, the caster may cause minor changes to the presentation as they may choose to cause the following: Their voice booms to several times its normal volume while flames flicker brighter or dim to meet their desires as an ominous background noise such as thunder, whispering voices or a raven’s cry accentuates the background. This effect lasts for as long as the caster maintains concentration."
                },
                {
                    "type": "paragraph",
                    "order": 18,
                    "data": "Convenient Trick"
                },
                {
                    "type": "paragraph",
                    "order": 19,
                    "data": "With but a gesture the caster may instantaneously open, close, dye, clean or soil an object no larger than 2’2. or dye, repair, clean or soil all their personal attire."
                },
                {
                    "type": "paragraph",
                    "order": 20,
                    "data": "Detect Arcane / Void"
                },
                {
                    "type": "paragraph",
                    "order": 21,
                    "data": "The caster sees a faint aura and may identify the Arcanum cast upon any affected creature or object. To determine the details of a magical item the caster must make a Perception + Scholar: Arcane + ML roll. This may only be attempted once unless an increase in Master Level is achieved. This effect lasts one minute."
                },
                {
                    "type": "list",
                    "order": 22,
                    "data": [
                        "Very Easy - Reveals Primary Arcanum",
                        "Easy - Reveals Secondary Arcanum & Purpose",
                        "Moderate - Reveals Basic Powers (Arcanum 1-3)",
                        "Difficult - Reveals Basic Commands & Active Corruption & Moderate Powers (Arcanum 4-6)",
                        "Very Difficult - Reveals Moderate Commands & Advanced Powers (Arcanum 7-9)",
                        "Heroic - Reveals Advanced Commands & Legendary Powers (Arcanum 10)",
                        "Legendary - Reveals Legendary Commands & Item Non-Active Corruption"
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 23,
                    "data": "Detect Curse"
                },
                {
                    "type": "paragraph",
                    "order": 24,
                    "data": "The caster sees a faint aura and may identify the Curse afflicting a visible creature or object. To determine the details of an affliction the caster must make a Perception + Scholar: Curses + ML roll. This may only be attempted once unless an increase in Master Level is achieved. This effect lasts one minute."
                },
                {
                    "type": "list",
                    "order": 25,
                    "data": [
                        "Very Easy or Easy - The target appears to not be cursed.",
                        "Moderate - Reveals Basic Curses (Arcanum 1-3)",
                        "Difficult - Reveals Basic Curse Remedies & Moderate Curses (Arcanum 4-6)",
                        "Very Difficult - Reveals Moderate Curse Remedies & Advanced Curses (Arcanum 7-9)",
                        "Heroic - Reveals Advanced Curse Remedies & Legendary Curses (Arcanum 10)",
                        "Legendary - Reveals Legendary Curse Remedies"
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 26,
                    "data": "Detect Disease"
                },
                {
                    "type": "paragraph",
                    "order": 27,
                    "data": "The caster sees a faint aura and may identify the Disease afflicting a visible creature or object. To determine the details of a disease the caster must make a Perception + Medicine + ML roll. This may only be attempted once unless an increase in Master Level is achieved. This effect lasts one minute."
                },
                {
                    "type": "list",
                    "order": 28,
                    "data": [
                        "Very Easy or Easy - The target appears to not be Diseased.",
                        "Moderate - Reveals Basic Diseases (Medicine 1-3)",
                        "Difficult - Reveals Basic Disease Remedies & Moderate Diseases (Medicine 4-6)",
                        "Very Difficult - Reveals Moderate Disease Remedies & Advanced Diseases (Medicine 7-9)",
                        "Heroic - Reveals Advanced Disease Remedies & Legendary Diseases (Medicine 10)",
                        "Legendary - Reveals Legendary Disease Remedies"
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 29,
                    "data": "Detect Extraplanar Creature"
                },
                {
                    "type": "paragraph",
                    "order": 30,
                    "data": "The caster sees a faint aura and may identify the nature of visible creatures or objects that are Celestial, Elemental, Infernal, Undead and Wild Fey in nature. If the target is concealed by a Veiling effect, then Pierce the Veil or a Heroic/Legendary Perception + Scholar + ML check is required prior to Detecting Extraplanar Creatures. To determine the details of an extraplanar creature the caster must make a Perception + Occult + ML roll. This may only be attempted once unless an increase in Master Level is achieved. This effect lasts one minute."
                },
                {
                    "type": "list",
                    "order": 31,
                    "data": [
                        "Very Easy or Easy - The target appears to not be Extraplanar",
                        "Moderate - Reveals details about Minor Extraplanar & Weaknesses (Arcanum 1-3)",
                        "Difficult - Reveals details about Moderate Extraplanar & Weaknesses (Arcanum 4-6)",
                        "Very Difficult - Reveals details about Advanced Extraplanar & Weaknesses (Arcanum 7-9)",
                        "Heroic - Reveals details about Legendary Extraplanar & Weaknesses (Arcanum 10)",
                        "Legendary - Reveals details about Named Unique Extraplanar & Weaknesses"
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 32,
                    "data": "Detect Poison"
                },
                {
                    "type": "paragraph",
                    "order": 33,
                    "data": "The caster sees a faint aura and may identify Poisons afflicting or coating any visible creature or object. To determine the details of a Poison the caster must make a Perception + Scholar: Alchemy or Flora and Fauna + ML roll. This may only be attempted once unless an increase in Master Level is achieved. This effect lasts one minute."
                },
                {
                    "type": "list",
                    "order": 34,
                    "data": [
                        "Very Easy or Easy - The target appears to not be poisoned.",
                        "Moderate - Reveals Basic Poisons (Artisan 1-3)",
                        "Difficult - Reveals Basic Poison Remedies & Moderate Poisons (Artisan 4-6)",
                        "Very Difficult - Reveals Moderate Poison Remedies & Advanced Poisons (Artisan 7-9)",
                        "Heroic - Reveals Advanced Poison Remedies & Legendary Poisons (Arcanum 10)",
                        "Legendary - Reveals Legendary Poison Remedies"
                    ],
                    "style_class": "list-disc pl-6 mb-4"
                },
                {
                    "type": "paragraph",
                    "order": 35,
                    "data": "Enkindle Entrée"
                },
                {
                    "type": "paragraph",
                    "order": 36,
                    "data": "With or without a kitchen, utensils, or spices at the caster’s disposal they may make any vegetables or cooked meat palatable. At their command the food shall be warmed, chilled, spiced, picked or curdled to the desired taste. To achieve the desired effect, require an Artisan Sum roll with a Moderate Difficulty. Once affected the food behaves normally as appropriate for the environment and storage."
                },
                {
                    "type": "paragraph",
                    "order": 37,
                    "data": "Esoteric Sigil"
                },
                {
                    "type": "paragraph",
                    "order": 38,
                    "data": "The caster may permanently create or erase a unique Arcane Sigil that all other casters associate with the caster. They may do this on anything that is their recognized property and has been in their possession for a month. This Sigil may only be removed upon the caster’s death or if they choose to remove it. The caster may mark two items per Mastery Level."
                },
                {
                    "type": "paragraph",
                    "order": 39,
                    "data": "Faceless Mask"
                },
                {
                    "type": "paragraph",
                    "order": 40,
                    "data": "The caster’s face becomes blurred and unrecognizable. An opponent may make a single check to pierce this veil once per day, but it requires a contested Awareness Sum v. Analyze Sum. Pierce the Veil or Third Eye automatically breaks this disguise. This effect lasts 1 hour."
                },
                {
                    "type": "paragraph",
                    "order": 41,
                    "data": "Midnight Candle"
                },
                {
                    "type": "paragraph",
                    "order": 42,
                    "data": "This creates a small light source that illuminate 1C. This light source cannot be seen from the outside and lasts as long as the caster maintains concentration."
                },
                {
                    "type": "paragraph",
                    "order": 43,
                    "data": "Prestidigitation"
                },
                {
                    "type": "paragraph",
                    "order": 44,
                    "data": "This creates a flamboyant series of the 1’ scintillating orbs hued as the caster desires that hover or glide as directed by the caster. Each orb illuminates the 1C it is in and every 1C adjacent to it and may be moved up to 5C from the caster. This effect lasts 1 hour per Mastery Level."
                },
                {
                    "type": "paragraph",
                    "order": 45,
                    "data": "Seasons Sortilege"
                },
                {
                    "type": "paragraph",
                    "order": 46,
                    "data": "By casting stones, runes, bones or using cards the caster gain insight into the weather in their area for the next 24 hours. This effect is instant."
                },
                {
                    "type": "paragraph",
                    "order": 47,
                    "data": "Sentinel’s Watch"
                },
                {
                    "type": "paragraph",
                    "order": 48,
                    "data": "The caster set security precautions against encroachment. Select an area equal to 2C per ML. Until the spell ends, an alarm alerts them whenever a creature intrudes into the area. When the spell is cast the caster designates allies or creature types (small insects, small mammals) that won’t activate the alarm. The alarm is silent, but it stimulates the caster’s mind awake while alerting them to intrusions. This effect lasts 1 hour per Mastery Level."
                },
                {
                    "type": "heading",
                    "order": 49,
                    "data": "1) Arcane Bolt",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 50,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 51,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 52,
                    "data": "Spell:  Arcane Bolt"
                },
                {
                    "type": "paragraph",
                    "order": 53,
                    "data": "PREQs:  Conjuration Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 54,
                    "data": "Range:  10’ (3M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 55,
                    "data": "AoE:  1 Target"
                },
                {
                    "type": "container",
                    "order": 56,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 57,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 58,
                    "data": "Essence:  1"
                },
                {
                    "type": "paragraph",
                    "order": 59,
                    "data": "CAP:  4"
                },
                {
                    "type": "paragraph",
                    "order": 60,
                    "data": "Duration:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 61,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 62,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 63,
                    "data": "Arcane Bolt"
                },
                {
                    "type": "paragraph",
                    "order": 64,
                    "data": "A single bolt of arcane energy is released from the casters hand targeting a single creature: Striking a target is determined by Exoergic Sum + Conjuring Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum v. Soak: Energy Sum."
                },
                {
                    "type": "heading",
                    "order": 65,
                    "data": "2) Elemental Bolt",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 66,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 67,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 68,
                    "data": "Spell:  Elemental Bolt"
                },
                {
                    "type": "paragraph",
                    "order": 69,
                    "data": "PREQs:  Arcane Bolt & Conjuration Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 70,
                    "data": "Range:  10’ (3M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 71,
                    "data": "AoE:  1 Target"
                },
                {
                    "type": "container",
                    "order": 72,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 73,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 74,
                    "data": "Essence:  2"
                },
                {
                    "type": "paragraph",
                    "order": 75,
                    "data": "CAP:  4"
                },
                {
                    "type": "paragraph",
                    "order": 76,
                    "data": "Duration:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 77,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 78,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 79,
                    "data": "Air Bolt - PREQs Air Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 80,
                    "data": "A single bolt of pressured air is released from the casters hand targeting a single creature Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Air Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Air Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 81,
                    "data": "Ash Bolt - PREQs Ash Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 82,
                    "data": "A spray of pressured caustic ash is released from the casters hand targeting a single creature Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Ash Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Ash Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 83,
                    "data": "Earth Bolt - PREQs Earth Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 84,
                    "data": "A single blast of earthen material is released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Earth Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Earth Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 85,
                    "data": "Fire Bolt - PREQs Fire Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 86,
                    "data": "A single condensed flame bolt is released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Fire Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Fire Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 87,
                    "data": "Ice Bolt - PREQs Ice Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 88,
                    "data": "A spike of ice is released from the caster’s hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Ice Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Ice Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 89,
                    "data": "Lightning Bolt - PREQs Lightning Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 90,
                    "data": "A single bolt of arcing electricity is released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Lightning Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Lightning Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 91,
                    "data": "Plant Bolt - PREQs Plant Tier 1"
                },
                {
                    "type": "paragraph",
                    "order": 92,
                    "data": "A single ray of photosynthesized light is released from the caster’s hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Plant Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Plant Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 93,
                    "data": "Water Bolt - PREQs Water 1"
                },
                {
                    "type": "paragraph",
                    "order": 94,
                    "data": "A single bolt of pressured water is released from the caster’s hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Water Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Water Sum v. Soak: Energy Sum."
                },
                {
                    "type": "heading",
                    "order": 95,
                    "data": "3) Arcane Bolt, Mass",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 96,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 97,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 98,
                    "data": "Spell:  Arcane Bolt, Mass"
                },
                {
                    "type": "paragraph",
                    "order": 99,
                    "data": "PREQs:  Arcane Bolt & Conjuration Tier 3"
                },
                {
                    "type": "paragraph",
                    "order": 100,
                    "data": "Range:  5’ (1.5M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 101,
                    "data": "AoE:  1 Target per ML"
                },
                {
                    "type": "container",
                    "order": 102,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 103,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 104,
                    "data": "Essence:  3"
                },
                {
                    "type": "paragraph",
                    "order": 105,
                    "data": "CAP:  5"
                },
                {
                    "type": "paragraph",
                    "order": 106,
                    "data": "Duration:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 107,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 108,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 109,
                    "data": "Arcane Bolt, Mass"
                },
                {
                    "type": "paragraph",
                    "order": 110,
                    "data": "2 bolts of arcane energy are released from the casters hand targeting one creature per additional essence expended: Striking a target is determined by Awareness Sum + Conjuring Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum v. Soak: Energy Sum."
                },
                {
                    "type": "heading",
                    "order": 111,
                    "data": "4) Elemental Bolt, Mass",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 112,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 113,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 114,
                    "data": "Spell:  Elemental Bolt, Mass"
                },
                {
                    "type": "paragraph",
                    "order": 115,
                    "data": "PREQs:  Arcane Bolt & Conjuration Tier 4"
                },
                {
                    "type": "paragraph",
                    "order": 116,
                    "data": "Range:  5’ (1.5M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 117,
                    "data": "AoE:  1 Target per ML"
                },
                {
                    "type": "container",
                    "order": 118,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 119,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 120,
                    "data": "Essence:  4"
                },
                {
                    "type": "paragraph",
                    "order": 121,
                    "data": "CAP:  5"
                },
                {
                    "type": "paragraph",
                    "order": 122,
                    "data": "Duration:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 123,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 124,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 125,
                    "data": "Air Bolt, Mass - PREQs Air Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 126,
                    "data": "2 bolts of pressurized air are released from the casters hand targeting one creature per additional essence expended: Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Air Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Air Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 127,
                    "data": "Ash Bolt, Mass - PREQs Ash Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 128,
                    "data": "2 sprays of pressured caustic ash are released from the casters hand targeting a single creature Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Ash Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Ash Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 129,
                    "data": "Earth Bolt, Mass - PREQs Earth Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 130,
                    "data": "2 blasts of earthen material are released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Earth Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Earth Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 131,
                    "data": "Fire Bolt, Mass - PREQs Fire Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 132,
                    "data": "2 bolts of condensed flame are released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Fire Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Fire Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 133,
                    "data": "Ice Bolt, Mass - PREQs Ice Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 134,
                    "data": "2 spikes of ice are released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Ice Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Ice Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 135,
                    "data": "Lightning Bolt, Mass - PREQs Lightning Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 136,
                    "data": "2 bolts arcing electricity is released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Lightning Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Lightning Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 137,
                    "data": "Plant Bolt, Mass - PREQs Plant Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 138,
                    "data": "2 rays of photosynthesized light are released from the casters hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Plant Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Plant Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 139,
                    "data": "Water Bolt, Mass - PREQs Water Tier 2"
                },
                {
                    "type": "paragraph",
                    "order": 140,
                    "data": "2 bolts of pressured water are released from the caster’s hand targeting a single creature. Striking a target is determined by Exoergic Sum + Conjuring Sum + Element, Water Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Water Sum v. Soak: Energy Sum."
                },
                {
                    "type": "heading",
                    "order": 141,
                    "data": "5) Toxic Cloud",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 142,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 143,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 144,
                    "data": "Spell:  Toxic Cloud"
                },
                {
                    "type": "paragraph",
                    "order": 145,
                    "data": "PREQs:  Conjuration Tier 5"
                },
                {
                    "type": "paragraph",
                    "order": 146,
                    "data": "Range:  5’ (1.5M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 147,
                    "data": "AoE:  5 Cube AOE per ML"
                },
                {
                    "type": "container",
                    "order": 148,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 149,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 150,
                    "data": "Essence:  6"
                },
                {
                    "type": "paragraph",
                    "order": 151,
                    "data": "CAP:  6"
                },
                {
                    "type": "paragraph",
                    "order": 152,
                    "data": "Duration:  5 Rounds"
                },
                {
                    "type": "container",
                    "order": 153,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 154,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 155,
                    "data": "The caster creates a zone of poisonous gas centering on a designated target and 1C per ML in all directions. Each round the cloud spreads to each adjacent 1C area even around corners. It lasts for the duration or until strong wind disperses it. Each round that a creature passes through or starts their turn in this zone they risk contamination. To avoid being affected by the poison a target must Occult Sum v. Bio Control Sum. Damage for those affected is equal to Occult Sum + Conjuring Sum v. Stamina Sum."
                },
                {
                    "type": "heading",
                    "order": 156,
                    "data": "6) Arcane Explosion",
                    "style_class": "text-xl text-purple-400 font-semibold pt-4"
                },
                {
                    "type": "container",
                    "order": 157,
                    "data": "open",
                    "style_class": "flex flex-col gap-8 max-w-screen-xl mx-auto px-8 sm:flex-row"
                },
                {
                    "type": "container",
                    "order": 158,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 159,
                    "data": "Spell:  Arcane Explosion"
                },
                {
                    "type": "paragraph",
                    "order": 160,
                    "data": "PREQs:  Conjuration Tier 6"
                },
                {
                    "type": "paragraph",
                    "order": 161,
                    "data": "Range:  5’ (1.5M) LoS per ML"
                },
                {
                    "type": "paragraph",
                    "order": 162,
                    "data": "AoE:  5 Cube AOE per ML"
                },
                {
                    "type": "container",
                    "order": 163,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 164,
                    "data": "open",
                    "style_class": "w-full sm:w-1/2"
                },
                {
                    "type": "paragraph",
                    "order": 165,
                    "data": "Essence:  7"
                },
                {
                    "type": "paragraph",
                    "order": 166,
                    "data": "CAP:  7"
                },
                {
                    "type": "paragraph",
                    "order": 167,
                    "data": "Duration:  Instantaneous"
                },
                {
                    "type": "container",
                    "order": 168,
                    "data": "close"
                },
                {
                    "type": "container",
                    "order": 169,
                    "data": "close"
                },
                {
                    "type": "paragraph",
                    "order": 170,
                    "data": "Arcane Explosion"
                },
                {
                    "type": "paragraph",
                    "order": 171,
                    "data": "An arcane energy explosion emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 172,
                    "data": "Air Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Air Tier 5"
                },
                {
                    "type": "paragraph",
                    "order": 173,
                    "data": "An explosion of pressurized air emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Air Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Air Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 174,
                    "data": "Ash Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Ash Tier 5"
                },
                {
                    "type": "paragraph",
                    "order": 175,
                    "data": "An explosion of caustic ash emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Ash Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Ash Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 176,
                    "data": "Earth Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Earth Tier 5"
                },
                {
                    "type": "paragraph",
                    "order": 177,
                    "data": "An explosion of earthen emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Earth Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Earth Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 178,
                    "data": "Fire Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Fire Tier 5"
                },
                {
                    "type": "paragraph",
                    "order": 179,
                    "data": "An explosion of condensed flame bolt emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Fire Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Fire Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 180,
                    "data": "Ice Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Ice Tier 5"
                },
                {
                    "type": "paragraph",
                    "order": 181,
                    "data": "An explosion of ice shards emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Ice Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Ice Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 182,
                    "data": "Lightning Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Lightning Tier 4"
                },
                {
                    "type": "paragraph",
                    "order": 183,
                    "data": "An explosion of arcing electricity emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Lightning Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Lightning Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 184,
                    "data": "Plant Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Plant Tier 4"
                },
                {
                    "type": "paragraph",
                    "order": 185,
                    "data": "An explosion of photosynthesized light emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Plant Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Plant Sum v. Soak: Energy Sum."
                },
                {
                    "type": "paragraph",
                    "order": 186,
                    "data": "Water Explosion (+15 XP to Learn) - PREQs Arcane Explosion & Water Tier 4"
                },
                {
                    "type": "paragraph",
                    "order": 187,
                    "data": "An explosion pressured emanates from a designated target in 1C per ML in all directions. All targets within this area are affected by an Exoergic Sum + Conjuring Sum + Element, Water Sum v. Dodge Sum. Damage is equal to Occult Sum + Conjuring Sum + Element, Water Sum v. Soak: Energy Sum."
                }
            ]
        }
    ]

    for section_data in sections:
        section = Section(
            title=section_data["title"],
            slug=section_data["slug"],
            chapter=section_data["chapter"],
            rulebook=section_data["rulebook"]
        )
        db.session.add(section)
        db.session.commit()

        for content_data in section_data["content"]:
            if isinstance(content_data["data"], str):
                cleaned_data = clean_text(content_data["data"])
            else:
                cleaned_data = content_data["data"]

            content = Content(
                section_id=section.id,
                content_type=content_data["type"],
                content_order=content_data["order"],
                content_data=cleaned_data,
                style_class=clean_text(content_data.get("style_class", ""))
            )
            db.session.add(content)

    db.session.commit()
    print("Darkholme rules seeded successfully!")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        print("Application context is active.")
        seed_rules()

