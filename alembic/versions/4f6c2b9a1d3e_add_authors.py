"""add authors

Revision ID: 4f6c2b9a1d3e
Revises: dd283eb7bf1c
Create Date: 2026-05-03 19:35:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f6c2b9a1d3e'
down_revision: Union[str, None] = 'dd283eb7bf1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if 'authors' not in inspector.get_table_names():
        op.create_table(
            'authors',
            sa.Column('full_name', sa.String(length=255), nullable=False),
            sa.Column('birth_year', sa.Integer(), nullable=True),
            sa.Column('bio', sa.Text(), nullable=True),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
            sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('id'),
        )

    index_names = {index['name'] for index in inspector.get_indexes('authors')}
    if 'ix_authors_full_name' not in index_names:
        op.create_index(op.f('ix_authors_full_name'), 'authors', ['full_name'], unique=False)


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if 'authors' in inspector.get_table_names():
        index_names = {index['name'] for index in inspector.get_indexes('authors')}
        if 'ix_authors_full_name' in index_names:
            op.drop_index(op.f('ix_authors_full_name'), table_name='authors')
        op.drop_table('authors')
