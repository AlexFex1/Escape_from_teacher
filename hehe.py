self.speedx = 0
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        
        if self.rect.right > WIDTH - 50:
            # self.rect.right = WIDTH
            self.speedx = 0
            Background().rect.x -= 8
        
        self.rect.x += self.speedx
        # if self.rect.left < 0:
        #     self.rect.left = 0
        if keystate[pygame.K_SPACE]:
            self.isJump = True

        if self.isJump is True:
            if self.jumpCount >= -7:
                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 0.5
            else:
                self.isJump = False
                self.jumpCount = 7