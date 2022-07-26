"""add status

Revision ID: 045cb2396292
Revises: 6303df2bc4c2
Create Date: 2022-07-24 19:42:15.112828

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '045cb2396292'
down_revision = '6303df2bc4c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bet', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bet', 'status')
    # ### end Alembic commands ###
