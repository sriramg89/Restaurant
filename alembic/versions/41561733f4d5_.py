"""empty message

Revision ID: 41561733f4d5
Revises: b02122b6062c
Create Date: 2021-02-25 02:11:53.079086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41561733f4d5'
down_revision = 'b02122b6062c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_item')
    op.drop_table('user')
    op.drop_table('orders')
    op.drop_table('wishlist')
    op.drop_table('restaurant')
    op.drop_table('inventory')
    op.drop_table('menu_category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('restid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['restid'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.Column('itemid', sa.INTEGER(), nullable=True),
    sa.Column('restaurantid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['itemid'], ['menu_item.id'], ),
    sa.ForeignKeyConstraint(['restaurantid'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.Column('open_time', sa.DATETIME(), nullable=True),
    sa.Column('close_time', sa.DATETIME(), nullable=True),
    sa.Column('rating', sa.INTEGER(), nullable=True),
    sa.Column('average_cost', sa.INTEGER(), nullable=True),
    sa.Column('userid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('wishlist',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('categoryid', sa.INTEGER(), nullable=True),
    sa.Column('no_of_votes', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['categoryid'], ['menu_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('userid', sa.INTEGER(), nullable=True),
    sa.Column('restid', sa.INTEGER(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('itemid', sa.INTEGER(), nullable=True),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['itemid'], ['menu_item.id'], ),
    sa.ForeignKeyConstraint(['restid'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('mobile', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile')
    )
    op.create_table('menu_item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('categid', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('cost', sa.INTEGER(), nullable=True),
    sa.Column('gluten_free', sa.VARCHAR(), nullable=True),
    sa.Column('vegetarian', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['categid'], ['menu_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
