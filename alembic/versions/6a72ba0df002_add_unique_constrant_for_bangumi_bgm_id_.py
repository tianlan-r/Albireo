"""add unique constrant for bangumi.bgm_id column

Revision ID: 6a72ba0df002
Revises: 93206f1acf90
Create Date: 2017-04-13 16:04:45.032210

"""

# revision identifiers, used by Alembic.
revision = '6a72ba0df002'
down_revision = '93206f1acf90'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'bangumi', ['bgm_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bangumi', type_='unique')
    # ### end Alembic commands ###