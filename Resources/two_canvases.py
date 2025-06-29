import pygame
import asyncio
import platform

# Initialize Pygame
def setup():
    global screen, canvas1, canvas2, WIDTH, HEIGHT
    pygame.init()
    WIDTH, HEIGHT = 800, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Two Canvases Example")
    
    # Create two separate surfaces (canvases)
    canvas1 = pygame.Surface((WIDTH // 2, HEIGHT))
    canvas2 = pygame.Surface((WIDTH // 2, HEIGHT))

# Update loop for drawing on canvases
def update_loop():
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return

    # Draw on canvas1 (red rectangle)
    canvas1.fill((0, 0, 0))  # Clear canvas1 with black
    pygame.draw.rect(canvas1, (255, 0, 0), (50, 50, 100, 100))

    # Draw on canvas2 (blue circle)
    canvas2.fill((0, 0, 0))  # Clear canvas2 with black
    pygame.draw.circle(canvas2, (0, 0, 255), (100, 200), 50)

    # Blit both canvases onto the main screen
    screen.blit(canvas1, (0, 0))  # Left half
    screen.blit(canvas2, (WIDTH // 2, 0))  # Right half

    # Draw a white divider line between canvases
    pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    pygame.display.flip()

# Main async function for Pyodide compatibility
async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / 60)  # 60 FPS

# Run the game
if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())