"""empty message

Revision ID: b14b3dd516dd
Revises: 
Create Date: 2017-11-28 13:58:40.158401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b14b3dd516dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_users',
    sa.Column('f_id', sa.Integer(), nullable=False),
    sa.Column('f_userName', sa.String(length=80), server_default='anonymous', nullable=False),
    sa.Column('f_password', sa.String(length=80), server_default='123456', nullable=False),
    sa.Column('f_email', sa.String(length=80), server_default='', nullable=True),
    sa.Column('f_cellPhone', sa.String(length=30), server_default='', nullable=True),
    sa.PrimaryKeyConstraint('f_id'),
    sa.UniqueConstraint('f_cellPhone'),
    sa.UniqueConstraint('f_email')
    )
    op.create_index(op.f('ix_t_users_f_userName'), 't_users', ['f_userName'], unique=True)
    op.create_index(op.f('ix_t_users_f_id'), 't_users', ['f_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_t_users_f_id'), table_name='t_users')
    op.drop_index(op.f('ix_t_users_f_userName'), table_name='t_users')
    op.drop_table('t_users')
    # ### end Alembic commands ###
