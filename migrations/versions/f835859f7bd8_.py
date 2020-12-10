"""empty message

Revision ID: f835859f7bd8
Revises: 
Create Date: 2020-12-10 10:00:57.350571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f835859f7bd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('size_reference',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topping_reference',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topping_type',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pizza',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['size_id'], ['size_reference.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topping_type_size',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=False),
    sa.Column('topping_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['size_id'], ['size_reference.id'], ),
    sa.ForeignKeyConstraint(['topping_type_id'], ['topping_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topping',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('topping_ref_id', sa.Integer(), nullable=False),
    sa.Column('topping_type_size_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['topping_ref_id'], ['topping_reference.id'], ),
    sa.ForeignKeyConstraint(['topping_type_size_id'], ['topping_type_size.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('topping')
    op.drop_table('topping_type_size')
    op.drop_table('pizza')
    op.drop_table('topping_type')
    op.drop_table('topping_reference')
    op.drop_table('size_reference')
    # ### end Alembic commands ###