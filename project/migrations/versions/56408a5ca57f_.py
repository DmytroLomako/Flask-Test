"""empty message

Revision ID: 56408a5ca57f
Revises: 08842f972397
Create Date: 2024-12-08 14:23:51.337579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56408a5ca57f'
down_revision = '08842f972397'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
