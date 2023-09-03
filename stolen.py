import pygame

scene_iterator = iter(scene_graph)
while not game_is_over:
    current_scene = next(scene_iterator)
    current_scene.start_scene()
    while current_scene.is_valid():
        clock.tick(current_scene.frame_rate())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("Bye bye!")
                current_scene.invalidate()
                _game_is_over = True
            current_scene.process_event(event)
        current_scene.update_scene()
        current_scene.draw()
        current_scene.render_updates()
        pygame.display.update()
    current_scene.end_scene()
# display_info()
pygame.quit()

