"""empty message

Revision ID: 980b66c49638
Revises: a7b264bb3b21
Create Date: 2021-03-02 13:38:55.250234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980b66c49638'
down_revision = 'a7b264bb3b21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
