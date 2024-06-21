# GallerySphere 
![Project Tools](https://skillicons.dev/icons?i=python,django)
## Introduction

Welcome to GallerySphere, a dynamic platform designed to showcase and share your favorite photographs with the world. Whether you're an amateur photographer looking to exhibit your work or a professional seeking a portfolio space, GallerySphere offers a seamless experience for managing and presenting your images.

## Features

- **User-Friendly Interface**: Easily upload, organize, and manage your photos in a visually appealing gallery.
- **Social Sharing**: Share your creations with friends, family, or followers across various social media platforms.
- **Interactive Comments**: Engage with your audience through comments and likes on your photos.
- **Responsive Design**: Access your gallery from any device, ensuring your photos look great on smartphones, tablets, and desktops.
- **Customizable Layouts**: Tailor the appearance of your gallery to match your personal style or brand.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.2+
- Pillow (for image processing)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/GallerySphere.git
   cd GallerySphere
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```
   python manage.py migrate
   ```

5. Load initial data (if applicable):
   ```
   python manage.py loaddata fixtures/initial_data.json
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to see your site.

## Usage

After starting the server, you can begin uploading photos by navigating to the upload section of the website. Use the intuitive interface to add titles, descriptions, and categorize your photos. Once uploaded, your photos will be displayed in a beautiful gallery format, ready to be shared with the world.
