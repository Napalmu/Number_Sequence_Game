# import pygame module in this program
import pygame
import numseq as ns


def main():
	pygame.init()

	white = (255, 255, 255)
	green = (0, 255, 0)
	blue = (0, 0, 128)

	# assigning values to X and Y variable
	X = 400
	Y = 400

	# create the display surface object
	# of specific dimension..e(X, Y).
	display_surface = pygame.display.set_mode((X, Y))

	# set the pygame window name
	pygame.display.set_caption('Show Text')

	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render(ns.getStr(1, 1), True, green, blue)

	textRect = text.get_rect()

	# set the center of the rectangular object.
	textRect.center = (X // 2, Y // 2)

	# infinite loop
	while True:

		display_surface.fill(white)
		display_surface.blit(text, textRect)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:

				pygame.quit()
				quit()

			pygame.display.update()


main()
