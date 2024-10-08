"""Add new Application, settings, dashboard model

Revision ID: a17e4b0e83ba
Revises: 5092fd02371e
Create Date: 2024-09-20 08:29:07.891174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a17e4b0e83ba'
down_revision: Union[str, None] = '5092fd02371e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('id', sa.CHAR(length=36), nullable=False),
    sa.Column('user_id', sa.CHAR(length=36), nullable=False),
    sa.Column('company', sa.String(length=255), nullable=False),
    sa.Column('position', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('applied_date', sa.String(length=255), nullable=False),
    sa.Column('notes', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user_settings',
    sa.Column('id', sa.CHAR(length=36), nullable=False),
    sa.Column('user_id', sa.CHAR(length=36), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('university', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('desired_role', sa.String(length=100), nullable=True),
    sa.Column('theme', sa.String(length=50), nullable=False),
    sa.Column('notification_preferences', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_user_settings_user_id'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_settings')
    op.drop_table('applications')
    # ### end Alembic commands ###
