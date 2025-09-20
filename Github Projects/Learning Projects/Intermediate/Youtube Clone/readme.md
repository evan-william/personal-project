# YouTube Front Page Clone

A static front-end recreation of the YouTube homepage built with HTML and CSS to practice layout design and responsive web development.

## What It Does

This is a pixel-perfect clone of YouTube's main interface that I built to practice advanced CSS layout techniques. The project replicates the header navigation, sidebar menu, and video grid system using only HTML and CSS without any JavaScript functionality.

Built this to understand modern web layout systems like CSS Grid and Flexbox, and to practice component-based styling architecture.

## Features

* YouTube-style header with logo, search bar, and user icons
* Collapsible sidebar navigation with icon tooltips
* Responsive video grid layout matching YouTube's design
* Clickable video titles ready for navigation integration
* CSS-only tooltips and hover effects
* Mobile-responsive design patterns
* Modular CSS architecture with separated concerns

## Project Structure

```
youtube-clone/
├── index.html              # Main page structure
├── styles/
│   ├── general.css         # Global styles and resets
│   ├── header.css          # Top navigation styling
│   ├── sidebar.css         # Side navigation menu
│   └── video.css           # Video card components
├── thumbnails/             # Video thumbnail images
├── channel-pictures/       # Channel profile images
├── icons/                  # SVG icons for interface
└── README.md              # This file
```

## Requirements

* Modern web browser with CSS Grid support
* No server requirements - runs as static files
* Internet connection for Google Fonts (Roboto)

## How to Run

Open the project in any web browser:

```bash
# Simply open index.html in your browser
open index.html
```

Or serve locally if preferred:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .
```

## How It Works

The layout uses CSS Grid for the main page structure and Flexbox for component alignment. The design is built with a mobile-first approach and uses media queries for responsive breakpoints. Each component is styled in separate CSS files for maintainability.

The video grid automatically adjusts based on screen size, and the sidebar can be extended to include collapse functionality with minimal JavaScript additions.

## What I Learned

* CSS Grid and Flexbox layout systems
* Responsive design principles and mobile-first development
* Component-based CSS architecture
* Advanced CSS selectors and pseudo-elements
* Image optimization and aspect ratio maintenance
* Modern CSS features like custom properties
* Cross-browser compatibility considerations

## Extending the Project

To add video page navigation:

```html
<a href="video.html">
  <p class="video-title">Video Title Here</p>
</a>
```

Create additional pages like `video.html` for a complete YouTube clone experience.

## Known Issues

* Static content only - no dynamic video loading
* Search functionality requires JavaScript implementation
* No user authentication or personalization features
* Limited to desktop and tablet layouts
* Images need to be manually added to directories

## Possible Improvements

Could add:
* JavaScript for interactive sidebar collapse
* Search functionality with filtering
* Video player page templates
* Dark mode theme toggle
* Infinite scroll simulation
* Local storage for user preferences
* Animation transitions for better UX

## Author

**Evan William** - Version 1.0 (2025)

Created this to master CSS layout techniques and understand how complex web interfaces are structured. It was excellent practice for component-based styling and responsive design patterns.

This was my first attempt at recreating a major website's interface, focusing on pixel-perfect accuracy and clean code organization.

*Learning project - demonstrates modern CSS layout techniques through YouTube interface recreation.*
