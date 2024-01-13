import pygame, sys, time
pygame.init()

# initiate resources
width, height = 700, 700
screen = pygame.display.set_mode([width, height])
rect_x_pos, rect_y_pos = [25, 250, 475, 25, 250, 475, 25, 250, 475], [25, 25, 25, 250, 250, 250, 475, 475, 475] 
rect_list = []
for i in range(9):
    rect = pygame.Rect(rect_x_pos[i], rect_y_pos[i], 200, 200)
    rect_list.append(rect)   
used_fields, p1_fields, p2_fields = [], [], []

# run main game loop
running = True
while running:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(9):
                if rect_list[i].collidepoint(mouse_pos): 
                    if i not in used_fields:
                        used_fields.append(i)
                        if len(used_fields) % 2 == 1: p1_fields.append(i)      
                        if len(used_fields) % 2 == 0: p2_fields.append(i)  

    # draw screen
    screen.fill("black")
    for i in range(9):
        if i not in p1_fields and i not in p2_fields: pygame.draw.rect(screen, "grey", (rect_x_pos[i], rect_y_pos[i], 200, 200))
        elif i in p1_fields: pygame.draw.rect(screen, "blue", (rect_x_pos[i], rect_y_pos[i], 200, 200))
        elif i in p2_fields: pygame.draw.rect(screen, "red", (rect_x_pos[i], rect_y_pos[i], 200, 200))

    # check possible ending conditions 
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    blue_wins, red_wins, draw = False, False, False
    for con in win_conditions:   
        if (con[0] in p1_fields) and (con[1] in p1_fields) and (con[2] in p1_fields): blue_wins = True
        elif (con[0] in p2_fields) and (con[1] in p2_fields) and (con[2] in p2_fields): red_wins = True
    if blue_wins == False and red_wins == False and (len(p1_fields) + len(p2_fields)) == 9: draw = True

    # print the ending result
    if blue_wins == True or red_wins == True or draw == True:
        font = pygame.font.Font(None, 100)
        if blue_wins == True: text = font.render("blue wins!", True, "white")
        if red_wins == True: text = font.render("red wins!", True, "white")
        if draw == True: text = font.render("draw!", True, "white")
        text_rect = text.get_rect(center=(width // 2, height // 2 ))
        screen.blit(text, text_rect)
        running = False

    pygame.display.flip()
time.sleep(3)
pygame.quit()