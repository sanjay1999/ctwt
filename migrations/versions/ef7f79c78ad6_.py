"""empty message

Revision ID: ef7f79c78ad6
Revises: e38b518b3c66
Create Date: 2020-04-28 12:18:33.604901

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ef7f79c78ad6'
down_revision = 'e38b518b3c66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'employeeid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.add_column('tgroup', sa.Column('tid', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'tgroup', 'teams', ['tid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tgroup', type_='foreignkey')
    op.drop_column('tgroup', 'tid')
    op.alter_column('tasks', 'employeeid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###
