"""Add financial fields to Property model

Revision ID: 001509cb35d7
Revises: 8c881fc064f9
Create Date: 2024-10-08 15:14:53.114436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001509cb35d7'
down_revision = '8c881fc064f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tenants', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('buying_price', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('year_bought', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('current_value', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.drop_column('current_value')
        batch_op.drop_column('year_bought')
        batch_op.drop_column('buying_price')
        batch_op.drop_column('tenants')

    # ### end Alembic commands ###
