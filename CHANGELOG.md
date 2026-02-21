# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-21

### Added
- Initial release of Memory AI Game
- Three difficulty levels (Easy, Medium, Hard)
- Four grid size options (3×4, 4×4, 4×5, 5×6)
- Minimax algorithm with Alpha-Beta pruning for AI
- Retro 8-bit aesthetic with Press Start 2P font
- Responsive design for mobile/tablet/desktop
- Sound toggle functionality
- Score tracking and winner determination
- Complete navigation system between pages
- Session-based game state management
- Adaptive AI difficulty (depth increases with fewer tiles)

### Technical Features
- Flask web framework
- Jinja2 templating
- Python game logic
- Gunicorn WSGI server
- Environment variable management
- Cross-platform compatibility

### Documentation
- Comprehensive README.md
- MIT License
- Procfile for deployment
- .gitignore for version control

## [Unreleased]

### Planned Features
- [ ] Multiplayer support (PvP mode)
- [ ] Different AI strategies (random, greedy, etc.)
- [ ] Leaderboard and scoring history
- [ ] Mobile app version (React Native)
- [ ] Sound effects and background music
- [ ] Undo/Replay functionality
- [ ] Advanced AI difficulty settings
- [ ] Game statistics dashboard
- [ ] User accounts and saved games
- [ ] Dark/Light theme toggle
- [ ] Accessibility improvements (WCAG 2.1)
- [ ] Internationalization (multiple languages)
- [ ] Keyboard controls
- [ ] Customizable grid appearance

### Known Issues
- AI depth increases after multiple moves, which may cause slight delay on slower systems
- Google Generative AI module loads but isn't actively used
- No data persistence between sessions (stateless server)

### Future Improvements
- Database integration for saving games
- Real-time multiplayer using WebSockets
- WebGL-based 3D board visualization
- Progressive Web App (PWA) capabilities
- Machine learning-based AI opponent
- Tournament mode with brackets
- Achievement system
