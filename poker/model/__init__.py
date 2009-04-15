"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.databases.mysql import MSBigInteger
from poker.model import meta
from poker.model import user, game, player

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine
    
table_user = sa.Table("user", meta.metadata,
                   sa.Column("id", MSBigInteger, primary_key=True),
                   sa.Column("username", sa.types.String(32)),
                   sa.Column("password", sa.types.String(32)),
                   sa.Column("email", sa.types.String(255)),
                   )

table_game = sa.Table("game", meta.metadata,
                      sa.Column("id", MSBigInteger, primary_key=True),
                      sa.Column("user_id", MSBigInteger),
                      sa.Column("name", sa.types.String(32)),
                      sa.Column("players",sa.types.Integer(2)),
                      sa.Column("sb",sa.types.Integer(11)),
                      sa.Column("bb",sa.types.Integer(11)),
                      sa.Column("anti",sa.types.Integer(11)),
                      sa.Column("on",sa.types.Integer(2)),
                      sa.Column("start",sa.types.Integer(2)),
                      sa.Column("dealer",sa.types.Integer(2)),
                      sa.Column("sb_on",sa.types.Integer(2)),
                      sa.Column("bb_on",sa.types.Integer(2)),
                      sa.Column("highestbet", sa.types.Integer(11)),
                      sa.Column("highestraise", sa.types.Integer(11)),
                      sa.Column("pot", sa.types.Integer(11)),
                      )

table_player = sa.Table("player", meta.metadata,
                      sa.Column("id", MSBigInteger, primary_key=True),
                      sa.Column("name", sa.types.String(32)),
                      sa.Column("game_id", MSBigInteger),
                      sa.Column("position", sa.types.Integer(2)),
                      sa.Column("in_bank", sa.types.Integer(11)),
                      sa.Column("in_play", sa.types.Integer(11)),
                      sa.Column("in_pot", sa.types.Integer(11)),
                      sa.Column("round_bet", sa.types.Integer(11)),
                      sa.Column("folded", sa.types.Integer(1)),
                      )


orm.mapper(user.User, table_user)
orm.mapper(game.Game, table_game)
orm.mapper(player.Player, table_player)


## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
