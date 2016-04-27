from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
course = Table('course', pre_meta,
    Column('course_num', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=80)),
    Column('student_id', VARCHAR(length=8)),
    Column('admin_id', VARCHAR(length=8)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['course'].columns['admin_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['course'].columns['admin_id'].create()
