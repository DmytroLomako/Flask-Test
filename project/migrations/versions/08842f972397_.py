"""empty message

Revision ID: 08842f972397
Revises: f6bb0465d383
Create Date: 2024-12-07 12:42:55.455882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08842f972397'
down_revision = 'f6bb0465d383'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
