import ahshklterraingeneration, ahshklbodyparts, ahshklobjects, random

Standing="standing up"
LyingDown="lying down"
Grass = "grassy area"
Snow = "snowy area"

positionChose = LyingDown
choosePosition = random.randint(1, 2)
if choosePosition==2:
	positionChose = Standing
landChose = Snow
chooseLand = random.randint(1, 2)
if chooseLand==2:
	landChose = Grass

