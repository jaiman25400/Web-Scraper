"""Models User Response migration

Revision ID: 46143e5dc81b
Revises: e627ac7f2ba7
Create Date: 2024-11-18 23:11:48.607982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46143e5dc81b'
down_revision = 'e627ac7f2ba7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_responses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('classify_user', sa.String(length=128), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_responses', schema=None) as batch_op:
        batch_op.drop_column('classify_user')

    # ### end Alembic commands ###
