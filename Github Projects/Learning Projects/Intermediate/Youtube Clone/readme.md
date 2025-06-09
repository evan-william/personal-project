# 📺 YouTube Front Page Clone

This is a simple front-end clone of the **YouTube homepage**, built using only **HTML and CSS**. It replicates the layout and styling of YouTube’s front page, including the header, sidebar, and video grid. Each video title is clickable and can be extended to link to individual video pages.

## 🔧 Features

* ✅ Responsive YouTube-style header with logo, search bar, and user icons
* ✅ Sidebar with YouTube navigation icons and labels
* ✅ Grid layout for video thumbnails, similar to YouTube’s real layout
* ✅ Clickable video titles (can be extended to redirect to video pages)
* ✅ CSS-based tooltips on icons
* ✅ Fully responsive layout with simple yet modern design

## 📂 Project Structure

```
youtube-clone/
│
├── index.html                  # Main homepage structure
├── styles/
│   ├── general.css             # Global styles (body, font, padding)
│   ├── header.css              # Styles for the top header section
│   ├── video.css               # Styles for video cards
│   └── sidebar.css            # Styles for the sidebar navigation
│
├── thumbnails/                # Contains video thumbnail images
├── channel-pictures/         # Profile pictures for video creators
├── icons/                     # SVG icons for YouTube-like interface
└── README.md                  # This file
```

## 📝 How to Use

1. Clone or download this repository.
2. Make sure all files are in the correct folders (as shown above).
3. Open `index.html` in your browser.
4. Hover over icons to see tooltips.
5. Click on video titles (currently can be linked to `video.html` or similar pages manually).

## 🔗 Example of Clickable Title

To make the titles clickable, wrap them like this in `index.html`:

```html
<a href="video.html">
  <p class="video-title">Talking Tech and AI with Google CEO Sundar Pichai!</p>
</a>
```

> 📌 You can create a separate `video.html` file to simulate a video watch page.

## 🚀 Technologies Used

* HTML5
* CSS3 (Flexbox & Grid)
* Google Fonts (Roboto)

## 📌 Notes

* No JavaScript is used — this is a **static-only** front-end mockup.
* Great for beginners to practice **HTML/CSS layout** and **component structuring**.


