"""empty message

Revision ID: e0e486101380
Revises: 
Create Date: 2025-03-22 12:34:37.124000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0e486101380'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dtm_txmtemplate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('patient_type', sa.String(length=200), nullable=False, comment='患者类型'),
    sa.Column('txm_template', sa.Text(), nullable=False, comment='模板内容'),
    sa.Column('hospital_id', sa.String(length=200), nullable=False, comment='医院id'),
    sa.Column('photos', sa.BLOB(), nullable=True, comment='照片'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lis_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False, comment='角色名称'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lis_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False, comment='姓名'),
    sa.Column('age', sa.Integer(), nullable=False, comment='年龄'),
    sa.Column('sex', sa.Integer(), nullable=False, comment='性别'),
    sa.Column('role_id', sa.Integer(), nullable=True, comment='角色id'),
    sa.Column('birthday', sa.Date(), nullable=False, comment='出生日期'),
    sa.ForeignKeyConstraint(['role_id'], ['lis_role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lis_user')
    op.drop_table('lis_role')
    op.drop_table('dtm_txmtemplate')
    # ### end Alembic commands ###
