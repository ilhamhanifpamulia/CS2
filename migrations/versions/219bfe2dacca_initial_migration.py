"""Initial migration.

Revision ID: 219bfe2dacca
Revises: 
Create Date: 2020-04-11 15:22:35.965954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '219bfe2dacca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nim', sa.String(length=8), nullable=True),
    sa.Column('nama_mahasiswa', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nama_mahasiswa'),
    sa.UniqueConstraint('nim')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
