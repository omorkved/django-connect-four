from django.db import models
import django.contrib.postgres.fields 

# Create your models here.


# Each player has one and only one theme
# Each time the players moves, a piece is added matching their color
# Each board has exactly two players. 
# Players must have different colors.

class Player(models.Model):
    name = models.CharField(max_length=50)
    color = models.OneToOneField(Color, 
            on_delete=models.CASCADE
    )

class Piece (models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
    )

class Board(models.Model):
    p1 = models.OneToOneField(
        Player, 
        on_delete=models.CASCADE,
    )
    p2 = models.OneToOneField(
        Player, 
        on_delete=models.CASCADE,
    )
    '''
    board = ArrayField(
        ArrayField(
            Piece,
            #rows
            size=6,
        ),
        #columns
        size=7,
    )'''
    test = models.ForeignKey

