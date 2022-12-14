"""added post column

Revision ID: 840d35ff6921
Revises: 56cc11c83449
Create Date: 2022-09-21 18:12:47.359905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '840d35ff6921'
down_revision = '56cc11c83449'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_created')
    # ### end Alembic commands ###
