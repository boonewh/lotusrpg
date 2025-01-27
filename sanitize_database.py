from lotusrpg import create_app, db
from lotusrpg.models import Content
import re

# Create the app context
app = create_app()
with app.app_context():
    # Query all content entries
    all_contents = Content.query.all()

    # Sanitize the content_data field
    for content in all_contents:
        print(f"Before: ID {content.id} - {content.content_data}")
        
        # Remove newlines and reduce multiple spaces to a single space
        sanitized_data = re.sub(r'\s+', ' ', content.content_data.strip())
        
        # Update the content_data if changes are needed
        if content.content_data != sanitized_data:
            content.content_data = sanitized_data
            print(f"After: ID {content.id} - {content.content_data}")

    # Commit changes to the database
    db.session.commit()
    print("Database has been updated successfully.")
