import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Get the project base directory
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(base_dir)

from app.models import Base  # Import your Base

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Debug: Print the path to ensure alembic.ini is being referenced correctly
print(f"Configuration file path: {config.config_file_name}")

# Debug: Print configuration sections and options
print("Alembic Configuration Sections:")
sections = config.get_section(config.config_ini_section)
print(sections)

# Debug: Print sqlalchemy.url
print(f"sqlalchemy.url from config: {config.get_main_option('sqlalchemy.url')}")

# Add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# Ensure the 'url' key is present in the configuration options
def get_url():
    url = config.get_main_option("sqlalchemy.url")
    if not url:
        url = os.getenv('DATABASE_URL')
    return url

def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    configuration = config.get_section(config.config_ini_section)
    url = get_url()
    print(f"Database URL: {url}")  # Debugging statement
    if not url:
        raise ValueError("Database URL not found in configuration")
    configuration['sqlalchemy.url'] = url
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
