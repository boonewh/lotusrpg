from lotusrpg import create_app, db
from lotusrpg.models import Section, Content
import re

def clean_text(text): 
    if not isinstance(text, str):  
        return text
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()

def seed_rules():
    print("Seeding Darkholme rules...")

    # Delete only content that belongs to Darkholme sections
    darkholme_section_ids = db.session.query(Section.id).filter_by(rulebook='darkholme').subquery()
    db.session.query(Content).filter(Content.section_id.in_(darkholme_section_ids)).delete(synchronize_session=False)

    # Now delete the darkholme sections
    db.session.query(Section).filter_by(rulebook='darkholme').delete()

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
            cleaned_data = clean_text(content_data["data"]) if isinstance(content_data["data"], str) else content_data["data"]

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
