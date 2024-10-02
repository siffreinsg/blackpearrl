import os

import dotenv
from plexapi.myplex import MyPlexAccount

# Load environment variables
dotenv.load_dotenv()
PLEX_TOKEN = os.getenv('PLEX_TOKEN')
PLEX_SERVER_NAME = os.getenv('PLEX_SERVER_NAME')

if not PLEX_TOKEN or not PLEX_SERVER_NAME:
    raise ValueError('Please provide PLEX_TOKEN and PLEX_SERVER_NAME in .env file')

account = MyPlexAccount(token=PLEX_TOKEN)
plex = account.resource(PLEX_SERVER_NAME).connect()
print(f'Connected to {plex.friendlyName}')

sections = plex.library.sections()

for section in sections:
    if section.type != 'movie':
        continue

    collections = plex.library.section(section.title).collections()

    for collection in collections:
        if collection.childCount != 0:
            continue
        collection.delete()
        print(f'Deleted empty collection {collection.title} from {section.title}')

    print(f'Collection cleanup for {section.title} completed')

print('All collections cleaned up')
