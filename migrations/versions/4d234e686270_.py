"""empty message

Revision ID: 4d234e686270
Revises: 09453915ae8f
Create Date: 2017-11-27 12:59:20.978325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d234e686270'
down_revision = '09453915ae8f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('user', 'password',
                    existing_type=sa.VARCHAR(length=100),
                    type_=sa.String(length=255)
                    )


def downgrade():
    pass
