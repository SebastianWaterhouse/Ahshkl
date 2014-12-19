import random, ahshklbodyparts

#
def defTheValues():
	Standing="standing up"
	LyingDown="lying down"
	Grass = "grassy area"
	Snow = "snowy area"

def chooseThePosition():
	positionChose = LyingDown
	choosePosition = random.randint(1, 2)
	if choosePosition==2:
		positionChose = Standing
def chooseTheLand():
	landChose = Snow
	chooseLand = random.randint(1, 2)
	if chooseLand==2:
		landChose = Grass


playerCoordsX = 0
playerCoordsY = 0

sceneBoundary1X = -20
sceneBoundary1Y = -20
sceneBoundary2X = -20
sceneBoundary2Y = 20
sceneBoundary3X = 20
sceneBoundary3Y = 20
sceneBoundary4X = 20
sceneBoundary4Y = -20
sceneBoundary1 = (-20, -20)
sceneBoundary2 = (-20, 20)
sceneBoundary3 = (20, 20)
sceneBoundary4 = (20, -20)

ahshklbodyparts.Hole1()