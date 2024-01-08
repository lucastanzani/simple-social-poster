import os

import dotenv

if os.getenv("SOCIAL_POSTER_ENV") in ['DEV', 'LOCAL', 'DEVELOPMENT']:
	__env_file = ".env.dev"
else:
	__env_file = os.environ.get("SOCIAL_POSTER_ENV_FILE") or ".env"

if __env_file is not None:
	dotenv.load_dotenv(dotenv.find_dotenv(__env_file), override=False)