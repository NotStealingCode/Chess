# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

board = pygame.image.load("assets/images/cb2.png")
white_pawn = pygame.image.load("assets/images/pawnw.png")
white_bishop = pygame.image.load("assets/images/bishopw.png")
white_knight = pygame.image.load("assets/images/knightw.png")
white_rook = pygame.image.load("assets/images/rookw.png")
white_queen = pygame.image.load("assets/images/queenw.png")
white_king = pygame.image.load("assets/images/kingw.png")

black_pawn = pygame.image.load("assets/images/pawnb.png")
black_bishop = pygame.image.load("assets/images/bishopb.png")
black_knight = pygame.image.load("assets/images/knightb.png")
black_rook = pygame.image.load("assets/images/rookb.png")
black_queen = pygame.image.load("assets/images/queenb.png")
black_king = pygame.image.load("assets/images/kingb.png")

white_pieces_locations = {
    'white_rook1': (0, 0),
    'white_knight1': (1, 0),
    'white_bishop1': (2, 0),
    'white_queen': (3, 0),
    'white_king': (4, 0),
    'white_bishop2': (5, 0),
    'white_knight2': (6, 0),
    'white_rook2': (7, 0),
    'white_pawn1': (0, 1),
    'white_pawn2': (1, 1),
    'white_pawn3': (2, 1),
    'white_pawn4': (3, 1),
    'white_pawn5': (4, 1),
    'white_pawn6': (5, 1),
    'white_pawn7': (6, 1),
    'white_pawn8': (7, 1),
}

black_pieces_locations = {
    'black_rook1': (0, 7),
    'black_knight1': (1, 7),
    'black_bishop1': (2, 7),
    'black_queen': (3, 7),
    'black_king': (4, 7),
    'black_bishop2': (5, 7),
    'black_knight2': (6, 7),
    'black_rook2': (7, 7),
    'black_pawn1': (0, 6),
    'black_pawn2': (1, 6),
    'black_pawn3': (2, 6),
    'black_pawn4': (3, 6),
    'black_pawn5': (4, 6),
    'black_pawn6': (5, 6),
    'black_pawn7': (6, 6),
    'black_pawn8': (7, 6),
}


def set_up_pieces():
    for i in white_pieces_locations:
        if "rook" in i:
            screen.blit(white_rook, (white_pieces_locations[i][0] * 100 + 20, white_pieces_locations[i][1] * 100 + 10))
        elif "knight" in i:
            screen.blit(white_knight,
                        (white_pieces_locations[i][0] * 100 + 20, white_pieces_locations[i][1] * 100 + 10))
        elif "bishop" in i:
            screen.blit(white_bishop,
                        (white_pieces_locations[i][0] * 100 + 20, white_pieces_locations[i][1] * 100 + 10))
        elif "queen" in i:
            screen.blit(white_queen, (white_pieces_locations[i][0] * 100 + 20, white_pieces_locations[i][1] * 100 + 10))
        elif "king" in i:
            screen.blit(white_king, (white_pieces_locations[i][0] * 100 + 20, white_pieces_locations[i][1] * 100 + 10))
        else:
            screen.blit(white_pawn, (white_pieces_locations[i][0] * 100 + 20, white_pieces_locations[i][1] * 100 + 10))
    for i in black_pieces_locations:
        if "rook" in i:
            screen.blit(black_rook, (black_pieces_locations[i][0] * 100 + 20, black_pieces_locations[i][1] * 100 + 10))
        elif "knight" in i:
            screen.blit(black_knight,
                        (black_pieces_locations[i][0] * 100 + 20, black_pieces_locations[i][1] * 100 + 10))
        elif "bishop" in i:
            screen.blit(black_bishop,
                        (black_pieces_locations[i][0] * 100 + 20, black_pieces_locations[i][1] * 100 + 10))
        elif "queen" in i:
            screen.blit(black_queen, (black_pieces_locations[i][0] * 100 + 20, black_pieces_locations[i][1] * 100 + 10))
        elif "king" in i:
            screen.blit(black_king, (black_pieces_locations[i][0] * 100 + 20, black_pieces_locations[i][1] * 100 + 10))
        else:
            screen.blit(black_pawn, (black_pieces_locations[i][0] * 100 + 20, black_pieces_locations[i][1] * 100 + 10))


def determine_piece_by_cursor(x_coordinate, y_coordinate):
    turn = white_turn
    location_spotted = (x_coordinate, y_coordinate)
    if turn:
        for w in white_pieces_locations:
            if location_spotted == white_pieces_locations[w]:
                return w
    else:
        for b in black_pieces_locations:
            if location_spotted == black_pieces_locations[b]:
                return b


def pawn_choices(pawn_number):
    turn = white_turn
    moves_list = []
    if turn:
        location = white_pieces_locations[pawn_number]
        enemies = black_pieces_locations
        if location[1] == 1:
            moves_list.append((location[0], location[1] + 1))
            moves_list.append((location[0], location[1] + 2))
        else:
            moves_list.append((location[0], location[1] + 1))
        for b in black_pieces_locations:
            if black_pieces_locations[b] == (location[0] + 1, location[1] + 1) or black_pieces_locations[b] == (location[0] - 1, location[1] + 1):
                moves_list.append(black_pieces_locations[b])
        for v in white_pieces_locations:
            if white_pieces_locations[v] in moves_list:
                moves_list = []
        return moves_list

    else:
        location = black_pieces_locations[pawn_number]
        enemies = white_pieces_locations
        if location[1] == 6:
            moves_list.append((location[0], location[1] - 1))
            moves_list.append((location[0], location[1] - 2))
        else:
            moves_list.append((location[0], location[1] - 1))
        for v in black_pieces_locations:
            if black_pieces_locations[v] in moves_list:
                moves_list = []
        return moves_list


def current_choices(choices):
    turn = white_turn
    if turn:
        for c in choices:
            pygame.draw.circle(screen, "blue", (c[0] * 100 + 50, c[1] * 100 + 50), 5)
    else:
        for c in choices:
            pygame.draw.circle(screen, "red", (c[0] * 100 + 50, c[1] * 100 + 50), 5)


def update_moves(piece_updated, coordinates):
    turn = white_turn
    if turn:
        for z in white_pieces_locations:
            if piece_updated == z:
                white_pieces_locations[z] = (coordinates[0], coordinates[1])
    else:
        for b in black_pieces_locations:
            if piece_updated == b:
                black_pieces_locations[b] = (coordinates[0], coordinates[1])


current_moves = []
running = True
white_turn = True
while running:
    screen.blit(board, (0, 0))
    set_up_pieces()
    current_choices(current_moves)
    # # poll for events
    # # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            coords = (x_coord, y_coord)
            print(coords)
            piece_location = determine_piece_by_cursor(x_coord, y_coord)
            print(piece_location)
            if piece_location is not None and white_turn:
                current_moves = []
                piece_name = piece_location
                moves = pawn_choices(piece_location)
                for n in moves:
                    current_moves.append(n)
            if coords in current_moves and white_turn:
                update_moves(piece_name, coords)
                current_moves = []
                white_turn = False
            if piece_location is not None and not white_turn:
                current_moves = []
                b_piece_name = piece_location
                moves = pawn_choices(piece_location)
                for n in moves:
                    current_moves.append(n)
            if coords in current_moves and not white_turn:
                update_moves(b_piece_name, coords)
                current_moves = []
                white_turn = True

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
